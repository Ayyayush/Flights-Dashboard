import streamlit as st
import pandas as pd
from dbhelper import DB
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Flight Price & Analytics Dashboard", layout="wide")
db = DB()

st.sidebar.title("✈️ Flights Analytics")
menu = st.sidebar.selectbox("Menu", ["Home", "Check Flights", "Analytics"])

# ===================== HOME =====================
if menu == "Home":
    st.title("✈️ Flight Price & Analytics Dashboard")
    st.caption("Real-time insights powered by MySQL + Streamlit")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("✈️ Total Flights", db.total_flights())
    c2.metric("🏢 Airlines", db.total_airlines())
    c3.metric("🏙 Cities Covered", db.total_cities())
    c4.metric("💰 Avg Price (₹)", db.average_price())

    left, right = st.columns(2)

    airline, freq = db.fetch_airline_frequency()
    left.plotly_chart(px.pie(names=airline, values=freq, title="Airline Market Share"), width="stretch")

    city, freq_city = db.busy_airport()
    right.plotly_chart(px.bar(x=city[:10], y=freq_city[:10], title="Top 10 Busiest Airports"), width="stretch")

# ===================== CHECK FLIGHTS =====================
elif menu == "Check Flights":

    st.title("✈️ Check Flights Between Cities")

    source = st.selectbox("Source City", db.fetch_source_cities())
    destination = st.selectbox(
        "Destination City",
        db.fetch_destinations_by_source(source)
    )

    if st.button("Search Flights"):
        result = db.fetch_all_flights(source, destination)
        df = pd.DataFrame(result, columns=["Airline", "Route", "Departure", "Duration", "Price"])
        st.dataframe(df, width="stretch")

# ===================== ANALYTICS =====================
else:
    st.title("📊 Flight Analytics")

    airline, freq = db.fetch_airline_frequency()
    st.plotly_chart(go.Figure(go.Pie(labels=airline, values=freq)), width="stretch")

    city, freq_city = db.busy_airport()
    st.plotly_chart(px.bar(x=city, y=freq_city), width="stretch")

    date, freq_date = db.daily_frequency()
    st.plotly_chart(px.line(x=date, y=freq_date), width="stretch")
