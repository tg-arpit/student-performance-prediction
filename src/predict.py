import joblib
import pandas as pd

model = joblib.load(r'C:\Users\Arpit Babu\Downloads\student-performance-prediction\Models\student_model.pkl')

new_student = pd.DataFrame({
    'StudyHours':[5],
    'Attendance':[85],
    'PreviousScore':[70]
})

prediction = model.predict(new_student)

if prediction[0] == 1:
    print("Pass")
else:
    print("Fail")