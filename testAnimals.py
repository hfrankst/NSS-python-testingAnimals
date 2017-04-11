import unittest
from animals import *

class TestAnimals(unittest.TestCase):

	@classmethod
	def setUpClass(self): 
		'''this is a special python class required for unit testing. The @classmethod above it allows the setUpClass to be used again without making new instances of it'''
		self.animal = Animal('Buddy', 'Panda')
		self.dog = Dog('Fido')


	def test_animal_name_is_correct(self):
		'''this is testing whether the Animal object has a property of name. This test is done by passing a name to Animal and then asserting that it is not equal to 'none' aka that it does exist'''
		self.assertEqual(self.animal.name, 'Buddy')

	def test_animal_species(self):
		'''testing the value of the species object on the potato instance has the correct value, which is the second parameter in the assertEqual method. Addtionally, this tests that there is a species attribute on the Animal object'''
		self.assertEqual(self.animal.species, 'Panda')

	def test_dog_species(self):
		'''testing the value of the species object on the potato instance has the correct value, which is the second parameter in the assertEqual method. Addtionally, this tests that there is a species attribute on the Animal object'''
		self.assertEqual(self.dog.species, 'Dog')

	def test_speed(self):
		'''setting the speed on both Dog and Animal, by invoking the walk method that is on the Animal object'''
		legs = 4
		self.animal.set_legs(legs)
		self.animal.walk()

		self.dog.set_legs(legs)
		self.dog.walk()

		self.assertEqual(self.animal.speed, 0.4)
		self.assertEqual(self.dog.speed, 0.8)

	def test_animal_instance_is_correct_type(self):
		'''testing to make sure that the animal object is an instance of animal object'''
		self.assertIsInstance(self.animal, Animal)

	def test_dog_instance_is_correct_type(self):
		'''testing to make sure that the dog object is actually an instance of the dog object'''
		self.assertIsInstance(self.dog, Dog)


#the next two lines fire the above functions and tests
if __name__ == '__main__':
    unittest.main()