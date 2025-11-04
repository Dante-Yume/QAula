from faker import Faker
import random


fake = Faker('pt_BR')  

persona = {
    "nome": fake.name(),
    "idade": random.randint(18, 70),  
    "cidade": fake.city()
}


print("Persona gerada:")
print(persona)