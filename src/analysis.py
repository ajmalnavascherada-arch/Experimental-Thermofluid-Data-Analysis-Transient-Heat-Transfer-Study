import numpy as np

def compute_temperature_gradient(df):
    dT_dt = np.gradient(df['temperature_K'], df['time_s'])
    df['dT_dt'] = dT_dt
    return df

def estimate_heat_trend(df):
    # Simple correlation between current and temperature
    correlation = df['current_A'].corr(df['temperature_K'])
    return correlation