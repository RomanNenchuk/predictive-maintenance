import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

# Виносимо схему даних як константи
CATEGORICAL_FEATURES = ['Type']
NUMERIC_FEATURES = [
    'Air temperature [K]',
    'Process temperature [K]',
    'Rotational speed [rpm]',
    'Torque [Nm]',
    'Tool wear [min]',
    'Temp_Diff',
    'Power',
    'Torque_Wear',
]


class FeatureEngineer(BaseEstimator, TransformerMixin):
    """
    Кастомний трансформер для розрахунку фізичних показників верстата.
    Наслідуємо BaseEstimator та TransformerMixin, щоб Pipeline міг 
    коректно працювати з методами fit() та transform().
    """
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        # Різниця температур
        X['Temp_Diff'] = X['Process temperature [K]'] - X['Air temperature [K]']
        
        # Потужність (Power = Torque * Angular Velocity)
        # Angular Velocity = RPM * 2 * PI / 60
        X['Power'] = X['Torque [Nm]'] * (X['Rotational speed [rpm]'] * 2 * np.pi / 60)
        
        # Взаємодія моменту та зносу
        X['Torque_Wear'] = X['Torque [Nm]'] * X['Tool wear [min]']
        
        return X