from __future__ import annotations
import pandas as pd
from src.config import scaling_cols
from sklearn.preprocessing import StandardScaler

class FeatureScaling:
    def __init__(self, df: pd.DataFrame) -> None:
        self.df: pd.DataFrame = df.copy()
        self.scaler: StandardScaler = StandardScaler()

    def scale_features(self) -> FeatureScaling:
        self.df[scaling_cols] = self.scaler.fit_transform(self.df[scaling_cols])
        return self
    
    def transform(self) -> pd.DataFrame:
        return self.scale_features().df
    

