class Rectangle:
    width = None
    height = None
    def set_width(self):
        while True:
            try:
                width = float(input("请输入宽度："))
            except ValueError:
                print("宽度必须是一个数字")
            else:
                if width > 0:
                    self.width = width
                    print(f"已将宽度设置为'{self.width}'")
                    break
                else:
                    print("宽度必须大于0")
    def set_height(self):
        while True:
            try:
                height = float(input("请输入高度："))
            except ValueError:
                print("高度必须是一个数字")
            else:
                if height > 0:
                    self.height = height
                    print(f"已将高度设置为'{self.height}'")
                    break
                else:
                    print("高度必须大于0")
    def ensure_width_height(self):
        if self.width is None:
            self.set_width()
        if self.height is None:
            self.set_height()

    def get_perimeter(self):
        self.ensure_width_height()
        return 2 * (self.width + self.height)
    def get_area(self):
        self.ensure_width_height()
        return self.width * self.height

r = Rectangle()
print(f"矩形的周长为：{r.get_perimeter()}")
print(f"矩形的面积为：{r.get_area()}")