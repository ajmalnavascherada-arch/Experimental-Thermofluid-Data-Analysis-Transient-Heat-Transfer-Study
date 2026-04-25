import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    df = df.dropna()

    # Convert to Kelvin
    df['temperature_K'] = df['temperature_C'] + 273.15

    return df