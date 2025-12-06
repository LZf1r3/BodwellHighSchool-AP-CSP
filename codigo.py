def armario(altura, profundidade, comprimento):
    lateral = print(f"\nLateral:\n    Altura = {altura}\n    Profundidade = {profundidade}\n")
    Superior = print(f"Superior:\n    Comprimento = {comprimento-3}\n    Profundidade = {profundidade}\n")
    fundo = print(f"Fundo:\n    Comprimento = {comprimento-3}\n    Altura = {altura-3}\n")
    D_V = print(f"Divisoria Vertical:\n    Altura = {altura-3}\n    Profundidade = {profundidade-2}\n")
    D_H = print(f"Divisoria Horizontal:\n    Comprimento = {comprimento-3}\n    Profundidade = {profundidade-2}\n")
    porta_1 = print(f"1 Porta:\n    Altura = {altura}\n    Comprimento = {comprimento}\n")
    porta_2 = print(f"2 Portas:\n    Altura = {altura}\n    Comprimento = {(comprimento-0.5)/2}\n")

def gaveteiro(altura, profundidade, comprimento):
    frente = print(f"\nFrente: \n   Altura: {altura}\n   Comprimento: {comprimento}")
    fundo = print(f"\nFrente/Fundo:\n   Comprimento: {comprimento - 5.5}\n   Altura: {altura - 5}")
    laterais = print(f"\nLaterais:\n   Profundidade: {profundidade - 10}\n   Altura: {altura - 5}")
    tampo = print(f"\nTampo:\n   Profundidade: {profundidade - 10}\n   Comprimento: {comprimento - 5.5}\n")

if __name__ == "__main__":
    while True:

        choose = int(input("Codigo Armario (1) ou Codigo Gaveteiro (2)?\n.: "))
        a = float(input("altura = "))
        p = float(input("Profundidade = "))
        c = float(input("Comprimento = "))

        if choose == 1:
            armario(a, p, c)
        
        elif choose == 2:
            gaveteiro(a, p, c)
        
        else:
            print("Invalido!")