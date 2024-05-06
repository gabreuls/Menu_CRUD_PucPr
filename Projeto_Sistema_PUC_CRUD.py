'''
Gabriel da Silva Antunes
Análise e Desenvolvimento de Sistemas (ADS)
'''

import json

def mostrar_menu_principal():
    print("----- MENU PRINCIPAL -----")
    print("1 - Estudante")
    print("2 - Professor")
    print("3 - Disciplina")
    print("4 - Turma")
    print("5 - Matrícula")
    print("0 - Sair")
    print("--------------------------\n")

    return input("Escolha uma das opções a cima: ")

def mostrar_menu_secundario():
    print(f"\n===== MENU DE OPERAÇÕES - {opcao} ======")
    print("1 - Incluir")
    print("2 - Listar")
    print("3 - Atualizar")
    print("4 - Excluir")
    print("0 - Voltar ao Menu Principal")
    print("===========================================\n")

    return input("Escolha uma das opções a cima: ")

def processar_menu_secundario(opcao1, opcao2, nome_arquivo):
    
    if opcao2 == '1':

        if opcao1 == 'ESTUDANTE' or opcao1 == 'PROFESSOR':
            cadastrar_pessoa(nome_arquivo)

        elif opcao1 == 'DISCIPLINA':
            cadastrar_disciplina(nome_arquivo)

        elif opcao1 == 'TURMA':
            cadastrar_turma(nome_arquivo)

        elif opcao1 == 'MATRÍCULA':
            cadastrar_matricula(nome_arquivo)

    elif opcao2 == '2':
        listar(nome_arquivo)
                
    elif opcao2 == '3':
        codigo = int(input("Digite o código do que deseja editar: "))
        atualizar(codigo, nome_arquivo)

    elif opcao2 == '4':
        codigo = int(input("Digite o código do que deseja excluir: "))
        excluir(codigo, nome_arquivo)

    elif opcao2 == '0':
        print("Voltando para o Menu Principal...\n")
        return False

    else: print("Opção Inválida.")

    return True

def cadastrar_pessoa(nome_arquivo):
    print(f"\n##### CADASTRAR - {opcao} #####\n")

    codigo = int(input(f"Digite o código do(a) {opcao}: "))
    nome = input(f"Digite o nome do(a) {opcao}: ")
    cpf = input(f"Digite o CPF do(a) {opcao}: ")
    dados = {
                "Cod": codigo,
                "Nome": nome,
                "CPF": cpf
            }
    
    lista = ler_arquivo(nome_arquivo)
    lista.append(dados)
    salvar_arquivo(lista, nome_arquivo)

    print(f"\n{opcao} adicionado(a) com sucesso.\n")

def cadastrar_disciplina(nome_arquivo):
    print("\n##### CADASTRAR - DISCIPLINA #####\n")

    codigo = int(input("Digite o código da disciplina: "))
    nome = input("Digite o nome da disciplina: ")
    dados = {
                "Cod": codigo,
                "Nome": nome
            }
    
    lista = ler_arquivo(nome_arquivo)
    lista.append(dados)
    salvar_arquivo(lista, nome_arquivo)

    print(f"{codigo} - {nome}. Disciplina adicionada com sucesso.\n")

def cadastrar_turma(nome_arquivo):
    print("\n##### CADASTRAR - TURMA #####\n")

    lista = ler_arquivo(nome_arquivo)

    turma = int(input("Digite o código da turma: "))

    for cadastro in lista:
        if cadastro["Turma"] == turma:
            print("Essa turma já está cadastrada!\n")
            return
    try: 
        professor = int(input("Digite o código do(a) professor: "))
        disciplina = int(input("Digite o código da disciplina: "))
        dados = {
                    "Turma": turma,
                    "Professor(a)": professor,
                    "Disciplina": disciplina
                }
            
        lista = ler_arquivo(nome_arquivo)
        lista.append(dados)
        salvar_arquivo(lista, nome_arquivo)

        print(f"Turma {turma} adicionada com sucesso.\n")
    
    except:
        print(TypeError, "O Cóigo só aceita números!")

def cadastrar_matricula(nome_arquivo):
    print("\n##### CADASTRAR - MATRÍCULA #####\n")

    turma = int(input("Digite o código da turma: "))
    estudante = int(input("Digite o código do estudante: "))

    lista = ler_arquivo(nome_arquivo)
    for cadastro in lista:
        if cadastro["Turma"] == turma and cadastro["Estudante"] == estudante:
            print("Essa matrícula já está cadastrada!\n")
            return
    dados = {
                "Turma": turma,
                "Estudante": estudante,
            }
    
    lista = ler_arquivo(nome_arquivo)
    lista.append(dados)
    salvar_arquivo(lista, nome_arquivo)

    print("Matrícula adicionada com sucesso.\n")

