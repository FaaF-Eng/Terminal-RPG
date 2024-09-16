#Projeto PYTHON SENAI - RPG DE TERMINAL - Por Fábio Teixeira.
#Requisitos do projeto:
# For ou While - OK
# Lista ou Tuple - OK
# IF ou Mathcase - OK

#Configurando escrita devagar
import sys
import time
import random

def escrever_devagar(texto, intervalo=0.1):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(intervalo)
#Fazendo a opção de Limpar o Terminal durante a execução do programa -> os.system("cls")
#Para interromper o Código durante a execução -> sys.exit()
import os

#Tela inicial do Jogo
print ('=====================================================\n\n\n\n\n')
escrever_devagar('Seja Bem-vindo ao RPG de Terminal\n\n\n\n\n', intervalo=0.1)
print('>Jogar<\n>Ajuda<\n>Sair<\n\n\n\n')
selecao_menu = input('Digite uma das opções acima: \n\n\n').lower()
while True:
    if selecao_menu == 'sair':
        os.system("cls")
        print ('=====================================================\n\n\n\n\n')
        escrever_devagar('\n\n\nSaindo do Jogo\n\n\n\n\n', intervalo=0.1)
        escrever_devagar('Desenvolvido por Fábio Teixeira\n\n\n', intervalo=0.1)
        sys.exit()
    elif selecao_menu == 'ajuda':
        os.system("cls")
        print('\n\n\n===============================================\n\n')
        escrever_devagar('\n\n\nMenu de Ajuda\n\n\n', intervalo=0.05)
        print ('Esse é o RPG de Terminal\n\n\nPara jogar basta selecionar as opções disponíveis na tela\n\n')
        print ('caso queira sair do jogo basta selecionar a opção "sair" no menu e para começar a aventura escreva "jogar"\n\n\n')
        pausa = input ('\n*Pressione a tecla "ENTER" para continuar')
        os.system("cls")
        print ('=====================================================\n\n\n\n\n')
    #Aqui que vai rolar o jogo:
    elif selecao_menu =='jogar':
        os.system("cls")
        print ('=====================================================\n\n\n\n\n')
        break
    #Caso o player escreva algo errado no menu principal:
    else:
        print ('\n\n\nPorfavor digite apenas as opções informadas!\n\n')
        escrever_devagar('Retornando ao Menu Principal...', intervalo=0.2)
        os.system("cls")
        print ('=====================================================\n\n\n\n\n')
    escrever_devagar('Seja Bem-vindo ao RPG de Terminal\n\n\n\n\n', intervalo=0.1)
    print('>Jogar<\n>Ajuda<\n>Sair<\n\n\n\n')
    selecao_menu = input('Digite uma das opções acima: \n\n\n').lower()


