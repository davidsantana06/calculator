import datetime

DATE_FORMAT = '%d/%m/%y, %H:%M:%S'

class Operation:

    def __init__ (self, id, operation):
        self.id = id
        self.operation = operation
        self.date = datetime.datetime.now()

    def __str__(self):
        return ('{0}) {1} [{2}]'.format(self.id, self.operation, self.date.strftime(DATE_FORMAT)))