
import pandas as pd

data = {
    'Student': ['Amit', 'Priya', None],
    'Marks': [78, None, 91],
    'Attendance': [85, 75, None],
    'Grade': ['B', 'B', 'A']
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Fill missing marks with average marks
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())

# Fill missing attendance with average attendance
df['Attendance'] = df['Attendance'].fillna(df['Attendance'].mean())

# Remove rows with missing student names
df = df.dropna(subset=['Student'])

print("\nUpdated Data:")
print(df)
