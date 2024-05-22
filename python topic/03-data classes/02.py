from dataclasses import dataclass

# dataclasses allow from version python 3.7
#طريقه تقدر تعرف بيها الكلاس جديده

@dataclass(order=True)
class Person:
    name: str
    age :int

    # def __str__(self):
    #     return self.name     #plan B 
    
p1 = Person('mahmoud',25)
p2 = Person ('ahmed',21)

# print(p1)
# print(p1.name)
# print(p1.age)


print(p1>p2) #TypeError: '>' not supported between instances of 'Person' and 'Person
