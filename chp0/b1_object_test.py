
class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_person(self):
        return '<Person (%s, %s)>' % (self.name, self.age)

if __name__ == '__main__':
    p = Person('Jhon', 32)
    print('Type of object:', type(p))
    print(p.get_person())
