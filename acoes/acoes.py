from tkinter import *
from functools import partial


def cadastrar(nome, idade, email, nome_usuario, senha):
    with open('dados/cadastrados.txt', 'r', encoding='UTF-8') as arquivo:
        arquivo.seek(0)

        if len(arquivo.readlines()) == 0:
            numero = 0
        else:
            # Processo de pegar o numero do usuario anterior e adicionar + 1 para usar no proximo usuario:
            arquivo.seek(0)  # -> Preciso mover o cursor de volta para o começo para ler todas as linhas novamente
            dado1 = arquivo.readlines()
            dado2 = dado1[-1].split(';')
            numero = int(dado2[0].split(' ')[1]) + 1

    with open('dados/cadastrados.txt', 'a', encoding='UTF-8') as arquivo:
        arquivo.write(f'USUARIO {numero}; NOME:{nome.capitalize()}; IDADE:{idade}; EMAIL:{email.capitalize()};'
                      f' USUARIO:{nome_usuario.capitalize()}; SENHA:{senha}\n')


def ler(janela, arq):
    import os

    if arq == 'arq1':
        os.startfile('dados\\livro1.txt')

    elif arq == 'arq2':
        os.startfile('dados\\livro2.txt')


def logout(janela):  # A interface gerada aqui deveria estar no visual.
    from visual.visual import alerta_sucesso_menu


    escolha = Toplevel(janela)
    escolha.title('Aviso')

    bloco = Frame(escolha)
    bloco.pack(anchor='w')

    texto = Label(bloco, text='Tem certeza que deseja deslogar?')
    texto.pack(side=LEFT, padx=(10, 2), pady=10)

    confirma = Button(bloco, text='SIM', width=5, command=partial(alerta_sucesso_menu, 'Deslogando...', janela, False))
    confirma.pack(side=LEFT, padx=(0, 10), pady=10)

    nega = Button(bloco, text='NÃO', width=5, command=lambda: escolha.after(2000, escolha.destroy()))
    nega.pack(side=LEFT, padx=(0, 10), pady=10)
