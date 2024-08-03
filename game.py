import math
import random
import itertools
import numpy as np


class Cuidiao:
    def __init__(self, red, cuidiao1_level, cuidiao2_level, cuidiao3_level, cuidiao4_level):
        self.red = np.array([red, 0, 0, 0, 0])
        self.cuidiao_level = np.array([cuidiao1_level, cuidiao2_level, cuidiao3_level, cuidiao4_level])
        self.occupation = 0
        self.advantage = np.array([0, 0, 0])

    def cuidiao1(self):
        if self.cuidiao_level[0] == 1:
            self.occupation = 1
            self.red[1] = self.red[0]
        elif self.cuidiao_level[0] == 2:
            self.occupation += 0
            self.red[1] = self.red[0]
            self.advantage[0] = 100
        elif self.cuidiao_level[0] == 3:
            self.occupation += 0
            self.red[1] = 2*self.red[0]
            self.advantage[0] = 100
        self.red[0] = 0
        return self.red, self.occupation

    def cuidiao2(self):
        if self.cuidiao_level[1] == 1:
            self.occupation += 1
            self.red[2] = self.red[1]
        elif self.cuidiao_level[1] == 2:
            self.occupation += 1
            self.red[2] = 2*self.red[1]
        elif self.cuidiao_level[1] == 3:
            self.red[2] = 2*self.red[1]
            self.advantage[1] = 100
        self.red[1] = 0
        return self.red, self.occupation

    def cuidiao3(self):
        if self.cuidiao_level[2] == 1:
            self.occupation += 1
            self.red[3] = self.red[2]
        elif self.cuidiao_level[2] == 2:
            self.occupation += 1
            self.red[3] = math.ceil(self.red[2]*2.4)
        elif self.cuidiao_level[2] == 3:
            self.red[3] = math.ceil(self.red[2]*2.4)
            self.advantage[2] = 100
        self.red[2] = 0
        return self.red, self.occupation

    def cuidiao4(self):
        self.occupation += 1
        self.red[4] = self.red[3]
        self.red[3] = 0
        cuidiao4_flag = 0
        if self.cuidiao_level[3] == 2:
            cuidiao4_flag = 2
        elif self.cuidiao_level[3] == 3:
            cuidiao4_flag = 3
        return self.red, self.occupation, cuidiao4_flag


class Lvchun:
    def __init__(self, blue, lvchun1_level, lvchun2_level, lvchun3_level):
        self.blue = np.array([blue, 0, 0, 0])
        self.yellow = 0
        self.lvchun_level = np.array([lvchun1_level, lvchun2_level, lvchun3_level])
        self.occupation = 0

    def lvchun1(self):
        self.occupation += 1
        if self.lvchun_level[0] == 1:
            self.blue[1] = math.ceil(self.blue[0]*0.5)
            self.yellow += math.floor(self.blue[0]*0.5)
        elif self.lvchun_level[0] == 2:
            self.blue[1] = math.ceil(self.blue[0]*0.8)
            self.yellow += math.floor(self.blue[0]*0.2)
        elif self.lvchun_level[0] == 3:
            self.blue[1] = self.blue[0]
            self.yellow += self.blue[0]
        self.blue[0] = 0
        return self.blue, self.yellow, self.occupation

    def lvchun2(self):
        self.occupation += 1
        if self.lvchun_level[1] == 1:
            self.blue[2] = math.ceil(self.blue[1]*0.4)
            self.yellow += math.floor(self.blue[1]*0.6)
        elif self.lvchun_level[1] == 2:
            self.blue[2] = math.ceil(self.blue[1]*0.6),
            self.yellow += math.floor(self.blue[1]*0.4)
        elif self.lvchun_level[1] == 3:
            self.blue[2] = math.ceil(self.blue[1]*0.8)
            self.yellow += math.floor(self.blue[1]*0.2)+2*self.blue[2]
        self.blue[1] = 0
        return self.blue, self.yellow, self.occupation

    def lvchun3(self):
        self.occupation += 1
        if self.lvchun_level[2] == 1:
            self.blue[3] = math.ceil(self.blue[2]*0.3),
            self.yellow += math.floor(self.blue[2]*0.7)
        elif self.lvchun_level[2] == 2:
            self.blue[3] = math.ceil(self.blue[2]*0.5)
            self.yellow += math.floor(self.blue[2]*0.5)
        elif self.lvchun_level[2] == 3:
            self.blue[3] = math.ceil(self.blue[2]*0.7)
            self.yellow += math.floor(self.blue[2]*0.3)+2*self.blue[3]
        self.blue[2] = 0
        return self.blue, self.yellow, self.occupation


