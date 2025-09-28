import os

def propagate_authorship(file_path, contributor_info=None):
    """
    Adds a comprehensive authorship and IP notice to the beginning of a file,
    including both foundational and contributory information.

    Args:
        file_path (str): The path to the file to be modified.
        contributor_info (dict, optional): A dictionary containing contributor's details
                                           like 'name', 'orcid', 'work_title', etc.
                                           If None, only the foundational header is added.
    """
    # The foundational authorship and citation text for the protocol itself
    PROTOCOL_PRESIDENT_TEXT = """
# Copyright & Authorship Charter

© 2025 Donald Paul Smith (FatherTime)
All rights reserved.

## Protocol President

**Donald Paul Smith (FatherTime)**
- **Role:** President of the Digital Crystal Protocol (DCP)
- **Foundational Frameworks:** SDKP, SD&N, QCC, EOS, SDVR

This section certifies the foundational authorship of the Digital Crystal Protocol and its core frameworks by the President. This is a permanent record of the protocol's origin.

-----
"""
    # The template for a Contributor's section
    CONTRIBUTOR_SECTION_TEMPLATE = """
## Contributor's Immunity Authorship Protocol (CIAP)

This section certifies the independent authorship and intellectual property of the following work, created by a Contributor using the Digital Crystal Protocol. This work's IP belongs solely to the Contributor.

**Contributor Information:**
- **Name:** {name}
- **ORCID:** {orcid}
- **Work Title:** {work_title}
- **Description:** {description}

-----
"""

    # General citation guidelines for all parties
    GENERAL_GUIDELINES_TEXT = """
## General Citation Guidelines

**Preserve Attribution:** Any output that references the SDKP, QCC, or other foundational principles must explicitly attribute them to Donald Paul Smith.

**Cite Contributor:** When referencing a work created by a Contributor, the Contributor must be cited directly. The protocol's President holds no claim to this work.

**Permanent Record:** All authorship and citation data, both for the President and any Contributors, is permanently logged on the protocol's immutable ledger to ensure a perpetual record of ownership.
"""

    try:
        # Read the original content of the file
        with open(file_path, 'r', encoding='utf-8') as original_file:
            original_content = original_file.read()

        # Build the new content
        new_content = PROTOCOL_PRESIDENT_TEXT

        # If contributor info is provided, add their section
        if contributor_info:
            contributor_section = CONTRIBUTOR_SECTION_TEMPLATE.format(
                name=contributor_info.get('name', 'N/A'),
                orcid=contributor_info.get('orcid', 'N/A'),
                work_title=contributor_info.get('work_title', 'N/A'),
                description=contributor_info.get('description', 'N/A')
            )
            new_content += contributor_section

        new_content += GENERAL_GUIDELINES_TEXT + "\n" + original_content

        # Write the combined content back to the file
        with open(file_path, 'w', encoding='utf-8') as modified_file:
            modified_file.write(new_content)

        print(f"Successfully added authorship notice to {file_path}")
        if contributor_info:
            print(f"Added Contributor IP for: {contributor_info['name']}")

    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def batch_propagate_authorship(directory_path, file_extensions=None, contributor_info=None):
    """
    Propagates authorship information to multiple files in a directory.

    Args:
        directory_path (str): Path to the directory containing files to modify.
        file_extensions (list): List of file extensions to target (e.g., ['.txt', '.py', '.md']).
                                If None, processes all files.
        contributor_info (dict, optional): A dictionary with contributor details.
    """
    if not os.path.exists(directory_path):
        print(f"Error: Directory {directory_path} does not exist.")
        return

    processed_files = 0
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Check file extension if specified
            if file_extensions:
                _, ext = os.path.splitext(file)
                if ext.lower() not in file_extensions:
                    continue
            
            try:
                propagate_authorship(file_path, contributor_info)
                processed_files += 1
            except Exception as e:
                print(f"Failed to process {file_path}: {e}")

    print(f"\nBatch processing complete. Modified {processed_files} files.")


