# CODIGO

# INFORMACION SENSIBLE --> DB, HOST, USERNAME, PASSWORD

# script para generar informacion

# Funciones para ingresar datos

# --- La persona ingresa cantidad de nuevos usuarios, cantidad de nuevas transacciones, ingresar datos de producto

cache = []

for x in range(5):

    if len(cache) == 0:
        cache = request.get("SELECT id FROM service master")

    f"INSERT INTO transactions SET({service_id, })"

    pass

# ---------------------------------------
import random
from faker import Faker
import base64

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

        print(f"INSERT INTO User (Username, Password, Mail, Birth Date, Gender) VALUES ('{username}', '{encoded_password}', '{email}', '{birth_date}', '{gender}');")

random_to_users(5) 