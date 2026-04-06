import sqlite3
from car import Car

def get_connection():
    return sqlite3.connect("cars.db")

def initialize_database():
    conn = sqlite3.connect("cars.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            make TEXT NOT NULL,
            model TEXT NOT NULL,
            year INTEGER NOT NULL,
            price REAL NOT NULL,
            mileage INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def import_cars():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM cars")
    count = cursor.fetchone()[0]

    if count > 0:
        print(f"ℹ️ Import skipped - {count} cars already in database.")
        conn.close()
        return
    
    sample_cars = [
        ("Toyota", "Camry", 2021, 24999.99, 15000),
        ("Honda", "Civic", 2020, 19500.00, 32000),
        ("Ford", "Mustang", 2019, 31750.50, 45000),
        ("Chevrolet", "Silverado", 2022, 42000.00, 8000),
        ("BMW", "3 Series", 2021, 45999.99, 12000),
        ("Tesla", "Model 3", 2023, 52000.00, 3000),
        ("Nissan", "Altima", 2018, 14800.00, 61000),
        ("Hyundai", "Tucson", 2022, 29500.00, 11000),
        ("Mazda", "CX-5", 2020, 26300.75, 27000),
        ("Volkswagen", "Jetta", 2019, 17999.00, 38000),

    ]

    cursor.executemany(
        "INSERT INTO cars (make, model, year, price, mileage) VALUES (?, ?, ?, ?, ?)",
        sample_cars
    )

    conn.commit()
    conn.close()

    print(f"✅ {len(sample_cars)} sample cars imported successfully!")

def add_car(car):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO cars (make, model, year, price, mileage) VALUES (?, ?, ?, ?, ?)",
        car.to_tuple()
    )

    car.id = cursor.lastrowid

    conn.commit()
    conn.close()

def get_all_cars():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM cars ORDER BY id")
    rows = cursor.fetchall()

    conn.close()

    return [Car(id=row[0], make=row[1], model=row[2],
                year=row[3], price=row[4], mileage=row[5])
                for row in rows]

def get_car_by_id(car_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM cars WHERE id = ?", (car_id,))
    row = cursor.fetchone()

    conn.close()

    if row is None:
        return None
    
    return Car(id=row[0], make=row[1], model=row[2],
               year=row[3], price=row[4], mileage=row[5])

def update_car(car):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE cars SET make=?, model=?, year=?, price=?, mileage=? WHERE id=?",
        (*car.to_tuple(), car.id)
    )

    conn.commit()
    conn.close()

def delete_car(car_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cars WHERE id = ?", (car_id,))

        conn.commit()

def search_cars(keyword):

    conn = get_connection()
    cursor = conn.cursor()

    pattern = f"%{keyword.lower()}%"

    cursor.execute("""
        SELECT * FROM cars
        WHERE LOWER(make) LIKE ?
        OR LOWER(model) LIKE ?
        OR CAST(year AS TEXT) LIKE ?
    """, (pattern, pattern, pattern))

    rows = cursor.fetchall()
    conn.close()

    return [Car(id=row[0], make=row[1], model=row[2],
                year=row[3], price=row[4], mileage=row[5])
                for row in rows]