escrever_devagar('\n\nVocê acorda em uma cabana de madeira, a luz do sol entra pela janela e você vê um homem alto e barbado a sua frente\n\n', intervalo=0.05)
escrever_devagar('\n\n<Mago>Seja bem-vindo ao mundo mágico de WRIFT! Uma terra cheia de magía, aventuras e códigos!\n\n',intervalo=0.05 )
nome_player = input ('\n\n<Mago> Qual o seu nome aventureiro(a)? ')
os.system("cls")
print ('=====================================================\n\n\n\n\n')
escrever_devagar(f'\n\n<Mago> Muito Prazer,{nome_player} eu me chamo JUBILEU! o mago\n', intervalo=0.05) 
pausa = input ('\n*Pressione a tecla "ENTER" para continuar')
os.system("cls")
print ('=====================================================\n\n\n\n\n')
escrever_devagar(f'\n\n<Jubileu> Ainda bem que acordou, preciso da ajuda de um grande guerreiro, estou velho de mais para me aventurar mundo a fora.', intervalo=0.05)
pausa =('')
escrever_devagar(f'\n\nCaro guerreiro(a) {nome_player} , você estaria hábil de atravessar a floresta sombria e recuperar o Livro de feitiços que fica em uma caverna localizada após a mata da morte?',intervalo=0.05)
print ('\n\n')
#Escolha 01
escolha_01 = input('Aceita a missão do Mago Jubileu? [s/n]').lower()
while True:
    #Escolha 01- NÃO -> Final Preguiçoso
    if escolha_01 == 'n':
        os.system("cls")
        print ('=====================================================\n\n\n\n\n')
        escrever_devagar(f'<Jubileu> Puxa vida...jurava que você seria a pessoa certa para ajudar um pobre mago cansado a realizar seus feitiços. Espero que o destino guarde coisas boas para você,{nome_player}',intervalo=0.05)
        print('\n\n\n\n\n\n\n\n')
        escrever_devagar('              FINAL PREGUIÇOSO\n\n',intervalo=0.05)
        escrever_devagar(f'Você recusou o pedido de ajuda do Mago Jubileu e voltou a dormir, o nome de {nome_player} ficará marcado por toda a terra de WRIFT como o mais preguiçoso de todos os tempos',intervalo=0.05)
        print('\n\n\n\n\n')
        escrever_devagar('Obrigado por ter jogado! RPG feito por Fábio Teixeira',intervalo=0.1)
        print('\n\n\n\n\n\n')
        pausa = input ('\n*Pressione a tecla "ENTER"')
        os.system("cls")
        print ('=====================================================\n\n\n\n\n')
        break
        
            
    #Escolha_01: Caso o jogador escolha a resposta SIM o jogo continua...        
    elif escolha_01 == 's':
        os.system("cls")
        print ('=====================================================\n\n\n\n\n')
        escrever_devagar(f'\n\n<Jubileu> Que maravilha! Escolha uma dessas armas e parta para sua jornada', intervalo=0.05)
        print ('\n\n\n\n\n')
        lista_armas = ['Espada','Arco+Flecha','pato de borracha',]
        print (lista_armas)
        print('\n\nQual arma você deseja carregar?\n\n')
        break
        #Escolha_01: Caso o Jogador escreva algo errado
    else:
        print('\n\nPorfavor digite apenas as opções informadas! \n\n')
        escrever_devagar('Retomando Ação...',intervalo=0.2)
        os.system("cls")
        print ('=====================================================\n\n\n\n\n')
        escrever_devagar(f'\n\nCaro guerreiro(a) {nome_player} , você estaria hábil de atravessar a floresta sombria e recuperar o Livro de feitiços que fica em uma caverna localizada após a mata da morte?',intervalo=0.05)
        print ('\n\n')
        escolha_01 = input('Aceita a missão do Mago Jubileu? [s/n]').lower()
#Interromper o código depois do final preguiçoso:
if escolha_01 == 'n':
    escrever_devagar('GAMEOVER\n\n\n\n\n', intervalo=0.1)
    sys.exit()

#Escolha_arma   
escolha_arma = input ('[1]\n[2]\n[3]\n')
while True:
    if escolha_arma == '1':
        print ('\n*Você selecionou a Espada')
        escrever_devagar(f'\n\n<Jubileu> Ótima escolha de armamento, {nome_player}', intervalo=0.05)
        pausa = input ('\n*Pressione a tecla "ENTER" para continuar')
        os.system("cls")
        print ('=====================================================\n\n\n\n\n')
        break
    elif escolha_arma == '2':
        print ('\n*Você selecionou o Arco com Flecha')
        escrever_devagar(f'\n\n<Jubileu> Ótima escolha de armamento, {nome_player}', intervalo=0.05)
        pausa = input ('\n*Pressione a tecla "ENTER" para continuar')
        os.system("cls")
        print ('=====================================================\n\n\n\n\n')
        break
    elif escolha_arma == '3':
        print ('\n*Você selecionou a porcaria de um pato de borracha')
        escrever_devagar(f'\n\n<Jubileu> Ótima escolha de armamento, {nome_player}', intervalo=0.05)
        pausa = input ('\n*Pressione a tecla "ENTER" para continuar')
        os.system("cls")
        print ('=====================================================\n\n\n\n\n') 
        break
        #Escolha_arma: Caso o jogador escreva algo errado
    else:
        print('\n\nPorfavor digite apenas as opções informadas! \n\n')
        escrever_devagar('Retomando Ação...',intervalo=0.2)
        os.system("cls")
        print ('=====================================================\n\n\n\n\n')  
        print (lista_armas)                                             
        print('\n\nQual arma você deseja carregar?\n\n')
        escolha_arma = input ('[1]\n[2]\n[3]\n')
        break


