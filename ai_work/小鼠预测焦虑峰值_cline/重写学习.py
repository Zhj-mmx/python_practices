import pandas as pandas
import numpy as np
from sklearn.svm import SVR
from sklearn.model_selection import LeaveOneOut
from sklearn.metrics import mean_squard_error, mean_absolute_error
from sklearn.preprocessing import StandardScaler
from sklearn.inspection import permytation_importance
from matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    df = pd.read_csv('data/mice/中心区移动距离-反向分析.csv')

    X = df[['中心区移动距离', '中心区进入数', '中心区时间']]
    y = df['综合焦虑Z评分']
    return df, X, y

def boostrap_ci(data, stastic, n_boostrap=2000, alpha=0.95)
    n = len(data)
    boot_stats = []

    for _ in range(n_bootstrap):
        sample = np.random.choice(data, size=n, replace=True)

        boot_stas.append(statistic(sample))

    boot_stas.append(statistic(sample))
    lower = np.percentile(boot_stats, (1 - alpha) / 2 * 100) 
    upper = np.percentile(boot_stats, (1 + alpha) / 2 * 100)

def evaluate_model():
    df, X, y = load_data()
    n_samples = len(y)

    model = SVR(kernel='rbf', C=1.0, epsilon=0.1)
    loo = LeaveOneOut()

    mae_scores = []
    mse_scores = []
    y_true_all = []
    y_pred_all = []


    for train_idx, test_idx in loo.split(X):
        X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
        y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

        scaler = StandardScaler()

        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        model.fit(X_train_scaled, y_train)

        y_pred = model.predict(X_test_scaled)[0]

        true_val = y_test.values[0]

        mae_scores.append(mean_absolute_error([true_val], [y_pred]))
        mse_scores.append(mean_squared_error([true_val], [y_pred]))

        y_true_all.append(true_val)
        y_pred_all.append(y_pred)

        mae_array = np.array(mae_scores)
        avg_mae = np.mean(mae_array)
        
        std_mae = np.std(mae_array, ddof=1)

        avg_rmse = np.sqrt(np.mean(mse_scores))

        y_true_all = np.array(y_true_all)
        y_pred_all = np.array(y_pred_all)   

        threshold = 0.5

        correct_loose = np.abs(y_true_all - y_pred_all) < threshold

        loose_acc = np.mean(correct_loose)

        y_binned = pd.cut(y, bins=3, labels=False)
        


