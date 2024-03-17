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

def random_to_users(iterations):
    fake = Faker()

    id = 0
    genders = ['Male', 'Female']
    email_domains = ['@gmail.com', '@hotmail.com.ar', '@hotmail.com', '@yahoo.com.ar', '@itba.edu.ar', 'yahoo.com']

    for _ in range(iterations):
        id += 1
        username = fake.user_name()
        password = fake.password()
        email_domain = random.choice(email_domains)
        email = f"{username}{email_domain}"
        birth_date = fake.date_of_birth(minimum_age=18, maximum_age=74)
        gender = random.choice(genders)

        print(f"INSERT INTO User (ID, Username, Password, Mail, Birth Date, Gender) VALUES ('{id}', '{username}', '{password}', '{email}', '{birth_date}', '{gender}');")

random_to_users(5) 
