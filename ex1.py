
activos = pd.ExcelFile("mensual.xlsx")
activos.sheet_names
activos = xl.parse("Hoja1")


print(df)
print(df.head())
print(df.columns)

df.iloc[2, 0]

df.loc[2, 'Brand']

df ['Brand']

def manufact(df):
    marcas = []
    for i in range(len(df)):
        if df.loc[i, 'Brand'] not in marcas:
            marcas.append(df.loc[i, 'Brand'])
        else:
            pass
    return marcas

manufact = manufact(df)

americanos = df[df['Brand'] == 'CHEVROLET']

def generar_df_excel(df, nombre_archivo):
    nombre_final = nombre_archivo + '.xlsx'
    writer = ExcelWriter(nombre_final)
    df.to_excel(writer, 'Manufacturas')
    writer.save()
    print('OK')

generar_df_excel(americanos, 'salfa_americanos')


