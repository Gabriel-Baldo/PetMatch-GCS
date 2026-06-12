def criar_usuario(nome, email, telefone):
    global id_atual

    usuario = {
        "id": id_atual,
        "nome": nome,
        "email": email,
        "telefone": telefone
    }

    usuarios.append(usuario)
    id_atual += 1
    print("Usuário criado com sucesso!")

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    for u in usuarios:
        print(u)


def buscar_usuario(id_usuario):
    for u in usuarios:
        if u["id"] == id_usuario:
            print(u)
            return
    print("Usuário não encontrado")

def atualizar_usuario(id_usuario, nome, email, telefone):
    for u in usuarios:
        if u["id"] == id_usuario:
            u["nome"] = nome
            u["email"] = email
            u["telefone"] = telefone
            print("Usuário atualizado com sucesso!")
            return
    print("Usuário não encontrado")