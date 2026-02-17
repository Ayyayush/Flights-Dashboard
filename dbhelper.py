import mysql.connector
from config import DB_CONFIG

class DB:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(**DB_CONFIG)
            self.cursor = self.conn.cursor()
        except:
            raise Exception("Database connection failed")

    # ===================== KPIs =====================
    def total_flights(self):
        self.cursor.execute("SELECT COUNT(*) FROM flights")
        return self.cursor.fetchone()[0]

    def total_airlines(self):
        self.cursor.execute("SELECT COUNT(DISTINCT airline) FROM flights")
        return self.cursor.fetchone()[0]

    def total_cities(self):
        self.cursor.execute("""
            SELECT COUNT(DISTINCT city) FROM (
                SELECT source AS city FROM flights
                UNION
                SELECT destination AS city FROM flights
            ) t
        """)
        return self.cursor.fetchone()[0]

    def average_price(self):
        self.cursor.execute("SELECT ROUND(AVG(price), 0) FROM flights")
        return self.cursor.fetchone()[0]

    # ===================== DROPDOWNS =====================
    def fetch_source_cities(self):
        self.cursor.execute("SELECT DISTINCT source FROM flights")
        return sorted([row[0] for row in self.cursor.fetchall()])

    def fetch_destinations_by_source(self, source):
        self.cursor.execute(
            "SELECT DISTINCT destination FROM flights WHERE source = %s",
            (source,)
        )
        return sorted([row[0] for row in self.cursor.fetchall()])

    # ===================== FLIGHT SEARCH =====================
    def fetch_all_flights(self, source, destination):
        self.cursor.execute("""
            SELECT airline, route, dep_time, duration, price
            FROM flights
            WHERE source = %s AND destination = %s
        """, (source, destination))
        return self.cursor.fetchall()

    # ===================== ANALYTICS =====================
    def fetch_airline_frequency(self):
        self.cursor.execute("""
            SELECT airline, COUNT(*)
            FROM flights
            GROUP BY airline
        """)
        data = self.cursor.fetchall()
        return [r[0] for r in data], [r[1] for r in data]

    def busy_airport(self):
        self.cursor.execute("""
            SELECT city, COUNT(*) FROM (
                SELECT source AS city FROM flights
                UNION ALL
                SELECT destination AS city FROM flights
            ) t
            GROUP BY city
            ORDER BY COUNT(*) DESC
        """)
        data = self.cursor.fetchall()
        return [r[0] for r in data], [r[1] for r in data]

    def daily_frequency(self):
        self.cursor.execute("""
            SELECT date_of_journey, COUNT(*)
            FROM flights
            GROUP BY date_of_journey
            ORDER BY date_of_journey
        """)
        data = self.cursor.fetchall()
        return [r[0] for r in data], [r[1] for r in data]
