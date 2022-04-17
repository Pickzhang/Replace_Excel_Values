import pandas as pd

data_old = ['桌子-售后维修', '凳子-售后维修', '椅子-售后维修']
data_new = ['桌子', '凳子', '椅子']
data = pd.read_excel('替换测试.xlsx', sheet_name=None)
with pd.ExcelWriter('new.xlsx') as workbook:
    for i, j in data.items():
        m = 0
        while m < len(data_old):
            j.replace(data_old[m], data_new[m], inplace=True)
            m += 1
        j.to_excel(workbook, sheet_name=i, index=False)
