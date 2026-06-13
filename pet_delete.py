def excluir_pet(lista_pets):
    print("--- Exclusão de Pet ---")

    nome = input("Nome do Pet a ser excluído: ")

    for pet in lista_pets:
        if pet.nome == nome:
            lista_pets.remove(pet)
            print(f"Sucesso! {nome} foi excluído do sistema!")
            return

    print("Pet não encontrado.")