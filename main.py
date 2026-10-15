
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from src.analysis import compute_temperature_gradient, estimate_heat_trend
from src.data_loader import load_data
from src.plotting import plot_temperature

# Output paths
DATA_PATH = "data/synthetic_thermal_data.csv"
PLOT_PATH = "results/plots"
PROCESSED_PATH = "results/processed_data.csv"


def generate_synthetic_data(
    n_points=10_000,
    duration_s=1000.0,
    seed=42,
):
    """Generate synthetic data using a lumped thermal model.

    This dataset is simulated, not experimentally measured.
    """
    rng = np.random.default_rng(seed)

    # Illustrative thermal parameters
    ambient_K = 293.15
    resistance_ohm = 0.8
    thermal_capacity_J_K = 500.0
    thermal_conductance_W_K = 2.0

    time_s = np.linspace(0, duration_s, n_points)
    dt = time_s[1] - time_s[0]

    # Time-varying electrical current
    current_A = (
        2.0
        + 1.2 * time_s / duration_s
        + 0.15 * np.sin(2 * np.pi * time_s / 200.0)
    )

    voltage_V = current_A * resistance_ohm
    heat_generation_W = current_A**2 * resistance_ohm

    # Simulate the transient thermal response
    temperature_true_K = np.zeros(n_points)
    temperature_true_K[0] = ambient_K

    for i in range(1, n_points):
        heat_loss_W = thermal_conductance_W_K * (
            temperature_true_K[i - 1] - ambient_K
        )

        dT_dt = (
            heat_generation_W[i - 1] - heat_loss_W
        ) / thermal_capacity_J_K

        temperature_true_K[i] = (
            temperature_true_K[i - 1] + dT_dt * dt
        )

    # Add small simulated sensor noise
    temperature_K = (
        temperature_true_K
        + rng.normal(0, 0.002, n_points)
    )

    df = pd.DataFrame({
        "time_s": time_s,
        "temperature_K": temperature_K,
        "temperature_C": temperature_K - 273.15,
        "current_A": current_A,
        "voltage_V": voltage_V,
        "heat_generation_W": heat_generation_W,
        "temperature_true_K": temperature_true_K,
    })

    return df


def main():
    # 1. Generate the synthetic dataset
    Path("data").mkdir(parents=True, exist_ok=True)
    Path("results").mkdir(parents=True, exist_ok=True)

    generated_df = generate_synthetic_data()

    generated_df.to_csv(DATA_PATH, index=False)

    print("Synthetic thermal dataset generated.")
    print(f"Number of observations: {len(generated_df):,}")
    print(f"Dataset saved to: {DATA_PATH}")

    # 2. Load the generated data through the existing loader
    df = load_data(DATA_PATH)

    # 3. Calculate temperature gradient
    df = compute_temperature_gradient(df)

    # 4. Analyse current-temperature correlation
    correlation = estimate_heat_trend(df)

    print(
        "Correlation (Current vs Temperature):",
        round(correlation, 4),
    )

    # 5. Generate plots
    plot_temperature(df, PLOT_PATH)



    # Calculate a smoothed temperature gradient
    df["dT_dt_smoothed"] = (
        df["dT_dt"].rolling(
            window=101,
            center=True,
            min_periods=1
        ).mean()
    )

    plt.figure(figsize=(10, 5))

    # Raw gradient: retain it to show measurement noise
    plt.plot(
        df["time_s"],
        df["dT_dt"],
        linewidth=0.5,
        alpha=0.2,
        label="Raw numerical gradient"
    )

    # Smoothed gradient: reveal the trend
    plt.plot(
        df["time_s"],
        df["dT_dt_smoothed"],
        linewidth=2,
        label="Smoothed numerical gradient"
    )

    # Model-based gradient, if available
    if "dT_dt_model_K_s" in df.columns:
        plt.plot(
            df["time_s"],
            df["dT_dt_model_K_s"],
            linewidth=2,
            label="Thermal model gradient"
        )

    plt.xlabel("Time (s)")
    plt.ylabel("Temperature gradient (K/s)")
    plt.title("Temperature Gradient vs Time")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(
        "results/plots/temperature_gradient_comparison.png",
        dpi=200
    )
    plt.show()

    # 6. Save processed results
    df.to_csv(PROCESSED_PATH, index=False)

    print(f"Processed data saved to: {PROCESSED_PATH}")
    print(f"Processed observations: {len(df):,}")
    print(f"Missing values: {df.isna().sum().sum()}")


if __name__ == "__main__":
    main()
