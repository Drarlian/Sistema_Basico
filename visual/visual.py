from tkinter import *
from functools import partial


def menu(old_janela=None, perm_cadastro=False):  # O padrão do cadastro é False, True apenas para criação/edição.

    if old_janela is not None:
        old_janela.destroy()

    janela_menu = Tk()

    janela_menu.title('Menu')
    janela_menu.geometry('200x280')  # -> 200x280

    texto_orientacao = Label(janela_menu, text='MENU:', font=('Arial', 15))
    texto_orientacao.pack(padx=10, pady=10, anchor=CENTER)

    if perm_cadastro:
        botao_pergunta = Button(janela_menu, text='Responder Perguntas', bg='RED', width=20, command=partial(acesso_negado2, janela_menu))
        botao_pergunta.pack(padx=10, pady=10)
    else:
        botao_pergunta = Button(janela_menu, text='Responder Perguntas', width=20, command=partial(formulario, janela_menu))
        botao_pergunta.pack(padx=10, pady=10)

    if not perm_cadastro:  # VERIFICANDO SE O ACESSO AO CADASTRO ESTA PERMITIDO.
        botao_cadastro = Button(janela_menu, text='Cadastrar', bg='RED', width=20, command=partial(acesso_negado1, janela_menu))
        botao_cadastro.pack(padx=10, pady=10)
    else:
        botao_cadastro = Button(janela_menu, text='Cadastrar', width=20, command=partial(cadastro, janela_menu))
        botao_cadastro.pack(padx=10, pady=10)

    botao_login = Button(janela_menu, text='Login', width=20, command=partial(login, janela_menu, perm_cadastro))
    botao_login.pack(padx=10, pady=10)

    botao_sair = Button(janela_menu, text='Sair', width=20, command=partial(sair, janela_menu))
    botao_sair.pack(padx=10, pady=10)

    # botao_sair = Button(janela_menu, text='TEMPORARIO', width=20, command=partial(menu_login, janela_menu))
    # botao_sair.pack(padx=10, pady=10)

    botao_ajuda = Button(janela_menu, text='?', width=3, command=partial(atalho, janela_menu))
    botao_ajuda.pack(side=RIGHT, anchor='se')

    janela_menu.mainloop()


def formulario(janela):
    from verifica.verifica_dado import verifica_formulario

    janela.destroy()

    janela_formulario = Tk()
    janela_formulario.title('Formulário')
    janela_formulario.geometry('500x350')

    texto_orientacao = Label(janela_formulario, text='FORMULÁRIO:', font=('Arial', 15))
    texto_orientacao.pack(anchor=CENTER, padx=10, pady=10)


    texto_pergunta1 = Label(janela_formulario, text='Pergunta 1: Qual a melhor facção, Horda ou Aliança?')
    texto_pergunta1.pack(padx=10)

    pergunta1 = Entry(janela_formulario, width=43)
    pergunta1.pack(pady=(2, 12))


    texto_pergunta2 = Label(janela_formulario, text='Pergunta 2: Qual o melhor tipo de spec, Melee ou Ranged?')
    texto_pergunta2.pack(padx=10)

    pergunta2 = Entry(janela_formulario, width=48)
    pergunta2.pack(pady=(2, 12))


    texto_pergunta3 = Label(janela_formulario, text='Pergunta 3: Qual é melhor, Paladino ou Bruxo')
    texto_pergunta3.pack(padx=10)

    pergunta3 = Entry(janela_formulario, width=38)
    pergunta3.pack(pady=(2, 12))


    bloco = Frame(janela_formulario)
    bloco.pack(anchor='n')

    botao_voltar = Button(bloco, text='Voltar',  width=15, command=partial(menu, janela_formulario))
    botao_voltar.pack(side=LEFT, padx=10, pady=(10, 0))

    botao_enviar = Button(bloco, text='Enviar', width=15,
                          command=lambda: verifica_formulario((pergunta1.get(), pergunta2.get(), pergunta3.get()), janela_formulario))
    botao_enviar.pack(side=LEFT, pady=(10, 0))

    botao_sair = Button(janela_formulario, text='Sair',  width=15, command=partial(sair, janela_formulario))
    botao_sair.pack(padx=10, pady=10)


    janela_formulario.mainloop()


