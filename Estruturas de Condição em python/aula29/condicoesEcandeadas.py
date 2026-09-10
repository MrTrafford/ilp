idade = int(input("Digite sua idade"))
if (idade<=15):
    print("O usuário não pode votar")
elif (idade>=16 and idade<=17) or (idade>=70):
    print("O usuário tem voto opcional")
else:
    print("O voto é obrigatório")

