import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Pinnacle Quant Studio | Viewer", layout="wide")
st.title("🏆 Pinnacle Quant Studio: Strategy Showcase")
st.info("💡 **Note:** This is a lightweight viewer for pre-calculated walk-forward optimization strategies. The core backend engine processes 200MB+ of Parquet files via Optuna machine learning to generate these subsets.")

# 1. Strategy Selector
strategy = st.selectbox("Select Pre-Computed Strategy to View", [
    "Strategy A: The Winter Seasonality Anomaly", 
    "Strategy B: Low-Volatility Steady State"
])

# 2. Load the Static Data
@st.cache_data
def load_static_data(file_name):
    try:
        df = pd.read_csv(file_name)
        df['kickoff'] = pd.to_datetime(df['kickoff'])
        return df
    except FileNotFoundError:
        st.error(f"Could not find the file: {file_name}. Make sure it is in the 'data' folder!")
        return pd.DataFrame() # Return empty if missing

if "Seasonality" in strategy:
    df = load_static_data("data/strategy_seasonality.csv")
    description = "This strategy isolates historical performance during specific winter months, capitalizing on bookmaker mispricing of winter fatigue and scheduling congestion."
else:
    df = load_static_data("data/strategy_steadystate.csv")
    description = "This strategy prioritizes a smooth equity curve, requiring an 80% green-month ratio across a massive sample size to eliminate lucky variance."

st.markdown(f"**Strategy Logic:** {description}")

# 3. Render the Metrics & Chart Instantly (If data exists)
if not df.empty:
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Bets", len(df))
    c2.metric("Win Rate", f"{(df['result'].sum() / len(df)) * 100:.1f}%")
    c3.metric("Net Profit", f"{df['p_and_l'].sum():.2f} Units")
    c4.metric("ROI / Yield", f"{(df['p_and_l'].sum() / len(df)) * 100:.2f}%")

    # The Equity Curve
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['kickoff'], y=df['running_bankroll'], mode='lines', name='Bankroll', line=dict(color='#00FF00', width=2)))
    fig.update_layout(title="Simulated Bankroll Growth (Out of Sample)", template="plotly_dark", height=400)
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Bet History (Sample)")
    st.dataframe(df[['kickoff', 'competition_type', 'opening_odds', 'probability', 'result', 'p_and_l']].head(100), use_container_width=True)