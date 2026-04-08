class Cars:
    def __init__(self, brand, model, platenum, dayrent, carid):
        self.brand = brand
        self.model = model
        self.platenum = platenum
        self.dayrent = dayrent
        self.carid = carid

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_platenum(self):
        return self.platenum

    def get_dayrent(self):
        return self.dayrent

    def get_carid(self):
        return self.carid

    def calc_rent(self, days, discount=1.0):
        return self.dayrent * days * discount


class EconomyCar(Cars):
    def __init__(self, brand, model, platenum, dayrent, carid):
        super().__init__(brand, model, platenum, dayrent, carid)
        self.subsidy = 50

    def calc_rent(self, days, discount=1.0):
        base_rent = super().calc_rent(days, discount)
        return base_rent - self.subsidy * days


class LuxuryCar(Cars):
    def __init__(self, brand, model, platenum, dayrent, carid):
        super().__init__(brand, model, platenum, dayrent, carid)
        self.insurance = 200

    def calc_rent(self, days, discount=1.0):
        base_rent = super().calc_rent(days, discount)
        return base_rent + self.insurance * days


class SportCar(Cars):
    def __init__(self, brand, model, platenum, dayrent, carid):
        super().__init__(brand, model, platenum, dayrent, carid)
        self.wear_fee = 150

    def calc_rent(self, days, discount=1.0):
        base_rent = super().calc_rent(days, discount)
        return base_rent + self.wear_fee * days


class SUV(Cars):
    def __init__(self, brand, model, platenum, dayrent, carid):
        super().__init__(brand, model, platenum, dayrent, carid)

    def calc_rent(self, days, discount=1.0):
        base_rent = super().calc_rent(days, discount)
        if days > 7:
            return base_rent * 0.7
        return base_rent


class CarRentalBusiness:
    def __init__(self):
        self.cars = {}
        self.stocks = {
            'EconomyCar': 0,
            'LuxuryCar': 0,
            'SportCar': 0,
            'SUV': 0
        }
        self.next_ids = {
            'EconomyCar': 10000,
            'LuxuryCar': 20000,
            'SportCar': 30000,
            'SUV': 40000
        }

    def operate(self):
        print("=" * 50)
        print("欢迎使用汽车租赁系统")
        print("=" * 50)
        while True:
            print("\n功能选项：")
            print("1. 录入汽车")
            print("2. 查看库存")
            print("3. 租车服务")
            print("4. 还车服务")
            print("5. 退出系统")
            choice = input("请输入选项(1-5): ")
            if choice == '1':
                self.register()
            elif choice == '2':
                self.get_stock()
            elif choice == '3':
                self.rent_car()
            elif choice == '4':
                self.return_car()
            elif choice == '5':
                print("感谢使用，再见！")
                break
            else:
                print("无效选项，请重新输入！")

    def register(self):
        print("\n--- 录入汽车 ---")
        car_type = input("请输入汽车类型(EconomyCar/LuxuryCar/SportCar/SUV): ")
        brand = input("请输入品牌: ")
        model = input("请输入型号: ")
        platenum = input("请输入车牌号: ")
        dayrent = float(input("请输入每天租金: "))

        car_classes = {
            'EconomyCar': EconomyCar,
            'LuxuryCar': LuxuryCar,
            'SportCar': SportCar,
            'SUV': SUV
        }

        if car_type in car_classes:
            carid = self.next_ids[car_type]
            car = car_classes[car_type](brand, model, platenum, dayrent, carid)
            self.cars[str(carid)] = car
            self.stocks[car_type] += 1
            self.next_ids[car_type] += 1
            print(f"{car_type} {brand} {model} 录入成功！")
            print(f"车辆编号: {carid}")
        else:
            print("无效的汽车类型！")

    def get_stock(self):
        print("\n--- 当前库存 ---")
        for car_type, count in self.stocks.items():
            print(f"{car_type}: {count} 辆")

    def rent_car(self):
        print("\n--- 租车服务 ---")
        carid = input("请输入要租的车辆编号: ")
        if carid not in self.cars:
            print("车辆不存在！")
            return

        car = self.cars[carid]
        car_type = type(car).__name__

        if self.stocks[car_type] <= 0:
            print("该车型已无库存！")
            return

        days = int(input("请输入租赁天数: "))
        discount = float(input("请输入折扣(如0.9表示9折, 默认1.0): ") or 1.0)

        total_rent = car.calc_rent(days, discount)
        print(f"\n租车成功！")
        print(f"车型: {car_type}")
        print(f"品牌: {car.get_brand()}")
        print(f"型号: {car.get_model()}")
        print(f"车牌: {car.get_platenum()}")
        print(f"租赁天数: {days}天")
        print(f"折扣: {discount}")
        print(f"总租金: {total_rent}元")

        self.stocks[car_type] -= 1

    def return_car(self):
        print("\n--- 还车服务 ---")
        carid = input("请输入要归还的车辆编号: ")
        if carid not in self.cars:
            print("车辆不存在！")
            return

        car = self.cars[carid]
        car_type = type(car).__name__

        print("还车成功！")
        self.stocks[car_type] += 1


if __name__ == "__main__":
    business = CarRentalBusiness()
    business.operate()