# 📊 Job Market Trend Analyzer

A data-driven web application that scrapes remote job listings using **Selenium** and analyzes in-demand **skills** using **Python**, **Streamlit**, and **AI-powered text analysis**.

## 🚀 Features

- 🔍 Scrapes real-time remote job listings from multiple job boards.
- 📌 Filters by **location**, **company**, and **keywords**.
- 📈 Displays **top trending skills** using bar charts.
- ☁️ Generates a **Word Cloud** of frequently mentioned skills.
- 🥧 Shows a **Pie Chart** to visualize skill distribution.
- 💾 Downloads job data to CSV for further analysis.

## 🌐 Data Sources

- [RemoteOK](https://remoteok.com)
- (Add other job boards here as you integrate them)

## 📦 Technologies Used

- `Python`
- `Selenium` (for web scraping)
- `Streamlit` (for interactive dashboard)
- `BeautifulSoup` (HTML parsing)
- `matplotlib`, `pandas`, `wordcloud`

<pre> ### 📁 Project Structure ``` job-market-trend-analyzer/ │ ├── analyzer.py # Skill analysis logic ├── dashboard.py # Streamlit UI code ├── scraper.py # Selenium job scraper (multi-source capable) ├── requirements.txt # Python dependencies ├── README.md # Project overview and usage ├── data/ │ └── jobs.csv # Scraped job listings (auto-generated) ├── .gitignore └── .github/ └── workflows/ └── deploy.yaml # GitHub Actions workflow ``` </pre>