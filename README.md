# 📰 News API Analyzer

## 🚀 Project Overview

The **News API Analyzer** is a Python-based data analytics project that fetches live news articles using the NewsAPI service and performs:

* 📡 API Integration
* 🧹 Data Cleaning
* 📊 Exploratory Data Analysis (EDA)
* 🧠 Basic NLP / Text Processing
* 📈 Data Visualization
* 🤖 Automation-Style Data Workflows

This project demonstrates how real-world semi-structured API data can be transformed into meaningful business insights using Python and pandas.

---

# 🛠️ Tech Stack

| Tool / Library | Purpose                       |
| -------------- | ----------------------------- |
| Python         | Core Programming Language     |
| pandas         | Data Cleaning & Analysis      |
| requests       | API Requests                  |
| matplotlib     | Data Visualization            |
| regex (`re`)   | Text Cleaning & Preprocessing |
| NewsAPI        | Live News Data Source         |

---

# ✨ Features

✅ Fetches live news data from NewsAPI   
✅ Parses nested JSON responses  
✅ Cleans and structures raw API data  
✅ Handles missing values and duplicates  
✅ Performs keyword frequency analysis  
✅ Extracts publishing trends from datetime data  
✅ Creates professional visualizations  
✅ Exports cleaned dataset to CSV  

---

# 📂 Project Workflow

```text
NewsAPI → JSON Response → Data Cleaning → EDA → NLP Analysis → Visualizations → CSV Export
```

---

# 📊 Analysis Performed

## 🔹 Publisher Analysis

* Most active news publishers
* Article frequency by source

## 🔹 Publishing Trends

* Most active publishing hours
* Datetime feature engineering

## 🔹 Headline Keyword Analysis

* Most common keywords in headlines
* Stopword filtering
* Text preprocessing using regex

---

# 📈 Sample Visualizations

### 📌 Top News Sources

* Bar chart showing publishers with highest article counts.

### 📌 Publishing Hours Analysis

* Visualization of peak publishing activity.

### 📌 Headline Keyword Frequency

* Most commonly appearing keywords in news headlines.

---

# 🧠 Key Insights

📌 Certain publishers dominate article output within the selected news category.

📌 Publishing activity peaks during specific hours of the day.

📌 Headline keyword analysis highlights strong focus on:

* Business
* AI
* Technology
* Markets
* Pricing Trends

📌 Text preprocessing improves keyword analysis by removing punctuation and stopwords.

---

# 📁 Project Structure

```text
news-api-analyzer/
│
├── automated_news_analyzer.py
├── news_analysis.csv
├── requirements.txt
├── README.md
├── top_news_sources.png
├── publishing_hours.png
└── headline_keywords.png
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/news-api-analyzer.git
```

## 2️⃣ Navigate Into Project Folder

```bash
cd news-api-analyzer
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 API Setup

This project uses:

🌐 🗨️url⭐NewsAPI⭐[https://newsapi.org/](https://newsapi.org/)

1. Create a free account
2. Generate your API key
3. Replace:

```python
api_key = "YOUR_API_KEY"
```

with your own API key.

⚠️ Never upload your real API key publicly.

---

# ▶️ Run The Project

```bash
python automated_news_analyzer.py
```

---

# 📚 Skills Demonstrated

This project demonstrates practical experience with:

* REST APIs
* JSON Parsing
* pandas DataFrames
* Data Cleaning
* Exploratory Data Analysis
* Datetime Processing
* Basic NLP Concepts
* Regex Text Processing
* Data Visualization
* Automation Workflows

---

# 💡 Future Improvements

🔹 Sentiment Analysis
🔹 Interactive Dashboards
🔹 SQL Database Integration
🔹 Automated Reporting
🔹 Streamlit Web App Version
🔹 Scheduled Data Collection Pipelines

---

# 👨‍💻 Author

**Gaurav Yadav**

Aspiring Data Analyst | Python Enthusiast | Automation & AI Learner

---

# ⭐ If You Found This Project Interesting

Consider giving the repository a ⭐ on GitHub.
