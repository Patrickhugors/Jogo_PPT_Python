import random

def play():
    user = input("Qual a sua escolha? Pedra, Papel ou Tesoura. \n")
    computer = random.choice(['pedra', 'papel', 'tesoura'])

    if user == computer:
        return "Empate!"

    if win(user, computer):
        return "Você ganhou!"

    return "Você perdeu!"

def win(player, opponent):

    if (player == 'pedra' and opponent == 'tesoura') or (player == 'tesoura' and opponent == 'papel') \
        or (player == 'papel' and opponent == 'pedra'):
        return True

print(play())