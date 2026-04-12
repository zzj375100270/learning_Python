import hashlib

class InputMixin:
    def passwd_is_valid(self, passwd):
        return len(passwd) == 6 and passwd.isdigit()


    def passwd_to_md5(self, passwd):
        md5 = hashlib.md5()
        md5.update(passwd.encode())
        return md5.hexdigest()


    def check_money(self, money):
        try:
            return float(money) >= 0
        except ValueError:
            return False


    def input_money(self):
        money = input('请输入金额：')
        while not self.check_money(money):
            print('金额格式错误！')
            money = input('请输入金额：')
        return float(money)



class Account(InputMixin):
    def __init__(self, username, password, cardid):
        self.username = username
        self.password = password
        self.cardid = cardid
        self.balance = 0.0


    def confirm_name(self, name):
        return self.username == name


    def confirm_passwd(self, passwd):
        return self.password == passwd


    def deposit(self):
        money = self.input_money()
        self.balance += money
        print(f'存款成功，存入{money}元，当前余额为{self.balance}元。')


    def withdraw(self):
        money = self.input_money()
        if money > self.balance:
            print('余额不足！')
            return
        self.balance -= money
        print(f'取款成功，取出{money}元，当前余额为{self.balance}元。')


    def get_balance(self):
        print(f"当前余额为{self.balance}元。")



class UserManager:
    def __init__(self):
        self.users_dict = {}
        self.next_cardid = 88888888


    def input_name(self):
        name = input('请输入姓名：')
        return name


    def input_passwd(self):
        passwd = input('请输入密码：')
        while not (len(passwd) == 6 and passwd.isdigit()):
            print('密码格式错误！')
            passwd = input('请输入密码：')
        md5 = hashlib.md5()
        md5.update(passwd.encode())
        return md5.hexdigest()


    def input_cardid(self):
        cardid = input("请输入卡号：")
        while not (cardid.isdigit() and int(cardid) > 0):
            print('卡号必须是正整数！')
            cardid = input("请输入卡号：")
        return cardid


    def input_transfer_cardid(self):
        cardid = input("请输入收款人卡号：")
        while not (cardid.isdigit() and int(cardid) > 0):
            print('卡号必须是正整数！')
            cardid = input("请输入收款人卡号：")
        return cardid


    def create_account(self):
        name = self.input_name()
        password = self.input_passwd()
        cardid = str(self.next_cardid)
        user = Account(name, password, cardid)
        init_money = user.input_money()
        user.balance = init_money
        self.users_dict[cardid] = user
        self.next_cardid += 1
        print(f'创建成功，卡号为 {cardid}，关联用户 -> {name}')


    def delete_account(self):
        cardid = self.input_cardid()
        if cardid not in self.users_dict:
            print("无此用户！")
            return
        password = self.input_passwd()
        if not self.users_dict[cardid].confirm_passwd(password):
            print("密码错误！")
            return
        name = self.input_name()
        if not self.users_dict[cardid].confirm_name(name):
            print("姓名错误！")
            return
        username = self.users_dict[cardid].username
        del self.users_dict[cardid]
        print(f'删除成功，卡号为 {cardid}，关联用户 -> {username}')


    def login(self):
        cardid = self.input_cardid()
        if cardid not in self.users_dict:
            print("无此用户！")
            return None
        password = self.input_passwd()
        if not self.users_dict[cardid].confirm_passwd(password):
            print("密码错误！")
            return None
        print(f'登录成功，卡号为 {cardid}，关联用户 -> {self.users_dict[cardid].username}')
        return cardid


    def transfer(self, cardid):
        target_cardid = self.input_transfer_cardid()
        if target_cardid == cardid:
            print("不能给自己转账！")
            return
        if target_cardid not in self.users_dict:
            print("收款人不存在！")
            return
        money = self.users_dict[cardid].input_money()
        if money > self.users_dict[cardid].balance:
            print('余额不足！')
            return
        self.users_dict[cardid].balance -= money
        self.users_dict[target_cardid].balance += money
        print(f'转账成功，转账{money}元，当前余额为{self.users_dict[cardid].balance}元。')



def main():
    manager = UserManager()
    print("欢迎使用鱼C银行账户管理系统~")
    while True:
        print("1.创建账户\n2.删除账户\n3.登录账户\n4.退出")
        choice_manager = input("请选择需要的功能：")
        if choice_manager == "1":
            manager.create_account()
        elif choice_manager == "2":
            manager.delete_account()
        elif choice_manager == "3":
            cardid = manager.login()
            if cardid:
                while True:
                    print("1.查询余额\n2.存款\n3.取款\n4.转账\n5.退出")
                    choice_account = input("请选择需要的功能：")
                    if choice_account == "1":
                        manager.users_dict[cardid].get_balance()
                    elif choice_account == "2":
                        manager.users_dict[cardid].deposit()
                    elif choice_account == "3":
                        manager.users_dict[cardid].withdraw()
                    elif choice_account == "4":
                        manager.transfer(cardid)
                    elif choice_account == "5":
                        print("退出成功！")
                        break
                    else:
                        print("输入错误！")
        elif choice_manager == "4":
            print("感谢使用鱼C银行账户管理系统~")
            break
        else:
            print("输入错误！")



if __name__ == "__main__":
    main()