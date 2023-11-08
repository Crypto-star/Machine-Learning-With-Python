#Training The Model
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

churn_df = pd.read_csv("churn_df.csv")

y = churn_df["churn"].values
X = churn_df[["account_length", "customer_service_calls"]].values


knn = KNeighborsClassifier(n_neighbors=6)


knn.fit(X, y)

#Predicting The Model
X_new = ([[30.0, 17.5],
          [107.0, 24.1],
          [213.0, 10.9]])
y_pred = knn.predict(X_new)

print("Predictions: {}".format(y_pred)) 