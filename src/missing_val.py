from __future__ import annotations
import pandas as pd
from src.config import median_impute_missing, mode_impute_missing, none_impute_missing, zero_impute_missing

class MissingValueHandler:
    def __init__(self, df: pd.DataFrame) -> None:
        self.df: pd.DataFrame = df.copy()

    def median_imputation(self) -> MissingValueHandler:  
        for col in median_impute_missing:
            self.df[col] = self.df[col].fillna(self.df[col].median())

        return self
    
    def mode_imputation(self) -> MissingValueHandler:
        for col in mode_impute_missing:
            self.df[col] = self.df[col].fillna(self.df[col].mode()[0])

        return self
    
    def none_imputation(self) -> MissingValueHandler: 
        for col in none_impute_missing:
            self.df[col] = self.df[col].fillna('None')

        return self
    
    def zero_imputation(self) -> MissingValueHandler:
        for col in zero_impute_missing:
            self.df[col] = self.df[col].fillna(0)
        
        return self
    
    def transform(self) -> pd.DataFrame: 
        return (
            self.median_imputation()
                .mode_imputation()
                .none_imputation()
                .zero_imputation()
                .df
        )


