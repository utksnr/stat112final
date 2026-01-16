import matplotlib
matplotlib.use("Agg")

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read clean the dataset (semicolon separated CSV)
df = pd.read_csv("data/Cleaned_ai_usage_112.csv", sep=";")

# Preview the data
print(df.head())
print(df.shape)

# Basic info about the dataset
print(df.info())
# Research Question:
# Does the effect of AI usage frequency on exam scores differ across academic majors?

#Visualization: Exam scores by AI usage frequency across majors
plt.figure(figsize=(11, 6))
sns.boxplot(
    data=df,
    x="ai_usage_frequency",
    y="exam_score",
    hue="major"
)

plt.title("Exam Scores by AI Usage Frequency Across Majors")
plt.xlabel("AI Usage Frequency")
plt.ylabel("Exam Score")

plt.legend(title="Major", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.savefig("figures/exam_score_ai_usage_by_major.png", dpi=300, bbox_inches="tight")
plt.close()


