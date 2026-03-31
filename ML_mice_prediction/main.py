"""
===============================================================================
小鼠 cart 肽疗法响应预测 - 主程序
===============================================================================
课题：用机器学习预测小鼠对 cart 肽疗法的响应
数据：20 只小鼠，5 组分类，行为学指标 + WB 蛋白表达量
任务：二分类（适合/不适合疗法）

作者：Dreamclaw
日期：2026-03-26
===============================================================================
"""

import pandas as pd
import numpy as np
import joblib
import warnings
warnings.filterwarnings('ignore') #调用各种库，相当于拿来需要的工具，但我并不清楚各种库的作用

from data_preprocessor import DataPreprocessor
from model_trainer import ModelTrainer
from evaluator import ModelEvaluator
from visualizer import ResultVisualizer #从其他 python 调用函数


def main(): #作为主程序
    """主流程"""
    print("=" * 70) #print用于反映运行流程，便于确认报错位置依旧运行状态
    print("小鼠 cart 肽疗法响应预测 - 建模流程")
    print("=" * 70)
    
    # ==================== 1. 加载数据 ====================
    print("\n[1/5] 加载数据...")
    data_path = r"C:\Users\96519\.openclaw\workspace\data\mice_experiment.csv" #文件路径，并设定为只读
    df = pd.read_csv(data_path, encoding='utf-8-sig') #用pd来读csv类型数据
    print(f"✓ 数据形状：{df.shape}") #显示数据形状
    print(f"✓ 列名：{list(df.columns)}") #显示列名
    print(f"✓ 分组情况：\n{df['类别'].value_counts()}")
    
    # ==================== 2. 数据预处理 ====================
    print("\n[2/5] 数据预处理...")
    preprocessor = DataPreprocessor() #面对对象编程的调用
    df_processed = preprocessor.process(df) #调用process功能
    
    # 计算标签
    df_labeled = preprocessor.define_labels(df_processed) #调用定义标签功能
    print(f"✓ 可用样本数：{len(df_labeled)}")
    print(f"✓ 标签分布：\n{df_labeled['label'].value_counts()}")
    
    # 准备特征和标签（移除所有非数值列）
    X = df_labeled.drop(columns=['label', '类别', '焦虑改善率', '行为改善率'], errors='ignore') #涉及数据处理了，相关操作并不熟悉
    y = df_labeled['label'] 
    print(f"✓ 特征矩阵形状：{X.shape}")
    print(f"✓ 特征列：{list(X.columns)}")
    
    # ==================== 3. 训练模型 ====================
    print("\n[3/5] 训练模型...")
    trainer = ModelTrainer() 
    trained_models = trainer.train_all_models(X, y)
    best_name, best_model = trainer.select_best_model(trained_models) #调用类及其功能
    model_comparison = {name: info['cv_accuracy'] for name, info in trained_models.items()}
    print(f"✓ 最佳模型：{best_name}")
    
    # ==================== 4. 模型评估 ====================
    print("\n[4/5] 模型评估...")
    evaluator = ModelEvaluator()
    metrics = evaluator.evaluate(best_model, X, y)
    evaluator.print_report(metrics)
    
    # ==================== 5. 可视化结果 ====================
    print("\n[5/5] 可视化结果...")
    visualizer = ResultVisualizer(output_dir='figures')
    
    # 准备带标签的 DataFrame 用于绘图
    df_viz = df_labeled.copy()
    feature_cols = list(X.columns)
    
    # 逐个绘制
    visualizer.plot_feature_distribution(df_viz, feature_cols)
    print("  ✓ 特征分布图已保存")
    visualizer.plot_feature_importance(best_model, feature_cols)
    print("  ✓ 特征重要性图已保存")
    visualizer.plot_roc_curve(best_model, X, y)
    print("  ✓ ROC 曲线已保存")
    visualizer.plot_confusion_matrix(best_model, X, y)
    print("  ✓ 混淆矩阵已保存")
    
    # ==================== 保存模型 ====================
    print("\n" + "=" * 70)
    print("保存模型...")
    joblib.dump(best_model, 'models/best_model.pkl')
    joblib.dump(metrics, 'models/metrics.pkl')
    print("✓ 模型已保存到 models/")
    print("=" * 70)
    
    return best_model, metrics


if __name__ == "__main__":
    best_model, metrics = main()
 #整个main的过程被分为六个部分，并另外写了六个类来进行这六个部分。这样的结构更清晰一些。每个部分都类似，调用类，调用类的方法完成相应功能，并填充print以反映程序运行情况