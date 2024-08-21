
def calculate_gvif(data, formula):
    import pandas as pd
    from statsmodels.stats.outliers_influence import variance_inflation_factor
    from patsy import dmatrices
    """
    Calculate GVIF for the given dataset and formula.
    
    :param data: pandas DataFrame containing the dataset
    :param formula: a string representing the regression formula as used in R
    :return: DataFrame with the GVIF values
    """
    # Prepare the design matrices using the formula
    y, X = dmatrices(formula, data, return_type='dataframe')
    
    # Add an intercept manually if not included
    if 'Intercept' not in X.columns:
        X = sm.add_constant(X)
    
    # Calculate VIF for each variable
    vif_data = pd.DataFrame()
    vif_data["variable"] = X.columns
    vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    
    # Adjusting VIF for categorical variables (GVIF)
    vif_data['GVIF'] = vif_data['VIF']**(1/(2*X['variable'].apply(lambda x: len(data[x].unique())-1 if x in data.columns else 1)))
    
    return vif_data
