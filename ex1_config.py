# ex1_config.py
# 基于ResNet50的ImageNet预训练配置
_base_ = 'mmpretrain::resnet/resnet50_8xb32_in1k.py'

# 模型配置
model = dict(
    # 修改分类头为5分类任务（对应花卉数据集的类别数）
    head=dict(
        num_classes=5,      # 分类类别数量
        topk=(1,),         # 评估指标：Top-1准确率
    )
)

# 数据集配置
data_root = './data/flower_dataset'  # 数据集根目录

# 训练数据加载器配置
train_dataloader = dict(
    dataset=dict(
        type='ImageNet',  # 数据集类型（按ImageNet格式组织）
        data_root=data_root,  # 数据集根路径
        ann_file='train.txt',  # 训练集标注文件
        data_prefix='train',   # 训练图像文件夹
    )
)

# 验证数据加载器配置
val_dataloader = dict(
    dataset=dict(
        type='ImageNet',  # 数据集类型
        data_root=data_root,  # 数据集根路径
        ann_file='val.txt',    # 验证集标注文件
        data_prefix='val',     # 验证图像文件夹
    )
)

# 训练配置
train_cfg = dict(
    max_epochs=20,  # 训练总轮次
)

# 优化器配置
optim_wrapper = dict(
    optimizer=dict(
        type='SGD',   # 优化器类型：随机梯度下降
        lr=0.001,     # 学习率
        momentum=0.9, # 动量参数
        weight_decay=0.0001  # 权重衰减
    )
)

# 预训练权重路径（用于模型微调）
load_from = './checkpoints/resnet50_8xb32_in1k_20210831-ea4938fc.pth'