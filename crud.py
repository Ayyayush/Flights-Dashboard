import mysql.connector
import pandas as pd

# ============================================================
# DATABASE CONNECTION
# ============================================================
try:
    conn = mysql.connector.connect(
        host="127.0.0.1",              # Local MySQL server
        user="root",                   # MySQL username
        password="#Ayush2003",          # MySQL password
        database="flights"             # Database name
    )
    cursor = conn.cursor()
    print("✅ Connected to flights database")
except Exception as e:
    print("❌ Database connection failed:", e)
    exit()

# ============================================================
# READ CSV FILE
# ============================================================
try:
    df = pd.read_csv("content/flights_cleaned - flights_cleaned.csv")
    print(f"📄 CSV loaded successfully with {len(df)} rows")
except Exception as e:
    print("❌ Error reading CSV:", e)
    conn.close()
    exit()

# ============================================================
# CLEAN & TRANSFORM DATA
# ============================================================

# Convert mixed-format dates safely
df["Date_of_Journey"] = pd.to_datetime(
    df["Date_of_Journey"],
    errors="coerce"
).dt.date

# Drop rows where date conversion failed (safety)
df = df.dropna(subset=["Date_of_Journey"])

# ============================================================
# SQL INSERT QUERY
# ============================================================
insert_query = """
INSERT INTO flights (
    airline,
    route,
    source,
    destination,
    dep_time,
    duration,
    price,
    date_of_journey
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

# ============================================================
# PREPARE DATA FOR INSERTION
# ============================================================
data = []

for _, row in df.iterrows():
    data.append((
        row["Airline"],            # Airline name
        row["Route"],              # Route
        row["Source"],             # Source city
        row["Destination"],        # Destination city
        row["Dep_Time"],           # Departure time
        row["Duration"],           # Flight duration
        int(row["Price"]),         # Ticket price
        row["Date_of_Journey"]     # Journey date (cleaned)
    ))

# ============================================================
# EXECUTE INSERT
# ============================================================
try:
    cursor.executemany(insert_query, data)
    conn.commit()
    print("🎉 CSV data inserted successfully into flights table")
except Exception as e:
    print("❌ Error inserting data:", e)
    conn.rollback()
    conn.close()
    exit()

# ============================================================
# VERIFY INSERTION
# ============================================================
cursor.execute("SELECT COUNT(*) FROM flights")
total_rows = cursor.fetchone()[0]
print(f"📊 Total rows in flights table: {total_rows}")

# ============================================================
# CLOSE CONNECTION
# ============================================================
cursor.close()
conn.close()
print("🔒 Database connection closed")
