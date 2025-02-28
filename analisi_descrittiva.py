def analisi_descrittiva(X, y, iris):
    df = pd.DataFrame(X, columns=iris.feature_names)
    df['Specie'] = y
    print("\nAnalisi Descrittiva:")
    print(df.describe())