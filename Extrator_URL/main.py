import os
from extrator_url import ExtratorURL

history = []

def menu():
    os.system('clear')
    print('------ Bem Vindo ao Extrator de URL ------\n')
    print('\t1. Validar nova URL')
    print('\t2. Extrair valor de uma URL')
    print('\t3. Histórico de URLs válidas')
    print('\t0. Sair\n')

def validar_url():
    os.system('clear')
    print('------ Validador de URL ------\n')
   
    continuar = True
    while continuar:
        if not continuar:
            break

        string = str(input('> Insira a sua URL: '))
        nova_url = ExtratorURL(string)

        if nova_url.valida:
            print(f'A URL {nova_url.url} é válida\n')
            history.append(nova_url)
        else:
            print(f'A string apresentada não é uma URL válida\n')
        
        while (True):
            print('Deseja validar outra URL? (1-Sim, 2-Não)')
            opcao = int(input('> '))
            if (opcao == 1):
                continuar = True
                break
            elif (opcao == 2):
                continuar = False
                break
            else:
                print('Opção inválida. Tente novamente.')
                continue

    input('\n> Pressione ENTER para voltar ao menu <')
    
def exibir_historico():
    os.system('clear')
    print('------ Historico ------\n')

    if not history:
        print('Ainda não há nenhuma URL válida no histórico.\n')
    else:
        index = 1
        for item in history:
            print(f'{index} - {item}\n')
            index += 1 

    input('\n> Pressione ENTER para voltar ao menu <')
    
def extrair_valor():
    os.system('clear')
    print('------ Extrair Valor ------\n')

    continuar = True
    while continuar:
        string = str(input('Insira uma URL com parâmetro: '))
        url = ExtratorURL(string)
        if url.valida and url.get_url_parametros():
            history.append(url)
            outro_param = True
            while outro_param:
                param = str(input('Insira o parâmetro à ser extraido: '))
                valor = url.get_valor_parametro(param)
                if valor is None:
                    print('Parâmetro não encontrado. Tente novamente.\n')
                    continue
                print(f'{param} = {valor}\n')
                
                while (True):
                    print('Deseja buscar outro parametro na mesma URL? (1-Sim, 2-Não)')
                    opcao = int(input('> '))
            
                    if (opcao == 1):
                        outro_param = True
                        break
                    elif (opcao == 2):
                        outro_param = False
                        break
                    else:
                        print('Opção inválida. Tente novamente.\n')
                        continue
        
            while (True):
                print('\nDeseja extrair outra URL? (1-Sim, 2-Não)')
                opcao = int(input('> '))
                if (opcao == 1):
                    continuar = True
                    break
                elif (opcao == 2):
                    continuar = False
                    break
                else:
                    print('Opção inválida. Tente novamente.\n')
                    continue
        else:
            print('A URL deve ser válida e deve possui parâmetros.\n')

    input('\n> Pressione ENTER para voltar ao menu <')


def main():
    while (True):
        try:
            menu()
            opcao = int(input('> '))
        
            match (opcao):
                case 1:
                    validar_url()
                case 2:
                    extrair_valor()
                case 3:
                    exibir_historico()
                case 0:
                    os.system('clear')
                    print('Programa encerrado.')
                    break
                case _:
                    print('Valor inválido.\n')
                    input('> Pressione ENTER para continuar <')
        except ValueError:
            print('Valor inválido.\n')
            input('> Pressione ENTER para continuar <')
        except KeyboardInterrupt:
                os.system('clear')
                print('Programa encerrado.')
                exit(1)

if __name__ == '__main__':
    main()