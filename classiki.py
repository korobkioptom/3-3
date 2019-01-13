class Human:
	def __init__(self, Name = 'Petya', age = 34):
		self.Name = Name
		self.age = age

		#if type(Name) is not str:
			#print ('name is not str')
		#if type(age) is not int:
			#print ('age is not int')

	def say_hello (self):
		return ('hello, my name is {}'.format(self.Name))

boom = Human()
print (boom.say_hello())


class Builder(Human):
	
	def __init__(self, profession = 'Manager'):
		self.profession = profession
		super().__init__()

	def say_hello(self):
		return('Hello, my name is {Name} and i am a {profession}'.format(profession=self.profession, Name=self.Name))

parapa = Builder()
print (parapa.say_hello())



class Writer(Human):

	def books(*args):

		return ('I wrote' ,args)
pisatel = Writer()
print (pisatel.books('kashtanka','atlant raspravil plechi','dubrovski'))