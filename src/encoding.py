from __future__ import annotations
import pandas as pd
from src.config import one_hot_enc_nomctg_ftrs, ordinal_encodes, label_encodes


class FeatureEncoding:
    def __init__(self, df: pd.DataFrame) -> None:
        self.df: pd.DataFrame = df.copy()

    def label_encoding(self) -> FeatureEncoding:
        for ftr, encodes in label_encodes.items():
            self.df[ftr] = self.df[ftr].map(encodes)

        return self
    
    def ordinal_encoding(self) -> FeatureEncoding:
        for ftr, encodes in ordinal_encodes.items():
            self.df[ftr] = self.df[ftr].map(encodes)

        return self
    
    def one_hot_encoding(self) -> FeatureEncoding:
        self.df = pd.get_dummies(data = self.df, columns = one_hot_enc_nomctg_ftrs, drop_first = True, dtype = int)
        return self
    
    def transform(self) -> pd.DataFrame:
        return (
            self.label_encoding()
                .ordinal_encoding()
                .one_hot_encoding()
                .df
        )


