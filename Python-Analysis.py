import pandas as pd
from scipy.stats import ttest_ind

file_path = 'C:/Users/user/Documents/Datasets/Business Retail Sales .xlsx'
df = pd.read_excel(file_path)

print(df.head())

art_sculpture = df[df['Product Type'] == 'Art & Sculpture']
basket = df[df['Product Type'] == 'Basket']
christmas = df[df['Product Type'] == 'Christmas']
home_decor = df[df['Product Type'] == 'Home Decor']
skin_care = df[df['Product Type'] == 'Skin Care']
kitchen = df[df['Product Type'] == 'Kitchen']

# Compare net quantity
t_statistic_net_quantity, p_value_net_quantity = ttest_ind(art_sculpture['Net Quantity'], basket['Net Quantity'])
t_statistic_net_quantity_2, p_value_net_quantity_2 = ttest_ind(christmas['Net Quantity'], home_decor['Net Quantity'])
t_statistic_net_quantity_3, p_value_net_quantity_3 = ttest_ind(skin_care['Net Quantity'], kitchen['Net Quantity'])

if p_value_net_quantity < 0.05:
    difference_net_quantity = art_sculpture['Net Quantity'].mean() - basket['Net Quantity'].mean()
    print(f'There is a significant difference between the means of the two groups for net quantity. The difference is {difference_net_quantity:.2f}.')
else:
    print('There is no significant difference between the means of the two groups for net quantity.')

if p_value_net_quantity_2 < 0.05:
    difference_net_quantity_2 = christmas['Net Quantity'].mean() - home_decor['Net Quantity'].mean()
    print(f'There is a significant difference between the means of the two groups for Christmas and Home Decor. The difference is {difference_net_quantity_2:.2f}.')
else:
    print('There is no significant difference between the means of the two groups for Christmas and Home Decor.')

if p_value_net_quantity_3 < 0.05:
    difference_net_quantity_3 = skin_care['Net Quantity'].mean() - kitchen['Net Quantity'].mean()
    print(f'There is a significant difference between the means of the two groups for Skin Care and Kitchen. The difference is {difference_net_quantity_3:.2f}.')
else:
    print('There is no significant difference between the means of the two groups for Skin Care and Kitchen.')

# Compare profits
t_statistic_profits, p_value_profits = ttest_ind(art_sculpture['Profits'], basket['Profits'])
t_statistic_profits_2, p_value_profits_2 = ttest_ind(christmas['Profits'], home_decor['Profits'])
t_statistic_profits_3, p_value_profits_3 = ttest_ind(skin_care['Profits'], kitchen['Profits'])

if p_value_profits < 0.05:
    difference_profits = art_sculpture['Profits'].mean() - basket['Profits'].mean()
    print(f'There is a significant difference between the means of the two groups for profits. The difference is {difference_profits:.2f}.')
else:
    print('There is no significant difference between the means of the two groups for profits.')

if p_value_profits_2 < 0.05:
    difference_profits_2 = christmas['Profits'].mean() - home_decor['Profits'].mean()
    print(f'There is a significant difference between the means of the two groups for Christmas and Home Decor. The difference is {difference_profits_2:.2f}.')
else:
    print('There is no significant difference between the means of the two groups for Christmas and Home Decor.')

if p_value_profits_3 < 0.05:
    difference_profits_3 = skin_care['Profits'].mean() - kitchen['Profits'].mean()
    print(f'There is a significant difference between the means of the two groups for Skin Care and Kitchen. The difference is {difference_profits_3:.2f}.')
else:
    print('There is no significant difference between the means of the two groups for Skin Care and Kitchen.')

# Compare returns 
t_statistic_returns, p_value_returns = ttest_ind(art_sculpture['Returns'], basket['Returns'])
t_statistic_returns_2, p_value_returns_2 = ttest_ind(christmas['Returns'], home_decor['Returns'])
t_statistic_returns_3, p_value_returns_3 = ttest_ind(skin_care['Returns'], kitchen['Returns'])

if p_value_returns < 0.05:
    difference_returns = art_sculpture['Returns'].mean() - basket['Returns'].mean()
    print(f'There is a significant difference between the means of the two groups for returns. The difference is {difference_returns:.2f}.')
else:
    print('There is no significant difference between the means of the two groups for returns.')

if p_value_returns_2 < 0.05:
    difference_returns_2 = christmas['Returns'].mean() - home_decor['Returns'].mean()
    print(f'There is a significant difference between the means of the two groups for Christmas and Home Decor. The difference is {difference_returns_2:.2f}.')
else:
    print('There is no significant difference between the means of the two groups for Christmas and Home Decor.')

if p_value_returns_3 < 0.05:
    difference_returns_3 = skin_care['Returns'].mean() - kitchen['Returns'].mean()
    print(f'There is a significant difference between the means of the two groups for Skin Care and Kitchen. The difference is {difference_returns_3:.2f}.')
else:
    print('There is no significant difference between the means of the two groups for Skin Care and Kitchen.')