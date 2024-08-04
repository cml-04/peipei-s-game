import math
import random
import itertools
import numpy as np
import tkinter as tk


class ConfigMenu(tk.Toplevel):
    def __init__(self, game):
        super().__init__()
        self.title("Configuration Menu")
        self.game = game

        # 创建并放置标签和输入框
        self.red_label = tk.Label(self, text="Red:")
        self.red_label.place(x=100, y=100, width=20, height=20)
        self.red_label.pack()
        self.red_entry = tk.Entry(self)
        self.red_entry.pack()

        self.purple_label = tk.Label(self, text="Purple:")
        self.purple_label.place(x=200, y=100, width=20, height=20)
        self.purple_label.pack()
        self.purple_entry = tk.Entry(self)
        self.purple_entry.pack()

        # ...为其他参数创建更多的标签和输入框...

        # 创建并放置确认按钮
        self.confirm_button = tk.Button(self, text="Confirm", command=self.confirm)
        self.confirm_button.pack()

    def confirm(self):
        # 获取输入框中的值并更新game的参数
        self.game.red = np.array([self.red_entry.get(), 0, 0, 0, 0])
        self.game.purple = np.array([self.purple_entry.get(), 0, 0, 0])
        # ...获取并更新其他参数...

        # 关闭配置菜单
        self.destroy()


