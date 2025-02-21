import matplotlib.pyplot as plt
import numpy as np

# 数据准备
X = [0, 5, 10, 15, 20, 25, 30, 35, 40]  # x轴数据

# -0.06x+3.3=y
# y轴数据
MCRB_Y = [3.3, 3, 2.7, 2.4, 2.1, 1.8, 1.5, 1.2, 0.9]
LR_Y = [4.2, 4.0, 3.95, 3.9, 3.85, 3.8, 3.7, 3.6, 3.5]
FITZ_Y = [4.2, 4.0, 3.9, 3.9, 3.85, 3.8, 3.65, 3.6, 3.45]
KAY_Y = [5.7, 4.8, 4.3, 3.8, 3.3, 3.2, 2.7, 2.5, 2.3]
MM_Y = [6.1, 4.5, 4.1, 3.1, 2.9, 2.5, 2.35, 2.1, 2]
MM_FITZ_Y = [6.1, 4.5, 3.9, 3.1, 2.8, 2.5, 2.3, 2, 1.9]


fig, ax = plt.subplots()
ax.plot(X, MCRB_Y, label='MCRB')
ax.plot(X, FITZ_Y, label='Fitz')
ax.plot(X, LR_Y, label='L&R')
ax.plot(X, KAY_Y, label='Kay')
ax.plot(X, MM_Y, label='M&M')
ax.plot(X, MM_FITZ_Y, label='M&M+L&R')

# 标记点
for i in range(9):
    plt.scatter(X[i], MCRB_Y[i], color='blue', marker='s')
for i in range(9):
    plt.scatter(X[i], FITZ_Y[i], color='orange', marker='o')
for i in range(9):
    plt.scatter(X[i], LR_Y[i], color='green', marker='*')
for i in range(9):
    plt.scatter(X[i], KAY_Y[i], color='red', marker='p')
for i in range(9):
    plt.scatter(X[i], MM_Y[i], color='purple', marker='>')
for i in range(9):
    plt.scatter(X[i], MM_FITZ_Y[i], color='brown', marker='H')

# 设置刻度值
plt.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40],
           ['0', '5', '10', '15', '20', '25', '30', '35', '40'])
plt.yticks([0, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5],
           ['0', '10e-14', '10e-12', '10e-10', '10e-8', '10e-6', '10e-4', '10e-2'])

# 设置图表标题、坐标轴标签等
ax.set_title("MSE Curves Of Different Frequency Offset Algorithms")
ax.set_xlabel("Eb/N0(dB)")
ax.set_ylabel("Normalization MSE")

# 显示图例
plt.legend()
plt.grid(True)
# 保存图表到文件
plt.savefig('img/Normalization_MSE.png')
plt.show()
