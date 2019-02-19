from firebase import firebase

url = 'https://aluapp-7a06e.firebaseio.com/'
fb = firebase.FirebaseApplication(url, None)
result = fb.patch('/students/', {'date_of_birth': 'someday', 'full_name': 'Alan Turing'})