def cadastro(janela):
    from verifica.verifica_dado import verifica_cadastro

    janela.destroy()

    janela_cadastro = Tk()
    janela_cadastro.title('Cadastro')
    janela_cadastro.geometry('300x400')

    texto_orientacao = Label(janela_cadastro, text='CADASTRO:', font=('Arial', 15))
    texto_orientacao.pack(pady=10, anchor=CENTER)

    # Frames:
    primeiro_bloco = Frame(janela_cadastro)
    primeiro_bloco.pack(anchor='n')  # -> Definindo a posição do frame.

    segundo_bloco = Frame(janela_cadastro)
    segundo_bloco.pack(anchor='n')

    terceiro_bloco = Frame(janela_cadastro)
    terceiro_bloco.pack(anchor='n')

    quarto_bloco = Frame(janela_cadastro)
    quarto_bloco.pack(anchor='n')

    quinto_bloco = Frame(janela_cadastro)
    quinto_bloco.pack(anchor='n')

    sexto_bloco = Frame(janela_cadastro)
    sexto_bloco.pack(anchor='n')

    setimo_bloco = Frame(janela_cadastro)
    setimo_bloco.pack(anchor='n')


    # Textos + Entrada de dados:
    texto_nome = Label(primeiro_bloco, text='Nome:')
    texto_nome.pack(side=LEFT, padx=(10, 0), pady=10)  # -> Definindo que vão ficar um do lado do outro.

    nome = Entry(primeiro_bloco)
    nome.pack(side=LEFT, pady=10)  # -> Definindo que vão ficar um do lado do outro.

    texto_idade = Label(segundo_bloco, text='Idade:')
    texto_idade.pack(side=LEFT, padx=(10, 0), pady=10)

    idade = Entry(segundo_bloco)
    idade.pack(side=LEFT, pady=10)

    texto_email = Label(terceiro_bloco, text='Email:')
    texto_email.pack(side=LEFT, padx=(10, 0), pady=10)

    email = Entry(terceiro_bloco)
    email.pack(side=LEFT, pady=10)

    texto_usuario = Label(quarto_bloco, text='Usuário:')
    texto_usuario.pack(side=LEFT, padx=(10, 0), pady=10)

    usuario = Entry(quarto_bloco)
    usuario.pack(side=LEFT, pady=10)

    texto_senha = Label(quinto_bloco, text='Senha:')
    texto_senha.pack(side=LEFT, padx=(10, 0), pady=10)

    senha = Entry(quinto_bloco, show='*')
    senha.pack(side=LEFT, pady=10)

    texto_senha_confere = Label(sexto_bloco, text='Senha:')
    texto_senha_confere.pack(side=LEFT, padx=(10, 0), pady=10)

    senha_confere = Entry(sexto_bloco, show='*')
    senha_confere.pack(side=LEFT, pady=10)

    # Botoes:
    botao_voltar = Button(setimo_bloco, text='Voltar',  width=15, command=partial(menu, janela_cadastro, True))
    botao_voltar.pack(side=LEFT, padx=10, pady=(10, 0))

    botao_enviar = Button(setimo_bloco, text='Enviar', width=15,
                          command=lambda: verifica_cadastro([nome.get(), idade.get(), email.get(), usuario.get(), senha.get(), senha_confere.get()], janela_cadastro))
    botao_enviar.pack(side=LEFT, pady=(10, 0))

    botao_sair = Button(janela_cadastro, text='Sair',  width=15, command=partial(sair, janela_cadastro))
    botao_sair.pack(padx=10, pady=10)


    janela_cadastro.mainloop()


def login(janela, permissao):
    from verifica.verifica_dado import verifica_login
    janela.destroy()

    janela_login = Tk()
    janela_login.title('Login')
    janela_login.geometry('260x220')

    texto_orientacao = Label(janela_login, text='LOGIN:', font=('Arial', 15))
    texto_orientacao.pack(padx=10, pady=10, anchor=CENTER)

    # Frames:
    primeiro_bloco = Frame(janela_login)
    primeiro_bloco.pack(anchor='n')

    segundo_bloco = Frame(janela_login)
    segundo_bloco.pack(anchor='n')

    terceiro_bloco = Frame(janela_login)
    terceiro_bloco.pack(anchor='n')

    # Textos + Entradas de dados:
    texto_usuario = Label(primeiro_bloco, text='Usuário: ')
    texto_usuario.pack(side=LEFT, padx=(10, 0), pady=10)

    usuario = Entry(primeiro_bloco)
    usuario.pack(side=LEFT, padx=(0, 10), pady=10)

    texto_senha = Label(segundo_bloco, text='Senha: ')
    texto_senha.pack(side=LEFT, padx=(18, 0), pady=10)  # -> Jogando um pouco para direita para alinhar com o Usuário:

    senha = Entry(segundo_bloco, show='*')
    senha.pack(side=LEFT, padx=(0, 10), pady=10)

    # Botões:
    botao_voltar = Button(terceiro_bloco, text='Voltar', width=13, command=partial(menu, janela_login, permissao))
    botao_voltar.pack(side=LEFT, padx=10, pady=(10, 0))

    botao_logar = Button(terceiro_bloco, text='Logar', width=13, command=lambda: verifica_login(usuario.get(), senha.get(), janela_login))
    botao_logar.pack(side=LEFT, pady=(10, 0))

    botao_sair = Button(janela_login, text='Sair', width=13, command=partial(sair, janela_login))
    botao_sair.pack(padx=10, pady=10)

    janela_login.mainloop()


