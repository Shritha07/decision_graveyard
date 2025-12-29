from database import get_connection

def add_decision(data):
    conn = get_connection()
    conn.execute("""
        INSERT INTO decisions (title, date, taken_path, reflection, mood)
        VALUES (?, ?, ?, ?, ?)
    """, (
        data["title"],
        data["date"],
        data["taken_path"],
        data.get("reflection", ""),
        data.get("mood", 3)
    ))
    conn.commit()
    conn.close()

def get_all_decisions():
    conn = get_connection()
    rows = conn.execute(
        "SELECT * FROM decisions ORDER BY date DESC"
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]