class Luojing:
    def __init__(self, yellow, luojing1_level, luojing2_level, luojing3_level):
        self.yellow = yellow
        self.luojing_level = np.array([luojing1_level, luojing2_level, luojing3_level])
        self.occupation = 0

    def luojing1(self):
        self.occupation += 1
        if self.luojing_level[0] == 1:
            self.yellow = self.yellow*2
        elif self.luojing_level[0] == 2:
            self.yellow = self.yellow*3
        elif self.luojing_level[0] == 3:
            self.yellow = self.yellow*5
        return self.yellow, self.occupation

    def luojing2(self):
        self.occupation += 1
        if self.luojing_level[1] == 1:
            self.yellow = self.yellow*3
        elif self.luojing_level[1] == 2:
            self.yellow = self.yellow*5
        elif self.luojing_level[1] == 3:
            self.yellow = self.yellow*8
        return self.yellow, self.occupation

    def luojing3(self):
        self.occupation += 1
        yellow_score_add = 0
        if self.luojing_level[2] == 1:
            self.yellow = self.yellow*5
        elif self.luojing_level[2] == 2:
            self.yellow = self.yellow*9
        elif self.luojing_level[2] == 3:
            self.yellow = self.yellow*9
            yellow_score_add = 1
        return self.yellow, self.occupation, yellow_score_add


class Zharou:
    def __init__(self, purple1, yellow, blue, red, zharou1_level, zharou2_level, zharou3_level):
        self.purple = np.array([purple1, 0, 0, 0])
        self.yellow = yellow
        self.blueI = blue[0]
        self.redII = red[1]
        self.zharou_level = np.array([zharou1_level, zharou2_level, zharou3_level])
        self.occupation = 0
        self.purple_score_add = 0

    def zharou1(self):
        self.occupation += 1
        if self.zharou_level[0] == 1:
            if self.purple[0] >= self.yellow:
                self.purple[1] = self.yellow
                self.purple[0] = self.purple[0] - self.yellow
                self.yellow = 0
            else:
                self.purple[1] = self.purple[0]
                self.yellow = self.yellow - self.purple[0]
                self.purple[0] = 0
        elif self.zharou_level[0] == 2:
            if self.purple1 != 0 and self.yellow != 0:
                self.purple[1] = math.ceil((self.purple[0]+self.yellow)*0.5)
                self.purple[0] = 0
                self.yellow = 0
        elif self.zharou_level[0] == 3:
            self.purple_score_add += 5
            if self.purple[0] != 0 and self.yellow != 0:
                self.purple[1] = math.ceil((self.purple[0]+self.yellow)*0.5)
                self.purple[0] = 0
                self.yellow = 0
        return self.purple, self.occupation, self.purple_score_add

    def zharou2(self):
        self.occupation += 1
        if self.zharou_level[1] == 1:
            if self.purple[1] >= self.blueI:
                self.purple[2] = self.blueI
                self.purple[1] = self.purple[1] - self.blueI
                self.blueI = 0
            else:
                self.purple[2] = self.purple[1]
                self.blueI = self.blueI - self.purple[1]
                self.purple[1] = 0
        elif self.zharou_level[1] == 2:
            self.purple_score_add = self.purple_score_add+15
            if self.purple[1] >= self.blueI:
                self.purple[2] = self.blueI
                self.purple[1] = self.purple[1] - self.blueI
                self.blueI = 0
            else:
                self.purple[2] = self.purple[1]
                self.blueI = self.blueI - self.purple[1]
                self.purple[1] = 0
        elif self.zharou_level[1] == 3:
            self.purple_score_add = self.purple_score_add+15
            if self.purple[1] != 0 and self.yellow != 0:
                self.purple[2] = math.ceil((self.purple[1]+self.yellow)*0.5)
                self.purple[1] = 0
                self.yellow = 0
        return self.purple, self.occupation, self.purple_score_add

    def zharou3(self):
        self.occupation += 1
        zharou_flag = 0
        if self.zharou_level[2] == 1:
            if self.purple[2] >= self.redII:
                self.purple[3] = self.redII
                self.purple[2] = self.purple[2] - self.redII
                self.redII = 0
            else:
                self.purple[3] = self.purple[2]
                self.redII = self.redII - self.purple[2]
                self.purple[2] = 0
        elif self.zharou_level[2] == 2:
            if self.purple[2] != 0 and self.yellow != 0:
                self.purple[3] = math.ceil((self.purple[2]+self.yellow)*0.5)
                self.purple[2] = 0
                self.yellow = 0
        elif self.zharou_level[2] == 3:
            if self.purple[2] != 0 and self.yellow != 0:
                self.purple[3] = math.ceil((self.purple[2]+self.yellow)*0.5)
                self.purple[2] = 0
                self.yellow = 0
                zharou_flag = 1
        return self.purple, self.occupation, zharou_flag


