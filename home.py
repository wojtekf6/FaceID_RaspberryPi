import RPi.GPIO as GPIO
from pydub import AudioSegment
from pydub.playback import play
import data_loader


class Home:
    def __init__(self):
        self.room1 = 18
        self.room2 = 15
        self.air_condition = 23
        self.custom = 24
        self.users_data = data_loader.load_data("users.json")
        self.set_up_pi()
        self.reset_settings()

    def set_up_pi(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.room1, GPIO.OUT)
        GPIO.setup(self.room2, GPIO.OUT)
        GPIO.setup(self.air_condition, GPIO.OUT)
        GPIO.setup(self.custom, GPIO.OUT)

    def reset_settings(self):
        GPIO.output(self.room1, False)
        GPIO.output(self.room2, False)
        GPIO.output(self.air_condition, False)
        GPIO.output(self.custom, False)

    def get_user_id(self, detected_user):
        for user in self.users_data:
            if user['name'] == detected_user:
                print(user['name'])
                return self.users_data.index(user)

    def log_user_data(self, user_id):
        print("User: " + str(self.users_data[user_id]['name']))
        print("Room: " + str(self.users_data[user_id]['room']))
        print("Air condition: " + str(self.users_data[user_id]['air_condition']))
        print("Custom device: " + str(self.users_data[user_id]['custom']))
        print("Music: " + str(self.users_data[user_id]['music']))

    def set_home(self, user):
        user_id = self.get_user_id(user)
        self.log_user_data(user_id)

        if self.users_data[user_id]['room'] == 1:
            GPIO.output(self.room1, True)
        elif self.users_data[user_id]['room'] == 2:
            GPIO.output(self.room2, True)

        if self.users_data[user_id]['air_condition'] == 1:
            GPIO.output(self.air_condition, True)

        if self.users_data[user_id]['custom'] == 1:
            GPIO.output(self.custom, True)

        if self.users_data[user_id]['music'] is not "":
            song = AudioSegment.from_mp3(self.users_data[user_id]['music'])
            play(song)