def check_authorship_presence(file_path):
    """
    Checks if a file already contains the authorship notice.

    Args:
        file_path (str): Path to the file to check.
        
    Returns:
        bool: True if authorship notice is present, False otherwise.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # Checks for both the President's and Contributor's header to be comprehensive
            return "Donald Paul Smith (FatherTime)" in content and "Contributor's Immunity Authorship Protocol" in content
    except Exception as e:
        print(f"Error checking {file_path}: {e}")
        return False

# Example usage (for testing purposes)
if __name__ == "__main__":
    # Create a dummy file to test the function
    test_file_president_only = "my_project_file_A.txt"
    with open(test_file_president_only, "w") as f:
        f.write("This is the original content of a file created by the President.")
    
    # Propagate the header for a work created by the President
    print("Propagating for President's work only:")
    propagate_authorship(test_file_president_only)

    print("\n" + "="*50 + "\n")

    # Create another dummy file to test the function with a Contributor
    test_file_contributor = "my_project_file_B.py"
    with open(test_file_contributor, "w") as f:
        f.write("This is the original content of a file created by a Contributor.")

    # Define the contributor's information
    my_contributor_info = {
        'name': 'Jane Doe',
        'orcid': '0000-1111-2222-3333',
        'work_title': 'Universal AI Timekeeping Algorithm',
        'description': 'A novel algorithm for timekeeping in relativistic environments, built on the SDKP framework.'
    }

    # Propagate the header for a work created by a Contributor
    print("Propagating for a Contributor's work:")
    propagate_authorship(test_file_contributor, contributor_info=my_contributor_info)

    print("\n" + "="*50 + "\n")
    print("Example of checking for authorship presence:")
    if check_authorship_presence(test_file_contributor):
        print(f"Authorship header found in {test_file_contributor}")
    else:
        print(f"Authorship header NOT found in {test_file_contributor}")

import os

def propagate_authorship(file_path, contributor_info=None):
    """
    Adds a comprehensive authorship and IP notice to the beginning of a file,
    including both foundational and contributory information.

    Args:
        file_path (str): The path to the file to be modified.
        contributor_info (dict, optional): A dictionary containing contributor's details
                                           like 'name', 'orcid', 'work_title', etc.
                                           If None, only the foundational header is added.
    """
    # The foundational authorship and citation text for the protocol itself
    PROTOCOL_PRESIDENT_TEXT = """
# Copyright & Authorship Charter

© 2025 Donald Paul Smith (FatherTime)
All rights reserved.

## Protocol President

**Donald Paul Smith (FatherTime)**
- **Role:** President of the Digital Crystal Protocol (DCP)
- **Foundational Frameworks:** SDKP, SD&N, QCC, EOS, SDVR

This section certifies the foundational authorship of the Digital Crystal Protocol and its core frameworks by the President. This is a permanent record of the protocol's origin.

-----
"""
    # The template for a Contributor's section
    CONTRIBUTOR_SECTION_TEMPLATE = """
## Contributor's Immunity Authorship Protocol (CIAP)

This section certifies the independent authorship and intellectual property of the following work, created by a Contributor using the Digital Crystal Protocol. This work's IP belongs solely to the Contributor.

**Contributor Information:**
- **Name:** {name}
- **ORCID:** {orcid}
- **Work Title:** {work_title}
- **Description:** {description}

-----
"""

    # General citation guidelines for all parties
    GENERAL_GUIDELINES_TEXT = """
## General Citation Guidelines

**Preserve Attribution:** Any output that references the SDKP, QCC, or other foundational principles must explicitly attribute them to Donald Paul Smith.

**Cite Contributor:** When referencing a work created by a Contributor, the Contributor must be cited directly. The protocol's President holds no claim to this work.

