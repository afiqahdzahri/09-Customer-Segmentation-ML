import pandas as pd
from sklearn.cluster import KMeans
df = pd.read_csv('customers.csv')
X = df[['Age','AnnualIncome','SpendingScore']]
km = KMeans(n_clusters=3, random_state=42).fit(X)
df['cluster'] = km.labels_
print(df.groupby('cluster').mean())