def listar(nome_arquivo):
    print(f"\n##### LISTAR - {opcao} #####\n")

    lista = ler_arquivo(nome_arquivo)

    if len(lista) == 0:
        print(f"Não há dados de {opcao} cadastrado.\n")

    elif opcao == 'ESTUDANTE' or opcao == 'PROFESSOR':
        for cadastro in lista:
            print(f"{cadastro['Cod']} - Nome: {cadastro['Nome']} - CPF: {cadastro['CPF']}\n")

    elif opcao == 'DISCIPLINA':
        for cadastro in lista:
            print(f"{cadastro['Cod']} - Nome: {cadastro['Nome']}\n")

    elif opcao == 'TURMA':
        for cadastro in lista:
            print(f"{cadastro['Turma']} - Professor: {cadastro['Professor(a)']} - Disciplina: {cadastro['Disciplina']}\n")

    elif opcao == 'MATRÍCULA':
        for cadastro in lista:
            print(f"Turma: {cadastro['Turma']} - Estudante: {cadastro['Estudante']}\n")        

def atualizar(codigo, nome_arquivo):
    print(f"\n##### ATUALIZAR - {opcao} #####")
    
    editar_cadastro = None
    lista = ler_arquivo(nome_arquivo)

    if opcao == 'ESTUDANTE' or opcao == 'PROFESSOR':
        for cadastro in lista:
            if cadastro["Cod"] == codigo:
                cadastro["Nome"] = input("Digite o novo nome: ")
                cadastro["CPF"] = input("Digite o novo CPF: ")
                salvar_arquivo(lista, nome_arquivo)
                print(f"\n{opcao} Atualizado!")

    elif opcao == 'DISCIPLINA':
        for cadastro in lista:
            if cadastro["Cod"] == codigo:
                cadastro["Nome"] = input("Digite o novo nome: ")
                salvar_arquivo(lista, nome_arquivo)
                print(f"\n{opcao} Atualizado!")

    elif opcao == 'TURMA':
        for cadastro in lista:
            if cadastro["Turma"] == codigo:
                try:
                    cadastro["Professor(a)"] = int(input("Digite o novo código do professor: "))
                    cadastro["Disciplina"] = int(input("Digite o novo código da disciplina: "))
                    salvar_arquivo(lista, nome_arquivo)
                    print(f"\n{opcao} Atualizado!")
                except:
                    print(TypeError, "O Cóigo só aceita números!")

    elif opcao == 'MATRÍCULA':
        for cadastro in lista:
            if cadastro["Turma"] == codigo:
                try: 
                    cadastro["Turma"] = int(input("Digite o código da nova turma: "))
                    cadastro["Estudante"] = int(input("Digite o novo código do estudante: "))
                    salvar_arquivo(lista, nome_arquivo)
                    print(f"\n{opcao} Atualizado!")
                except:
                    print(TypeError, "O Cóigo só aceita números!")
    
    else:
        print(f"{opcao} não encontrado(a)!")
        
def excluir(codigo, nome_arquivo):
    print(f"\n##### EXCLUIR - {opcao} #####")

    remover_cadastro = None
    lista = ler_arquivo(nome_arquivo)

    if opcao == "TURMA" or opcao == "MATRÍCULA":
        for cadastro in lista:
            if cadastro["Turma"] == codigo:
                remover_cadastro = cadastro
    else:
        for cadastro in lista:
            if cadastro["Cod"] == codigo:
                remover_cadastro = cadastro

    if remover_cadastro is None:
        print(f"\n{opcao} não encontrado(a)!")

    else:
        lista.remove(remover_cadastro)
        salvar_arquivo(lista, nome_arquivo)
        print(f"\n{opcao} removido(a)!")

def salvar_arquivo(lista, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_aberto:
        json.dump(lista, arquivo_aberto)

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_aberto:
            lista_arquivo = json.load(arquivo_aberto)

        return lista_arquivo
    
    except:
        return []

arquivo_estudantes = "estudantes.json"
arquivo_professores = "professores.json"
arquivo_disciplinas = "disciplinas.json"
arquivo_turmas = "turmas.json"
arquivo_matriculas = "matriculas.json"

while True:
    
    menu = mostrar_menu_principal()
    if menu == '1':
        opcao = 'ESTUDANTE'

        while True:
            
            menu2 = mostrar_menu_secundario()
            print("")
            if not processar_menu_secundario(opcao, menu2, arquivo_estudantes):
                break

    elif menu == '2':
        opcao = 'PROFESSOR'

        while True:
            
            menu2 = mostrar_menu_secundario()
            print("")
            if not processar_menu_secundario(opcao, menu2, arquivo_professores):
                break

    elif menu == '3':
        opcao = 'DISCIPLINA'

        while True:
            
            menu2 = mostrar_menu_secundario()
            print("")
            if not processar_menu_secundario(opcao, menu2, arquivo_disciplinas):
                break

    elif menu == '4':
        opcao = 'TURMA'

        while True:
            
            menu2 = mostrar_menu_secundario()
            print("")
            if not processar_menu_secundario(opcao, menu2, arquivo_turmas):
                break

    elif menu == '5':
        opcao = 'MATRÍCULA'
        
        while True:
            
            menu2 = mostrar_menu_secundario()
            print("")
            if not processar_menu_secundario(opcao, menu2, arquivo_matriculas):
                break

    elif menu == '0':
        print("Saindo...")
        break 

    else: print("Opção escolhida inválida!\n")
