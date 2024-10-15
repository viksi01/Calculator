class History:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def show(self):
        for record in self.records:
            print(record)