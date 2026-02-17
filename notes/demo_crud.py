import mysql.connector



# ============================================================
# DATABASE CONNECTION
# ============================================================
try:
    conn = mysql.connector.connect(
        host="127.0.0.1",          # MySQL running locally
        user="root",               # MySQL username
        password="#Ayush2003",      # MySQL password
        database="flights"         # Database shown in Workbench
    )
    cursor = conn.cursor()
    print("✅ Connection established with flights database")
except Exception as e:
    print("❌ Connection error:", e)
    exit()





# ============================================================
# READ: FETCH SOME FLIGHT RECORDS
# ============================================================
print("\n📌 Fetching first 5 flight records...\n")

cursor.execute("""
SELECT flight_id, airline, source, destination, price
FROM flights
LIMIT 5
""")

rows = cursor.fetchall()

for row in rows:
    print(row)




# ============================================================
# UPDATE: UPDATE PRICE OF A FLIGHT (DEMO)
# ============================================================
print("\n📌 Updating price for a demo flight...\n")

cursor.execute("""
UPDATE flights
SET price = price + 500
WHERE flight_id = 1
""")

conn.commit()
print("✅ Price updated successfully")




# ============================================================
# VERIFY UPDATE
# ============================================================
cursor.execute("""
SELECT flight_id, airline, price
FROM flights
WHERE flight_id = 1
""")

print("\n📌 Updated flight record:")
print(cursor.fetchone())





# ============================================================
# DELETE: DELETE A FLIGHT RECORD (OPTIONAL DEMO)
# ⚠️ COMMENT THIS OUT IF YOU DON'T WANT TO DELETE DATA
# ============================================================
# print("\n📌 Deleting a demo flight record...\n")
#
# cursor.execute("""
# DELETE FROM flights
# WHERE flight_id = 9999
# """)
#
# conn.commit()
# print("✅ Flight deleted (if existed)")






# ============================================================
# FINAL CHECK: TOTAL NUMBER OF FLIGHTS
# ============================================================
cursor.execute("""
SELECT COUNT(*) FROM flights
""")

print("\n📊 Total flights in database:", cursor.fetchone()[0])

# ============================================================
# CLOSE CONNECTION
# ============================================================
cursor.close()
conn.close()
print("\n🔒 Database connection closed")
