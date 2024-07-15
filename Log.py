import datetime
import os

class Logger():
    def __init__(self):
        self.logs_text = ""
        self.enabled = False
        self.file_name = f"{datetime.datetime.now().strftime('%H-%M-%S')}.txt"
        self.file_name = os.path.normpath(self.file_name)
        
    def log(self, logged_text: str):
        if self.enabled:
            self.logged_message = f"[{datetime.datetime.now().strftime('%X')}]: {logged_text}\n"
            self.logs_text += self.logged_message
            print(self.logged_message)
    
    def create_logfile(self):
        with open(self.file_name, "w") as log_file:
            log_file.write(self.logs_text)