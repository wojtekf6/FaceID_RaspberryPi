import pi_face_recognition
from home import Home

myHome = Home()
detected_user = pi_face_recognition.run()
myHome.set_home(detected_user)




