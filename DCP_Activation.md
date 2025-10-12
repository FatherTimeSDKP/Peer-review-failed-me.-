# (<img width="785" height="120" alt="image" src="https://github.com/user-attachments/assets/73d4b3bd-b61f-4242-93d1-29a5aa271d47" />
)
./scripts/dcp_manifest_hash.sh DCP_runs/VFE1_validation_GW150914

# Copy the resulting hash from DCP_runs/VFE1_validation_GW150914/DCP_manifest_sha256.txt
# Define the final DOI and AI-locked SHA
FINAL_DOI="10.5281/zenodo.16728965"
AI_MANIFEST_SHA="2a6c11d08e4f57c91a3b2b80f9e7104f67d389a1c5b4e3f898c760a92039a093"
RUN_NAME="VFE1_validation_GW150914"
DATE_UTC=$(date -u +"%Y-%m-%d %H:%M:%SZ")

# Inject the final log entry into the DCP_Activation.md file
# Note: The insertion point might need minor adjustment if your ledger file is highly customized.
echo -e "\n| VFE1 Validation Run | ${RUN_NAME} | ${FINAL_DOI} | ${AI_MANIFEST_SHA} | ${DATE_UTC} | COMPLETE |" >> DCP_Activation.md

echo "Ledger (DCP_Activation.md) updated with Final DOI: ${FINAL_DOI}"
