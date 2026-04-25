from src.data_loader import load_data
from src.analysis import compute_temperature_gradient, estimate_heat_trend
from src.plotting import plot_temperature, plot_gradient

DATA_PATH = "data/sample_data.csv"
PLOT_PATH = "results/plots"

def main():
    df = load_data(DATA_PATH)

    df = compute_temperature_gradient(df)

    correlation = estimate_heat_trend(df)

    print("Correlation (Current vs Temperature):", correlation)

    plot_temperature(df, PLOT_PATH)
    plot_gradient(df, PLOT_PATH)

    df.to_csv("results/processed_data.csv", index=False)

if __name__ == "__main__":
    main()