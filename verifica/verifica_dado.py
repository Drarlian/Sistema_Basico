def verifica_formulario(respostas, janela):
    from visual.visual import menu, alerta_problema, alerta_sucesso_menu

    gabarito = ('Horda', 'Melee', 'Paladino')

    for elemento in respostas:
        if len(elemento) == 0:
            alerta_problema('Resposta Vazia Detectada!', janela)
            return None


    if respostas == gabarito:
        alerta_sucesso_menu('Respostas Corretas!', janela, True)
    else:
        alerta_problema('Respostas Erradas!', janela)


def verifica_cadastro(dados, janela):
    from visual.visual import alerta_problema, alerta_sucesso_menu
    from acoes.acoes import cadastrar

    for elemento in dados:
        if len(elemento) == 0:
            alerta_problema('Campo Vazio Detectado!', janela)
            return None

    nome = dados[0]
    idade = verifica_idade(dados[1], janela)
    email = verifica_email(dados[2], janela)

    nome_usuario = verifica_usuario_C(dados[3], janela)

    senha = verifica_senha_C(dados[4], dados[5], janela)

    if (nome is None) or (idade is None) or (email is None) or (nome_usuario is None) or (senha is None):
        pass
    else:
        cadastrar(nome, idade, email, nome_usuario, senha)

        alerta_sucesso_menu('Cadastro Realizado com Sucesso!', janela, True)


def verifica_usuario_C(usuario, janela):
    from visual.visual import alerta_problema

    mensagem = 'Usuario Inválido - Uso de Caractere inválido'

    caracteres = [' ', '!', '@', '#', '$', '%', '¨', '&', '*', '(', ')', '-', '=', '_', '+', '/', '*', '<', ',', '>',
                  '.', ':', ';', '?', '}', ']', '^', '~', '`', '´', '{', '[', '\\']

    valido = True

    for caractere in caracteres:
        if caractere in usuario:
            alerta_problema(mensagem, janela)
            valido = False

    if valido:
        existe = verifica_usuario_C_existe(usuario)

        if not existe:
            return usuario
        else:
            alerta_problema('O nome de usuário informado já está em uso.', janela)
            return None


def verifica_senha_C(senha, senha_verifica, janela):
    from visual.visual import alerta_problema

    mensagem1 = 'As senhas digitadas devem ser iguais.'
    mensagem2 = 'Senha muito pequena.'

    if senha != senha_verifica:
        alerta_problema(mensagem1, janela)
    elif len(senha) < 6:
        alerta_problema(mensagem2, janela)
    else:
        return senha


def verifica_usuario_C_existe(usuario):  # VERIFICA SE O USUARIO DIGITADO JÁ EXISTE.
    with open('dados/cadastrados.txt', 'r') as arquivo:
        arquivo.seek(0)
        dados = arquivo.readlines()

    for elemento in dados:
        if usuario.capitalize() == elemento.split(';')[4].split(':')[1]:
            return True

    return False


def verifica_idade(numero, janela):
    from visual.visual import alerta_problema

    mensagem = 'Informe uma idade válida!'

    if numero.isnumeric():
        return int(numero)
    else:
        alerta_problema(mensagem, janela)


def verifica_email(email, janela):
    from visual.visual import alerta_problema

    mensagem = 'Informe um e-mail válido'

    if ('@' in email) and (('gmail' in email) or ('hotmail' in email)) and ((email[-4:] == '.com') or (email[-7:] == '.com.br')):
        existe = verifica_email_existe(email)
        if not existe:
            return email
        else:
            alerta_problema('O e-mail informado já está em uso.', janela)
            return None
    else:
        alerta_problema(mensagem, janela)
        return None


def verifica_email_existe(email):
    with open('dados/cadastrados.txt', 'r') as arquivo:
        arquivo.seek(0)
        dados = arquivo.readlines()

    for elemento in dados:
        if email.capitalize() == elemento.split(';')[3].split(':')[1]:
            return True

    return False


def verifica_login(usuario, senha, janela):
    from visual.visual import alerta_problema, alerta_sucesso_menu_login

    if (len(usuario) == 0) or (len(senha) == 0):
        alerta_problema('Campo Vazio Detectado!', janela)
        return None

    usuario, n_usuario = verifica_usuario_L(usuario)  # n_usuario -> numero do usuario (identificador)
    # print(n_usuario)  # -> Checando o numero do usuário
    senha = verifica_senha_L(senha, n_usuario)

    if usuario and senha:
        alerta_sucesso_menu_login('Acesso Permitido!', janela)
    else:
        alerta_problema('Acesso Negado!', janela)


def verifica_usuario_L(usuario):  # n_usuario -> numero do usuario (identificador)
    with open('dados/cadastrados.txt', 'r', encoding='UTF-8') as arquivo:
        arquivo.seek(0)

        # Retornar o numero do usuario tbm, para verificar se o usuario e a senha são da msm pessoa.
        for linha in arquivo.readlines():
            if usuario.capitalize() == linha.split(';')[4].split(':')[1]:
                return True, linha.split(';')[0].split(' ')[1]


        return False, None


def verifica_senha_L(senha, n_usuario):
    with open('dados/cadastrados.txt', 'r', encoding='UTF-8') as arquivo:
        arquivo.seek(0)

        # Retornar o numero do usuario tbm, para verificar se o usuario e a senha são da msm pessoa.
        for linha in arquivo.readlines():
            if (senha == linha.split(';')[5].split(':')[1].replace('\n', '')) and (n_usuario == linha.split(';')[0].split(' ')[1]):
                return True

        return False


def verifica_atalho(codigo, janela):
    from visual.visual import alerta_sucesso_menu, alerta_problema

    if codigo == 'batman':
        alerta_sucesso_menu(':)', janela, True)
    else:
        alerta_problema(':/', janela)