class Game:
    def __init__(self, red, purple, blue, yellow, table=2):
        self.red = np.array([red, 0, 0, 0, 0])
        self.purple = np.array([purple, 0, 0, 0])
        self.blue = np.array([blue, 0, 0, 0])

        self.red_score = np.array([1, 2, 10, 35, 85])
        self.purple_score = np.array([1, 2, 22, 105])
        self.blue_score = np.array([1, 5, 50, 500])

        self.yellow = yellow
        self.yellow_score = 1
        # 标志定义
        self.zharou_flag = 0
        self.cuidiao_flag = 0

        self.total_occupation = 0
        self.score = 0
        self.table = table

        self.operation_list = []

    def calculate_score(self):
        self.score += sum(self.red_score*self.red)
        self.score += sum(self.purple_score*self.purple)
        self.score += self.yellow_score*self.yellow
        self.score += sum(self.blue_score*self.blue)
        if self.cuidiao_flag:
            if self.cuidiao_flag == 2:
                self.score += 1500*(self.table-self.total_occupation)
            elif self.cuidiao_flag == 3:
                self.score += 5000*(self.table-self.total_occupation)
        if (self.zharou_flag == 1 and all(
                value == 0 for array in [self.red, self.blue, self.yellow] for value in array)
                and all(value == 0 for value in self.purple[:3])):
            self.score += self.purple_score[3]*100

    def game(self):
        # 所有可能的操作序列
        operations = ['cuidiao1', 'cuidiao2', 'cuidiao3', 'cuidiao4',
                      'lvchun1', 'lvchun2', 'lvchun3',
                      'luojing1', 'luojing2', 'luojing3',
                      'zharou1', 'zharou2', 'zharou3']
        max_score = 0
        best_operations = []

        # 遍历所有操作序列的排列组合
        for ops in itertools.permutations(operations, self.table+3):
            red = self.red
            purple = self.purple
            blue = self.blue
            yellow = self.yellow

            cuidiao = Cuidiao(red[0], 3, 3, 3, 3)
            lvchun = Lvchun(blue[0], 3, 3, 3)
            luojing = Luojing(yellow, 3, 3, 3)
            zharou = Zharou(purple[0], yellow, blue, red, 3, 3, 3)

            for op in ops:
                if self.total_occupation >= self.table:
                    break
                if op.startswith('cuidiao'):
                    cuidiao_method = getattr(cuidiao, op)
                    result = cuidiao_method()
                    self.red = result[0]
                    self.total_occupation += result[1]
                    if op == 'cuidiao4':
                        self.cuidiao_flag = result[2]
                elif op.startswith('lvchun'):
                    lvchun_method = getattr(lvchun, op)
                    result = lvchun_method()
                    self.blue = result[0]
                    self.yellow = result[1]
                    self.total_occupation += result[2]
                elif op.startswith('luojing'):
                    luojing_method = getattr(luojing, op)
                    result = luojing_method()
                    self.yellow = result[0]
                    self.total_occupation += result[1]
                elif op.startswith('zharou'):
                    zharou_method = getattr(zharou, op)
                    result = zharou_method()
                    self.purple = result[0]
                    self.total_occupation += result[1]
                    if op == 'zharou3':
                        self.zharou_flag = result[2]

            self.calculate_score()
            if self.score > max_score:
                max_score = self.score
                best_operations = ops

        return max_score, best_operations

    # 游戏执行示例
game = Game(100, 50, 30, 20, table=6)
final_score, operations = game.game()
print(f"最终得分: {final_score}")
print(f"最佳操作序列: {operations}")




