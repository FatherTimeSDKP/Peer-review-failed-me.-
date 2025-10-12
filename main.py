# main.py

from protocol_engine import DigitalCrystalProtocol

if __name__ == "__main__":
    
    # Initialize the Autonomous Engine
    dcp = DigitalCrystalProtocol()
    
    # --- Input Parameters (Example Discovery Scenario) ---
    # These parameters represent a specific SGL vector for computation:
    size_param = 1000  
    density_param = 5.5
    rotation_param = 0.02
    velocity_param = 34000
    vib_freq_param = 6.3e14 # High VFE1 coefficient
    d_grad_param = 0.12     # Local density gradient ratio
    photon_density_param = 9.1e25
    
    # --- Execute QCC-AE Analysis ---
    T, E, Δt = dcp.run_analysis(
        size=size_param,
        density=density_param,
        rotation=rotation_param,
        velocity=velocity_param,
        vib_freq=vib_freq_param,
        d_grad=d_grad_param,
        photon_density=photon_density_param
    )

    if T is not None:
        print("\n--- Digital Crystal Protocol (DCP) Analysis Summary ---")
        print(f"SDKP Time (Geometric Metric): {T:.3e}")
        print(f"VFE₁ Energy (Quantum Entanglement): {E:.3e} J")
        print(f"CWT Discrete t (Amiyah Rose Law): {Δt:.3e} s")
        print("------------------------------------------------------")

    # --- Final Immutability Protocol ---
    # Generates the JSON matrix and the IP-securing PDF.
    dcp.export_authorship_and_ip()
