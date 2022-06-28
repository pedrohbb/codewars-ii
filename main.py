from src.business.cadastros import Cadastro
from src.entities.holerite import Holerite, gerar_todos_holerites
from src.exceptions.not_found_error import NotFoundError
from src.exceptions.not_valid_format_error import NotValidFormatError
from src.exceptions.duplicated_entry_error import DuplicatedEntryError


def main():

    print("__________________________________________________________________\n")
    print('Bem vindo ao sistema de folha de pagamento da XPTO Alimentos!')

    menu()

    enunciado = "\n\n\
    1 - Realizar nova operação \n\
    0 - Encerrar o sistema : "

    while True:
        nova_tarefa = input(enunciado)
        if nova_tarefa not in list('10'):
            print('\nOpção inválida! Tente novamente\n')
        elif nova_tarefa == '1':
            print('\n')
            menu()
        else:
            print('\nSistema encerrado!')
            break

def menu():

    enunciado = "Selecione uma opção no menu: \n\
        1 - Cadastrar novo funcionário\n\
        2 - Excluir funcionário do cadastro \n\
        3 - Consultar funcionário por matricula ou cpf \n\
        4 - Alterar dados de um funcionário \n\
        5 - Listar todos os funcionários cadastrados \n\
        6 - Gerar holerite de um funcionário específico no mês escolhido \n\
        7 - Gerar holerites de todos os funcionários no mês escolhido: "

    num_tarefas = enunciado.count('\n')

    while True:
        opcao = input(enunciado)
        if opcao not in [str(i) for i in range(1,num_tarefas+1)]:
            print("\nOpção Inválida! Tente novamente\n")
            continue
        break

    # opcao = input(enunciado)

    # if opcao not in [str(i) for i in range(1,num_tarefas+1)]:
    #     print("\nOpção Inválida! Tente novamente\n")
    #     return

    ####---------Submenu (início)---------####

    # if opcao == '4':
    #     opcao = submenu_tarefa4()

    #####---------Submenu (fim)---------######

    try:
        tarefas(opcao)
    except NotFoundError as nfderror: 
        print('\n'+nfderror.args[0]+'\n')
    except NotValidFormatError as nvferror:
        print('\n'+nvferror.args[0]+'\n')
    except DuplicatedEntryError as dtderror: 
        print('\n'+dtderror.args[0]+'\n')

def tarefas(opcao):

    cadastro = Cadastro()
    opcao = int(opcao)

    print('\n')
    if opcao == 1:
        nome = input('Digite o nome do funcionário: ') 
        cpf = input('Digite o CPF do funcionário: ')
        data_admissao = input('Digite a data de admissão do funcionário: ')
        codigo_cargo = input('Digite o cargo do funcionário: ')
        comissao = input('O funcionário possui comissão? 1 - Sim / 0 - Não: ')
        print('\n')
        cadastro.inserir(nome, cpf, data_admissao, codigo_cargo, comissao)
    elif opcao == 2:
        chave = input('Insira a matrícula ou CPF do funcionário a ser excluído: ')
        print('\n')
        cadastro.excluir(chave)
    elif opcao == 3:
        chave = input('Insira a matrícula ou CPF do funcionário a ser consultado: ')
        print('\n')
        print(cadastro.consultar(chave))
    elif opcao == 4:
        chave = input("Insira a matrícula ou cpf do funcionário: ")
        sub_opcao = submenu_tarefa4()
        print('\n')
        dado = input(f"{sub_opcao} novo(a): ")
        cadastro.alterar(chave, sub_opcao, dado)
    elif opcao == 5:
        print(cadastro.listar())
    elif opcao == 6:
        chave = input('Insira a matrícula ou CPF do funcionário a ser consultado: ')
        mes_ano = input("Insira mês e ano no formato MM/AAAA: ")
        faltas = float(input("Informe o número de faltas do funcionário no mês: "))
        print('\n')
        holerite = Holerite(mes_ano, chave, faltas)
        holerite.gerar_holerite()
    elif opcao == 7:
        cadastro = Cadastro()
        mes_ano = input("Insira mês e ano no formato MM/AAAA: ")
        print('\n')
        gerar_todos_holerites(cadastro, mes_ano)

def submenu_tarefa4():

    enunciado_tar4 = "Digite\n\
        1 para modificar o NOME,\n\
        2 para modificar o CPF,\n\
        3 para modificar a DATA DE ADMISSÃO no formato AAAA-MM-DD,\n\
        4 para modificar o CARGO ou\n\
        5 para modificar o RECEBE COMISSÃO: "
    
    campos = ['nome', 'cpf', 'data_admissao', 'codigo_cargo', 'comissao'] 
    while True:
        campo = input(enunciado_tar4)
        if campo not in list('12345'):
            print("\nCampo inválido! Tente novamente\n")
            continue

        campo = campos[int(campo)-1]
        break    

    return campo

main()