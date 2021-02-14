
class Game:

    def __init__(self, my_hp, enemy_hp):
        # 初始化属性
        self.my_hp = my_hp
        self.my_power = 200
        self.enemy_hp = enemy_hp
        self.enemy_power = 199

    def fight(self):
        count = 0
        while True:
            count += 1
            print(f"第{count}回合")
            # 角色的剩余血量
            self.my_hp = self.my_hp - self.enemy_power
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
    def xiuxi(self, time_num):
        print(f"太累了 休息{time_num} 分钟")

if __name__ == '__main__':
    game = Game(1000,100)
    game.fight()
