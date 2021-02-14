from game_oop import Game


class HouYi(Game):
    def __init__(self):
        self.defense = 100
        # 继承父类构造方法
        super().__init__()

    def fight(self):
        count = 0
        while True:
            count += 1
            print(f"第{count}回合")
            # 角色的剩余血量
            self.my_hp = self.my_hp + self.defense - self.enemy_power
            # 敌人的剩余血量
            self.enemy_hp = self.enemy_hp - self.my_power

            print(f"我的血量：{self.my_hp}")
            print(f"敌人的血量：{self.enemy_hp}")
            print()

            if self.my_hp <= 0:
                print("我输了")
                print(f"回合次数{count}")
                break
            elif self.enemy_hp <= 0:
                print("我赢了")
                print(f"回合次数{count}")
                break



if __name__ == '__main__':
    houyi = HouYi()
    houyi.fight()

