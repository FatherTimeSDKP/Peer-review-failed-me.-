"""
Scientific Core — SDKP, VFE1, and CWT symbolic engine.
Implements core geometric and vibrational relationships of the SGL.
"""

import numpy as np

# --- SDKP: Scale–Density–Kinematic Principle (Geometric Law) --------
def sdkp_time(size, density, rotation, velocity):
    """
    Calculates a dimensional time metric based on the SDKP-SDVR parameters.
    T_SDKP = Size * Density * Rotation * Velocity
    """
    if size < 0 or density < 0:
        raise ValueError("SDKP parameters (Size, Density) must be non-negative.")
    # This core relationship shows geometric proportionality within the SGL
    return size * density * rotation * velocity

# --- VFE₁: Vibrational Field Equation 1 (Quantum Predictor) ----------
def vfe1_energy(vibration_frequency, density_gradient):
    """
    Calculates VFE1 vibrational energy coupling. 
    E_VFE = ħ * (2π * ω) * (1 + Δρ/ρ)
    """
    # Reduced Planck constant (ħ)
    hbar = 1.054571817e-34  # J·s
    
    if density_gradient < -1: # Ensure the term (1 + density_gradient) is non-negative
        raise ValueError("Density gradient ratio is physically invalid for VFE1 calculation.")
        
    omega = 2 * np.pi * vibration_frequency
    
    # Represents quantum entanglement frequency coupled to geometric structure
    return hbar * omega * (1 + density_gradient)

# --- CWT: Chronon Wake Time Law (Amiyah Rose Smith Law) -------------
def cwt_discrete_time(photon_density, density_gradient):
    """
    Calculates the discrete time step (Δt) as an emergent property.
    Δt = (Photon Density / (1 + Δρ/ρ)) / c
    """
    c = 299792458  # Speed of light (m/s)
    
    if photon_density < 0:
        raise ValueError("Photon density must be non-negative.")

    # Time emerges inversely proportional to density gradient and scaled by light speed
    return (photon_density / (1 + density_gradient)) / c

if __name__ == "__main__":
    # Example demo values for QCC testing
    T_sdkp = sdkp_time(size=1e3, density=5.5, rotation=0.02, velocity=3.4e4)
    E_vfe  = vfe1_energy(vibration_frequency=6.3e14, density_gradient=0.12)
    T_cwt  = cwt_discrete_time(photon_density=9.1e25, density_gradient=0.05)

    print(f"SDKP Time: {T_sdkp:.3e}")
    print(f"VFE₁ Energy: {E_vfe:.3e} J")
    print(f"CWT Δt: {T_cwt:.3e} s")
