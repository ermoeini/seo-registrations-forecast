import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import plotly.graph_objects as go

st.set_page_config(page_title="SEO Registrations Forecast", layout="wide")
st.title("SEO Non-Branded Registrations: 1403 vs 1404 Forecast")

uploaded = st.file_uploader("Upload CSV (columns: year, month, registrations)", type=["csv"])
if uploaded is None:
    st.info("Upload a CSV file to continue.")
    st.stop()

# Read CSV
df = pd.read_csv(uploaded)
df = df.astype({"year": int, "month": int, "registrations": int})

st.write("### Data Preview")
st.dataframe(df.head())

# Helper: ensure full 12 months
def ensure_full_year(year, df):
    months = pd.DataFrame({"month": range(1, 13)})
    sub = df[df["year"] == year].set_index("month").reindex(range(1, 13), fill_value=0).reset_index()
    sub["year"] = year
    return sub[["year", "month", "registrations"]]

df_1403 = ensure_full_year(1403, df)
df_1404 = ensure_full_year(1404, df)

# Forecasting method selector
method = st.selectbox(
    "Select Forecasting Method",
    ["Linear Regression", "Moving Average", "Naïve (Last Value)"]
)

# Forecast next 6 months for 1404 (7–12)
train = df_1404[df_1404["month"] <= 6]

if method == "Linear Regression":
    X = train["month"].values.reshape(-1, 1)
    y = train["registrations"].values
    model = LinearRegression()
    model.fit(X, y)
    future_months = np.arange(7, 13).reshape(-1, 1)
    y_pred = model.predict(future_months)

elif method == "Moving Average":
    window = 3 if len(train) >= 3 else len(train)
    avg = train["registrations"].rolling(window=window).mean().iloc[-1]
    y_pred = np.repeat(avg, 6)

elif method == "Naïve (Last Value)":
    last_val = train["registrations"].iloc[-1]
    y_pred = np.repeat(last_val, 6)

y_pred = np.maximum(y_pred, 0)  # avoid negatives

forecast_1404 = pd.DataFrame({
    "year": [1404] * 6,
    "month": range(7, 13),
    "registrations": y_pred.round(1),
    "type": "forecast"
})

# --- Trendline only for 1403 ---
X_1403 = df_1403["month"].values.reshape(-1, 1)
y_1403 = df_1403["registrations"].values
lr = LinearRegression()
lr.fit(X_1403, y_1403)
trend_1403 = lr.predict(np.array(range(1, 13)).reshape(-1, 1))

# --- Plot ---
fig = go.Figure()

# 1403 actual
fig.add_trace(go.Scatter(
    x=df_1403["month"], y=df_1403["registrations"],
    mode="lines+markers", name="1403 Actual",
    line=dict(width=3, color="blue")
))

# 1403 trendline
fig.add_trace(go.Scatter(
    x=df_1403["month"], y=trend_1403,
    mode="lines", name="1403 Trend",
    line=dict(dash="dot", color="blue", width=2),
    opacity=0.4
))

# 1404 actual (months 1–6)
fig.add_trace(go.Scatter(
    x=train["month"], y=train["registrations"],
    mode="lines+markers", name="1404 Actual (1–6)",
    line=dict(width=3, color="orange")
))

# 1404 forecast (months 6–12) → start from last actual point
forecast_with_anchor = pd.concat([
    train.tail(1),  # month 6 actual
    forecast_1404   # months 7–12 forecast
])

fig.add_trace(go.Scatter(
    x=forecast_with_anchor["month"], y=forecast_with_anchor["registrations"],
    mode="lines+markers", name=f"1404 Forecast (6–12) - {method}",
    line=dict(width=2, dash="dash", color="red")
))

fig.update_layout(
    title=f"SEO Registrations: 1403 vs 1404 ({method} Forecast)",
    xaxis_title="Month (1–12)",
    yaxis_title="Registrations",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

st.plotly_chart(fig, use_container_width=True)

# Show forecast table
st.subheader("Forecast for 1404 (Months 7–12)")
st.dataframe(forecast_1404[["year", "month", "registrations"]])

csv_download = forecast_1404.to_csv(index=False)
st.download_button("Download Forecast CSV", csv_download, file_name="1404_forecast.csv")
