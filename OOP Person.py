class Person:
    def __init__(self, name, job =None, pay =0):
        self.name = name
        self.job = job
        self.pay = pay
    def Job(self):
        return self.job
    def LastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.percent = percent
        self.pay2 = int(self.pay * (1 + self.percent))
        return self.pay2
    def __str__(self):
        return ('Person {0}, vith salary {1} euros per our'.format(self.name, self.pay))
    def __repr__(self):
        return ('Person {}'.format(self.name))
class Manager(Person):
    def __init__(self, name, job, pay):
        self.person = Person(name, job, pay)        # used onli nwithout nasled, itd meen thst if we have unknown attribute in class manager wego to Person
    def giveRaise(self, percent, bonus = .10):
        Person.giveRaise(self, percent + bonus)
        print ("New salary become {} ".format(self.pay2))
    def __getattr__(self, item):                   # used onli nwithout nasled, itd meen thst if we have unknown attribute in class manager wego to Person
        return getattr(self.person, item)

if __name__ =='__main__':
    rec1 = Person('Bob Smith', 'Hunter',40)
    # sue = Person('Sue Jones', job ='manager', pay = 10)
    print(rec1.name, rec1.job, rec1.pay)
    print(list(Person.__dict__.keys()))
    print(list(rec1.__dict__.keys()))
    print(rec1.LastName())
    print(rec1.giveRaise(0.1))
    # print(sue.Job())

    # if sue.Job() =='manager':

    sue = Manager('Sue Jones', job ='manager', pay = 10)
    sue.giveRaise(.10)
    print(' for Person {}, {}, {} {}'.format(sue.name, sue.job, sue.pay2, sue.LastName()))
    print(list(Manager.__dict__.keys()))
    print('--ALL tree---')
    for object in (sue, rec1):
        print(object.name, object. pay2)

