import sqlite3

# Create a temporary in-memory database for this demonstration.
connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL
    )
""")

cursor.executemany(
    "INSERT INTO users (username) VALUES (?)",
    [("alice",), ("bob",), ("charlie",)]
)

def unsafe_search(username):
    """Demonstrate why concatenating user input into SQL is unsafe."""
    query = (
        "SELECT username FROM users "
        f"WHERE username = '{username}'"
    )
    try:
        cursor.execute(query)
        return [row[0] for row in cursor.fetchall()]
    except sqlite3.Error as error:
        return f"Database error: {error}"

def safe_search(username):
    """Use a parameterized query to treat input as data."""
    cursor.execute(
        "SELECT username FROM users WHERE username = ?",
        (username,)
    )
    return [row[0] for row in cursor.fetchall()]

print("=== SQL Injection Prevention Demo ===")

normal_input = "alice"
test_input = "' OR '1'='1' --"

print("\n1. Normal input:", normal_input)
print("Unsafe query result:", unsafe_search(normal_input))
print("Safe query result:", safe_search(normal_input))

print("\n2. SQL-like test input:", test_input)
print("Unsafe query result:", unsafe_search(test_input))
print("Safe query result:", safe_search(test_input))

print("\nConclusion:")
print("Parameterized queries treat user input as data,")
print("rather than allowing it to change SQL query logic.")

connection.close()
