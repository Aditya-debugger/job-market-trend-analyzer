import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from analyzer import analyze_skills

# MUST be the first Streamlit call
st.set_page_config(page_title="Job Market Trend Analyzer", layout="wide")

# Title
st.title("📊 Job Market Trend Analyzer")
st.markdown("Analyze remote job listings using AI + Web Scraping")

# Load job data
df = pd.read_csv("data/jobs.csv")

# Sidebar Filters
with st.sidebar:
    st.header("🔍 Filter Jobs")
    location = st.multiselect("Filter by Location", options=df["Location"].unique())
    company = st.multiselect("Filter by Company", options=df["Company"].unique())
    keyword = st.text_input("Search Keyword")

# Apply filters
filtered_df = df.copy()
if location:
    filtered_df = filtered_df[filtered_df["Location"].isin(location)]
if company:
    filtered_df = filtered_df[filtered_df["Company"].isin(company)]
if keyword:
    filtered_df = filtered_df[filtered_df["Title"].str.contains(keyword, case=False, na=False)]

# Reset index to start from 1
filtered_df.reset_index(drop=True, inplace=True)
filtered_df.index += 1

# Job Listings Table
st.subheader("🧾 Job Listings")
st.dataframe(filtered_df[["Title", "Company", "Location", "Salary", "Tags"]].head(20))

# Analyze Skills
skill_df = analyze_skills()

# Bar Chart - Trending Skills
st.subheader("📈 Trending Skills (Top 10)")
st.bar_chart(skill_df.head(10).set_index("Skill"))

# Pie Chart - Skill Distribution
st.subheader("📊 Skill Frequency Pie Chart")
fig_pie, ax_pie = plt.subplots(figsize=(8, 6))
top_skills = skill_df.head(10)

# Group "Other" skills if more than 5
if len(top_skills) > 5:
    top_skills = pd.concat([
        top_skills.head(5),
        pd.DataFrame([{
            "Skill": "Other",
            "Frequency": top_skills["Frequency"].iloc[5:].sum()
        }])
    ])

# Pie chart with clear labels and no overlap
wedges, texts, autotexts = ax_pie.pie(
    top_skills["Frequency"],
    labels=top_skills["Skill"],
    autopct="%1.1f%%",
    startangle=140,
    textprops={'fontsize': 11},
    pctdistance=0.85,
    labeldistance=1.2
)

for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_color('black')
    autotext.set_weight("bold")

ax_pie.axis("equal")
st.pyplot(fig_pie)

# Word Cloud
st.subheader("☁️ Word Cloud of Skills")
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="white"
).generate_from_frequencies(dict(zip(skill_df["Skill"], skill_df["Frequency"])))

fig_wc, ax_wc = plt.subplots(figsize=(10, 4))
ax_wc.imshow(wordcloud, interpolation="bilinear")
ax_wc.axis("off")
st.pyplot(fig_wc)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "© 2025 Job Market Trend Analyzer — Powered by Selenium, Streamlit, and BeautifulSoup."
    "</div>",
    unsafe_allow_html=True
)
