import sqlite3
import os

print("▶ Starting script...")

if not os.path.exists('schema.sql'):
    print("❌ schema.sql not found in this folder.")
    exit()

print("✅ Found schema.sql")

conn = sqlite3.connect('video_tracker.db')
cursor = conn.cursor()

try:
    with open('schema.sql', 'r') as f:
        schema_sql = f.read()
        cursor.executescript(schema_sql)
        print("✅ Schema loaded into database.")
except Exception as e:
    print(f"❌ Failed to load schema: {e}")
    conn.close()
    exit()

try:
    cursor.execute("INSERT INTO clients (name, email, company) VALUES (?, ?, ?)", 
                   ("Denise Tan", "denise@email.com", "PropertyGuru"))
    cursor.execute("INSERT INTO projects (client_id, title, start_date, status, phase) VALUES (?, ?, ?, ?, ?)", 
                   (1, "Normanton Park Tour", "2025-08-05", "In Progress", "Offline Edit"))
    cursor.execute("INSERT INTO deliverables (project_id, version, delivery_date, feedback, approved) VALUES (?, ?, ?, ?, ?)", 
                   (1, "v1", "2025-08-06", "Trim intro by 5 seconds", 0))
    print("✅ Sample data inserted.")
except Exception as e:
    print(f"❌ Failed to insert data: {e}")
    conn.close()
    exit()

try:
    cursor.execute("""
    SELECT p.title, c.name, p.phase, p.status
    FROM projects p
    JOIN clients c ON p.client_id = c.client_id
    WHERE p.status = 'In Progress'
    """)
    
    rows = cursor.fetchall()
    if rows:
        print("📊 In-Progress Projects:")
        for row in rows:
            print(f"→ Project: {row[0]} | Client: {row[1]} | Phase: {row[2]} | Status: {row[3]}")
    else:
        print("ℹ️ No in-progress projects found.")
except Exception as e:
    print(f"❌ Failed to run query: {e}")

conn.commit()
conn.close()