**Permanent Record:** All authorship and citation data, both for the President and any Contributors, is permanently logged on the protocol's immutable ledger to ensure a perpetual record of ownership.
"""

    try:
        # Read the original content of the file
        with open(file_path, 'r', encoding='utf-8') as original_file:
            original_content = original_file.read()

        # Build the new content
        new_content = PROTOCOL_PRESIDENT_TEXT

        # If contributor info is provided, add their section
        if contributor_info:
            contributor_section = CONTRIBUTOR_SECTION_TEMPLATE.format(
                name=contributor_info.get('name', 'N/A'),
                orcid=contributor_info.get('orcid', 'N/A'),
                work_title=contributor_info.get('work_title', 'N/A'),
                description=contributor_info.get('description', 'N/A')
            )
            new_content += contributor_section

        new_content += GENERAL_GUIDELINES_TEXT + "\n" + original_content

        # Write the combined content back to the file
        with open(file_path, 'w', encoding='utf-8') as modified_file:
            modified_file.write(new_content)

        print(f"Successfully added authorship notice to {file_path}")
        if contributor_info:
            print(f"Added Contributor IP for: {contributor_info['name']}")

    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def batch_propagate_authorship(directory_path, file_extensions=None, contributor_info=None):
    """
    Propagates authorship information to multiple files in a directory.

    Args:
        directory_path (str): Path to the directory containing files to modify.
        file_extensions (list): List of file extensions to target (e.g., ['.txt', '.py', '.md']).
                                If None, processes all files.
        contributor_info (dict, optional): A dictionary with contributor details.
    """
    if not os.path.exists(directory_path):
        print(f"Error: Directory {directory_path} does not exist.")
        return

    processed_files = 0
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Check file extension if specified
            if file_extensions:
                _, ext = os.path.splitext(file)
                if ext.lower() not in file_extensions:
                    continue
            
            try:
                propagate_authorship(file_path, contributor_info)
                processed_files += 1
            except Exception as e:
                print(f"Failed to process {file_path}: {e}")

    print(f"\nBatch processing complete. Modified {processed_files} files.")


def check_authorship_presence(file_path):
    """
    Checks if a file already contains the authorship notice.

    Args:
        file_path (str): Path to the file to check.
        
    Returns:
        bool: True if authorship notice is present, False otherwise.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # Checks for both the President's and Contributor's header to be comprehensive
            return "Donald Paul Smith (FatherTime)" in content and "Contributor's Immunity Authorship Protocol" in content
    except Exception as e:
        print(f"Error checking {file_path}: {e}")
        return False

# Example usage (for testing purposes)
if __name__ == "__main__":
    # Create a dummy file to test the function
    test_file_president_only = "my_project_file_A.txt"
    with open(test_file_president_only, "w") as f:
        f.write("This is the original content of a file created by the President.")
    
    # Propagate the header for a work created by the President
    print("Propagating for President's work only:")
    propagate_authorship(test_file_president_only)

    print("\n" + "="*50 + "\n")

    # Create another dummy file to test the function with a Contributor
    test_file_contributor = "my_project_file_B.py"
    with open(test_file_contributor, "w") as f:
        f.write("This is the original content of a file created by a Contributor.")

    # Define the contributor's information
    my_contributor_info = {
        'name': 'Jane Doe',
        'orcid': '0000-1111-2222-3333',
        'work_title': 'Universal AI Timekeeping Algorithm',
        'description': 'A novel algorithm for timekeeping in relativistic environments, built on the SDKP framework.'
    }

    # Propagate the header for a work created by a Contributor
    print("Propagating for a Contributor's work:")
    propagate_authorship(test_file_contributor, contributor_info=my_contributor_info)

    print("\n" + "="*50 + "\n")
    print("Example of checking for authorship presence:")
    if check_authorship_presence(test_file_contributor):
        print(f"Authorship header found in {test_file_contributor}")
    else:
        print(f"Authorship header NOT found in {test_file_contributor}")
