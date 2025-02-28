def menu():
    while True:
        print("\nMenu:")
        print("1. Generazione dati")
        print("2. Analisi descrittiva")
        print("3. Visualizzazione grafico")
        print("4. Classification Report")
        print("5. Esci")
        scelta = input("Seleziona un'opzione: ")
        
        if scelta == '1':
            global X, y, iris
            X, y, iris = generazione_dati()
            print("Dati generati con successo!")
        elif scelta == '2':
            analisi_descrittiva(X, y, iris)
        elif scelta == '3':
            kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
            y_kmeans = kmeans.fit_predict(X)
            visualizzazione_grafico(X, y_kmeans)
        elif scelta == '4':
            kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
            y_kmeans = kmeans.fit_predict(X)
            classificazione_report(y, y_kmeans)
        elif scelta == '5':
            print("Uscita...")
            break
        else:
            print("Scelta non valida, riprova.")


menu()