class Game:
    def __init__(self, red, purple, blue, yellow, root,
                 cuidiaoI_level=3, cuidiaoII_level=3, cuidiaoIII_level=3, cuidiaoIV_level=3,
                 lvchunI_level=3, lvchunII_level=3, lvchunIII_level=3,
                 zharouI_level=3, zharouII_level=3, zharouIII_level=3,
                 luojingI_level=3, luojingII_level=3, luojingIII_level=3,
                 table=2):
        self.red = np.array([red, 0, 0, 0, 0])自己的红色值为一个numpy数组，其中包含红色分量（red）、透明度（0）、蓝色分量（0）、绿色分量（0）和alpha值（0）。
        self.purple = np.array([purple, 0, 0, 0])
        self.blue = np.array([blue, 0, 0, 0])
        self.yellow = yellow

        self.red_score = np.array([1, 2, 10, 35, 85])
        self.purple_score = np.array([1, 2, 22, 105])
        self.blue_score = np.array([1, 5, 50, 500])
        self.yellow_score = 1

        self.cuidiao_level = np.array([cuidiaoI_level, cuidiaoII_level, cuidiaoIII_level, cuidiaoIV_level])
        self.lvchun_level = np.array([lvchunI_level, lvchunII_level, lvchunIII_level])
        self.zharou_level = np.array([zharouI_level, zharouII_level, zharouIII_level])
        self.luojing_level = np.array([luojingI_level, luojingII_level, luojingIII_level])

        self.cuidiao_advantage = np.array([1, 1, 1, 1])
        self.lvchun_advantage = np.array([1, 1, 1])
        self.zharou_advantage = np.array([1, 1, 1])
        self.luojing_advantage = np.array([1, 1, 1])

        # 标志定义
        self.cuidiao_flag = 0
        self.zharou_flag = 0

        self.occupation = 0
        self.score = 0
        self.table = table

        self.operation_list = []

        self.root = root
        self.root.title('Game')
        self.create_widgets()
        self.level_label = ["初级", "中级", "高级"]

    def open_config_menu(self):
        ConfigMenu(self)

    def create_widgets(self):
        # 创建并放置需要的组件
        # 这里只是一个示例，您需要根据实际需要添加和配置组件
        self.label = tk.Label(self.root, text="PeiPei's Classroom!")
        self.label.pack()
        self.start_button = tk.Button(self.root, text="Start", command=self.start_game)
        self.start_button.pack()
        self.config_button = tk.Button(self.root, text="Config", command=self.open_config_menu)
        self.config_button.pack()


    def start_game(self,):
        # 在这里添加开始游戏���代码
        self.label.destroy()
        self.start_button.destroy()

        self.table_label = tk.Label(self.root, text=f"工作台数量: {self.table}")
        self.table_label.pack()

        self.occupation_label = tk.Label(self.root, text=f"已占用工作台数量: {self.occupation}")
        self.occupation_label.pack()

        self.red_label = tk.Label(self.root, text=f"火焰伊纳: {self.red[0]}")
        self.red_label.pack()

        self.blue_label = tk.Label(self.root, text=f"草伊纳: {self.blue[0]}")
        self.blue_label.pack()

        self.purple_label = tk.Label(self.root, text=f"天空伊纳: {self.purple[0]}")
        self.purple_label.pack()

        self.yellow_label = tk.Label(self.root, text=f"沙伊纳: {self.yellow}")
        self.yellow_label.pack()

        self.cuidiaoI_set = tk.Button(self.root, text=self.level_label[self.cuidiao_level[0]-1]+"淬雕I", command=self.cuidiaoI_and_destroy)
        self.cuidiaoI_set.pack()

    def cuidiaoI_and_destroy(self):
        self.cuidiaoI()
        self.cuidiaoI_set.destroy()

    def cuidiaoI(self):
        if self.cuidiao_level[0] == 1:
            self.occupation += 1
            self.red[1] = self.red[0]
        elif self.cuidiao_level[0] == 2:
            self.red[1] = self.red[0]
            self.advantage[0] = 100
        elif self.cuidiao_level[0] == 3:
            self.red[1] = 2 * self.red[0]
            self.cuidiao_advantage[0] = 100
        self.red[0] = 0
        self.red_label.config(text=f"火焰伊纳I: {self.red[1]}")
        self.occupation_label.config(text="已占用工作台数量: "+str(self.occupation))
        return self

    def cuidiaoII(self):
        if self.cuidiao_level[1] == 1:
            self.occupation += 1
            self.red[2] = self.red[1]
        elif self.cuidiao_level[1] == 2:
            self.occupation += 1
            self.red[2] = 2 * self.red[1]
        elif self.cuidiao_level[1] == 3:
            self.red[2] = 2 * self.red[1]
            self.cuidiao_advantage[1] = 90
        self.red[1] = 0
        return self

    def cuidiaoIII(self):
        if self.cuidiao_level[2] == 1:
            self.occupation += 1
            self.red[3] = self.red[2]
        elif self.cuidiao_level[2] == 2:
            self.occupation += 1
            self.red[3] = math.ceil(self.red[2] * 2.4)
        elif self.cuidiao_level[2] == 3:
            self.red[3] = math.ceil(self.red[2] * 2.4)
            self.cuidiao_advantage[2] = 80
        self.red[2] = 0
        return self

    def cuidiaoIV(self):
        self.occupation += 1
        self.red[4] = self.red[3]
        self.red[3] = 0
        if self.cuidiao_level[3] == 2:
            self.cuidiao_flag = 2
        elif self.cuidiao_level[3] == 3:
            self.cuidiao_flag = 3
        return self

    def lvchunI(self):
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
        return self

    def lvchunII(self):
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
        return self

    def lvchunIII(self):
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
        return self

    def zharouI(self):
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
                self.purple[1] = math.ceil((self.purple[0] + self.yellow) * 0.5)
                self.purple[0] = 0
                self.yellow = 0
        elif self.zharou_level[0] == 3:
            self.purple_score += 5
            if self.purple[0] != 0 and self.yellow != 0:
                self.purple[1] = math.ceil((self.purple[0] + self.yellow) * 0.5)
                self.purple[0] = 0
                self.yellow = 0
        return self

    def zharouII(self):
        self.occupation += 1
        if self.zharou_level[1] == 1:
            if self.purple[1] >= self.blueI:
                self.purple[2] = self.blueI
                self.purple[1] = self.purple[1] - self.blueI
                self.blue[0] = 0
            else:
                self.purple[2] = self.purple[1]
                self.blue[0] = self.blue[0] - self.purple[1]
                self.purple[1] = 0
        elif self.zharou_level[1] == 2:
            self.purple_score += 15
            if self.purple[1] >= self.blueI:
                self.purple[2] = self.blueI
                self.purple[1] = self.purple[1] - self.blueI
                self.blue[0] = 0
            else:
                self.purple[2] = self.purple[1]
                self.blue[0] = self.blue[0] - self.purple[1]
                self.purple[1] = 0
        elif self.zharou_level[1] == 3:
            self.purple_score += 15
            if self.purple[1] != 0 and self.yellow != 0:
                self.purple[2] = math.ceil((self.purple[1] + self.yellow) * 0.5)
                self.purple[1] = 0
                self.yellow = 0
        return self

    def zharouIII(self):
        self.occupation += 1
        if self.zharou_level[2] == 1:
            if self.purple[2] >= self.red[3]:
                self.purple[3] = self.red[3]
                self.purple[2] = self.purple[2] - self.red[3]
                self.red[3] = 0
            else:
                self.purple[3] = self.purple[2]
                self.red[3] = self.red[3] - self.purple[2]
                self.purple[2] = 0
        elif self.zharou_level[2] == 2:
            if self.purple[2] != 0 and self.red[3] != 0:
                self.purple[3] = math.ceil((self.purple[2]+self.red[3])*0.5)
                self.purple[2] = 0
                self.red[3] = 0
        elif self.zharou_level[2] == 3:
            if self.purple[2] != 0 and self.red[3] != 0:
                self.purple[3] = math.ceil((self.purple[2]+self.red[3])*0.5)
                self.purple[2] = 0
                self.red[3] = 0
                self.zharou_flag = 1
        return self

    def luojingI(self):
        self.occupation += 1
        if self.luojing_level[0] == 1:
            self.yellow = self.yellow*2
        elif self.luojing_level[0] == 2:
            self.yellow = self.yellow*3
        elif   埃利夫 self.luojing_level[0] == 3:   导入数学
            self.yellow = self.yellow*5   进口随机
        return   返回 self   出现进口itertools
   导入numpy为np
    def luojingII(self):
        self.occupation   占领 += 1
        if   如果 self.luojing_level[1] == 1:
            self.yellow = self.yellow*3
        elif   埃利夫 self.luojing_level[1] == 2:
            self.yellow = self.yellow*5
        elif   埃利夫 self.luojing_level[1] == 3:
            self.yellow = self.yellow*8
        return   返回 self

    def luojingIII(self):
        self.occupation   占领 += 1
        if   如果 self.luojing_level[2] == 1:
            self.yellow = self.yellow*5
        elif   埃利夫 self.luojing_level[2] == 2:
            self.yellow = self.yellow*9
        elif   埃利夫 self.luojing_level[2] == 3:
            self.yellow = self.yellow*9
            self.yellow_score += 1
        return   返回 self


    def calculate_score(self):
        self.score   分数 += sum(self.red_score*self.red   红色的)
        self.score   分数 += sum(self.purple_score*self.purple)
        self.score   分数 += self.yellow_score*self.yellow
        self.score   分数 += sum(self.blue_score*self.blue)
        if   如果 self.table   表格-self.occupation   占领 < 0:
            self.score   分数 = -1
        if   如果 self.cuidiao_flag:
            if   如果 self.cuidiao_flag == 2:
                self.score   分数 += 1500*(self.table   表格   表格-self.occupation   占领   占领)
            elif   埃利夫 self.cuidiao_flag == 3:
                self.score   分数 += 5000*(self.table   表格-self.occupation   占领)
        if   如果 (self.zharou_flag == 1 and   和 all(
                value == 0 for array in   在……里面 [self.red   红色的, self.blue, self.yellow] for value in   在……里面 array)
                and   和 all(value == 0 for value in   在……里面 self.purple[:3])):
            self.score   分数 += self.purple_score[3]*100

    def game(self):
        # 所有可能的操作序列
        operations = ['cuidiaoI', 'cuidiaoII', 'cuidiaoIII', 'cuidiaoIV',
                      'lvchunI', 'lvchunII', 'lvchunIII',
                      'luojingI', 'luojingII', 'luojingIII',
                      'zharouI', 'zharouII', 'zharouIII']
        max_score = 0
        best_operations = []



# 游戏执行示例
root = tk.Tk()
game = Game(70, 10, 10, 10, root,cuidiaoI_level=1, table=6)
root.mainloop()
print(game.score   分数)
print(game.table   表格-game.occupation   占领)
print(game.red   红色的)
