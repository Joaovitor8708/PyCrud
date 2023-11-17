import mysql.connector
from time import sleep
banco = mysql.connector.connect(
    host='localhost',
    user='root',
    password='302302',
    database='academia'
)
print('--------------------------------------------Bem vindo ao Banco de dados da academia--------------------------------------------')
sleep(1)
while True:
    print('Qual tabela deseja utilizar? ')

    tabela=input('[1] Alunos\n[2] Funcionários\n[3] Modalidades\n[4] Personal\nEscolha uma das opções: ')
    if tabela == '1':
        meucursor=banco.cursor()
        pesquisa='select * from alunos;'
    elif tabela =='2':
        meucursor = banco.cursor()
        pesquisa = 'select * from funcionarios'
    elif tabela =='3':
        meucursor=banco.cursor()
        pesquisa='select * from modalidades;'
    elif tabela=='4':
        meucursor = banco.cursor()
        pesquisa = 'select * from personal;'
    else:
        print('Opção inválida')
        exit()

    print('Agora escolha qual operação você quer realizar:')

    opcao=input('[1] inserir dados\n[2] Consultar tabela\n[3] Deletar dados\n[4] Alterar dados\nEscolha uma das opções: ')

    if opcao == '1' and tabela =='1':
        nome = input('Nome: ')
        cpf = int(input('CPF: '))
        idade = int(input('Idade:'))
        telefone = int(input('Telefone: '))
        meucursor=banco.cursor()
        sql = 'insert into alunos (nome,cpf,idade,telefone) values (%s,%s,%s,%s)'
        data = (nome,cpf,idade,telefone)
        meucursor.execute(sql,data)
        banco.commit()
        print('Dado adicionado com sucesso.')

    elif opcao == '1' and tabela =='2':
        nome = input('Nome: ')
        cpf = int(input('CPF: '))
        idade = int(input('Idade: '))
        telefone = int(input('Telefone: '))
        salario = float(input('Salário: '))
        meucursor=banco.cursor()
        sql = 'insert into funcionarios (nome,cpf,idade,telefone,salario) values (%s,%s,%s,%s,%s)'
        data = (nome,cpf,idade,telefone,salario)
        meucursor.execute(sql,data)
        banco.commit()
        print('Dado adicionado com sucesso.')

    elif opcao == '1' and tabela =='3':
        nome = input('Nome: ')
        duracao = int(input('Duração: '))
        meucursor = banco.cursor()
        sql = 'insert into modalidades (nome,duracao) values (%s,%s)'
        data = nome,duracao
        meucursor.execute(sql,data)
        banco.commit()
        print('Dado adicionado com sucesso.')

    elif opcao == '1' and tabela =='4':
        nome = input('Nome: ')
        cpf = int(input('CPF: '))
        idade = int(input('Idade: '))
        telefone = int(input('Telefone: '))
        salario = float(input('Salário: '))
        meucursor=banco.cursor()
        sql = 'insert into personal (nome,cpf,idade,telefone,salario) values (%s,%s,%s,%s,%s)'
        data = (nome,cpf,idade,telefone,salario)
        meucursor.execute(sql,data)
        banco.commit()
        print('Dado adicionado com sucesso.')

    elif opcao == '2' and tabela == '1':
        meucursor.execute(pesquisa)
        resultados = meucursor.fetchall()
        print('Foi encontrado em aluno as seguintes informações:')
        for x in resultados:
            print(x)

    elif opcao == '2' and tabela == '2':
        meucursor.execute(pesquisa)
        resultados = meucursor.fetchall()
        print('Foi encontrado em funcionarios as seguintes informações:')
        for x in resultados:
            print(x)

    elif opcao == '2' and tabela == '3':
        meucursor.execute(pesquisa)
        resultados = meucursor.fetchall()
        print('Foi encontrado em modalidades as seguintes informações:')
        for x in resultados:
            print(x)

    elif opcao == '2' and tabela == '4':
        meucursor.execute(pesquisa)
        resultados = meucursor.fetchall()
        print('Foi encontrado em personal as seguintes informações:')
        for x in resultados:
            print(x)

    elif opcao == '3' and tabela == '1':
        id = int(input('Digite o ID que deseja deletar: '))
        deletar = f'delete from alunos where id_matricula = {id};'
        meucursor.execute(deletar)
        banco.commit()
        print('Registro deletado com sucesso.')

    elif opcao == '3' and tabela == '2':
        id = int(input('Digite o ID que deseja deletar: '))
        deletar = f'delete from funcionarios where id_funcionario = {id};'
        meucursor.execute(deletar)
        banco.commit()
        print('Registro deletado com sucesso.')

    elif opcao == '3' and tabela == '3':
        id = int(input('Digite o ID que deseja deletar: '))
        deletar = f'delete from modalidades where id_modalidade = {id};'
        meucursor.execute(deletar)
        banco.commit()
        print('Registro deletado com sucesso.')

    elif opcao == '3' and tabela == '4':
        id = int(input('Digite o ID que deseja deletar: '))
        deletar = f'delete from personal where id_personal = {id};'
        meucursor.execute(deletar)
        banco.commit()
        print('Registro deletado com sucesso.')

    elif opcao == '4' and tabela == '1':
            id = int(input('Digite o ID que deseja atualizar: '))
            atributo = input('Escolha o atributo que deseja modificar (nome, cpf, idade, telefone): ').lower()
            novo_valor = input(f'Digite o novo valor para {atributo}: ')
            meucursor = banco.cursor()
            if atributo not in ['nome', 'cpf', 'idade', 'telefone']:
                print('Atributo inválido.')
                exit()
            sql = f'update alunos set {atributo} = %s where id_matricula = %s'
            data = (novo_valor, id)
            meucursor.execute(sql, data)
            banco.commit()
            print('Dado atualizado com sucesso.')

    elif opcao == '4' and tabela == '2':
            id = int(input('Digite o ID que deseja atualizar: '))
            atributo = input('Escolha o atributo que deseja modificar (nome, cpf, idade, telefone, salario ): ').lower()
            novo_valor = input(f'Digite o novo valor para {atributo}: ')
            meucursor = banco.cursor()
            if atributo not in ['nome', 'cpf', 'idade', 'telefone', 'salario']:
                print('Atributo inválido.')
                exit()
            sql = f'update funcionarios set {atributo} = %s where id_funcionario = %s'
            data = (novo_valor, id)
            meucursor.execute(sql, data)
            banco.commit()
            print('Dado atualizado com sucesso.')

    elif opcao == '4' and tabela == '3':
            id = int(input('Digite o ID que deseja atualizar: '))
            atributo = input('Escolha o atributo que deseja modificar (nome, duracao): ').lower()
            novo_valor = input(f'Digite o novo valor para {atributo}: ')
            meucursor = banco.cursor()
            if atributo not in ['nome', 'duracao']:
                print('Atributo inválido.')
                exit()
            sql = f'update modalidades set {atributo} = %s where id_modalidade = %s'
            data = (novo_valor, id)
            meucursor.execute(sql, data)
            banco.commit()
            print('Dado atualizado com sucesso.')
    elif opcao == '4' and tabela == '4':
            id = int(input('Digite o ID que deseja atualizar: '))
            atributo = input('Escolha o atributo que deseja modificar (nome, cpf, idade, telefone, salario): ').lower()
            novo_valor = input(f'Digite o novo valor para {atributo}: ')
            meucursor = banco.cursor()
            if atributo not in ['nome', 'cpf', 'idade', 'telefone', 'salario']:
                print('Atributo inválido.')
                exit()
            sql = f'update personal set {atributo} = %s where id_personal = %s'
            data = (novo_valor, id)
            meucursor.execute(sql, data)
            banco.commit()
            print('Dado atualizado com sucesso.')

    else:
        print('Opção inválida')
        exit()
    continuar = input('Deseja realizar novas ações? ').lower()
    if continuar not in ['s','sim']:
        print('Consultas encerradas')
        exit()
