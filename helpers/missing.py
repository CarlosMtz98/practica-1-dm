import pandas as pd

def missing_values_table(df):
    total = df.isnull().sum()
    percent = 100 * total/len(df)
    missingValue_table = pd.concat([total, percent], axis = 1)
    ren_table = missingValue_table.rename(columns = {0: 'Total de valores faltantes', 1: 'Porcentaje de valores faltantes'})
    ren_table = ren_table[ren_table.iloc[:,1]!=0].sort_values('Porcentaje de valores faltantes', ascending = False).round(2)
    print('De: {}'.format(df.shape[1]) + ' columnas, {}'.format(ren_table.shape[0]) + ' cuentan con valores faltantes')
    return ren_table