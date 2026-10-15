# Experimental Thermofluid Data Analysis – Transient Heat Transfer Study

## Overview

This project uses Python to analyse transient thermal behaviour and investigate how temperature changes over time under varying electrical operating conditions. It includes data preprocessing, numerical differentiation, correlation analysis, thermal simulation, and visualisation.

The project starts with a small sample dataset and can be extended with a synthetic dataset generated using a lumped thermal-capacitance model. Synthetic data are simulated and must not be interpreted as measurements collected in a physical laboratory.

## Objectives

- Analyse temperature variation over time.
- Calculate temperature gradients (\(dT/dt\)).
- Investigate the relationship between electrical current and temperature.
- Simulate transient heating using electrical heat generation and heat loss.
- Compare numerical temperature gradients with model-based predictions.
- Automate data processing and visualisation using Python.

## Methods

### 1. Data Processing

The workflow loads time-series data using pandas, validates the input, calculates temperature gradients using NumPy, and saves the processed results as a CSV file.

### 2. Temperature Gradient Analysis

The temperature gradient represents the rate of temperature change over time:

\[
\frac{dT}{dt}
\]

Positive values indicate heating, negative values indicate cooling, and values close to zero indicate that temperature is changing slowly.

Numerical differentiation can amplify noise in temperature measurements. Comparing raw gradients with smoothed estimates helps reveal the underlying trend while preserving the original data for reference.

### 3. Synthetic Thermal Simulation

The project can be extended with a lumped thermal-capacitance model that represents electrical heating and convective heat loss:

\[
mc_p\frac{dT}{dt}=I^2R-UA(T-T_\infty)
\]

Where:

- \(m\): component mass (kg)
- \(c_p\): specific heat capacity (J/kg·K)
- \(I\): electrical current (A)
- \(R\): electrical resistance (Ω)
- \(U\): overall heat-transfer coefficient (W/m²·K)
- \(A\): exposed surface area (m²)
- \(T\): component temperature (K)
- \(T_\infty\): ambient temperature (K)

The simulation uses illustrative parameters to demonstrate transient thermal behaviour. Its assumptions and parameters have not been validated against laboratory measurements.

A reproducible simulation can generate 10,000 time-series observations for testing the data-processing pipeline. These are **synthetic observations, not experimental measurements**.

### 4. Correlation Analysis

The workflow calculates the correlation between current and temperature to explore their statistical association. Correlation alone does not establish causation because thermal response also depends on heat capacity, heat losses, and other operating conditions.

### 5. Visualisation

Matplotlib is used to generate plots of:

- Temperature versus time
- Temperature gradient versus time
- Current–temperature relationships

## Technologies Used

- Python
- NumPy
- pandas
- Matplotlib

## Project Structure

```text
Experimental-Thermofluid-Data-Analysis-Transient-Heat-Transfer-Study/
├── data/
│   ├── sample_data.csv
│   └── synthetic_thermal_data.csv
├── src/
│   ├── data_loader.py
│   ├── analysis.py
│   └── plotting.py
├── results/
│   ├── processed_data.csv
│   └── plots/
├── main.py
└── README.md
```

The synthetic dataset is generated when the simulation script is executed. Additional simulation scripts can be added under `src/`. Generated files may not exist until the workflow has been run.

## Installation

Install the required Python packages:

```bash
pip install numpy pandas matplotlib
```

## Running the Project

From the repository root, execute:

```bash
python main.py
```

This runs the existing data-loading, gradient-calculation, correlation-analysis, and plotting workflow.

If a separate synthetic-data generator has been added, run that script according to its instructions before analysing the generated dataset.

## Interpretation and Limitations

- The original sample dataset contains 11 observations.
- A generated dataset containing 10,000 rows demonstrates processing capability but does not establish that 10,000 physical measurements were collected.
- The thermal model assumes a sufficiently uniform component temperature. Its suitability depends on the physical system and the validity of the lumped-capacitance assumption.
- Numerical gradients calculated from noisy data can fluctuate substantially.
- The simulated data demonstrate the analysis workflow but do not constitute experimental validation.
- No quantified reduction in manual analysis time is claimed without a documented comparison of equivalent manual and automated workflows.

## Future Work

- Validate the thermal model using real experimental data.
- Document the origin of model parameters and justify their values.
- Compare numerical differentiation and smoothing methods.
- Implement automated data-quality checks and energy-balance validation.
- Benchmark manual and automated processing time using a reproducible procedure.
- Extend the workflow to additional heat-transfer conditions and operating profiles.
