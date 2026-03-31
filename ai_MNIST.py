# 安装必要的库（在命令行中运行）
# pip install torch torchvision matplotlib numpy

import torch
import torchvision
import matplotlib.pyplot as plt
import numpy as np

# 打印环境信息
print(f"PyTorch版本: {torch.__version__}")
print(f"CUDA是否可用: {torch.cuda.is_available()}")  # 如果有GPU会显示True

# 加载MNIST数据集
train_dataset = torchvision.datasets.MNIST(
    root='./data',           # 数据存储路径
    train=True,              # 训练集
    download=True,           # 如果不存在则下载
    transform=torchvision.transforms.ToTensor()  # 将图像转换为张量
)

test_dataset = torchvision.datasets.MNIST(
    root='./data',
    train=False,             # 测试集
    download=True,
    transform=torchvision.transforms.ToTensor()
)

# 探索数据集
print(f"训练集样本数: {len(train_dataset)}")
print(f"测试集样本数: {len(test_dataset)}")

# 查看一个样本
sample_image, sample_label = train_dataset[0]
print(f"图像形状: {sample_image.shape}")  # 应该是 [1, 28, 28] - 单通道，28x28像素
print(f"标签: {sample_label}")

# 可视化一个样本
plt.figure(figsize=(8, 4))
for i in range(6):  # 显示6个样本
    plt.subplot(2, 3, i+1)
    image, label = train_dataset[i]
    plt.imshow(image.squeeze(), cmap='gray')  # 去掉通道维度并显示灰度图
    plt.title(f'Label: {label}')
    plt.axis('off')
plt.tight_layout()
plt.savefig('mnist_samples.png', dpi=150, bbox_inches='tight')
print("图像已保存为 mnist_samples.png")
