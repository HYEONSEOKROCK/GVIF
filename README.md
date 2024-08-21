
# 1. Data example

```
data = pd.DataFrame({
    'Size': [1500, 1800, 2400, 3000, 3500],
    'Bedrooms': [3, 4, 3, 5, 4],
    'Age': [10, 15, 20, 5, 0],
    'Type': ['House', 'Apartment', 'House', 'House', 'Apartment']
})
```
# 2. How to use
```
cat_columns = ['Type']
vif_result = calculate_vif(data, cat_columns)
print(vif_result)
```
