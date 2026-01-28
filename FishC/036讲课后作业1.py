#036讲课后作业1
print("""欢迎进入鱼C影评小程序
1.数据录入
2.查询数据
3.退出程序""")
movie = []
is_running = True
while is_running:
    func = input("请输入想要的功能（1/2/3）：")
    if func not in ['1','2','3']:
        print("输入错误！请重新输入")
        continue
    elif func == '3':
        print("感谢使用！")
        break
    elif func == '1':
        name = input("请输入电影名称：")
        date = input("请输入上映日期：")
        director = input("请输入导演名字（多人请用 / 分隔）：")
        actor = input("请输入演员名字（多人请用 / ）分隔：")
        score = input("请输入电影评分：")
        movie_info = [name,date,director,actor,score]
        movie.append(movie_info)
        check = input("请问是否继续录入（Y/N）:")
        if check == 'Y':
            continue
        elif check == 'N':
            continue
        else:
            print("输入错误！")
    elif func == '2':
        if not movie:
            print("没有电影信息，请先录入！")
            continue
        part_name = input("请输入电影名称：")
        found = False
        for each in movie:
            name,date,director,actor,score = each
            if part_name in name:
                found = True
                director = [direc.strip() for direc in director.split('/')]
                actor = [act.strip() for act in actor.split('/')]
                print(f'''电影名称：{name}
上映日期：{date}
导演名单：{director}
演员名单：{actor}
当前评分：{score}''')
        if not found:
            print("没找到这个电影！")
        continue