class RobotVacuum:
    def __init__(self, id, model):
        self.id = id
        self.model = model

    def start_cleaning(self):
        return f"Robot {self.id} is now cleaning."

    def stop_cleaning(self):
        return f"Robot {self.id} has stopped cleaning."
