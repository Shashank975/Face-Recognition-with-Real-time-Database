
from firebase_admin import db
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecoapplication-default-rtdb.firebaseio.com/",
    'storageBucket': "facerecoapplication.appspot.com"
})


ref = db.reference('Students')

data = {

    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "821142":
        {
            "name": "Shashank Chhoker",
            "major": "Computer Science",
            "starting_year": 2021,
            "total_attendance": 142,
            "standing": "3",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "821165":
        {
            "name": "Vedant Shrimali",
            "major": "Computer Science",
            "starting_year": 2021,
            "total_attendance": 156,
            "standing": "3",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "821147":
        {
            "name": "Siddharth Bhople",
            "major": "Computer Science",
            "starting_year": 2021,
            "total_attendance": 75,
            "standing": "3",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "821173":
        {
            "name": "yash Gupta",
            "major": "Computer Science",
            "starting_year": 2021,
            "total_attendance": 75,
            "standing": "3",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963811":
        {
            "name": "Emma watson",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)