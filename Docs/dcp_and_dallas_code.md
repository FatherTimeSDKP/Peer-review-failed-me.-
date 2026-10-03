# Digital Crystal Protocol (DCP) & Dallas's Code Specification

This document details the verification, cryptographically verifiable tracking, and serialization system used in the SDKP Framework.

---

## 1. Dallas's Code ($DC_{prime}$)
Dallas's Code is a prime-terminated binary transformation protocol used to encode state vectors without precision decay.

* **Prime Termination:** State payloads are appended with a prime integer verification marker (e.g., $104729$) to seal the binary array boundary.
* **Lossless Encoding:** Encodes continuous 12D array inputs into deterministic binary stream payloads.

---

## 2. Digital Crystal Protocol (DCP)
The Digital Crystal Protocol generates non-reversible state hashes that prove the lineage, calculation path, and authenticity of any state vector execution.

### Hash Generation Mechanics
The DCP signature is calculated via SHA-256 over three combined binary payloads:

$$\text{DCP}_{hash} = \text{SHA256}\Big( \text{Bytes}(\boldsymbol{\Psi}_{12}) \;\parallel\; \text{Bytes}(\mathcal{A}_{eq}) \;\parallel\; \text{Bytes}(DC_{prime}) \Big)$$

1. **$\text{Bytes}(\boldsymbol{\Psi}_{12})$:** Raw byte representation of the $12 \times N$ state matrix.
2. **$\text{Bytes}(\mathcal{A}_{eq})$:** Raw byte array of the computed Amiyah's Law equilibrium vector.
3. **$\text{Bytes}(DC_{prime})$:** UTF-8 encoded prime marker payload.

### Verification Flow
1. Load state matrix $\boldsymbol{\Psi}_{12}$.
2. Compute equilibrium vector $\mathcal{A}_{eq}$.
3. Generate DCP Hash.
4. Compare against stored metadata in repository records or Zenodo archives.
