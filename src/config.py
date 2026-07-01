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


# data-encoding
ordinal_enc_catg_ftrs: list[str] = ['Exter Qual', 'Exter Cond', 'Bsmt Qual', 'Bsmt Cond', 
    'Heating QC', 'Kitchen Qual', 'Fireplace Qu', 'Garage Qual', 'Garage Cond', 'Pool QC',
    'Bsmt Exposure', 'BsmtFin Type 1', 'BsmtFin Type 2', 'Garage Finish']

one_hot_enc_nomctg_ftrs: list[str] = ['MS SubClass', 'MS Zoning', 'Alley', 'Lot Shape', 'Land Contour', 
    'Utilities', 'Lot Config', 'Land Slope', 'Neighborhood', 'Bldg Type', 'House Style', 'Roof Style', 
    'Roof Matl', 'Exterior 1st', 'Exterior 2nd', 'Mas Vnr Type', 'Foundation', 
    'Heating', 'Electrical', 'Functional', 'Garage Type','Condition 1', 'Condition 2', 
    'Paved Drive', 'Fence', 'Misc Feature', 'Sale Type', 'Sale Condition']

label_enc_nomctg_ftrs: list[str] = ['Street', 'Central Air']

label_encodes = {
    "Street" : {"Pave" : 1, "Grvl" : 0},
    "Central Air" : {"Y" : 1, "N" : 0}
}

ordinal_encodes = {
    "Exter Qual": {
        "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5
    },

    "Exter Cond": {
        "Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5
    },

    "Bsmt Qual": {
        "None": 0, "Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5
    },

    "Bsmt Cond": {
        "None": 0, "Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5
    },

    "Heating QC": {
        "Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5
    },

    "Kitchen Qual": {
        "Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5
    },

    "Fireplace Qu": {
        "None": 0, "Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5
    },

    "Garage Qual": {
        "None": 0, "Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5
    },

    "Garage Cond": {
        "None": 0, "Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5
    },

    "Pool QC": {
        "None": 0, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5
    },

    "Bsmt Exposure": {
        "None": 0,
        "No": 1,
        "Mn": 2,
        "Av": 3,
        "Gd": 4
    },

    "BsmtFin Type 1": {
        "None": 0,
        "Unf": 1,
        "LwQ": 2,
        "Rec": 3,
        "BLQ": 4,
        "ALQ": 5,
        "GLQ": 6
    },

    "BsmtFin Type 2": {
        "None": 0,
        "Unf": 1,
        "LwQ": 2,
        "Rec": 3,
        "BLQ": 4,
        "ALQ": 5,
        "GLQ": 6
    },

    "Garage Finish": {
        "None": 0,
        "Unf": 1,
        "RFn": 2,
        "Fin": 3
    }
}