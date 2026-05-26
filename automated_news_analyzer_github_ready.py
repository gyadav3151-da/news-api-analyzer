#!/usr/bin/env python
# coding: utf-8

# # News API Analyzer
# This project fetches live news data using NewsAPI,
# performs data cleaning and exploratory data analysis (EDA),
# extracts keyword trends from headlines, and visualizes insights.
# 
# Skills Demonstrated:
# - API Integration
# - JSON Parsing
# - Data Cleaning
# - Exploratory Data Analysis (EDA)
# - Text Processing / Basic NLP
# - Data Visualization
# - Automation Workflow
# - CSV Export
# 
# Author: Gaurav Yadav

# ## Imports

# In[1]:


# Importing Python Modules
import requests
import pandas as pd
import matplotlib.pyplot as plt
import re


# In[2]:


# =========================
# API Configuration
# =========================
api_key = "YOUR_API_KEY"
query = "Business" 

url = (
    f"https://newsapi.org/v2/everything?"
    f"q={query}&language=en&sortBy=publishedAt&apiKey={api_key}"
)

# =========================
# Fetch API Data
# =========================

response = requests.get(url)

# Check request status
if response.status_code != 200:
    raise Exception(
        f"API Request Failed | Status Code: {response.status_code}"
    )

raw_dump = response.json()

print("API Request Successful")
print(f"Total Articles Retrieved: {len(raw_dump['articles'])}")


# ## JSON Parsing

# In[3]:


clean_dump = []

for article in raw_dump["articles"]:

    clean_dump.append({
        "source": article["source"]["name"],
        "author": article["author"],
        "title": article["title"],
        "description": article["description"],
        "published_date": pd.to_datetime(article["publishedAt"]),
        "url": article["url"]
    })


# ## DataFrame Creation

# In[4]:


news_df = pd.DataFrame(clean_dump)

print("\nDataFrame Created Successfully")
print(news_df.head())


# ## Data Inspection

# In[5]:


print("\n========== DATAFRAME INFO ==========")
print(news_df.info())

print("\n========== NULL VALUES ==========")
print(news_df.isna().sum())

print("\n========== DUPLICATES ==========")
print(news_df.duplicated().sum())


# ## Data Cleaning

# In[6]:


# Remove duplicate articles based on title
news_df = news_df.drop_duplicates(subset="title")

# Fill missing author names
news_df["author"] = news_df["author"].fillna("unknown")

# Fill missing descriptions
news_df["description"] = news_df["description"].fillna("no description")

# Standardize string columns
string_cols = news_df.select_dtypes(include=["object", "string"]).columns

for col in string_cols:
    news_df[col] = news_df[col].str.lower().str.strip()

print("\nData Cleaning Complete")


# ## Feature Engineering

# In[7]:


news_df["publish_hour"] = news_df["published_date"].dt.hour
news_df["publish_date"] = news_df["published_date"].dt.date


# ## Exploratory Data Analysis

# In[8]:


print("\n========== TOP NEWS SOURCES ==========")
source_counts = news_df["source"].value_counts()
print(source_counts.head(10))


print("\n========== MOST ACTIVE PUBLISHING HOURS ==========")
publish_hour_counts = (
    news_df["publish_hour"]
    .value_counts()
    .sort_index()
)
print(publish_hour_counts)


# ## Basic NLP / Text Analysis

# In[9]:


# Combine all titles into one text block
all_titles = " ".join(news_df["title"].dropna())

# Remove punctuation
all_titles = re.sub(r"[^\w\s]", "", all_titles)

# Convert to lowercase and split into words
words = all_titles.lower().split()

# Common stopwords
stopwords = {
    "the", "and", "of", "to", "a", "in", "for", "on",
    "are", "his", "her", "new", "with", "after",
    "from", "at", "by", "is", "as", "an", "all"
}

# Remove stopwords and short words
words = [word for word in words if word not in stopwords and len(word) > 2]

# Word frequency counting
word_counts = {}

for word in words:

    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Convert word frequencies into DataFrame
word_count_df = (
    pd.DataFrame(
        word_counts.items(),
        columns=["word", "count"]
    )
    .sort_values(by="count", ascending=False)
)

print("\n========== TOP KEYWORDS ==========")
print(word_count_df.head(10))


# ## Visualizations

# In[10]:


# ----- Top News Sources -----

plt.figure(figsize=(12, 6))

source_counts.head(10).plot(kind="bar")

plt.title("Top News Sources")
plt.xlabel("Source")
plt.ylabel("Number of Articles")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("top_news_sources.png")
plt.show()


# In[11]:


# ----- Publishing Hours -----

plt.figure(figsize=(12, 6))

plt.bar(
    publish_hour_counts.index,
    publish_hour_counts.values
)

plt.title("Most Active Publishing Hours")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Articles")
plt.xticks(range(0, 24))

plt.tight_layout()
plt.savefig("publishing_hours.png")
plt.show()


# In[12]:


# ----- Top Keywords -----

plt.figure(figsize=(12, 6))

plt.bar(
    word_count_df.head(10)["word"],
    word_count_df.head(10)["count"]
)

plt.title("Most Common Headline Keywords")
plt.xlabel("Keyword")
plt.ylabel("Frequency")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("headline_keywords.png")
plt.show()


# ## Insights

# The most common headline keywords suggest business coverage is distributed among oil, prices and ai news.

# In[13]:


print("\n========== PROJECT INSIGHTS ==========")

# Top source insight
print(
    f"1. The most active news publisher in this dataset is "
    f"'{source_counts.idxmax()}', contributing the highest "
    f"number of articles."
)

# Publishing hour insight
print(
    f"2. News publishing activity peaks around "
    f"{publish_hour_counts.idxmax()}:00 hours, suggesting this "
    f"is a highly active publishing window."
)

# Keyword insight
print(
    f"3. The most frequently appearing keyword in headlines is "
    f"'{word_count_df.iloc[0]['word']}', indicating strong focus "
    f"on this topic in current business news coverage."
)

print(
    "4. Headline keyword analysis suggests that business news "
    "coverage is heavily centered around markets, pricing, "
    "technology, and AI-related developments."
)


# ## Export Final Dataset

# In[14]:


news_df.to_csv("news_analysis.csv", index=False)

print("\nFinal Dataset Exported Successfully")
print("Project Completed")

