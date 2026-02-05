import random
cards = ("♥A","♥2","♥3","♥4","♥5","♥6","♥7","♥8","♥9","♥10","♥J","♥Q","♥K",
         "♠A","♠2","♠3","♠4","♠5","♠6","♠7","♠8","♠9","♠10","♠J","♠Q","♠K",
         "♣A","♣2","♣3","♣4","♣5","♣6","♣7","♣8","♣9","♣10","♣J","♣Q","♣K",
         "♦A","♦2","♦3","♦4","♦5","♦6","♦7","♦8","♦9","♦10","♦J","♦Q","♦K",
         "大王","小王")
first_player = input("请输入第一位玩家的名称：")
second_player = input("请输入第二位玩家的名称：")
third_player = input("请输入第三位玩家的名称：")

def wash_cards(cards):  #洗牌函数
    cards_list = list(cards)
    length = len(cards_list)
    for i in range(length-1,-1,-1):
        j = random.randint(0,i)
        cards_list[i] , cards_list[j] = cards_list[j] , cards_list[i]
    return cards_list

def choose_one(first,second,third):     #选地主
    players = [first,second,third]
    chosen_player = random.choice(players)
    return chosen_player

def giving_cards(cards,chosen_player):   #发牌
    received_cards = cards.copy()
    dizhu = received_cards[51:54]
    first_cards = received_cards[0:51:3]
    second_cards = received_cards[1:51:3]
    third_cards = received_cards[2:51:3]
    if first_player == chosen_player:
        first_cards.extend(dizhu)
    elif second_player == chosen_player:
        second_cards.extend(dizhu)
    else:
        third_cards.extend(dizhu)
    players_cards = [first_cards,second_cards,third_cards]
    return players_cards

chosen_player = choose_one(first_player,second_player,third_player)
new_cards = wash_cards(cards)
received_cards = giving_cards(new_cards,chosen_player)
print(f"地主是{chosen_player}")
print(f"[{first_player}]拿到的牌是：{' '.join(received_cards[0])}")
print(f"[{second_player}]拿到的牌是：{' '.join(received_cards[1])}")
print(f"[{third_player}]拿到的牌是：{' '.join(received_cards[2])}")