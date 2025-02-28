def visualizzazione_grafico(X, y_kmeans):
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)

    plt.figure(figsize=(10, 5))
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y_kmeans, cmap='viridis', alpha=0.6, label="Clusters K-Means")
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red', marker='X', label="Centroidi")
    plt.xlabel("Prima componente principale")
    plt.ylabel("Seconda componente principale")
    plt.title("Visualizzazione Clustering con K-Means (PCA)")
    plt.legend()
    plt.show()