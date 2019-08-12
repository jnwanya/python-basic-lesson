class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.number = (1, 34, 56, 90)

    def total(self):
        return sum(self.number)


player_one = LotteryPlayer('John')
player_one.number = (3, 5, 90)
player_two = LotteryPlayer('Jude')
# print(player_one.name == player_two.name)
# print(player_one.total())


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @staticmethod
    def go_to_school():
        print('I am going to school')


anna = Student('Anna', 'MIT')
anna.marks.append(45)
print(anna.marks)
print(anna.average())
Student.go_to_school()
