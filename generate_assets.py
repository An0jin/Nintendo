import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib

# Load data
df = pd.read_csv('NintendoGames.csv')

# Clean data
df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')
df_clean = df.dropna(subset=['platform', 'user_score'])

# Platform analysis
platform_analysis = df_clean.groupby('platform')['user_score'].agg(['mean', 'count', 'std']).sort_values(by='mean', ascending=False)

# 1. Bar Chart: Average User Score by Platform
plt.figure(figsize=(12, 6))
sns.barplot(x=platform_analysis.index, y=platform_analysis['mean'], palette='viridis', hue=platform_analysis.index, legend=False)
plt.title('Average User Score by Platform')
plt.ylabel('Average User Score')
plt.xlabel('Platform')
plt.xticks(rotation=45)
plt.axhline(platform_analysis['mean'].mean(), color='red', linestyle='--', label='Overall Average')
plt.legend()
plt.tight_layout()
plt.savefig('bar_chart.png')
print("Generated bar_chart.png")

# 2. Box Plot: User Score Distribution by Platform
plt.figure(figsize=(12, 6))
sns.boxplot(x='platform', y='user_score', data=df_clean, palette='viridis', hue='platform', legend=False)
plt.title('User Score Distribution by Platform')
plt.ylabel('User Score')
plt.xlabel('Platform')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('box_plot.png')
print("Generated box_plot.png")
