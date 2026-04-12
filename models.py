import sqlite3
from datetime import datetime

class Store:
    def __init__(self, name, location):
        self.name = name
        self.location = location

class FoodItem:
    def __init__(self, name, price, store_id, date_recorded=None):
        self.name = name
        self.price = price
        self.store_id = store_id
        self.date_recorded = date_recorded or datetime.now().strftime('%Y-%m-%d')

class PriceTracker:
    def __init__(self, db_name='food_prices.db'):
        self.db_name = db_name
        self.create_tables()

    def create_tables(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS stores (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                location TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS food_items (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                store_id INTEGER,
                date_recorded TEXT,
                FOREIGN KEY (store_id) REFERENCES stores (id)
            )
        ''')
        conn.commit()
        conn.close()

    def add_store(self, name, location):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO stores (name, location) VALUES (?, ?)', (name, location))
        conn.commit()
        conn.close()

    def get_stores(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, location FROM stores')
        stores = cursor.fetchall()
        conn.close()
        return stores

    def add_food_item(self, name, price, store_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO food_items (name, price, store_id, date_recorded) VALUES (?, ?, ?, ?)',
                       (name, price, store_id, datetime.now().strftime('%Y-%m-%d')))
        conn.commit()
        conn.close()

    def get_food_items(self, store_id=None):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        if store_id:
            cursor.execute('''
                SELECT fi.name, fi.price, fi.date_recorded, s.name
                FROM food_items fi
                JOIN stores s ON fi.store_id = s.id
                WHERE fi.store_id = ?
                ORDER BY fi.date_recorded DESC
            ''', (store_id,))
        else:
            cursor.execute('''
                SELECT fi.name, fi.price, fi.date_recorded, s.name
                FROM food_items fi
                JOIN stores s ON fi.store_id = s.id
                ORDER BY fi.date_recorded DESC
            ''')
        items = cursor.fetchall()
        conn.close()
        return items

    def get_average_price(self, item_name):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT price FROM food_items WHERE name = ?', (item_name,))
        prices = cursor.fetchall()
        conn.close()
        if prices:
            return sum(p[0] for p in prices) / len(prices)
        return None