def menu_login(janela):
    from acoes.acoes import ler, logout
    janela.destroy()

    janela_menu_login = Tk()

    janela_menu_login.title('Sistema')
    janela_menu_login.geometry('200x280')

    texto_orientacao = Label(janela_menu_login, text='SISTEMA:', font=('Arial', 15))
    texto_orientacao.pack(padx=10, pady=10, anchor=CENTER)

    botao_ler1 = Button(janela_menu_login, text='Livro 1', width=20, command=partial(ler, janela_menu_login, 'arq1'))
    botao_ler1.pack(padx=10, pady=10)

    botao_ler2 = Button(janela_menu_login, text='Livro 2', width=20, command=partial(ler, janela_menu_login, 'arq2'))
    botao_ler2.pack(padx=10, pady=10)

    botao_logout = Button(janela_menu_login, text='Logout', width=20, command=partial(logout, janela_menu_login))
    botao_logout.pack(padx=10, pady=10)

    botao_sair = Button(janela_menu_login, text='Sair', width=20, command=partial(sair, janela_menu_login))
    botao_sair.pack(padx=10, pady=10)

    janela_menu_login.mainloop()


def sair(janela):
    janela.destroy()


def acesso_negado1(janela):
    aviso = Toplevel(janela)
    aviso.title('Aviso')

    texto = Label(aviso, text='Acesso ao Cadastro Negado.\nResponda as perguntas primeiro.')
    texto.pack(padx=10, pady=10)

    texto.after(4000, lambda: aviso.destroy())


def acesso_negado2(janela):
    aviso = Toplevel(janela)
    aviso.title('Aviso')

    texto = Label(aviso, text='Acesso as perguntas Negado.\nVocê já respondeu as perguntas corretamente.')
    texto.pack(padx=10, pady=10)

    texto.after(4000, lambda: aviso.destroy())


def alerta_problema(mensagem, janela):
    alerta = Toplevel(janela)
    alerta.title('Aviso')

    texto = Label(alerta, text=mensagem)
    texto.pack(padx=10, pady=10)

    alerta.after(2000, lambda: alerta.destroy())  # -> Fechando a janela de alerta 2s depois dela abrir.


def alerta_sucesso_menu(mensagem, janela, acesso_cadastro):
    aviso = Toplevel(janela)
    aviso.title('Aviso')

    texto = Label(aviso, text=mensagem)
    texto.pack(padx=10, pady=10)

    aviso.after(2000, lambda: menu(janela, perm_cadastro=acesso_cadastro))  # -> Voltando para janela menu.
    # -> Depois de 2s eu chamo a função menu e passo janela como parametro.


def alerta_sucesso_menu_login(mensagem, janela):
    aviso = Toplevel(janela)
    aviso.title('Aviso')

    texto = Label(aviso, text=mensagem)
    texto.pack(padx=10, pady=10)

    aviso.after(2000, lambda: menu_login(janela))  # -> Voltando para janela menu.
    # -> Depois de 2s eu chamo a função menu e passo janela como parametro.


def atalho(janela):
    from verifica.verifica_dado import verifica_atalho
    ata = Toplevel(janela)
    ata.title('?')

    bloco = Frame(ata)
    bloco.pack(anchor='n')

    texto_codigo = Label(bloco, text='Código:')
    texto_codigo.pack(side=LEFT, padx=(10, 0), pady=10)

    codigo = Entry(bloco, show='*')
    codigo.pack(side=LEFT, padx=(0, 10), pady=10)

    botao_codigo = Button(ata, text='?', width=6, command=lambda: verifica_atalho(codigo.get(), janela))
    botao_codigo.pack(padx=(25, 10), pady=(0, 10))
