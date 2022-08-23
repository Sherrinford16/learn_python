class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if 0 <= self.score < 60:
            return 'C'
        if 60 <= self.score < 80:
            return 'B'
        if 80 <= self.score <= 100:
            return 'A'
        else:
            raise ValueError
