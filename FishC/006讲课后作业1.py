while True:
    score = input("请输入你的分数：")
    if score == "e":
        break
    else:
        score = int(score)
        if score < 0 or score > 100:
            print("别逗！")
        else:
            if score == 100:
                print("S")
            else:
                if score >= 90:
                    print("A")
                else:
                    if score >= 80:
                        print("B")
                    else:
                        if score >= 60:
                            print("C")
                        else:
                            print("D")
