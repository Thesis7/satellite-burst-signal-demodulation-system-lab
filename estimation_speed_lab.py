import matplotlib.pyplot as plt

DATA_LENGTH = 41

# X轴数据
X = []
for i in range(DATA_LENGTH):
    X.append(i)
print(X)

# Y轴数据
MM_Y = [0, 0.04, 0.08, 0.13, 0.18, 0.25,
        0.33, 0.42, 0.52, 0.63, 0.75,
        0.89, 1.04, 1.2, 1.37, 1.55,
        1.75, 1.96, 2.18, 2.42, 2.67,
        2.94, 3.22, 3.52, 3.83, 4.16,
        4.5, 4.86, 5.23, 5.62, 6.02,
        10.33, 10.67, 11.02, 11.38,11.75,
        12.13, 12.52, 12.92, 13.33, 13.75]

FITZ_Y = [0, 0.08, 0.13, 0.21, 0.3, 0.42,
          0.55, 0.69, 0.85, 1.02, 1.2,
          1.41, 1.64, 1.89, 2.16, 2.44,
          2.75, 3.07, 3.41, 3.77, 4.15,
          4.56, 4.98, 5.43, 5.89, 6.37,
          6.87, 7.39, 7.93, 8.49, 9.07,
          16.52, 16.88, 17.24, 17.61, 17.99,
          18.38, 18.78, 19.19, 19.61, 20.04]

LR_Y = [0, 0.12, 0.21, 0.33, 0.45, 0.59,
        0.75, 0.92, 1.1, 1.3, 1.52,
        1.76, 2.02, 2.29, 2.58, 2.89,
        3.21, 3.55, 3.91, 4.29, 4.68,
        5.1, 5.54, 6, 6.48, 6.98,
        7.5, 8.04, 8.6, 9.18, 9.78,
        18.45, 18.84, 19.24, 19.65,20.07,
        20.5, 20.94, 21.39, 21.85, 22.32]

KAY_Y = [0, 0.06, 0.11, 0.18, 0.25, 0.34,
         0.44, 0.55, 0.67, 0.8, 0.94,
         1.09, 1.26, 1.44, 1.63, 1.84,
         2.06, 2.29, 2.54, 2.8, 3.08,
         3.37, 3.68, 4, 4.34, 4.69,
         5.06, 5.44, 5.84, 6.25, 6.68,
         12.22, 12.56, 12.91, 13.27, 13.64,
         14.02, 14.41, 14.81, 15.22, 15.64]

MM_FITZ_Y = [0, 0.12, 0.21, 0.34, 0.48, 0.65,
             0.84, 1.06, 1.3, 1.57, 1.86,
             2.18, 2.53, 2.9, 3.3, 3.73,
             4.18, 4.66, 5.16, 5.69, 6.24,
             6.82, 7.43, 8.06, 8.72, 9.4,
             10.11, 10.85, 11.61, 12.4, 13.22,
             17.56, 18.12, 18.7, 19.3, 19.92,
             20.56, 21.22, 21.9, 22.6, 23.32]

COSTAS_Y = [0, 0.2, 0.35, 0.55, 0.8, 1.1,
            1.45, 1.85, 2.3, 2.8, 3.35,
            4, 4.7, 5.45, 6.25, 7.1,
            8, 8.95, 9.95, 11, 12.1,
            13.25, 14.45, 15.7, 17, 18.35,
            19.75, 21.2, 22.7, 24.25, 25.85,
            27.5, 29.2, 30.95, 32.75, 34.6,
            36.5, 38.45, 40.45, 42.5, 44.6]

fig, ax = plt.subplots()
ax.plot(X, MM_Y, label='M&M')
ax.plot(X, FITZ_Y, label='Fitz')
ax.plot(X, LR_Y, label='L&R')
ax.plot(X, KAY_Y, label='Kay')
ax.plot(X, MM_FITZ_Y, label='M&M+L&R')
ax.plot(X, COSTAS_Y, label='Costas')

# 标记点
for i in range(DATA_LENGTH):
    plt.scatter(X[i], MM_Y[i], color='blue', marker='.')
    plt.scatter(X[i], FITZ_Y[i], color='orange', marker='.')
    plt.scatter(X[i], LR_Y[i], color='green', marker='.')
    plt.scatter(X[i], KAY_Y[i], color='red', marker='.')
    plt.scatter(X[i], MM_FITZ_Y[i], color='purple', marker='.')
    plt.scatter(X[i], COSTAS_Y[i], color='brown', marker='.')

# 设置刻度值
plt.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40],
           ['0', '5', '10', '15', '20', '25', '30', '35', '40'])
plt.yticks([0, 5, 10, 15, 20, 25],
           ['0', '5', '10', '15', '20', '25'])

# 设置图表标题、坐标轴标签等
ax.set_title("Estimation Speed Of Different Frequency Offset Algorithms")
ax.set_xlabel("Sample Length")
ax.set_ylabel("Estimation Speed Value (ms)")

# 显示图例
plt.legend()
plt.grid(True)
# 保存图表到文件
plt.savefig('img/Estimation_Speed_Lab.png')
plt.show()
