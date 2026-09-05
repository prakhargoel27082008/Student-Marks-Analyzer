
import pandas as pd
import matplotlib.pyplot as plt
def calculate_grade(percentage):
    if percentage>=90:
        return "A+"
    elif percentage>=80:
        return "A"
    elif percentage>=70:
        return "B"
    elif percentage>=60:
        return "C"
    elif percentage>=50:
        return "D"
    else:
        return "F"
def check_status(row):
    for subject in subjects:
        if row[subject]<33:
            return "Fail"
        else:
            return "Pass"
# Read Students Data
data = pd.read_csv("data/students.csv")
subjects = ["Maths", "Physics", "Chemistry", "English"]
# Calculate Total, Average,  Percentage and Status
data["Total"] = data[subjects].sum(axis=1)
data["Average"] = data[subjects].mean(axis=1)
data["Percentage"] = (data["Total"]/400)*100
data["Grade"] = data["Percentage"].apply(calculate_grade)
data["Status"] = data.apply(check_status, axis=1)
print(data.to_string())
topper = data.loc[data["Total"].idxmax()]
ranked_data = data.sort_values(by = "Total", ascending=False)
print("\n Ranked Data")
print(ranked_data.to_string())
print("\n========================")
print("🏆 TOPPER")
print("========================")
print("Name :", topper["Name"])
print("Total:", topper["Total"])
print("Grade:", topper["Grade"])
ranked_data.insert(0, "Rank", range(1, len(ranked_data) + 1))
print(
    ranked_data[["Rank", "Name", "Total", "Percentage", "Grade", "Status"]]
    .to_string(index=False)
)
student_name = input("\n Enter the student's name: ")
student = data[data["Name"].str.lower() == student_name.lower()]
if student.empty:
    print("Student not found.")
else:
    print(student.to_string(index=False))

plt.figure(figsize = (8, 5))
plt.bar(data["Name"], data["Total"])
plt.title("Total Marks of Students")
plt.xlabel("Students")
plt.ylabel("Total Marks")
plt.savefig("total_marks.png")
plt.show()
data.to_csv("results.csv", index=False)
print("\nResults saved successfully as results.csv")
