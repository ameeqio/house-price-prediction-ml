
median_impute_missing: list[str] = ['Lot Frontage']

zero_impute_missing: list[str] = ['Garage Cars', 'Garage Area', 'Mas Vnr Area', 'BsmtFin SF 1', 'BsmtFin SF 2', 
        'Bsmt Unf SF', 'Total Bsmt SF', 'Bsmt Full Bath', 'Bsmt Half Bath']

none_impute_missing: list[str] = ['Alley', 'Mas Vnr Type', 'Bsmt Exposure', 'BsmtFin Type 1', 
        'BsmtFin Type 2', 'Garage Type', 'Garage Finish', 'Fence', 'Misc Feature', 'Bsmt Qual', 'Bsmt Cond', 
        'Fireplace Qu', 'Garage Qual', 'Garage Cond', 'Pool QC']

mode_impute_missing: list[str] = ['Electrical']

# later_handle = ['Garage Yr Blt']