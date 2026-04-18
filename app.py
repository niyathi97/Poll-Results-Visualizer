import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(page_title="Poll Results Visualizer", layout="wide")

st.title("📊 Poll Results Visualizer (Mental Health Survey)")

# -------------------------
# LOAD DATA
# -------------------------
df = pd.read_csv("data/survey_results_public.csv")

# Cleaning
df = df.dropna()

# -------------------------
# SIDEBAR FILTERS
# -------------------------
st.sidebar.header("🔍 Filters")

countries = st.sidebar.multiselect(
    "Select Country",
    df['Country'].unique(),
    default=df['Country'].unique()[:5]
)

genders = st.sidebar.multiselect(
    "Select Gender",
    df['Gender'].unique(),
    default=df['Gender'].unique()
)

filtered_df = df[
    (df['Country'].isin(countries)) &
    (df['Gender'].isin(genders))
]

# -------------------------
# KPI CARDS
# -------------------------
st.subheader("📌 Key Insights")

col1, col2, col3 = st.columns(3)

col1.metric("Total Responses", len(filtered_df))
col2.metric("Countries", filtered_df['Country'].nunique())
col3.metric("Avg Age", int(filtered_df['Age'].mean()))

# -------------------------
# TREATMENT ANALYSIS
# -------------------------
st.subheader("🧠 Treatment Seeking Analysis")

treatment = filtered_df['treatment'].value_counts()

fig1 = px.pie(
    values=treatment.values,
    names=treatment.index,
    title="Treatment Seeking (Yes/No)"
)

st.plotly_chart(fig1, use_container_width=True)

# -------------------------
# WORK INTERFERENCE
# -------------------------
st.subheader("💼 Work Interference Due to Mental Health")

work = filtered_df['work_interfere'].value_counts()

fig2 = px.bar(
    x=work.index,
    y=work.values,
    title="Work Interference Levels"
)

st.plotly_chart(fig2, use_container_width=True)

# -------------------------
# GENDER DISTRIBUTION
# -------------------------
st.subheader("👥 Gender Distribution")

gender = filtered_df['Gender'].value_counts()

fig3 = px.bar(
    x=gender.index,
    y=gender.values,
    title="Gender Count"
)

st.plotly_chart(fig3, use_container_width=True)

# -------------------------
# COUNTRY DISTRIBUTION
# -------------------------
st.subheader("🌍 Top Countries")

country = filtered_df['Country'].value_counts().head(10)

fig4 = px.bar(
    x=country.index,
    y=country.values,
    title="Top Countries"
)

st.plotly_chart(fig4, use_container_width=True)

# -------------------------
# AGE DISTRIBUTION
# -------------------------
st.subheader("🎯 Age Distribution")

fig5 = px.histogram(
    filtered_df,
    x='Age',
    title="Age Distribution"
)

st.plotly_chart(fig5, use_container_width=True)

# -------------------------
# RAW DATA
# -------------------------
if st.checkbox("Show Raw Data"):
    st.dataframe(filtered_df)