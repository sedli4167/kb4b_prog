import csv


from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

X = []
Y = []

cesta = r"Exam_Score_Prediction.csv"
with open(cesta, "r", encoding="utf-8") as file:
    for radek in csv.DictReader(file):


        if radek["gender"] == "Male":
            gender = 1
        elif radek["gender"] == "Female":
            gender = 2
        else:
            gender = 3


        age = int(radek["age"]) 
        study_hours = float(radek["study_hours"])
        class_attendance = float(radek["class_attendance"])
        sleep = float(radek["sleep_hours"])
        exam_score = float(radek["exam_score"])
        if exam_score >= 90:
            exam_score = 1
        elif exam_score < 90 and exam_score >= 80:
            exam_score = 2
        elif exam_score < 80 and exam_score >= 65:
            exam_score = 3
        elif exam_score < 65 and exam_score >=50:
            exam_score = 4
        else:
            exam_score = 5

        X.append([gender, age, study_hours, class_attendance, sleep])
        Y.append([exam_score])



rows = len(X)
split = round(0.8 * rows)

trening_X, test_X, trening_Y, test_Y =  train_test_split(
        X, Y,
        test_size=0.2, 
        random_state=42
)

neuronka = MLPClassifier(
    hidden_layer_sizes=(8,6),
    activation="relu",
    max_iter=5_000
)

neuronka.fit(trening_X, trening_Y)

predikce = neuronka.predict(test_X)
pocet = len(predikce)


results = neuronka.predict(test_X)

correct = 0
for i in range(len(results)):
    if test_Y[i] == results[i]:
        correct += 1
print("Přesnost:", correct / len(results))


ConfusionMatrixDisplay.from_predictions(
    test_Y, results)
plt.show()
 