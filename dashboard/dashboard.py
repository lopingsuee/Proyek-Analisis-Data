import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

sns.set_theme(
    style="whitegrid",
    context="talk",
    rc={
        "grid.linestyle": "--",
        "grid.alpha": 0.6,
        "axes.edgecolor": "#333333",
        "axes.linewidth": 1
    }
)

@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["dteday"] = pd.to_datetime(df["dteday"])
    return df

df = load_data("main_data.csv")

st.title("Bike Sharing Dashboard")
st.write("Ringkasan interaktif peminjaman sepeda berdasarkan kondisi cuaca dan tipe hari.")

min_date = df["dteday"].min().date()
max_date = df["dteday"].max().date()

default_start = pd.to_datetime("2011-01-01").date()
default_end = pd.to_datetime("2011-01-31").date()

with st.sidebar:
    st.header("Filter")
    date_range = st.date_input(
        "Rentang tanggal",
        value=(default_start, default_end),
        min_value=min_date,
        max_value=max_date
    )


    weather_options = sorted([w for w in df["weather"].dropna().unique().tolist()])
    selected_weather = st.multiselect("Kondisi cuaca", options=weather_options, default=weather_options)

    day_options = ["Working Day", "Weekend", "Holiday"]
    existing_day_options = [d for d in day_options if d in df["day_type"].unique().tolist()]
    selected_day = st.multiselect("Tipe hari", options=existing_day_options, default=existing_day_options)

if isinstance(date_range, tuple) and len(date_range) == 2:
    start_date, end_date = date_range
else:
    st.warning("Silakan pilih rentang tanggal (tanggal awal dan akhir).")
    st.stop()
mask = (
    (df["dteday"].dt.date >= start_date) &
    (df["dteday"].dt.date <= end_date) &
    (df["weather"].isin(selected_weather)) &
    (df["day_type"].isin(selected_day))
)
fdf = df.loc[mask].copy()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Jumlah hari", f"{len(fdf):,}")
c2.metric("Rata-rata peminjaman (cnt)", f"{fdf['cnt'].mean():,.0f}" if len(fdf) else "0")
c3.metric("Median peminjaman (cnt)", f"{fdf['cnt'].median():,.0f}" if len(fdf) else "0")
c4.metric("Total peminjaman (cnt)", f"{fdf['cnt'].sum():,}" if len(fdf) else "0")

left, right = st.columns(2)

with left:
    st.subheader("Rata-rata Peminjaman Harian per Kondisi Cuaca")
    if len(fdf) == 0:
        st.info("Tidak ada data pada filter yang dipilih.")
    else:
        weather_avg = (
            fdf.groupby("weather")["cnt"]
               .mean()
               .sort_values(ascending=False)
               .reset_index()
        )
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.barplot(data=weather_avg, x="weather", y="cnt", color="#4C72B0", ax=ax)
        ax.set_title("Mean Rentals by Weather")
        ax.set_xlabel("Weather")
        ax.set_ylabel("Average Rentals (cnt)")
        ax.grid(axis="y", linestyle="--", alpha=0.7)
        sns.despine(left=True, bottom=True)
        plt.tight_layout()
        st.pyplot(fig)

with right:
    st.subheader("Rata-rata Peminjaman Harian per Tipe Hari")
    if len(fdf) == 0:
        st.info("Tidak ada data pada filter yang dipilih.")
    else:
        day_order = [d for d in ["Working Day", "Weekend", "Holiday"] if d in fdf["day_type"].unique().tolist()]
        day_avg = (
            fdf.groupby("day_type")["cnt"]
               .mean()
               .reindex(day_order)
               .reset_index()
        )
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.barplot(data=day_avg, x="day_type", y="cnt", color="#55A868", ax=ax)
        ax.set_title("Mean Rentals by Day Type")
        ax.set_xlabel("Day Type")
        ax.set_ylabel("Average Rentals (cnt)")
        ax.grid(axis="y", linestyle="--", alpha=0.7)
        sns.despine(left=True, bottom=True)
        plt.tight_layout()
        st.pyplot(fig)

st.subheader("Tren Peminjaman Harian (Time Series)")
if len(fdf) == 0:
    st.info("Tidak ada data pada filter yang dipilih.")
else:
    daily = fdf.sort_values("dteday")[["dteday", "cnt"]]
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(daily["dteday"], daily["cnt"])
    ax.set_title("Daily Rentals Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Rentals (cnt)")
    ax.grid(True, linestyle="--", alpha=0.5)
    sns.despine()
    plt.tight_layout()
    st.pyplot(fig)

with st.expander("Lihat data terfilter"):
    st.dataframe(fdf.sort_values("dteday"))
