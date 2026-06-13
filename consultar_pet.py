pets = [
    {"id": 1, "nome": "Rex", "especie": "Cachorro"},
    {"id": 2, "nome": "Mingau", "especie": "Gato"}
]

id_pet = int(input("Digite o ID do pet: "))

encontrado = False

for pet in pets:
    if pet["id"] == id_pet:
        print("Pet encontrado:")
        print(f"Nome: {pet['nome']}")
        print(f"Espécie: {pet['especie']}")
        encontrado = True

if not encontrado:
    print("Pet não encontrado.")