#Diálogo_01: 
escrever_devagar(f'\n\n<Jubileu> A floresta sombria é perigosa, mas nada se compara a caverna , {nome_player}\n\n\n', intervalo=0.05)
escrever_devagar('*Selecione seu Diálogo:\n\n\n\n\n',intervalo=0.01)
print('[1] "Conte comigo para qualquer desafio, irei recuperar esse livro de feitiços!"\n')
print('[2] "Eu vou ganhar alguma recompensa por isso?"\n')
print('[3] "Espera...como foi que eu fui parar aqui na sua cabana?"\n\n\n')

dialogo_01 = input ('')

while True:
    #Segue o jogo com o caminho padrão
    if dialogo_01 == '1':
        os.system("cls")
        print ('=====================================================\n\n\n\n\n')
        escrever_devagar(f'\n\n<{nome_player}> Conte comigo para qualquer desafio, irei recuperar esse livro de feitiços!\n\n\n', intervalo=0.05)
        escrever_devagar(f'\n\n<Jubileu> É isso que gosto de ouvir! Até logo {nome_player}\n\n\n\n\n',intervalo=0.05)
        escrever_devagar(f'Jubileu te da um tapinha nas costas e você atravessa a porta da cabana, logo a sua frente inicia-se uma mata que vai ficando cada vez mais densa...',intervalo=0.05)
        break
    #Segue o Jogo com o caminho padrão
    elif dialogo_01 == '3':
        os.system("cls")
        print ('=====================================================\n\n\n\n\n')
        escrever_devagar(f'\n\n<{nome_player}> Espera...como foi que eu fui parar aqui na sua cabana??\n\n\n', intervalo=0.05)       
        escrever_devagar(f'\n\n<Jubileu> Digamos que você escutou uma verdade tão chocante que o fez desmaiar, eu apenas o ajudei,{nome_player}\n\n\n\n\n',intervalo=0.1)
        escrever_devagar(f'\n\n<{nome_player}> Entendo,obrigado pela ajuda, seguirei minha aventura então\n\n\n\n\n', intervalo=0.05)
        escrever_devagar(f'Jubileu te da um tapinha nas costas e você atravessa a porta da cabana, logo a sua frente inicia-se uma mata que vai ficando cada vez mais densa...',intervalo=0.05)
        break  
    #Pode seguir pro Final Secreto
    elif dialogo_01 == '2':
        os.system("cls")
        print ('=====================================================\n\n\n\n\n')
        escrever_devagar(f'\n\n<{nome_player}> Eu vou ganhar alguma recompensa por isso?\n\n\n', intervalo=0.05)                
        escrever_devagar(f'\n\n<Jubileu> Ah...eu posso te dar algum prêmio caso você volte vivo.\n\n\n\n\n',intervalo=0.05)
        escrever_devagar(f'\n\n<{nome_player}> Caso eu volte vivo? Vou arriscar minha vida e você nem fala o que é esse prêmio?!\n\n\n', intervalo=0.05)
        escrever_devagar(f'\n\n<Jubileu> Escute...Isso é um RPG, você deveria aproveitar a jornada e aprender lições no caminho.\n\n\n\n\n',intervalo=0.05)
        escrever_devagar(f'\n\n<{nome_player}>',intervalo=0.05) 
        escrever_devagar('RPG?', intervalo=1)
        escrever_devagar(f'\n\n\n\n\n<Jubileu> Sim, isso é uma aventura interativa dentro de um terminal, nossa realidade é uma mentira, por essa razão eu queria tanto aquele livro de feitiços, para poder me libertar daqui.\n\n\n\n\n',intervalo=0.1)
        pausa = input ('\n*Pressione a tecla "ENTER" para continuar')
        os.system("cls")
        print ('=====================================================\n\n\n\n\n')
        escrever_devagar(f'\n\n<Jubileu> Vamos {nome_player}, você tem certeza que não quer me ajudar com esse grande propósito?\n\n\n\n\n',intervalo=0.05)
        escrever_devagar('*Selecione sua ação: \n\n\n\n\n',intervalo=0.01)
        print ('[1] Aceitar a missão do Mago Jubileu e ir pra floresta.\n')
        print ('[2] Lutar contra o Mago Jubileu.\n\n\n')
        escolha_02 = input ('')
        break
    #Caso o player escreva errado:
    else:
        escrever_devagar('\n\nPorfavor digite apenas as opções informadas! \n\n', intervalo=0.2)
        os.system("cls")
        print ('=====================================================\n\n\n\n\n')
        escrever_devagar(f'\n\n<Jubileu> A floresta sombria é perigosa, mas nada se compara a caverna , {nome_player}\n\n\n', intervalo=0.05)
        escrever_devagar('*Selecione seu Diálogo:\n\n\n\n\n',intervalo=0.01)
        print('[1] "Conte comigo para qualquer desafio, irei recuperar esse livro de feitiços!"\n')
        print('[2] "Eu vou ganhar alguma recompensa por isso?"\n')
        print('[3] "Espera...como foi que eu fui parar aqui na sua cabana?"\n\n\n')
        dialogo_01 = input ('')
        

