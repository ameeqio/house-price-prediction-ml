# missing value imputations
median_impute_missing: list[str] = ['Lot Frontage']

zero_impute_missing: list[str] = ['Garage Cars', 'Garage Area', 'Mas Vnr Area', 'BsmtFin SF 1', 'BsmtFin SF 2', 
        'Bsmt Unf SF', 'Total Bsmt SF', 'Bsmt Full Bath', 'Bsmt Half Bath']

none_impute_missing: list[str] = ['Alley', 'Mas Vnr Type', 'Bsmt Exposure', 'BsmtFin Type 1', 
        'BsmtFin Type 2', 'Garage Type', 'Garage Finish', 'Fence', 'Misc Feature', 'Bsmt Qual', 'Bsmt Cond', 
        'Fireplace Qu', 'Garage Qual', 'Garage Cond', 'Pool QC']

mode_impute_missing: list[str] = ['Electrical']

# engineering features
age_features: dict[str, list[str]] = {
    "HouseAge" : ["Yr Sold", "Year Built"],
    "GarageAge" : ["Yr Sold", "Garage Yr Blt"],
    "RemodelAge" : ["Yr Sold", "Year Remod/Add"]
}

area_features: dict[str, list[str]] = {
    "TotalHousingSF" : ["Pool Area", "Garage Area", "Gr Liv Area", "Total Bsmt SF"],
    "TotalPorchSF" : ["Wood Deck SF", "Open Porch SF", "Enclosed Porch", "3Ssn Porch", "Screen Porch"]
}

number_features: dict[str, list[str]] = {
    "TotalBathrooms" : ['Bsmt Full Bath', 'Bsmt Half Bath', 'Full Bath', 'Half Bath']
}

drop_features: list[str] = ["Order", "PID"]
# 'gargageAge' and 'garage yr' : 159 missing values