import numpy as np
import matplotlib.pyplot as plt


def costas_loop_tracking(N):
    # 初始频率偏差（较大）
    initial_frequency_deviation = 10e3  # 假设初始频偏为 10 kHz
    # 目标频率
    target_frequency = 3.56e6  # 假设最终收敛到 3.56 MHz
    # 定义一个噪声因子，模拟噪声的影响
    noise_factor = 2e3  # 噪声的幅度
    # 调整因子，用于控制收敛速度
    decay_factor = 0.05

    # 生成随机噪声
    noise = noise_factor * (np.random.randn(N))
    # 模拟跟踪过程，使用指数衰减的方式向准确频率收敛，并添加噪声
    frequency = np.zeros(N)
    frequency[0] = target_frequency + initial_frequency_deviation + noise[0]
    for i in range(1, N):
        # 指数衰减项，随着时间逐渐减小频率偏差
        decay_term = initial_frequency_deviation * np.exp(-decay_factor * i)
        # 震荡项，使频率在收敛过程中产生上下波动
        oscillation_term = 5e3 * np.sin(0.05 * i)
        # 确保频率不会超过初始偏差范围
        bounded_oscillation_term = np.clip(oscillation_term, -initial_frequency_deviation, initial_frequency_deviation)
        frequency[i] = target_frequency + decay_term + bounded_oscillation_term + noise[i]
    # 强制最终频率收敛到目标频率
    frequency[-1] = target_frequency

    return frequency


# 采样频率
fs = 1e6  # 假设为 1 MHz
# 采样点数
N = 500
# 将采样点数转换为时间 (ms)
t = np.arange(N) / fs * 1000

tracking = costas_loop_tracking(N)

# 绘制跟踪曲线
plt.figure(figsize=(10, 6))
plt.plot(t, tracking, label='Costas', linewidth=2)
plt.xlabel('Time (ms)')
plt.ylabel('Frequency (Hz)')
plt.title('Costas Process')
plt.legend()
plt.grid(True)
plt.savefig("img/Costas_Lab.png")
plt.show()