#Código para fazer o jogo prosseguir normalmente:
if dialogo_01 == '1':
    print ('\n\n*Pressione ENTER para continuar')
    escolha_02 = input('')
if dialogo_01 == '3':
    print ('\n\n*Pressione ENTER para continuar')
    escolha_02 = input('')

#A continuação da Escolha_02:
elif escolha_02 == '1':
    os.system("cls")
    print ('=====================================================\n\n\n\n\n')
    escrever_devagar(f'\n\n<{nome_player}> Certo...acredito que encontrar o livro seja o melhor a se fazer\n\n\n', intervalo=0.05)  
    escrever_devagar(f'\n\n<Jubileu> É isso que gosto de ouvir! Até logo {nome_player}\n\n\n\n\n',intervalo=0.05)
    escrever_devagar(f'Jubileu te da um tapinha nas costas e você atravessa a porta da cabana, logo a sua frente inicia-se uma mata que vai ficando cada vez mais densa...',intervalo=0.05)
    pausa = input ('\n*Pressione a tecla "ENTER" para continuar')
    os.system("cls")
    print ('=====================================================\n\n\n\n\n')        
elif escolha_02 == '2':
    #FINAL SECRETO
    os.system("cls")
    print ('=====================================================\n\n\n\n\n')
    # Função para limpar a tela (compatível com Windows e Unix)
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')    
    # Função para desenhar um dado de 20 lados (D20) com um número aleatório
    def draw_d20(number):
        dado = f"""
      Rolando 1D20
         ________
        /        \\
       /          \\
      /            \\
     /      20      \\
     \\              /
      \\            /
       \\          /
        \\________/

            Número: {number:^3}
        """
        print(dado)

    # Função para animar a rolagem do dado e retornar o número final
    def roll_d20_animation():
        for _ in range(10):  # Número de "rolagens"
            clear_screen()
            number = random.randint(1, 20)
            draw_d20(number)
            time.sleep(0.2)  # Controla a velocidade da animação
        
        # Mostra o resultado final
        clear_screen()
        final_number = random.randint(1, 20)
        draw_d20(final_number)
        print(f"O dado rolou e parou no número: {final_number}")
        return final_number  # Certifique-se de que o número final é retornado

    # Parte inicial da narrativa
    os.system("cls")
    print ('=====================================================\n\n\n\n\n')
    escrever_devagar(f'\n\nVocê fica em choque ao descobrir a verdadeira natureza da sua realidade, é uma verdade que não quer aceitar...', intervalo=0.05)
    escrever_devagar(f'\n\n<{nome_player}> Mago...Eu não sei a sua verdadeira intenção comigo nesse lugar desconhecido, mas eu vou acabar com você aqui mesmo!!!\n\n\n', intervalo=0.05)
    escrever_devagar(f'\n\n<Jubileu>  {nome_player}, você não foi feito para lidar com a verdade, eu preciso do livro de feitiços e não posso ir busca-lo sozinho, então acho que terei que te vencer...assim sua memória será deletada quando o terminal reiniciar o RPG.\n\n\n\n\n', intervalo=0.05)
    escrever_devagar(f'\n\n<{nome_player}> Vou te mostrar que não sou qualquer guerreiro!\n\n\n', intervalo=0.05)
    pausa = input ('\n*Pressione a tecla "ENTER" para continuar')

    # Combate
    os.system("cls")
    print ('=====================================================\n\n\n\n\n')
    escrever_devagar('\n               COMBATE \n\n\n', intervalo=0.05)

    # DESENHO DO MAGO
    def mago_ascii():
        mago = [
            "        /\\        ",
            "       /  \\   *   ",
            "        o o   |    ",
            "         V    |    ",
            "    o         o    ",
            "     /       \\     ",
            "    /_________\\    "
        ]
        return mago

    # DESENHO GUERREIRO
    def guerreiro_ascii():
        guerreiro = [
            "       ______       ",
            "      | o  o |  |   ",
            "     |   -  |  |   ",
            "    o         -o-  ",
            "     |      |  |   ",
            "     | ____ |  |   ",
            "     |_|  |_|      "
        ]
        return guerreiro

    # Função para imprimir os desenhos lado a lado
    def imprimir_lado_a_lado():
        mago = mago_ascii()
        guerreiro = guerreiro_ascii()
        
        # Verifica se ambos têm o mesmo número de linhas
        for linha_mago, linha_guerreiro in zip(mago, guerreiro):
            print(linha_mago + "   " + linha_guerreiro)

    imprimir_lado_a_lado()

    # Pausa e início da rolagem do dado
    pausa = input ('\n\n\n*Pressione a tecla "ENTER" para continuar')
    os.system("cls")
    print ('=====================================================\n\n\n\n\n')
    print ('\n\nPara batalhar você deve rolar 1D20, se o valor for maior ou igual a 10 você causará dano ao inimigo')
    pausa = input ('\n\n*Pressione a tecla "ENTER" para rolar 1D20')
    os.system("cls")
    print ('=====================================================\n\n\n\n\n')

    # Rolando o dado
    final_number = roll_d20_animation()

    # Verificando o resultado do dado
    pausa = input ('\n\n*Pressione a tecla "ENTER" para continuar')
    os.system("cls")
    print ('=====================================================\n\n\n\n\n')

    # Condição do ataque
    if final_number >= 10 and escolha_arma == '3':
        escrever_devagar(f'\n\nVocê pode ter feito um ataque forte, mas um pato de borracha é inútil', intervalo=0.05)
        escrever_devagar(f'\n\n<Jubileu>  Sinto muito por isso, {nome_player}. Tentaremos novamente quando você acordar.\n\n\n\n\n', intervalo=0.05)
        escrever_devagar(f'\n\nJubileu faz uma dancinha encantada que lança uma bola de luz em sua direção, tudo de repente se desliga...\n\n', intervalo=0.05)
        pausa = input ('\n\n*Pressione a tecla "ENTER" para continuar')
        os.system("cls")
        print ('=====================================================\n\n\n\n\n')
        escrever_devagar('GAMEOVER\n\n\n\n\n', intervalo=0.1)
        escrever_devagar('Obrigado por ter jogado! RPG feito por Fábio Teixeira', intervalo=0.1)
        sys.exit()
    elif final_number >=10:
        escrever_devagar(f'\n\nVocê acerta o mago de forma certeira e crítica, fazendo cair no chão muito ferido\n', intervalo=0.05)
        escrever_devagar(f'\n\n<Jubileu>  Você lutou bem...{nome_player}. Sempre soube que era forte para concluir a missão...\n\n\n\n\n', intervalo=0.05)
        escrever_devagar(f'\n\nJubileu está morto...e agora você está livre para fazer o que quiser.\n', intervalo=0.05)
        pausa = input ('\n\n*Pressione a tecla "ENTER" para continuar')
        os.system("cls")
        print ('=====================================================\n\n\n\n\n')
        escrever_devagar('              FINAL SECRETO\n\n',intervalo=0.05)
        escrever_devagar(f'Você assassinou o mago, na próxima tente ser mais amigável',intervalo=0.05)
        print('\n\n\n\n\n')
        escrever_devagar('Obrigado por ter jogado! RPG feito por Fábio Teixeira',intervalo=0.1)
        print('\n\n\n\n\n\n')
        sys.exit()
    elif final_number <10:
        escrever_devagar(f'\n\nVocê tenta mas seu ataque não é eficaz\n', intervalo=0.05)
        escrever_devagar(f'\n\n<Jubileu>  Sinto muito por isso, {nome_player}. Tentaremos novamente quando você acordar.\n\n\n\n\n', intervalo=0.05)
        escrever_devagar(f'\n\nJubileu faz uma dancinha encantada que lança uma bola de luz em sua direção, tudo de repente se desliga...\n\n', intervalo=0.05)
        pausa = input ('\n\n*Pressione a tecla "ENTER" para continuar')
        os.system("cls")
        print ('=====================================================\n\n\n\n\n')
        escrever_devagar('GAMEOVER\n\n\n\n\n', intervalo=0.1)
        escrever_devagar('Obrigado por ter jogado! RPG feito por Fábio Teixeira', intervalo=0.1)
        sys.exit()

