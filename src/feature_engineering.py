from __future__ import annotations
import pandas as pd
from src.config import age_features, area_features, number_features, drop_features

class FeatureEngineer:
    def __init__(self, df: pd.DataFrame) -> None:
        self.df: pd.DataFrame = df.copy()

    def drop_ftrs(self) -> FeatureEngineer:
        self.df.drop(columns=drop_features, inplace=True)
        return self

    def fix_garage_yr(self) -> FeatureEngineer:
        self.df.loc[self.df["Garage Yr Blt"] > self.df["Yr Sold"], "Garage Yr Blt"] = pd.NA
        return self

    def eng_area_ftrs(self) -> FeatureEngineer: 
        for new_ftr, ftrs in area_features.items():
            self.df[new_ftr] = self.df[ftrs].sum(axis = 1)

        return self 
        
    def eng_number_ftrs(self) -> FeatureEngineer:
        for new_ftr, ftrs in number_features.items():
            self.df[new_ftr] = self.df[ftrs].sum(axis = 1)

        return self
    
    def eng_age_ftrs(self) -> FeatureEngineer:
        for new_ftr, (ftr1, ftr2) in age_features.items():
            self.df[new_ftr] = self.df[ftr1] - self.df[ftr2]

        self.df['GarageAge'] = self.df['GarageAge'].fillna(-1)
        self.df.drop("Garage Yr Blt", axis = 1, inplace = True)
        return self
    
    def transform(self) -> pd.DataFrame:
        return (
            self.drop_ftrs()
                .fix_garage_yr()
                .eng_area_ftrs()
                .eng_number_ftrs()
                .eng_age_ftrs()
                .df
        )
    

