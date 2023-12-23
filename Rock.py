import random

cpu_score = player_score = 0

beats = {
    "Kéo":"Bao",
    "Bao": "Búa",
    "Búa":"Kéo"
}

def rps (computer, player):
    global cpu_score, player_score
    if beats[computer] == player:
        cpu_score += 1
        return"Máy Thắng"
    
    if beats[player]==computer:
        player_score += 1
        return "Bạn thắng"
    
    return "Hòa"

choices = ("Kéo", "Búa", "Bao")
i = 6
while i > 0:
    computer = random.choice(choices)
    player = input("Kéo, Búa hay Bao: ").capitalize()

    if player == "End":
        print("Điểm cuối cùng")
        print(f"Điểm của máy\t: {cpu_score}")
        print(f"Điểm của bạn\t: {player_score}")
        break
    elif player not in choices:
        print("Lựa chọn không hợp lệ.")
    else:
        print(rps(computer, player))
        i -= 1
        print("Điểm cuối cùng")
        print(f"Điểm của máy\t: {cpu_score}")
        print(f"Điểm của bạn\t: {player_score}")
