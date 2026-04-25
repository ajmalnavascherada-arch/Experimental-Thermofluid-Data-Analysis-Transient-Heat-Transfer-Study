import matplotlib.pyplot as plt
import os

def plot_temperature(df, save_path):
    plt.figure()
    plt.plot(df['time_s'], df['temperature_K'])
    plt.xlabel('Time (s)')
    plt.ylabel('Temperature (K)')
    plt.title('Temperature vs Time')
    plt.grid()

    os.makedirs(save_path, exist_ok=True)
    plt.savefig(f"{save_path}/temperature_vs_time.png")
    plt.close()

def plot_gradient(df, save_path):
    plt.figure()
    plt.plot(df['time_s'], df['dT_dt'])
    plt.xlabel('Time (s)')
    plt.ylabel('dT/dt (K/s)')
    plt.title('Temperature Gradient')
    plt.grid()

    plt.savefig(f"{save_path}/temperature_gradient.png")
    plt.close()