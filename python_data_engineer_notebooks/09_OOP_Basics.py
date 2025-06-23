# Object-Oriented Programming
class DataProcessor:
    def __init__(self, name):
        self.name = name

    def process(self):
        print(f"Processing data for {self.name}")

dp = DataProcessor("Dev")
dp.process()