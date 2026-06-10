import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        sslmode=os.getenv("DB_SSLMODE")
    )

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY,
            title TEXT,
            price NUMERIC,
            rating NUMERIC,
            num_ratings INTEGER,
            url TEXT,
            photo TEXT,
            keyword TEXT,
            fetched_at TIMESTAMP DEFAULT NOW()
        )
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("Table created successfully.")

def load_products(df, keyword):
    conn = get_connection()
    cur = conn.cursor()
    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO products 
            (title, price, rating, num_ratings, url, photo, keyword)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            row["product_title"], row["product_price"],
            row["product_star_rating"], row["product_num_ratings"],
            row["product_url"], row["product_photo"], keyword
        ))
    conn.commit()
    cur.close()
    conn.close()
    print(f"Loaded {len(df)} products into database.")

# Test it
if __name__ == "__main__":
    from fetch import fetch_products
    from clean import clean_products
    raw = fetch_products("laptop")
    df = clean_products(raw)
    create_table()
    load_products(df, "laptop")