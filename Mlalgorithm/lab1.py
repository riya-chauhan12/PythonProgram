'''    1. Create a Data Frame using dictionary containing students’ marks details with columns Student_ID, Student_Name, Gender, Sub1, Sub2, Sub3 with the marks of 20 students. 
Or you can create an excel file for the same and import it.
    (i) Find the mean and median marks in each subject.
    (ii) Find the mode of ‘Gender’ column. 
    (iii) Find the variance and standard deviation of marks in each subject. 
'''
# ============================================================
# MACHINE LEARNING LAB
# Experiment 1: Statistical Analysis of Student Marks
# ============================================================

# Import the pandas library.
# Pandas is used for creating and manipulating DataFrames.
import pandas as pd


# ------------------------------------------------------------
# 1. CREATE A DATA FRAME USING A DICTIONARY
# ------------------------------------------------------------

# Create a dictionary containing the details of 20 students.
# Each key represents a column and each list contains the
# corresponding values for that column.

student_data = {
    "Student_ID": [
        101, 102, 103, 104, 105,
        106, 107, 108, 109, 110,
        111, 112, 113, 114, 115,
        116, 117, 118, 119, 120
    ],

    "Student_Name": [
        "Aarav", "Diya", "Rohan", "Ananya", "Kabir",
        "Ishita", "Arjun", "Meera", "Vivaan", "Sanya",
        "Aditya", "Priya", "Rahul", "Kavya", "Yash",
        "Neha", "Karan", "Sneha", "Varun", "Aditi"
    ],

    "Gender": [
        "Male", "Female", "Male", "Female", "Male",
        "Female", "Male", "Female", "Male", "Female",
        "Male", "Female", "Male", "Female", "Male",
        "Female", "Male", "Female", "Male", "Female"
    ],

    "Sub1": [
        78, 85, 67, 92, 74,
        88, 56, 81, 73, 95,
        69, 84, 77, 90, 62,
        79, 71, 87, 65, 93
    ],

    "Sub2": [
        82, 79, 71, 89, 76,
        91, 63, 85, 78, 94,
        72, 88, 69, 86, 65,
        83, 75, 90, 68, 92
    ],

    "Sub3": [
        75, 88, 69, 94, 72,
        85, 61, 79, 81, 96,
        70, 87, 73, 91, 64,
        82, 77, 89, 66, 95
    ]
}


# Convert the dictionary into a Pandas DataFrame.
df = pd.DataFrame(student_data)


# Display the complete DataFrame.
print("Student Marks Data:")
print(df)


# ------------------------------------------------------------
# (i) FIND MEAN AND MEDIAN MARKS IN EACH SUBJECT
# ------------------------------------------------------------

# Select only the subject columns because Student_ID,
# Student_Name and Gender are not marks.
subjects = ["Sub1", "Sub2", "Sub3"]


# Calculate the mean (average) marks for each subject.
# mean() calculates the average of all values in each column.
mean_marks = df[subjects].mean()

print("\nMean Marks in Each Subject:")
print(mean_marks)


# Calculate the median marks for each subject.
# median() returns the middle value after arranging
# the values in ascending order.
median_marks = df[subjects].median()

print("\nMedian Marks in Each Subject:")
print(median_marks)


# ------------------------------------------------------------
# (ii) FIND THE MODE OF THE 'GENDER' COLUMN
# ------------------------------------------------------------

# Mode is the value that occurs most frequently.
# mode() can return more than one value if multiple values
# have the same highest frequency.

gender_mode = df["Gender"].mode()

print("\nMode of Gender:")
print(gender_mode)


# ------------------------------------------------------------
# (iii) FIND VARIANCE AND STANDARD DEVIATION
# ------------------------------------------------------------

# Calculate variance for each subject.
# Variance measures how much the marks are spread out
# from their mean.
variance_marks = df[subjects].var()

print("\nVariance of Marks in Each Subject:")
print(variance_marks)


# Calculate standard deviation for each subject.
# Standard deviation is the square root of variance and
# represents the spread of marks in the same unit as marks.
standard_deviation = df[subjects].std()

print("\nStandard Deviation of Marks in Each Subject:")
print(standard_deviation)


