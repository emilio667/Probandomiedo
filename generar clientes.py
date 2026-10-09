import json
from datetime import datetime  # <-- Cambio 1: Importación de datetime
from faker import Faker
from modelos import crear_estructura_cliente

# Inicializamos Faker con español de España (o es_MX si prefieres nombres más latinoamericanos)
fake = Faker("es_ES")
Faker.seed(67)

clientes = []

for i in range(10000):
    cliente = crear_estructura_cliente(
        id_cliente=f"CLI-{i+1:05d}",
        nombre=fake.name(),
        # fake.unique asegura que no se repitan correos en los 10,000 registros
        correo=fake.unique.email(),
        telefono=fake.numerify("8#######"),
        cedula=f"{fake.random_int(1,9)}-{fake.random_int(1000,9999)}-{fake.random_int(1000,9999)}",
        direccion={
            "provincia": fake.random_element([
                "San José",
                "Alajuela",
                "Cartago",
                "Heredia",
                "Guanacaste",
                "Puntarenas",
                "Limón"
            ]),
            "canton": fake.city(),
            "distrito": fake.city(),
            "direccion_exacta": fake.street_address()
        }
    )
    clientes.append(cliente)

with open("clientes.json", "w", encoding="utf-8") as archivo:
    # default=str evita que json.dump falle con el objeto datetime
    json.dump(clientes, archivo, ensure_ascii=False, indent=4, default=str)

print(f"Se generaron {len(clientes)} clientes exitosamente en 'clientes.json'.")
