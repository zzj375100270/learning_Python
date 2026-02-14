# 展示所有牌型（考虑到用户自己输入比较麻烦，展示出来便于拷贝）
def show_cards():
    all_cards = ["♦3", "♦4", "♦5", "♦6", "♦7", "♦8", "♦9", "♦10", "♦J", "♦Q", "♦K", "♦1", "♦2",
                 "♥3", "♥4", "♥5", "♥6", "♥7", "♥8", "♥9", "♥10", "♥J", "♥Q", "♥K", "♥1", "♥2",
                 "♣3", "♣4", "♣5", "♣6", "♣7", "♣8", "♣9", "♣10", "♣J", "♣Q", "♣K", "♣1", "♣2",
                 "♠3", "♠4", "♠5", "♠6", "♠7", "♠8", "♠9", "♠10", "♠J", "♠Q", "♠K", "♠1", "♠2",
                 "🌙", "☀"]
    
    all_cards = all_cards[::-1]

    for i in range(54):
        print(all_cards.pop(), end=' ')
        if (i+1) % 13 == 0:
            print()
    print()
    

# 2 张拍的情况：对牌
def is_pair(cards):
    if cards[0] == cards[1]:
        return True
    else:
        return False


# 2 张牌的情况：火箭
def is_rocket(cards):
    if 14 in cards and 15 in cards:
        return True
    else:
        return False


# 3 张牌的情况：三张牌相同
def is_three(cards):
    if len(set(cards)) == 1:
        return True
    else:
        return False


# 4 张牌的情况：炸弹
def is_bomb(cards):
    if len(set(cards)) == 1:
        return True
    else:
        return False


# 获取用户输入的扑克牌
def get_input():
    cards = input("请出牌（空格间隔，退出请输入Q）：")
    if cards == 'Q':
        return 0
    else:
        cards = cards.split() # "♠1 ♠2 ♠3 ♠4 ♠5" -> ['♠1', '♠2', '♠3', '♠4', '♠5']
        return cards


# 将扑克牌映射成代表权限的数字
def change_input(cards):
    result = []
    target = {'3':1, '4':2, '5':3, '6':4, '7':5, '8':6, '9':7, '10':8, 'J':9, 'Q':10, 'K':11, '1':12, '2':13}
    for each in cards:
        num = target.get(each[1:])
        if num:
            result.append(num)
        else:
            result.append(14 if each == '🌙' else 15)

    return result


# 检查组合是否符合出牌规则
def check(cards):
    # 检查2张牌的情况
    if len(cards) == 2:
        if is_pair(cards):
            print("符合规则：对牌")
        elif is_rocket(cards):
            print("符合规则：火箭")
        else:
            print("不符合规则！")
            
    # 检查3张牌的情况       
    elif len(cards) == 3:
        if is_three(cards):
            print("符合规则：三张牌相同")
        else:
            print("不符合规则！")
            
    # 检查4张牌的情况
    elif len(cards) == 4:
        if is_bomb(cards):
            print("符合规则：炸弹")
        else:
            print("不符合规则！")


# 程序主流程
show_cards()
cards = get_input()
while cards:
    cards = change_input(cards)
    check(cards)
    cards = get_input()
