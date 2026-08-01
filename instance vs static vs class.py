class Demo:
    college = "MIT"

    def show(self):
        print("Instance Method")

    @staticmethod
    def display():
        print("Static Method")

    @classmethod
    def info(cls):
        print(cls.college)

d = Demo()
d.show()
Demo.display()
Demo.info()