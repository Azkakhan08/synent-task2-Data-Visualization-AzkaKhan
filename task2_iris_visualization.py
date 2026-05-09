# Task 2 - Data Visualization
# Dataset  - Iris Dataset
# Language - Python
# Run      - python task2_iris_visualization.py

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd

# load iris dataset
iris = load_iris()

# define data
data = pd.DataFrame(iris.data, columns=["sepal_length", "sepal_width",
                                         "petal_length", "petal_width"])
data["species"] = [iris.target_names[i] for i in iris.target]

# show data
print("==============================")
print("       IRIS DATASET")
print("==============================")
print(data.head(10))
print()
print("Shape   :", data.shape)
print("Species :", list(data["species"].unique()))
print()

# separate by species
setosa     = data[data["species"] == "setosa"]
versicolor = data[data["species"] == "versicolor"]
virginica  = data[data["species"] == "virginica"]

# average petal length per species
avg_petal = data.groupby("species")["petal_length"].mean()

print("==============================")
print("  AVG PETAL LENGTH BY SPECIES")
print("==============================")
print(avg_petal)
print()

# setup figure and subplots
plt.figure(figsize=(14, 5))

# bar chart - average petal length by species
plt.subplot(1, 3, 1)
plt.bar(avg_petal.index, avg_petal.values,
        color=["lightpink", "skyblue", "lightgreen"],
        edgecolor="black")
plt.xlabel("Species")
plt.ylabel("Avg Petal Length (cm)")
plt.title("Bar Chart\nAvg Petal Length by Species")
plt.xticks(rotation=15)

# histogram - sepal length distribution
plt.subplot(1, 3, 2)
plt.hist(setosa["sepal_length"],     bins=10, color="lightpink",
         edgecolor="black", label="setosa",     alpha=0.7)
plt.hist(versicolor["sepal_length"], bins=10, color="skyblue",
         edgecolor="black", label="versicolor", alpha=0.7)
plt.hist(virginica["sepal_length"],  bins=10, color="lightgreen",
         edgecolor="black", label="virginica",  alpha=0.7)
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.title("Histogram\nSepal Length Distribution")
plt.legend()

# scatter plot - sepal length vs petal length
plt.subplot(1, 3, 3)
plt.scatter(setosa["sepal_length"],     setosa["petal_length"],
            color="lightpink",  edgecolor="black", label="setosa",     s=60)
plt.scatter(versicolor["sepal_length"], versicolor["petal_length"],
            color="skyblue",    edgecolor="black", label="versicolor", s=60)
plt.scatter(virginica["sepal_length"],  virginica["petal_length"],
            color="lightgreen", edgecolor="black", label="virginica",  s=60)
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.title("Scatter Plot\nSepal Length vs Petal Length")
plt.legend()

# display
plt.tight_layout()
plt.savefig("task2_output.png")
plt.show()
print("Saved : task2_output.png")
