import json
import psycopg2
import random
from faker import Faker
import base64

secrets = json.load(open('secrets.json'))

host = secrets["HOST"]
database = secrets["DATABASE"]
user = secrets["USERNAME"]
password = secrets["PASSWORD"]

conn = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password
)

cursor = conn.cursor()

def random_to_users(iterations):
    fake = Faker()

    genders = ['Male', 'Female']
    email_domains = ['@gmail.com', '@hotmail.com.ar', '@hotmail.com', '@yahoo.com.ar', '@itba.edu.ar', 'yahoo.com']

    for _ in range(iterations):

        username = fake.user_name()
        password = fake.password()
        encoded_password = base64.b64encode(password.encode()).decode()
        email_domain = random.choice(email_domains)
        email = f"{username}{email_domain}"
        birth_date = fake.date_of_birth(minimum_age=18, maximum_age=74)
        gender = random.choice(genders)

        sql = f"INSERT INTO users (username, password, mail, birthdate, Gender) VALUES (%s, %s, %s, %s, %s)"
        values = (username, encoded_password, email, birth_date, gender)
        cursor.execute(sql, values)
        conn.commit()

        print(f"Usuario creado exitosamente: {username}")

def insert_service():
    name = input("Ingresá un nombre del servicio: ")
    description = input("Ingresá una descripción del servicio: ")
    price = input("Insertá el valor del servicio: ")

    sql = "INSERT INTO service_master (name, description, price) VALUES (%s, %s, %s::float)"
    values = (name, description, price)
    cursor.execute(sql, values)
    conn.commit()
    print(f"Servicio insertado correctamente: {name}")

from datetime import datetime, timedelta

def random_to_transactions(quantity):
    cursor.execute("SELECT COUNT(*) FROM user")
    num_users = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM service_master")
    num_services = cursor.fetchone()[0]

    for _ in range(quantity):
        user_id = random.randint(1, num_users)
        service_id = random.randint(1, num_services)
        
        quantity = random.randint(1, 10)
        timestamp = datetime.now() - timedelta(days=random.randint(1, 30))

        timestamp_str = timestamp.strftime('%Y-%m-%d %H:%M:%S')
        
        sql = "INSERT INTO transactions (user_id, service_id, quantity, timestamp) VALUES (%s, %s, %s, %s)"
        values = (user_id, service_id, quantity, timestamp_str)
        cursor.execute(sql, values)
        conn.commit()
        print(f"Servicio insertado correctamente: {service_id}")

insert_service_manually()
random_to_users(5)
generate_random_transactions(5)

cursor.close()
conn.close()