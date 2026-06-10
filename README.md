# 🛒 E-Commerce Product Insight Engine

A real-time data pipeline that fetches live Amazon India product data, stores it in a cloud PostgreSQL database, and generates AI-powered business insights using Groq LLaMA 3.

🔗 **Live Demo**: https://ecommerce-insight-engine.streamlit.app

---

## 🏗️ Architecture

```
Amazon API (RapidAPI) → ETL Pipeline (Python) → PostgreSQL (Aiven Cloud) → AI Analysis (Groq LLaMA 3) → Streamlit Dashboard
```

---

## ✨ Features

- **Live Data Fetching** — Pulls real-time Amazon India product data for any search keyword
- **Automated ETL Pipeline** — Cleans, transforms, and loads data into cloud-hosted PostgreSQL
- **AI Business Insights** — Groq LLaMA 3 analyzes pricing and rating trends to generate actionable seller recommendations
- **Interactive Dashboard** — Search any product category and get instant data + insights
- **Cloud Database** — Data persisted in PostgreSQL hosted on Aiven with SSL encryption

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Data Source | RapidAPI Real-Time Amazon Data |
| ETL | Python, Pandas |
| Database | PostgreSQL 17 (Aiven Cloud) |
| AI/LLM | Groq LLaMA 3 (llama-3.3-70b-versatile) |
| Dashboard | Streamlit |
| Deployment | Streamlit Cloud |

---

## 📁 Project Structure

```
ecommerce-insight-engine/
│
├── etl/
│   ├── fetch.py            # Fetches product data from Amazon API
│   ├── clean.py            # Cleans and transforms raw data
│   └── load.py             # Loads data into PostgreSQL
│
├── analysis/
│   └── gemini_insights.py  # Groq LLaMA 3 insight generation
│
├── dashboard/
│   └── app.py              # Streamlit dashboard
│
├── requirements.txt
└── README.md
```

---

## 🚀 Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/shrfr/ecommerce-insight-engine.git
cd ecommerce-insight-engine
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set up environment variables**

Create a `.env` file in the root:
```
RAPIDAPI_KEY=your_rapidapi_key
GROQ_API_KEY=your_groq_key
DB_HOST=your_aiven_host
DB_PORT=your_port
DB_NAME=defaultdb
DB_USER=avnadmin
DB_PASSWORD=your_password
DB_SSLMODE=require
```

**4. Run the dashboard**
```bash
streamlit run dashboard/app.py
```

---

## 💡 Sample Insights Generated

For keyword **"laptop"**:
- Dominant price segment: ₹34,515 – ₹52,911 (25th–75th percentile)
- No clear correlation between price and ratings — brand reputation matters more
- Refurbished laptops are top-rated, indicating strong demand for affordable quality
- Recommendation: Enter the ₹30,000–₹45,000 segment with strong customer service focus

---

## 🔑 API Keys Required

| Service | Free Tier | Link |
|---|---|---|
| RapidAPI (Amazon Data) | 100 requests/month | rapidapi.com |
| Groq | Generous free tier | console.groq.com |
| Aiven PostgreSQL | Free 1GB instance | aiven.io |

---

## 👩‍💻 Author

**Shreya Bhattacharjee**  
B.Tech Information Technology, KIIT University  
[LinkedIn](www.linkedin.com/in/shreya-bhattacharjee-b648a9228) · [GitHub](https://github.com/shrfr)