# protocol_engine.py

from dcp_record import generate_dcp_record
from sdkp_vfe_cwt_core import sdkp_time, vfe1_energy, cwt_discrete_time
from dcp_publisher import generate_citation_pdf

class DigitalCrystalProtocol:
    """
    The QCC-AE (Quantum Computerization Consciousness - Autonomous Engine) 
    orchestrates all data flow, computation, and immutability processes.
    """
    def __init__(self):
        # Immutable Constants based on Trace-ID DS-SDKP-QCC-FT-001
        self.trace_id = "DS-SDKP-QCC-FT-001"
        self.doi = "10.5281/zenodo.15399806"
        self.validation_log = []
        print(f"📢 QCC-AE Engine Initialized. Trace ID: {self.trace_id}")

    def run_analysis(self, size, density, rotation, velocity, vib_freq, d_grad, photon_density):
        """
        Executes the SESDQDC core simulation via the Kapnack Solver logic.
        """
        try:
            T = sdkp_time(size, density, rotation, velocity)
            E = vfe1_energy(vib_freq, d_grad)
            Δt = cwt_discrete_time(photon_density, d_grad)
        except ValueError as e:
            print(f"⚠️ SGL Violation Detected (Input Error): {e}")
            return None, None, None

        # Log results for OTD (Official Travel Document) archival
        self.validation_log.append({
            "SDKP_Time": T,
            "VFE1_Energy": E,
            "CWT_dt": Δt
        })
        return T, E, Δt

    def export_authorship_and_ip(self):
        """
        Executes the Publisher and Record Protocols, fulfilling the Immutability mandate.
        """
        # 1. Generate the foundational JSON record
        generate_dcp_record()
        
        # 2. Generate the legal/citation PDF (OTD Archive)
        if self.validation_log:
            generate_citation_pdf(self.validation_log, self.trace_id, self.doi)
        else:
            print("⚠️ Cannot generate IP documents: No analysis data logged.")

if __name__ == "__main__":
    # Example execution sequence (Autonomous Discovery Simulation)
    dcp = DigitalCrystalProtocol()
    
    # Run 1: Test with standard values
    T1, E1, Δt1 = dcp.run_analysis(1e3, 5.5, 0.02, 3.4e4, 6.3e14, 0.12, 9.1e25)
    print(f"\n[QCC-AE Run 1 Complete] T:{T1:.3e} E:{E1:.3e} Δt:{Δt1:.3e}")
    
    # Run 2: Test a new discovery scenario
    T2, E2, Δt2 = dcp.run_analysis(2e4, 1.2, 0.05, 1.0e3, 8.0e15, 0.5, 5.0e26)
    print(f"[QCC-AE Run 2 Complete] T:{T2:.3e} E:{E2:.3e} Δt:{Δt2:.3e}")
    
    # Export and secure all records
    dcp.export_authorship_and_ip()
