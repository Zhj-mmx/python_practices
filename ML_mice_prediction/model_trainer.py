"""
===============================================================================
模型训练模块
===============================================================================
功能：
1. 训练多个候选模型
2. 留一法交叉验证 (LOOCV)
3. 模型选择
===============================================================================
"""

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import LeaveOneOut, cross_val_predict
from sklearn.preprocessing import StandardScaler


class ModelTrainer:
    """模型训练器"""
    
    def __init__(self):
        self.models = {
            # 逻辑回归 - 基线模型，推荐作为主模型
            'LogisticRegression': LogisticRegression(
                C=1.0, 
                penalty='l2', 
                solver='lbfgs',
                max_iter=1000,
                random_state=42
            ),
            
            # SVM - 小样本表现好
            'SVM_linear': SVC(
                kernel='linear',
                C=1.0,
                probability=True,
                random_state=42
            ),
            
            # 随机森林 - 限制复杂度防止过拟合
            'RandomForest': RandomForestClassifier(
                n_estimators=5,      # 很少的树，防止过拟合
                max_depth=2,         # 限制深度
                min_samples_leaf=2,  # 每叶至少 2 样本
                random_state=42
            )
        }
        self.loo = LeaveOneOut()
    
    def train_all_models(self, X, y):
        """
        训练所有候选模型
        
        参数：
            X: 特征矩阵 (已标准化)
            y: 标签向量
        
        返回：
            trained_models: 训练好的模型字典
        """
        trained_models = {}
        
        for name, model in self.models.items():
            print(f"\n  训练 {name}...")
            
            # 留一法交叉验证
            cv_predictions = cross_val_predict(model, X, y, cv=self.loo, method='predict')
            cv_proba = cross_val_predict(model, X, y, cv=self.loo, method='predict_proba')[:, 1]
            
            # LOOCV 准确率
            cv_accuracy = (cv_predictions == y).mean()
            
            print(f"    LOOCV 准确率：{cv_accuracy:.3f}")
            
            # 用全部数据训练最终模型
            model.fit(X, y)
            trained_models[name] = {
                'model': model,
                'cv_accuracy': cv_accuracy,
                'cv_predictions': cv_predictions,
                'cv_proba': cv_proba
            }
        
        return trained_models
    
    def select_best_model(self, trained_models):
        """
        选择最佳模型
        
        选择标准：
        1. LOOCV 准确率最高
        2. 如果有多个相同，优先选择逻辑回归（可解释性强）
        
        参数：
            trained_models: 训练好的模型字典
        
        返回：
            best_name: 最佳模型名称
            best_model: 最佳模型对象
        """
        # 按准确率排序
        sorted_models = sorted(
            trained_models.items(),
            key=lambda x: x[1]['cv_accuracy'],
            reverse=True
        )
        
        best_name = sorted_models[0][0]
        best_model = trained_models[best_name]['model']
        
        # 打印所有模型性能比较
        print("\n  模型性能比较：")
        for name, info in sorted_models:
            print(f"    {name}: {info['cv_accuracy']:.3f}")
        
        return best_name, best_model
    
    def get_feature_importance(self, model, feature_names):
        """
        获取特征重要性
        
        参数：
            model: 训练好的模型
            feature_names: 特征名称列表
        
        返回：
            importance_df: 特征重要性 DataFrame
        """
        import pandas as pd
        
        if hasattr(model, 'coef_'):
            # 逻辑回归、SVM 线性核
            coef = model.coef_[0]
            importance = np.abs(coef)
        elif hasattr(model, 'feature_importances_'):
            # 随机森林
            importance = model.feature_importances_
        else:
            return None
        
        importance_df = pd.DataFrame({
            '特征': feature_names,
            '重要性': importance
        }).sort_values('重要性', ascending=False)
        
        return importance_df
