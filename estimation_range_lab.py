import matplotlib.pyplot as plt
import numpy as np

# X轴数据
X = []
for i in range(42):
    X.append(i)
print(X)

# Y轴数据
MM_Y = [0, 2.05, -1.5, 0.3, 0.2, -0.7,
        0.5, 0.2, 0.2, 0, -0.25,
        0.1, -0.25, 0.65, 0.4, -0.75,
        0.4, 0.1, 1.6, -0.6, -1.05,
        -0.6, 0.1, -0.6, -0.35, 0.55,
        -0.25, -0.2, 1.2, -0.75, 0.55,
        0.1, -1.1, -0.7, 0.25, -0.7,
        0.6, 0, 0.75, -0.2, 0.2,
        0.4]
FITZ_Y = [-0.06, -0.01, -0.043, 0.038, 0.005, 0.045,
          -0.02, 0.019, -0.018, -0.04, -0.029,
          -0.049, 0.044, -0.015, -0.025, 0.025,
          0.015, -0.028, -0.005, -0.021, 0.044,
          0.058, 0.019, 0.03, -0.016, 0.016,
          -0.02, 0.001, -0.017, -0.025, 0.025,
          0.012, -0.018, -0.034, 0.044, -0.015,
          -0.005, 0.039, -0.003, -0.022, -0.055,
          0.052]
LR_Y = []
KAY_Y = []



fig, ax = plt.subplots()
ax.plot(X, MM_Y, label='M&M')
ax.plot(X, FITZ_Y, label='Fitz')
# ax.plot(X, LR_Y, label='L&R')
# ax.plot(X, KAY_Y, label='Kay')
# ax.plot(X, MM_Y, label='M&M')
# ax.plot(X, MM_FITZ_Y, label='M&M+Fitz')

# 标记点
for i in range(42):
    plt.scatter(X[i], MM_Y[i], color='blue', marker='s')
for i in range(42):
    plt.scatter(X[i], FITZ_Y[i], color='orange', marker='o')
# for i in range(9):
#     plt.scatter(X[i], LR_Y[i], color='green', marker='*')
# for i in range(9):
#     plt.scatter(X[i], KAY_Y[i], color='red', marker='p')
# for i in range(9):
#     plt.scatter(X[i], MM_Y[i], color='purple', marker='>')
# for i in range(9):
#     plt.scatter(X[i], MM_FITZ_Y[i], color='brown', marker='H')

# 设置刻度值
plt.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45],
           ['0', '5', '10', '15', '20', '25', '30', '35', '40', '45'])
plt.yticks([-1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5],
           ['-1.5', '-1', '-0.5', '0', '0.5', '1', '1.5', '2', '2.5'])

# 设置图表标题、坐标轴标签等
ax.set_title("Estimation Range Of Different Frequency Offset Algorithms")
ax.set_xlabel("Sequence Length")
ax.set_ylabel("Frequency Offset Estimation Value")

# 显示图例
plt.legend()
plt.grid(True)
# 保存图表到文件
plt.savefig('img/Estimation_Range_Lab.png')
plt.show()
