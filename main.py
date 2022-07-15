#'w' substitui todo o arquivo, 'r' lê todo o arquivo e 'a' adiciona.
arquivo =  open('arquivo.txt' , 'a')
mensagem = '1'
i = 1

while mensagem != '':
    mensagem = input("Mensagem:")
    if mensagem == '':
        arquivo.write('conversa encerrada\n\n')
    else:
        arquivo.write('Mensagem(' + str(i) + '):')
        arquivo.write(str(mensagem) + '\n')
        i += 1
