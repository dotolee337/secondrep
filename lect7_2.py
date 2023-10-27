#객체지향 프로그래밍
#클래스 와 속성출력
"""
class Person :
	name = "python"
	age = 23
	number = "01012345678"
 
p = Person()
print(p.name)
print(p.age)
print(p.number)

p1 = Person()
print(p1.name)
print(p1.age)
print(p1.number)
"""
#self 키워드

#메서드
"""
class Person :
	name = "python"
	age = 23
	number = "01012345678"

	def getIntroduce(self):
		return f"My name is {self.name}"

p = Person()
print(p.name)
print(p.age)
print(p.number)
print(p.getIntroduce())

#생성자 메서드
class Person :
	def __init__(self, name, age, number):
		self.name = name
		self.age = age
		self.number = number
  
p = Person("hello", 24, '01111111111' )
p1 = Person("he", 21, "0108")
p2 = Person("hee",24,"0281654654")

print(p.name)
print(p1.name)
print(p2.name)
"""
#클래스 변수
#
class Person :
	count = 0

	def __init__(self, name, age, number):
		self.name = name
		self.age = age
		self.nmuber = number
		Person.count += 1

	@classmethod
	def getCount(cls) : 
		return cls.count
  
p = Person("hello", 24, '01111111111' )
print(p.name)
print(p.count)
print(p.getCount)
p1 = Person("he", 21, "0108")
print(p1.name)
print(p1.count)
print(p1.getCount)
p2 = Person("hee",24,"0281654654")
print(p2.name)
print(p2.count)
print(p2.getCount)

print(p.count)
print(p1.count)
print(p2.count)
 