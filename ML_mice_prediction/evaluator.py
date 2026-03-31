"""
===============================================================================
模型评估模块
===============================================================================
功能：
1. 留一法交叉验证评估
2. 计算各项指标（准确率、AUC、灵敏度、特异度）
3. 置信区间估计（Bootstrap）
===============================================================================
"""

import numpy as np
from sklearn.model_selection import LeaveOneOut, cross_val_predict
from sklearn.metrics import (
    accuracy_score, roc_auc_score, confusion_matrix, recall_score
)
from sklearn.utils import resample


class ModelEvaluator:
    """模型评估器"""
    
    def __init__(self, n_bootstrap=1000, random_state=42):
        """
        参数：
            n_bootstrap: Bootstrap 重抽样次数
            random_state: 随机种子
        """
        self.loo = LeaveOneOut()
        self.n_bootstrap = n_bootstrap
        self.random_state = random_state
    
    def evaluate(self, model, X, y):
        """
        全面评估模型性能
        
        参数：
            model: 训练好的模型
            X: 特征矩阵
            y: 标签向量
        
        返回：
            metrics: 指标字典
        """
        # 留一法预测
        cv_predictions = cross_val_predict(model, X, y, cv=self.loo, method='predict')
        cv_proba = cross_val_predict(model, X, y, cv=self.loo, method='predict_proba')[:, 1]
        
        # 基本指标
        accuracy = accuracy_score(y, cv_predictions)
        
        # AUC（小样本下可能不稳定）
        try:
            auc = roc_auc_score(y, cv_proba)
        except ValueError:
            auc = np.nan  # 单类别时无法计算 AUC
        
        # 混淆矩阵
        tn, fp, fn, tp = confusion_matrix(y, cv_predictions).ravel()
        
        # 灵敏度（= recall）、特异度
        sensitivity = recall_score(y, cv_predictions)
        specificity = tn / (tn + fp) if (tn + fp) > 0 else 0
        
        # F1 分数
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        f1 = 2 * precision * sensitivity / (precision + sensitivity) if (precision + sensitivity) > 0 else 0
        
        # Bootstrap 置信区间
        auc_ci = self._bootstrap_auc(model, X, y)
        
        metrics = {
            'accuracy': accuracy,
            'auc': auc,
            'auc_ci': auc_ci,
            'sensitivity': sensitivity,
            'specificity': specificity,
            'precision': precision,
            'f1_score': f1,
            'confusion_matrix': {
                'TP': int(tp),
                'FP': int(fp),
                'TN': int(tn),
                'FN': int(fn)
            }
        }
        
        return metrics
    
    def _bootstrap_auc(self, model, X, y):
        """
        Bootstrap 法估计 AUC 置信区间
        
        返回：
            (ci_lower, ci_upper): 95% 置信区间
        """
        np.random.seed(self.random_state)
        auc_scores = []
        
        for _ in range(self.n_bootstrap):
            # 有放回抽样
            indices = resample(np.arange(len(y)), n_samples=len(y), replace=True)
            X_boot = X.iloc[indices]
            y_boot = y.iloc[indices]
            
            # 去重（有些样本可能被重复抽取）
            unique_indices = np.unique(indices)
            if len(np.unique(y_boot)) < 2:
                continue  # 单类别跳过
            
            # 训练并预测
            try:
                model.fit(X_boot, y_boot)
                proba = model.predict_proba(X_boot)[:, 1]
                auc = roc_auc_score(y_boot, proba)
                auc_scores.append(auc)
            except:
                continue
        
        if len(auc_scores) < 10:
            return (np.nan, np.nan)
        
        # 95% 置信区间
        ci_lower = np.percentile(auc_scores, 2.5)
        ci_upper = np.percentile(auc_scores, 97.5)
        
        return (ci_lower, ci_upper)
    
    def print_report(self, metrics):
        """打印评估报告"""
        print("\n" + "=" * 50)
        print("模型评估报告")
        print("=" * 50)
        
        print(f"\n【判别能力】")
        print(f"  准确率：  {metrics['accuracy']:.3f}")
        print(f"  AUC:      {metrics['auc']:.3f} (95% CI: {metrics['auc_ci'][0]:.3f} - {metrics['auc_ci'][1]:.3f})")
        
        print(f"\n【分类性能】")
        print(f"  灵敏度：  {metrics['sensitivity']:.3f} (真阳性率)")
        print(f"  特异度：  {metrics['specificity']:.3f} (真阴性率)")
        print(f"  精确率：  {metrics['precision']:.3f}")
        print(f"  F1 分数：  {metrics['f1_score']:.3f}")
        
        print(f"\n【混淆矩阵】")
        cm = metrics['confusion_matrix']
        print(f"           预测阳性  预测阴性")
        print(f"  实际阳性    {cm['TP']}        {cm['FN']}")
        print(f"  实际阴性    {cm['FP']}        {cm['TN']}")
        
        print("\n" + "=" * 50)
