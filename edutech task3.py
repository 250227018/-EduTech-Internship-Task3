import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("C:/Users/hp/OneDrive/Desktop/datasets/Iris.csv")

# 1. Summary Statistics
print(df.head())
print(df.describe())
print(df.info())

# 2. Species count plot
plt.figure(figsize=(6,4))
sns.countplot(x='Species', data=df)
plt.title('Species Count')
plt.savefig('species_count.png')
plt.show()

# 3. Histogram
df.hist(figsize=(10,8))
plt.suptitle('Feature Distribution')
plt.savefig('histogram.png')
plt.show()

# 4. Correlation Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig('heatmap.png')
plt.show()

# 5. Pairplot
sns.pairplot(df, hue='Species')
plt.savefig('pairplot.png')
plt.show()

print("Done! All graphs saved.")