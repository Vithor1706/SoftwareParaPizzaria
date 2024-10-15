#Nome e menu da pizzaria
print("Bem-vido a pizzaria do Vithor Bach de Ávila")
print("Opções de pizzas:")
print("1. Pizza Salgada (PS)")
print("2. Pizza Doce (PD)")
print("Tamanhos de pizza: P (pequena), M (média), G (grande)")

#Referência de preços
precos = {
    "PS": {"P": 30, "M": 45, "G": 60},
    "PD": {"P": 34, "M": 48, "G": 66}
        }

#Acumulador
total_pedido = 0

while True: 
    sabor = input("DIgite o sabor da pizza (PS/PD): ").upper()
    if sabor not in ["PS", "PD"]:
        print("Sabor inválido, tente novamente.")
        continue #volta ao inicio do loop

    tamanho = input("Digite o tamanho da pizza(P/M/G): ").upper()
    if tamanho not in ["P","M","G"]:
        print ("Tamanho inválido, tente novamente.")
        continue #volta ao inicio do loop

#Estrutura para calcular o preco baseado no tamanho e sabor
    preco_pizza = precos[sabor][tamanho]
    total_pedido += preco_pizza
    print(f"Voce pediu uma pizza {sabor} de tamanho {tamanho} no valor de R${preco_pizza:.2f}.")

#Perguntando se o cliente deseja mais alguma coisa
    mais_pedido = input("Deseja pedir mais alguma coisa? (S/N): ").upper()
    if mais_pedido == "N":
        break #Encerra o loop

#Exibindo o total do pedido
print(f"Valor total do pedido: R${total_pedido:.2f}")
print("Obrigado por comprar na pizzaria do Vithor Bach de Ávila!!!")
