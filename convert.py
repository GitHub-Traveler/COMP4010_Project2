import pandas as pd
import os
def getExcel(filepath):
    df = pd.read_excel(filepath)
    newname = os.path.splitext(filepath)[0] + '.csv'
    df.to_csv(newname, index=False, header=True)
    return df

filepath = 'surfaces_temp.xlsx'
getExcel(filepath=filepath)