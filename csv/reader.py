import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

file_path = '' #enter file path to csv here
df = pd.read_csv(file_path)

pd.set_option('display.max_columns', None)
print("Dataset loaded successfully. Shape:", df.shape)

os.makedirs('/home/danieljakob/INF103/csv/plots', exist_ok=True)

categorical_cols = df.select_dtypes(include=['object', 'category', 'str', 'string']).columns

for col in categorical_cols:
    plt.figure(figsize=(12, 6))
    
    top_categories = df[col].value_counts().index[:10]
    filtered_data = df[df[col].isin(top_categories)]
    
    sns.countplot(data=filtered_data, y=col, order=top_categories)
    plt.title(f'Top Categories in {col}')
    plt.subplots_adjust(left=0.3)
    
    safe_col_name = col.replace(" ", "_").replace("/", "_")
    output_path = f'/plots/{safe_col_name}.png'
    
    plt.savefig(output_path)
    plt.close()
    
    print(f"Saved plot for '{col}' to: {output_path}")