import csv 
import matplotlib.pyplot as plt
import random
"""
with open("2. prace_se_soubory/data/teploty.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    
    roky = []
    teploty = []
    avg_teploty = []
    avg_roky = []
    for radek in reader:
        roky.append(int(radek["YEAR"]))
        teploty.append(float(radek["TEMPERATURE"]))
    
        if radek["TIME"] == "AVG":
            avg_teploty.append(float(radek["TEMPERATURE"]))
            avg_roky.append(int(radek["YEAR"]))
        elif 

minimum = min(teploty)
maximum = max(teploty)
prumer = sum(teploty) / len(teploty)
prumer_avg = sum(avg_teploty) / len(avg_teploty)



print(minimum)
print(maximum)
print(prumer)
print(prumer_avg)

with open("2. prace_se_soubory/data/vypis.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([minimum, maximum, prumer])



plt.plot(avg_roky, avg_teploty)
plt.title("Večerní teplota podle roku")
plt.xlabel("Rok")
plt.ylabel("Teplota [°C]")
plt.show()
"""
with open("2. prace_se_soubory/data/citaty.txt", "r", encoding="utf-8") as file:
    citaty = file.readlines()
    
    emoji1 = ["🌺", "🌼", "🌞", "🐻", "❤️‍", "🔥"]
    emoji2 = ["💥", "🔥", "❤️‍", "😎", "🤣"]


vybrany_citat = random.choice(citaty).strip()
citat, autor = vybrany_citat.split("—")

print("Citát dne:")

pocet_emoji1 = random.randint(3, 5)
for i in range(pocet_emoji1):
    print(random.choice(emoji1))
print()

print(citat.strip())          

print("###", (autor.strip()), "###")

pocet_emoji2 = random.randint(1, 1)
for i in range(pocet_emoji2):
    print(random.choice(emoji2), end="")
print()