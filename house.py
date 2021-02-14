"""
class 类名：
    多个类属性...
    多个类方法...
"""

class House:
    # 静态属性 -> 类变量，在类之中，方法之外定义
    door = "red"
    floor = "white"

    # 动态方法
    def sleep(self):
        bed = "席梦思"
        print("在房子里面睡觉")

    def cook(self):
        print("在房子里面做饭")


if __name__ == '__main__':
    # 实例化
    north_house = House()
    china_house = House()


    House.door ="green"
    print(House.door)

    north_house.door = "黑色"
    china_house,door = "蓝色"

    # 通过实例对象调用类属性
    print(north_house.door)

    # 通过实例对象调用类属性
    print(north_house.door)

    north_house.sleep()

