class Pet:
    def __init__(self, nome, especie, idade, porte):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.porte = porte
        self.status = "Disponível"

def cadastrar_pet():
    print("--- Cadastro de Novo Pet ---")
    nome = input("Nome do Pet: ")
    especie = input("Espécie (Cachorro/Gato): ")
    idade = input("Idade (anos): ")
    porte = input("Porte (P/M/G): ")
    
    novo_pet = Pet(nome, especie, idade, porte)
    print(f"Sucesso! {novo_pet.nome} foi cadastrado e está {novo_pet.status} para adoção!")
    return novo_pet

if __name__ == "__main__":
    cadastrar_pet()
