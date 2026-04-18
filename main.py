import pandas as pd

print("📊 Loading Dataset...")

# Load dataset (your current file)
df = pd.read_csv("data/survey_results_public.csv")

print("\n✅ Dataset Loaded Successfully!")

print("\n📌 Available Columns:")
print(df.columns)

# -------------------------
# CLEANING
# -------------------------
df = df.drop_duplicates()
df = df.dropna()

print("\n🔍 Cleaned Data Preview:")
print(df.head())

# -------------------------
# ANALYSIS (POLL STYLE)
# -------------------------

# Treatment (Yes/No poll)
treatment = df['treatment'].value_counts()

print("\n🧠 Treatment Seeking:")
print(treatment)

# Work interference
work = df['work_interfere'].value_counts()

print("\n💼 Work Interference:")
print(work)

# Gender distribution
gender = df['Gender'].value_counts()

print("\n👥 Gender Distribution:")
print(gender)

# Country distribution
country = df['Country'].value_counts().head(10)

print("\n🌍 Top Countries:")
print(country)

# Age distribution
age = df['Age'].value_counts().head(10)

print("\n🎯 Age Distribution:")
print(age)

print("\n✅ Analysis Completed Successfully!")