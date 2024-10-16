# importar o modulo equacoes

import os
from equacoes import *

#programa principal 

if __name__ == "__main__":
    while True:
        print("0 - Sair do programa.")
        print("1 - Calcular equação do 1° grau.")
        print("2 - Calcular equação do 2° grau.")
        
        opcao = input("Opção desejada: ")
        
        os.system("cls")
        
        match opcao:
            case "0":
                print("Obrigado volte sempre!")
                break
            case "1":
                try:
                    a = float(input("Informe o valor de 'a': ").replace(",","."))
                    b = float(input("Informe o valor de 'b': ").replace(",","."))
                    
                    print(f"Valor de x: {primeiro_grau(a,b)}.")
                except Exception as e:
                    print(f"Não foi possível calcular a equação do 1° grau. {e}.")
                finally:
                    continue
            case "2":
                try:
                    a = float(input("Informe o valor de 'a': ").replace(",","."))
                    b = float(input("Informe o valor de 'b': ").replace(",","."))
                    c = float(input("Informe o valor de 'c': ").replace(",","."))
                    
                    resultados = segundo_grau(a, b, c)
                    for resultados in resultados:
                        print(resultados)
                        
                except Exception as e:
                    print(f"Não foi possível calcular a equação do 2° grau. {e}.")
                finally:
                    continue
            case _: 
                print("Opção inválida!")
                continue
                    
        
