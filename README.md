# 🏆 Pinnacle Quant Studio (Walk-Forward Optimization Engine)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pquant.streamlit.app)

**Pinnacle Quant Studio** is a proprietary algorithmic sports betting engine designed to process high-volume historical odds data, identify mispriced markets, and simulate capital allocation using flat or fractional Kelly criterion staking. 

> 🔒 **Note:** The core Walk-Forward Optimization (WFO) algorithms, Parquet pipelines, and raw datasets are housed in a private repository to protect the intellectual property of the model. This public repository contains the architecture breakdown and a lightweight Viewer App showcasing the pre-calculated, out-of-sample results.

## 🧠 The Architecture & Tech Stack
To bypass hardware limitations when running Pandas optimizations on massive historical datasets, the architecture was explicitly decoupled:
* **Data Storage:** Raw data is partitioned by betting market into highly compressed `.parquet` files for rapid I/O memory loading.
* **Compute Engine:** Optuna handles hyperparameter tuning using strict Walk-Forward Optimization to prevent historical overfitting. Hosted on a dedicated bare-metal Ubuntu Linux VPS utilizing optimized SSD Swap memory.
* **Frontend Visualization:** A decoupled Streamlit UI powered by Plotly for granular equity curve rendering and Monte Carlo stress testing.

## 📊 Visual Showcase & System Workflow

### 1. Data Ingestion & Interface Architecture
The platform ingests large-scale `.parquet` files and routes them through 5 specialized optimization engines, each designed to test different market inefficiencies. 
![Quant_Intro](https://github.com/user-attachments/assets/d504f7e3-efe0-4898-84f5-526fa553ba04)

### 2. Machine Learning & Parameter Optimization
The system utilizes Optuna to run hundreds of Walk-Forward trials, automatically filtering out strategies with high drawdown or low sample sizes. Winning parameter parameters are generated, evaluated in the Strategy Performance Report, and exported as JSON configurations.
![Core_Optimizer](https://github.com/user-attachments/assets/97689985-d558-42cf-b361-cf8923772315)

### 3. Granular Equity Analytics & Extraction
Backtested strategies are visualized through interactive Plotly dashboards, allowing for variable staking analysis (e.g., Fractional Kelly vs. Fixed Flat) across different temporal granularities. Verified out-of-sample data is then extracted via CSV for the decoupled Viewer App.
![Equity_Curve](https://github.com/user-attachments/assets/488dced9-3d5b-46c6-8617-4c2f0551737d)

## ⚙️ Core Optimization Modules Built
1. **The Fast Track (1M/1M) Engine:** Analyzes short-term form by training on 30 days of data and testing strictly on the subsequent 30 days.
2. **The Seasonality Engine:** Temporal data stitcher that isolates specific months across multiple years to exploit bookmaker pricing lags.
3. **The "Buy the Dip" Engine:** A mean-reversion algorithm that identifies historically profitable strategies currently experiencing mathematical variance while maintaining positive Closing Line Value (CLV).
4. **The Steady State Engine:** Optimizes for a high "Green Month Ratio" to identify low-volatility, consistent yield opportunities.
