import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
from collections import Counter
import os

plt.style.use('default')
output_dir = 'plots'
os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv('../data/final/jobs.csv')

print("Dataset shape:", df.shape)
print("\nSample data:")
print(df.head())

# Clean and prepare
df = df.dropna(subset=['job_title', 'location'])
df['job_title'] = df['job_title'].str.strip()
df['location'] = df['location'].str.strip()

print(f"\nTotal jobs analyzed: {len(df)}")

# 1. Top Job Titles
print("\n=== TOP 10 JOB TITLES ===")
top_titles = df['job_title'].value_counts().head(10)
print(top_titles)

plt.figure(figsize=(12, 6))
top_titles.plot(kind='bar')
plt.title('Top 10 Job Titles')
plt.xlabel('Job Title')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(f'{output_dir}/top_titles.png', dpi=300, bbox_inches='tight')
plt.show()

# 2. Top Locations
print("\n=== TOP 10 LOCATIONS ===")
top_locs = df['location'].value_counts().head(10)
print(top_locs)

plt.figure(figsize=(12, 6))
top_locs.plot(kind='bar')
plt.title('Top 10 Job Locations')
plt.xlabel('Location')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(f'{output_dir}/top_locations.png', dpi=300, bbox_inches='tight')
plt.show()

# 3. Top Companies (if multi)
print("\n=== TOP COMPANIES ===")
top_comp = df['company'].value_counts().head(10)
print(top_comp)

# 4. Entry-level jobs
entry_keywords = ['Junior', 'Entry', 'Intern', 'Associate', 'Fresher']
entry_df = df[df['job_title'].str.contains('|'.join(entry_keywords), case=False, na=False)]
print(f"\nEntry-level jobs ({len(entry_df)}): {len(entry_df)/len(df)*100:.1f}%")
print(entry_df['job_title'].value_counts().head(5))

# 5. Skills analysis
if 'required_skills' in df.columns and df['required_skills'].notna().sum() > 0:
    print("\n=== TOP SKILLS ===")
    all_skills = []
    for skills in df['required_skills'].dropna():
        skill_list = re.split(r'[;,|]', skills)
        all_skills.extend([s.strip().lower() for s in skill_list if s.strip()])
    
    skill_counter = Counter(all_skills)
    top_skills = skill_counter.most_common(15)
    print(top_skills)
    
    skills_df = pd.DataFrame(top_skills, columns=['skill', 'count'])
    plt.figure(figsize=(12, 8))
    sns.barplot(data=skills_df, x='count', y='skill')
    plt.title('Top 15 Required Skills')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/top_skills.png', dpi=300, bbox_inches='tight')
    plt.show()
else:
    print("\nNo skills data available for analysis")

# 6. Department distribution
print("\n=== DEPARTMENT DISTRIBUTION ===")
dept_dist = df['department'].value_counts()
print(dept_dist)
dept_dist.plot(kind='pie', autopct='%1.1f%%')
plt.title('Jobs by Department')
plt.ylabel('')
plt.savefig(f'{output_dir}/dept_pie.png', dpi=300, bbox_inches='tight')
plt.show()

print(f"\nPlots saved to {output_dir}/")
print("Analysis complete!")

