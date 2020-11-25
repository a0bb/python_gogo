

class Student:

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be int')
        if score < 0 or score > 100:
            raise ValueError('score must >= 0 or <= 100')
        self.__score = score


if __name__ == '__main__':
    student = Student('张三', 100)

    # 使用@property后，score使用__命名修饰，达到私有化的目的
    # print(student.__score)

    score = student.score
    print(score)

    student.score = 90

    score = student.score
    print(score)
