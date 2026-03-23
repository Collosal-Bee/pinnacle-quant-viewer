# 🏆 Pinnacle Quant Studio (Walk-Forward Optimization Engine)

**Pinnacle Quant Studio** is a proprietary algorithmic sports betting engine designed to process high-volume historical odds data, identify mispriced markets, and simulate capital allocation using fractional Kelly criterion staking. 

> 🔒 **Note:** The core WFO optimization algorithms and raw datasets are housed in a private repository to protect the intellectual property of the model. This public repository contains the architecture breakdown and a lightweight Viewer App showcasing the out-of-sample results.

## 🧠 The Architecture & Tech Stack
To bypass hardware limitations when running Pandas optimizations on massive historical datasets, the architecture was explicitly decoupled:
* **Data Storage:** Raw data is partitioned by betting market into highly compressed `.parquet` files for rapid I/O memory loading.
* **Compute Engine:** Optuna handles hyperparameter tuning using strict Walk-Forward Optimization (WFO) to prevent historical overfitting.
* **Frontend Visualization:** A decoupled Streamlit UI powered by Plotly for granular equity curve rendering and Monte Carlo stress testing.

## ⚙️ Core Modules Built
1. **The Fast Track (1M/1M) Engine:** Analyzes short-term form by training on 30 days of data and testing strictly on the subsequent 30 days.
2. **The Seasonality Engine:** Temporal data stitcher that isolates specific months across multiple years to exploit bookmaker pricing lags.
3. **The "Buy the Dip" Engine:** A mean-reversion algorithm that identifies historically profitable strategies currently experiencing mathematical variance (short-term drawdown) while maintaining positive Closing Line Value (CLV).
