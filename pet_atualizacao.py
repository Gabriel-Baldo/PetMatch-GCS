class Pet:
    def __init__(self, nome, especie, idade, porte):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.porte = porte
        self.status = "Disponível"


def atualizar_pet():
    print("--- Atualização de Pet ---")

    nome = input("Nome do Pet: ")
    especie = input("Espécie (Cachorro/Gato): ")
    idade = input("Nova idade (anos): ")
    porte = input("Novo porte (P/M/G): ")

    pet_atualizado = Pet(nome, especie, idade, porte)

    print(f"Sucesso! Os dados de {pet_atualizado.nome} foram atualizados!")
    return pet_atualizado


if __name__ == "__main__":
    atualizar_pet()