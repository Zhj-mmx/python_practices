"""
===============================================================================
数据预处理模块
===============================================================================
功能：
1. 数据清洗
2. 标签定义（根据疗法响应标准）
3. 特征工程
4. 数据标准化
===============================================================================
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.base import BaseEstimator, TransformerMixin #不清楚调用的功能


class DataPreprocessor(BaseEstimator, TransformerMixin): #对应数据处理部分
    """数据预处理器"""
    
    def __init__(self, anxiety_threshold=0.30, behavior_threshold=0.40):
        """
        参数：
            anxiety_threshold: 焦虑改善阈值 (默认 30%)
            behavior_threshold: 行为敏化改善阈值 (默认 40%)
        """
        self.anxiety_threshold = anxiety_threshold
        self.behavior_threshold = behavior_threshold
        self.scaler = StandardScaler()
        self.feature_cols = None
        self.is_fitted = False #不清楚各个参数的含义
    
    def process(self, df):
        """
        数据清洗和预处理
        
        参数：
            df: 原始 DataFrame
        
        返回：
            df_clean: 清洗后的 DataFrame
        """
        df_clean = df.copy()
        
        # 1. 处理缺失值
        df_clean = df_clean.dropna() #这个dropna是哪来的？干嘛用的
        
        # 2. 处理异常值（可选，根据实际数据）
        # 这里暂时不做，因为样本量太小
        
        # 3. 特征衍生（谨慎添加）
        df_clean = self._create_features(df_clean)
        
        return df_clean
    
    def _create_features(self, df):
        """
        特征工程 - 创建衍生特征
        
        注意：小样本下不宜创建太多特征
        """
        #创建特征似乎是机器学习的知识，有待补充
        #创建特征通过原本的数据获得了新的数据，有什么说法吗
        df_new = df.copy()
        
        # 1. 蛋白比值
        df_new['gb1_gb2_ratio'] = df_new['gb1 表达量'] / (df_new['gb2 表达量'] + 1e-6)
        
        # 2. 焦虑指数（开臂时间/开臂次数）
        df_new['焦虑指数'] = df_new['开臂时间'] / (df_new['开臂次数'] + 1e-6)
        
        # 3. 单位活动度的开臂时间
        df_new['单位活动开臂'] = df_new['开臂时间'] / (df_new['活动度'] + 1e-6)
        
        return df_new
    
    def define_labels(self, df):
        """
        定义标签：适合/不适合 cart 疗法
        
        判定标准：
        - 焦虑改善 ≥ 30%
        - 行为敏化改善 ≥ 40%
        - 两者同时满足 = 适合疗法 (1)
        
        参数：
            df: 预处理后的 DataFrame
        
        返回：
            df_labeled: 带标签的 DataFrame（仅包含 cart 治疗组）
        """
        df_labeled = df.copy()
        
        # 计算各组均值作为基线
        # “基线”这个概念出自哪里？
        # 下面的操作都看不懂e
        group_means = df_labeled.groupby('类别')[['开臂时间', '活动度']].mean()
        
        # 获取对照组和戒断组基线
        control_openarm = group_means.loc['对照组', '开臂时间']
        acute_withdrawal_openarm = group_means.loc['急性戒断', '开臂时间']
        chronic_withdrawal_openarm = group_means.loc['慢性戒断', '开臂时间']
        
        control_activity = group_means.loc['对照组', '活动度']
        acute_withdrawal_activity = group_means.loc['急性戒断', '活动度']
        chronic_withdrawal_activity = group_means.loc['慢性戒断', '活动度']
        
        print("\n基线数据：")
        print(f"  对照组 - 开臂时间：{control_openarm:.2f}, 活动度：{control_activity:.2f}")
        print(f"  急性戒断 - 开臂时间：{acute_withdrawal_openarm:.2f}, 活动度：{acute_withdrawal_activity:.2f}")
        print(f"  慢性戒断 - 开臂时间：{chronic_withdrawal_openarm:.2f}, 活动度：{chronic_withdrawal_activity:.2f}")
        
        # 初始化标签
        df_labeled['label'] = np.nan
        df_labeled['焦虑改善率'] = np.nan
        df_labeled['行为改善率'] = np.nan #还是不懂
        
        # 对 cart 治疗组计算标签
        for idx, row in df_labeled.iterrows():
            group = row['类别']
            
            if group == '急性+cart':
                # 与急性戒断组比较
                baseline_openarm = acute_withdrawal_openarm
                baseline_activity = acute_withdrawal_activity
            elif group == '慢性+cart':
                # 与慢性戒断组比较
                baseline_openarm = chronic_withdrawal_openarm
                baseline_activity = chronic_withdrawal_activity
            else:
                # 非治疗组，排除
                continue
            
            # 计算改善率
            anxiety_improvement = (row['开臂时间'] - baseline_openarm) / (baseline_openarm + 1e-6)
            behavior_improvement = (baseline_activity - row['活动度']) / (baseline_activity + 1e-6)
            
            df_labeled.at[idx, '焦虑改善率'] = anxiety_improvement
            df_labeled.at[idx, '行为改善率'] = behavior_improvement
            
            # 判定标签
            if (anxiety_improvement >= self.anxiety_threshold) and \
               (behavior_improvement >= self.behavior_threshold):
                df_labeled.at[idx, 'label'] = 1  # 适合疗法
            else:
                df_labeled.at[idx, 'label'] = 0  # 不适合疗法
        
        # 只保留 cart 治疗组
        df_labeled = df_labeled[df_labeled['类别'].isin(['急性+cart', '慢性+cart'])].copy()
        df_labeled = df_labeled.dropna(subset=['label'])
        df_labeled['label'] = df_labeled['label'].astype(int)
        
        # 打印标签详情
        print("\n标签详情：") #怎么打标签的过程也看不懂
        for idx, row in df_labeled.iterrows():
            print(f"  {row['类别']} - 焦虑改善：{row['焦虑改善率']:.2%}, "
                  f"行为改善：{row['行为改善率']:.2%} → 标签：{row['label']}")
        
        return df_labeled
    
    def fit(self, X, y=None):
        """拟合标准化器"""
        #拟合又是干什么的
        self.feature_cols = X.columns.tolist()
        self.scaler.fit(X)
        self.is_fitted = True
        return self
    
    def transform(self, X):
        """转换数据（标准化）"""
        if not self.is_fitted:
            raise ValueError("预处理器未拟合，请先调用 fit()")
        
        # 确保列顺序一致
        X = X[self.feature_cols]
        
        # 标准化
        X_scaled = self.scaler.transform(X)
        
        return pd.DataFrame(X_scaled, columns=self.feature_cols, index=X.index)
    
    def fit_transform(self, X, y=None):
        """拟合并转换"""
        return self.fit(X, y).transform(X)
    
    def inverse_transform(self, X_scaled):
        """逆变换（恢复原始尺度）"""
        X_original = self.scaler.inverse_transform(X_scaled)
        return pd.DataFrame(X_original, columns=self.feature_cols)