#NÃO MEXER
else:
    while True: 
        escrever_devagar('\n\nPorfavor digite apenas as opções informadas! \n\n', intervalo=0.2)
        os.system("cls")
        print ('=====================================================\n\n\n\n\n')
        escrever_devagar(f'\n\n<Jubileu> Vamos {nome_player}, você tem certeza que não quer me ajudar com esse grande propósito?\n\n\n\n\n',intervalo=0.05)
        escrever_devagar('*Selecione sua ação: \n\n\n\n\n',intervalo=0.01)
        print ('[1] Aceitar a missão do Mago Jubileu e ir pra floresta.\n')
        print ('[2] Lutar contra o Mago Jubileu.\n\n\n')
        escolha_02 = input ('')
        break     

#FINAL DEMO -fim da demo do jogo
os.system("cls")
print ('=====================================================\n\n\n\n\n')
escrever_devagar('              DEMO COMPLETA\n\n',intervalo=0.05)
escrever_devagar(f'Olá, aventureiro(a)! esse caminho ainda não foi finalizado pelo DEV, mas até o presente momento está disponível 2 finais Bônus para você explorar.',intervalo=0.05)
escrever_devagar('\n\n\nObrigado por ter jogado! RPG feito por Fábio Teixeira\n\n\n', intervalo=0.1)
sys.exit()