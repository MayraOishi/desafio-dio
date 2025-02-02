nome = input("Qual o seu nome? ")
xp = int(input("Qual o seu XP? "))  # Convertendo a entrada para inteiro

if xp <= 1000:
    nivel = "Ferro"
elif 1001 <= xp <= 2000:
    nivel = "Bronze"
elif 2001 <= xp <= 5000:
    nivel = "Prata"
elif 5001 <= xp <= 8000:
    nivel = "Platina Diamante"
elif 8001 <= xp <= 9000:
    nivel = "Ascendente"
elif 9001 <= xp <= 10000:
    nivel = "Imortal"
else:
    nivel = "Radiante"

print(f"O herói de nome {nome} está no nível de {nivel}.")