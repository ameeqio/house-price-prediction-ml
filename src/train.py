from __future__ import annotations
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

class ModelTrainEval:
    def __init__(self, df: pd.DataFrame, target_var: str = "SalePrice") -> None:
        self.df: pd.DataFrame = df.copy()

        self.X: pd.DataFrame = self.df.drop(target_var, axis = 1)
        self.y: pd.Series = self.df[target_var]

        self.X_train: pd.DataFrame | None = None
        self.X_test: pd.DataFrame | None = None
        self.y_train: pd.Series | None = None
        self.y_test: pd.Series | None = None


    def split_data(self) -> ModelTrainEval:
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size = 0.2, random_state = 42)
        
        return self
        

    def train_linear_reg(self) -> dict[str, float | str]:
        lin_reg_model = LinearRegression()
        lin_reg_model.fit(self.X_train, self.y_train) # type: ignore

        return self.model_evaluation("Linear-Regression", lin_reg_model)
        

    def train_rf_reg(self) -> dict[str, float | str]:
        rf_model = RandomForestRegressor(n_estimators = 100, random_state = 42)
        rf_model.fit(self.X_train, self.y_train) # type: ignore

        return self.model_evaluation("Random-Forest-Regressor", rf_model)
    
    def train_xgb_reg(self) -> dict[str, float | str]:
        xgb_reg = XGBRegressor(n_estimators = 100, learning_rate = 0.1, max_depth = 3, random_state = 42,
                    objective="reg:squarederror")
        xgb_reg.fit(self.X_train, self.y_train)

        return self.model_evaluation("XGB-Regressor", xgb_reg)


    def model_evaluation(self, model_name : str, model_inst) -> dict[str, float | str]:
        y_pred = model_inst.predict(self.X_test)
        mae = mean_absolute_error(self.y_test, y_pred) # type: ignore
        rmse = mean_squared_error(self.y_test, y_pred) ** 0.5 # type: ignore
        r2_val = r2_score(self.y_test, y_pred) # type: ignore

        return {
            "Model-Name" : model_name,
            "R2-score" : r2_val,
            "MAE" : mae,
            "RMSE" : rmse
        }

    def train_eval_models(self) -> pd.DataFrame:
        self.split_data()

        results = [
            self.train_linear_reg(),
            self.train_rf_reg(),
            self.train_xgb_reg()
        ]

        return pd.DataFrame(results)