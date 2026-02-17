# ✈️ Flight Analytics Dashboard (Python + MySQL + Streamlit)

## 📌 Project Overview

This project is an **end-to-end Flight Analytics Dashboard** built using **Python, MySQL, and Streamlit**.

The objective of this project is to:
- Store real flight data in a **SQL database**
- Perform analytics using **SQL queries**
- Visualize insights through an **interactive dashboard**

This project follows a **proper data engineering + analytics workflow**, not just CSV-based plotting.

---

## 🧠 Why This Project Matters

✔ Demonstrates SQL database design  
✔ Shows one-time data ingestion (CSV → MySQL)  
✔ Clean separation of concerns (ingestion, queries, UI)  
✔ Interactive dashboard with real data  
✔ Interview-ready real-world project  

---

## 🛠️ Tech Stack Used

- Python  
- MySQL (Workbench)  
- Streamlit  
- Pandas  
- Plotly  
- mysql-connector-python  

---

## 📂 Project Structure

Flights-Dashboard/
│
├── app.py # Streamlit dashboard
├── dbhelper.py # Database query layer
├── crud.py # One-time CSV → MySQL ingestion
├── config.py # Database configuration
├── requirements.txt
│
├── content/
│ └── flights_cleaned - flights_cleaned.csv
│
└── sql/
└── schema.sql # Database & table creation



---

## 🔁 Complete Project Workflow

### 1️⃣ Database Setup (MySQL Workbench)
- Created `flights` database
- Created `flights` table using `schema.sql`
- Defined proper schema and indexes

---

### 2️⃣ Data Ingestion (CSV → MySQL)
- Used `crud.py` to:
  - Read cleaned CSV data
  - Handle mixed date formats
  - Insert records into MySQL
- This step is executed **only once**

---

### 3️⃣ Database Query Layer
- `dbhelper.py` handles all SQL queries:
  - Fetch city names
  - Fetch flights between cities
  - Airline frequency
  - Busiest airport analysis
  - Daily flight count
- Uses parameterized queries for safety

---

### 4️⃣ Streamlit Dashboard
- `app.py` builds the interactive dashboard
- Dashboard fetches data **directly from MySQL**
- No CSV is used at runtime

---

## 📊 Dashboard Features

### 🔹 View Flights Between Cities
- Dropdown option: **View Flights**
- User selects:
  - Source city
  - Destination city
- Flights between selected cities are displayed in a table

---

### 🔹 Airline Market Share (Pie Chart)
- Pie chart showing:
  - Number of flights per airline
- Helps understand airline dominance

---

### 🔹 Busiest Airport Analysis (Bar Chart)
- Bar chart showing:
  - Most busy airports (combined source & destination)
- Highlights high traffic cities

---

### 🔹 Daily Number of Flights Analysis
- Line chart showing:
  - Daily count of flights
- Can be extended with airline filters

---

## ▶️ How to Run This Project

### 1️⃣ Create & Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

streamlit run app.py
