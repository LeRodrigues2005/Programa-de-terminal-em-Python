while True:
    print('\033[0;36m=========\033[m \033[1;39;41mSEJA BEM-VINDO(A)\033[m \033[0;36m=========\033[m')
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    print('''\033[1;31m[1] \033[0;36msoma\033[m
\033[1;31m[2]\033[m \033[0;36mmultipliação\033[m
\033[1;31m[3]\033[m \033[0;36midentificar o maior número\033[m
\033[1;31m[4]\033[m \033[0;36mnovos números\033[m
\033[1;31m[5]\033[m \033[0;36msair do programa\033[m''')
    ação = int(input('''\033[0;33m>>> Qual ação você deseja realizar?\033[m 
\033[0;31mDigite o número correspondente: \033[m'''))
    if ação == 1:
        conta = a + b
        print('\033[0;36m{} + {} = {}\033[m'.format(a, b, conta))
    elif ação == 2:
        conta = a * b
        print('\033[0;36m{} x {} = {}\033[m'.format(a, b, conta))
    elif ação == 3:
        if a > b:
            print('\033[0;36m{} é o maior número\033m'.format(a))
        elif a < b:
            print('\033[0;36m{} é o maior número\033[m'.format(b))
        else:
            print('\033[0;36mOs dois números são iguais!\033[m')
    elif ação == 4:
        continue
    elif ação == 5:
        break
    else:
        erro = print('\033[1;31mOpção inválida\033[m')