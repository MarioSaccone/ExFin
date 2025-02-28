def classificazione_report(y, y_kmeans):
    print("\nClassification Report:")
    print(classification_report(y, y_kmeans))