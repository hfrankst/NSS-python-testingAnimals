import unittest
from animals import Animal, Dog

class TestAnimals(unittest.TestCase):

	@classmethod
	def setUpClass(self): 
		'''this is a special python class required for unit testing. The @classmethod above it allows the setUpClass to be used again without making new instances of it'''
		self.animal = Animal('Dog')
		self.dog = Dog('Fido')


	def test_animal_name(self):
		'''this is testing whether the Animal object has a property of name. This test is done by passing a name to Animal and then asserting that it is not equal to 'none' aka that it does exist'''
		ani = Animal('Fido')
		self.assertIsNotNone(ani.name)

	def test_species(self):
		'''testing the value of the species object on the potato instance has the correct value, which is the second parameter in the assertEqual method. Addtionally, this tests that there is a species attribute on the Animal object'''
		potato = Animal(species='Dog')
		self.assertEqual(potato.species, 'Dog')

	def test_speed(self):
		'''setting the speed on both Dog and Animal, by invoking the walk method that is on the Animal object'''
		potato = Animal()
		potato.set_legs(4)
		potato.walk()
		self.assertEqual(potato.speed, 0.4)

	def test_animal_instance(self):
		'''testing to make sure that the animal object is an instance of animal object'''
		new_animal = Animal()
		self.assertIsInstance(new_animal, Animal)

	def test_dog_instance(self):
		'''testing to make sure that the dog object is actually an instance of the dog object'''
		new_dog = Dog('Fido')
		self.assertIsInstance(new_dog, Dog)


#the next two lines fire the above functions and tests
if __name__ == '__main__':
    unittest.main()