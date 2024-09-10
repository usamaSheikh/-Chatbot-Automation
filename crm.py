import sqlite3

class CRM:
    def __init__(self):
        # Connect to the SQLite database
        self.conn = sqlite3.connect('chatbot_db.sqlite')
        self.cursor = self.conn.cursor()
        
        # Create leads table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT,
                phone TEXT
            )
        ''')
        self.conn.commit()

    # Add lead to the database
    def add_lead(self, name, email, phone):
        self.cursor.execute('''
            INSERT INTO leads (name, email, phone)
            VALUES (?, ?, ?)
        ''', (name, email, phone))
        self.conn.commit()

    # Retrieve all leads from the database
    def get_all_leads(self):
        self.cursor.execute("SELECT * FROM leads")
        leads = self.cursor.fetchall()
        return leads
