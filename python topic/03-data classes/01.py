class Person:
    def __init__(self,name,age):
        self.name = name
        self.age= age

    def __str__(self):
        return f'{self.name}, - {self.age}'
    
    def __gt__(self,other):
        return self.age > other.age

    def __lt__(self,other):
        pass

p1 = Person('mahmoud',25)
p2 = Person ('ahmed',21)

print(p1)
print(p1.name)
print(p1.age)
# Noraml cody

#print(p1>p2) #TypeError: '>' not supported between instances of 'Person' and 'Person'


print(p1>p2)
 