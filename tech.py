# IT-III (Data Analytics)
# Technical Asessement 3 by MR. ARSHIL NOOR
# Learning CLUSTERING OF DATA
import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
df=pd.read_excel("C:\\Users\\पज\\Desktop\\Office\\5. Even Sem (2023-24)\\B.Tech [Third Year CS (6th Sem)]\\Practical (DA)\\Income.xlsx")
Xfeatures=df[['Income']]
model=KMeans(n_clusters=3)
model.fit(Xfeatures)
pred=model.predict(Xfeatures)
df['Clusters']=pred
df[['Income','Clusters']]
sns.countplot(x='Clusters',data=df)
plt.figure(figsize=(20,10))
plt.title('CLUSTERING OF INCOME RANGE: CS/IT 2025 BATCH STUDENTS')
sns.scatterplot(data=df, x='Income', y='Name', hue='Clusters')
plt.show() 