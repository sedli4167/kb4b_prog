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
            gender = 0
        elif radek["gender"] == "Female":
            gender = 1
        else:
            gender = 2


        age = int(radek["age"]) 
        study_hours = float(radek["study_hours"])
        study_method = radek["study_method"]
        class_attendance = float(radek["class_attendance"])
        sleep = float(radek["sleep_hours"])
        sleep_quality = radek["sleep_quality"]
        exam_score = float(radek["exam_score"])
        internet_access = radek["internet_access"]
        facility_rating = radek["facility_rating"]
        exam_difficulty = radek["exam_difficulty"]
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

        if sleep_quality == "poor":
            sleep_quality = 1
        elif sleep_quality == "average":
            sleep_quality = 2
        else: 
            sleep_quality = 3
        
        if study_method == "self-study":
            study_method = 1
        elif study_method == "online_videos":
            study_method = 2
        elif study_method == "coaching":
            study_method = 3
        else:  
            study_method = 4

        if internet_access == "yes":
            internet_access = 1
        else:
            internet_access = 0

        if facility_rating == "low":
            facility_rating = 1
        elif facility_rating == "medium":
            facility_rating = 2
        else:
            facility_rating = 3

        if exam_difficulty == "hard":
            exam_difficulty = 3
        elif exam_difficulty == "moderate":
            exam_difficulty = 2
        else: 
            exam_difficulty = 1
        

        X.append([gender, age, study_hours, class_attendance, sleep, sleep_quality, study_method, internet_access, facility_rating, exam_difficulty])
        Y.append(exam_score)



rows = len(X)
split = round(0.8 * rows)

trening_X, test_X, trening_Y, test_Y =  train_test_split(
        X, Y,
        test_size=0.2, 
        random_state=42
)

neuronka = MLPClassifier(
    hidden_layer_sizes=(20,20,10),
    activation="relu",
    max_iter=2000,
    verbose=True,
    random_state=4,
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
 