from business.cadastros import Cadastro
from entities.holerite import Holerite


def main():

    cadastro = Cadastro()
    opcoes()

    nova_opcao = input('Deseja realizar outra operação? S ou N: ')

    opcao_invalida = True

    while opcao_invalida:

        if nova_opcao == 'S':
            opcao_invalida = False
            main()


def opcoes():
    opcao_invalida = True

    while opcao_invalida:

        opcao = input('Bem vindo ao sistema de folha de pagamento da XPTO Alimentos! \n\n'
                      'Selecione uma opção no menu: \n'
                      '1 - Cadastrar novo funcionário\n'
                      '2 - Excluir funcionário do cadastro \n'
                      '3 - Consultar funcionário por chave \n'
                      '4 - Alterar dados de um funcionário \n'
                      '5 - Listar todos os funcionários cadastrados \n'
                      '6 - Gerar holerite de um funcionário específico \n'
                      '7 - Gerar holerites de todos os funcionários no mês escolhido \n'
                      )

        if opcao == '1':
            opcao_invalida = False
            cadastro.inserir()
        elif opcao == '2':
            opcao_invalida = False
            cadastro.excluir()
        elif opcao == '3':
            opcao_invalida = False
            cadastro.consultar()
        elif opcao == '4':
            opcao_invalida = False
            cadastro.alterar()
        elif opcao == '5':
            opcao_invalida = False
            cadastro.listar()
        elif opcao == '6':
            opcao_invalida = False
            holerite = Holerite()
            holerite.gerar_holerite()
        elif opcao == '7':
            opcao_invalida = False
            gerar_todos_holerites()
        else:
            print('Opção inválida!')
