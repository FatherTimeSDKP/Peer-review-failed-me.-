#!/usr/bin/env python3
"""
github_audit.py
Clone and audit all public repos for a given GitHub username.
Outputs:
 - ./audit_output/manifest.json
 - ./audit_output/summary.csv
 - ./audit_output/repos/<repo_name>/ (cloned repo)
 - ./audit_output/repos/<repo_name>/metadata.json
Usage:
    python github_audit.py --user FatherTimeSDKP
"""

import os, sys, subprocess, json, hashlib, csv, argparse, datetime
from pathlib import Path

def run(cmd, cwd=None):
    print("+", " ".join(cmd))
    return subprocess.run(cmd, cwd=cwd, check=True)

def sha256_of_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def clone_or_update(repo_url, dest):
    if dest.exists():
        # pull latest
        run(["git", "pull"], cwd=str(dest))
    else:
        run(["git", "clone", repo_url, str(dest)])

def repo_list_for_user(user):
    # Simple GitHub URL listing; you can extend to use GitHub API if you supply a token.
    # This naive approach assumes standard public repos names are known; fallback: ask user to pass repo list.
    raise RuntimeError("Use --repo-list or provide token to use GitHub API. See README in script.")

def collect_repo_metadata(repo_dir):
    repo_dir = Path(repo_dir)
    metadata = {}
    metadata['path'] = str(repo_dir)
    metadata['files'] = []
    for root, _, files in os.walk(repo_dir):
        for fn in files:
            p = Path(root) / fn
            rel = p.relative_to(repo_dir).as_posix()
            try:
                sha = sha256_of_file(p)
            except Exception as e:
                sha = None
            metadata['files'].append({'path': rel, 'size': p.stat().st_size, 'sha256': sha})
    # attempt to read README, LICENSE
    for name in ("README.md", "README.MD", "README", "LICENSE", "LICENSE.md"):
        rp = repo_dir / name
        if rp.exists():
            metadata[name] = rp.read_text(encoding='utf-8', errors='ignore')
    # get last commit info
    try:
        p = subprocess.run(["git","-C", str(repo_dir), "log", "-1", "--pretty=%H%n%ci%n%an"], capture_output=True, text=True, check=True)
        lines = p.stdout.strip().splitlines()
        if len(lines) >= 3:
            metadata['last_commit_hash'] = lines[0]
            metadata['last_commit_date'] = lines[1]
            metadata['last_commit_author'] = lines[2]
    except Exception:
        pass
    return metadata

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--user", required=True, help="GitHub username")
    parser.add_argument("--out", default="audit_output", help="output folder")
    parser.add_argument("--repos", nargs="*", help="optional list of repo URLs (full URLs). If omitted, you must provide a token to use the API.")
    parser.add_argument("--token", help="GitHub token to list repos via API (optional)")
    args = parser.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    repos_dir = out / "repos"
    repos_dir.mkdir(exist_ok=True)

    repo_urls = []
    if args.repos:
        repo_urls = args.repos
    elif args.token:
        import requests
        headers = {"Authorization": f"token {args.token}"}
        url = f"https://api.github.com/users/{args.user}/repos?per_page=200"
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        data = resp.json()
        for r in data:
            repo_urls.append(r['clone_url'])
    else:
        print("No repo list provided and no token. Please provide --repos or --token to enumerate repos.")
        sys.exit(1)

    manifest = {"user": args.user, "generated_at": datetime.datetime.utcnow().isoformat()+"Z", "repos": []}
    for repo_url in repo_urls:
        name = repo_url.rstrip("/").split("/")[-1]
        safe_name = name.replace(" ", "_").replace(".", "_")
        dest = repos_dir / safe_name
        clone_or_update(repo_url, dest)
        meta = collect_repo_metadata(dest)
        meta['repo_url'] = repo_url
        manifest['repos'].append(meta)
        # save per-repo metadata
        with open(out / "repos" / f"{safe_name}_metadata.json", "w", encoding='utf-8') as f:
            json.dump(meta, f, indent=2, ensure_ascii=False)

    # save manifest
    with open(out / "manifest.json", "w", encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    # write CSV summary
    csv_path = out / "summary.csv"
    with open(csv_path, "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["repo", "num_files", "total_size_bytes", "last_commit_date", "last_commit_author", "repo_url"])
        for r in manifest['repos']:
            total_size = sum([fi['size'] or 0 for fi in r['files']])
            writer.writerow([r.get('path',''), len(r['files']), total_size, r.get('last_commit_date',''), r.get('last_commit_author',''), r.get('repo_url','')])

    print("Audit complete. Output in:", out)

if __name__ == "__main__":
    main()
