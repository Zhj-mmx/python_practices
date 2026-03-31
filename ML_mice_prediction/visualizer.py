"""
===============================================================================
结果可视化模块
===============================================================================
功能：
1. 特征分布图
2. 特征重要性图
3. ROC 曲线
4. 混淆矩阵
===============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import roc_curve, auc, confusion_matrix
import os


class ResultVisualizer:
    """结果可视化器"""
    
    def __init__(self, output_dir=r"D:\python_code\ML_mice_prediction\figures"):
        """
        参数：
            output_dir: 图片保存目录
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
        # 设置中文字体
        plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']
        plt.rcParams['axes.unicode_minus'] = False
        
        # 设置风格
        sns.set_style("whitegrid")
    
    def plot_feature_distribution(self, df, feature_cols):
        """
        绘制特征分布图（按标签分组）
        
        参数：
            df: 带标签的 DataFrame
            feature_cols: 特征列名列表
        """
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        axes = axes.flatten()
        
        for idx, col in enumerate(feature_cols[:4]):  # 最多画 4 个
            ax = axes[idx]
            
            # 按标签分组绘制箱线图
            df_temp = df[['label', col]].dropna()
            label_0 = df_temp[df_temp['label'] == 0][col]
            label_1 = df_temp[df_temp['label'] == 1][col]
            
            # 箱线图
            data_to_plot = [label_0.values, label_1.values]
            bp = ax.boxplot(data_to_plot, labels=['不适合 (0)', '适合 (1)'], patch_artist=True)
            
            # 设置颜色
            colors = ['#FF6B6B', '#4ECDC4']
            for patch, color in zip(bp['boxes'], colors):
                patch.set_facecolor(color)
            
            ax.set_ylabel(col, fontsize=10)
            ax.set_title(f'{col} 分布', fontsize=12)
            
            # 添加数据点
            for i, label_data in enumerate([label_0, label_1]):
                y = np.random.normal(i + 1, 0.04, size=len(label_data))
                ax.scatter(y, label_data.values, alpha=0.5, s=30, color='black')
        
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, '01_feature_distribution.png'), dpi=150)
        plt.close()
    
    def plot_feature_importance(self, model, feature_names):
        """
        绘制特征重要性图
        
        参数：
            model: 训练好的模型
            feature_names: 特征名称列表
        """
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # 获取特征重要性
        if hasattr(model, 'coef_'):
            importance = np.abs(model.coef_[0])
            coef = model.coef_[0]
        elif hasattr(model, 'feature_importances_'):
            importance = model.feature_importances_
            coef = importance  # 随机森林没有方向
        else:
            print("模型不支持特征重要性提取")
            return
        
        # 排序
        sorted_idx = np.argsort(importance)[::-1]
        
        # 绘制条形图
        colors = ['#4ECDC4' if c > 0 else '#FF6B6B' for c in coef[sorted_idx]]
        bars = ax.barh(range(len(importance)), importance[sorted_idx], color=colors)
        
        ax.set_yticks(range(len(importance)))
        ax.set_yticklabels([feature_names[i] for i in sorted_idx])
        ax.set_xlabel('重要性', fontsize=12)
        ax.set_title('特征重要性', fontsize=14)
        
        # 添加数值标签
        for bar, val in zip(bars, importance[sorted_idx]):
            ax.text(val + 0.01, bar.get_y() + bar.get_height()/2, f'{val:.3f}', 
                   va='center', fontsize=10)
        
        # 图例说明
        from matplotlib.patches import Patch
        legend_elements = [
            Patch(facecolor='#4ECDC4', label='正相关 (系数>0)'),
            Patch(facecolor='#FF6B6B', label='负相关 (系数<0)')
        ]
        ax.legend(handles=legend_elements, loc='lower right')
        
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, '02_feature_importance.png'), dpi=150)
        plt.close()
    
    def plot_roc_curve(self, model, X, y):
        """
        绘制 ROC 曲线
        
        参数：
            model: 训练好的模型
            X: 特征矩阵
            y: 标签向量
        """
        fig, ax = plt.subplots(figsize=(8, 8))
        
        # 留一法预测概率
        cv_proba = cross_val_predict(model, X, y, cv=5, method='predict_proba')[:, 1] \
                   if len(y) >= 5 else model.predict_proba(X)[:, 1]
        
        # 计算 ROC
        fpr, tpr, thresholds = roc_curve(y, cv_proba)
        roc_auc = auc(fpr, tpr)
        
        # 绘制曲线
        ax.plot(fpr, tpr, color='#4ECDC4', lw=2, label=f'ROC 曲线 (AUC = {roc_auc:.3f})')
        ax.plot([0, 1], [0, 1], color='gray', lw=1, linestyle='--', label='随机猜测')
        
        # 填充面积
        ax.fill_between(fpr, tpr, alpha=0.3, color='#4ECDC4')
        
        ax.set_xlim([0.0, 1.0])
        ax.set_ylim([0.0, 1.05])
        ax.set_xlabel('假阳性率 (1 - 特异度)', fontsize=12)
        ax.set_ylabel('真阳性率 (灵敏度)', fontsize=12)
        ax.set_title('ROC 曲线', fontsize=14)
        ax.legend(loc='lower right')
        
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, '03_roc_curve.png'), dpi=150)
        plt.close()
    
    def plot_confusion_matrix(self, model, X, y):
        """
        绘制混淆矩阵
        
        参数：
            model: 训练好的模型
            X: 特征矩阵
            y: 标签向量
        """
        fig, ax = plt.subplots(figsize=(6, 5))
        
        # 留一法预测
        cv_pred = cross_val_predict(model, X, y, cv=5, method='predict') \
                  if len(y) >= 5 else model.predict(X)
        
        # 计算混淆矩阵
        cm = confusion_matrix(y, cv_pred)
        
        # 绘制热力图
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                   xticklabels=['预测阴性 (0)', '预测阳性 (1)'],
                   yticklabels=['实际阴性 (0)', '实际阳性 (1)'],
                   ax=ax, cbar_kws={'label': '样本数'})
        
        ax.set_xlabel('预测标签', fontsize=12)
        ax.set_ylabel('实际标签', fontsize=12)
        ax.set_title('混淆矩阵', fontsize=14)
        
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, '04_confusion_matrix.png'), dpi=150)
        plt.close()
