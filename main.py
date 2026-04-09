#Zadanie 1
print("\n----- Zadanie 1 -----\n")

import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()

dfIris = pd.DataFrame(data=iris.data, columns=iris.feature_names)
dfIris['target'] = iris.target

print(f"Kilka pierwszych wierszy: \n{dfIris.head()}"
      f"\n\nRozmiar danych: {dfIris.shape}"
      f"\n\nTypy kolumn: \n{dfIris.dtypes}")


#Zadanie 2
print("\n\n\n----- Zadanie 2 -----\n")

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

#podzielenie parametrów na cechy
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(f"Dokładność trenowania: {accuracy_score(y_test, y_pred)}"
      f"\nPodstawowe metryki: \n{classification_report(y_test, y_pred)}")


#Zadanie 3
print("\n----- Zadanie 3 -----")

import joblib
joblib.dump(model, 'model.joblib')

print("Model został zapisany do pliku model.joblib")