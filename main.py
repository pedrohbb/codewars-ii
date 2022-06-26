from src.business.cadastros import Cadastro
from src.entities.holerite import Holerite, gerar_todos_holerites


def main():

    print("__________________________________________________________________\n")
    print('Bem vindo ao sistema de folha de pagamento da XPTO Alimentos! \n\n')

    tarefas()

    opcao_invalida = True

    while opcao_invalida:

        nova_tarefa = input(
            'Deseja realizar outra operação? 1 - Sim / 0 - Não : ')

        if nova_tarefa == 'Sim' or nova_tarefa == '1':
            tarefas()
        elif nova_tarefa == 'Não' or nova_tarefa == '0':
            opcao_invalida = False
        else:
            print('Opção inválida! Tente novamente')


def tarefas():

    opcao_invalida = True

    while opcao_invalida:
        print("\n")
        tarefa = input(
            'Selecione uma opção no menu: \n'
            '1 - Cadastrar novo funcionário\n'
            '2 - Excluir funcionário do cadastro \n'
            '3 - Consultar funcionário por chave \n'
            '4 - Alterar dados de um funcionário \n'
            '5 - Listar todos os funcionários cadastrados \n'
            '6 - Gerar holerite de um funcionário específico no mês escolhido\n'
            '7 - Gerar holerites de todos os funcionários no mês escolhido \n'
        )

        cadastro = Cadastro()

        if tarefa == '1':
            opcao_invalida = False
            cadastro.inserir()
        elif tarefa == '2':
            opcao_invalida = False
            matricula = int(
                input('Insira a matrícula ou CPF do funcionário a ser excluído: '))
            cadastro.excluir(matricula)
        elif tarefa == '3':
            opcao_invalida = False
            matricula = int(
                input('Insira a matrícula ou CPF do funcionário a ser consultado: '))
            print(cadastro.consultar(matricula))
        elif tarefa == '4':
            opcao_invalida = False
            cadastro.alterar()
        elif tarefa == '5':
            opcao_invalida = False
            print(cadastro.listar())
        elif tarefa == '6':
            opcao_invalida = False
            matricula = input("Matricula do funcionário: ")
            mes_ano = input("Insira mês e ano no formato MM/AAAA: ")
            faltas = int(
                input("Informe o número de faltas do funcionário no mês: "))
            holerite = Holerite(mes_ano, matricula, faltas)
            holerite.gerar_holerite()
        elif tarefa == '7':
            opcao_invalida = False
            cadastro = Cadastro()
            mes_ano = input("Insira mês e ano no formato MM/AAAA: ")
            gerar_todos_holerites(cadastro, mes_ano)
        else:
            print('Opção inválida!')


main()
