#Zadanie 3
print("----- Zadanie 3 -----")

import joblib
import numpy as np

loadedModel = joblib.load('model.joblib')

names = ['setosa', 'versicolor', 'virginica']

sampleData = np.array([[5.1, 3.5, 1.4, 0.2]])
prediction = loadedModel.predict(sampleData)

index = prediction[0]

print(f"Predykcja (dla rekordu {sampleData}): \nIndeks: {index} \nNazwa gatunku: {names[index]}")
