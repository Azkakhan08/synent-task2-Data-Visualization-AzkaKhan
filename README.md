# Task 2 - Data Visualization

## Problem Statement
Data alone is hard to understand. Visualization helps us see patterns clearly. In this task we load the Iris dataset and create three types of charts to compare features across three flower species.

---

## Dataset Details

 Field        | Details                              
--------------|--------------------------------------
 Dataset Name | Iris Dataset                         
 Total Rows   | 150 flowers                          
 Total Columns | 5 columns                            
 Source       | Built into scikit-learn library      
 Column Name  | Description                
--------------|----------------------------
sepal_length | Length of sepal in cm      
 sepal_width  | Width of sepal in cm       
 petal_length | Length of petal in cm      
 petal_width  | Width of petal in cm       
 species      | setosa versicolor virginica

---

## Approach

Step 1 - Load Iris dataset from sklearn.datasets

Step 2 - Create DataFrame and add species column

Step 3 - Separate data by species setosa versicolor virginica

Step 4 - Calculate average petal length per species

Step 5 - Create Bar Chart showing average petal length by species

Step 6 - Create Histogram showing sepal length distribution for all species

Step 7 - Create Scatter Plot showing sepal length vs petal length

---

## Results

 Chart        |               Finding                       
--------------------------------------------------------------------
 Bar Chart    | Virginica has longest petals  Setosa has shortest    |
 Histogram    | Setosa sepal length is clearly smaller              
 Scatter Plot | Setosa is completely separated from other two species

 Metric       |             Value                        
--------------|------------------------------
 Total flowers  | 150                          
 Species      | setosa  versicolor  virginica
Chart saved  | task2_output.png             

