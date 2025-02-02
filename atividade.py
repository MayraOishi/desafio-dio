nome = input("Qual o seu nome? ")
xp = int(input("Qual o seu XP? "))  # Convertendo a entrada para inteiro

if xp <= 1000:
    nivel = "Ferro"
elif 1001 <= xp <= 2000:
    nivel = "Bronze"
elif xp >= 2001:
    nivel = "Prata"
else:
    nivel = "Desconhecido"

print(f"O herói de nome {nome} está no nível de {nivel}.")