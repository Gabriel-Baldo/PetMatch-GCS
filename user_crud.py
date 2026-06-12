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