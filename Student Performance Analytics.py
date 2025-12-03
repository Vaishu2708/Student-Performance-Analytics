import mysql.connector
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# SQL Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vaishu2708",  
    database="student_db"
)

query = "SELECT * FROM student_marks"
df = pd.read_sql(query, conn)

# Total & Percentage Calculation
df["Total Marks"] = df[["maths", "science", "english", "computer"]].sum(axis=1)
df["Percentage"] = df["Total Marks"] / 4

fig, axs = plt.subplots(2, 2, figsize=(13, 10))
fig.suptitle("Student Performance Analytics Dashboard", fontsize=16, fontweight='bold')

# 1️⃣ Average Marks by Subject
subjects_mean = df[["maths", "science", "english", "computer"]].mean()
axs[0, 0].bar(subjects_mean.index, subjects_mean.values)
axs[0, 0].set_title("Average Marks by Subject")
axs[0, 0].set_ylabel("Marks")

# 2️⃣ Gender-Based Performance
sns.barplot(x="gender", y="Percentage", data=df, estimator=sum, ax=axs[0, 1])
axs[0, 1].set_title("Gender vs Performance")

# 3️⃣ Attendance vs Percentage
sns.scatterplot(x="attendance", y="Percentage", data=df, hue="gender", s=120, ax=axs[1, 0])
axs[1, 0].set_title("Attendance vs Percentage")

# 4️⃣ Correlation Heatmap (numeric columns only)
numeric_df = df.select_dtypes(include=['int64', 'float64'])
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=axs[1, 1])
axs[1, 1].set_title("Correlation Heatmap")

plt.tight_layout()
plt.show()
