class EmptyQueueError(Exception):
	pass

class WrongTypeError(Exception):
	pass

class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species
		self.next = None

class Queue:
	def __init__(self, species):
		self.species = species
		self.first = None
		self.last = None

	def enqueue(self, animal):
		if animal.species != self.species:
			raise WrongTypeError('tried enqueuing {0} in {1} queue'.format(animal.species, self.species))
		if not self.last:
			self.first = animal
		else:
			self.last.next = animal
		self.last = animal
		animal.next = None

	def dequeue(self):
		if not self.first:
			raise EmptyQueueError('tried dequeuing from empty queue')
		animal = self.first
		if self.first is self.last:
			self.first, self.last = None, None
		else:
			self.first = self.first.next
		return animal

class AnimalShelter:
	def __init__(self, *types):
		self.num_animals = 0
		self.inventory = {species: Queue(species) for species in types}

	def enqueue(self, animal):
		if animal.species not in self.inventory:
			raise WrongTypeError('AnimalShelter does not support {0}'.format(animal.species))
		self.num_animals += 1
		animal.id = self.num_animals
		self.inventory[animal.species].enqueue(animal)

	def dequeue_any(self):
		oldest = None
		for queue in self.inventory.values():
			if queue.first is not None:
				animal = queue.first
				if oldest is None or oldest.id > animal.id:
					oldest = animal
		if oldest is None:
			raise EmptyQueueError('AnimalShelter has no animals!')
		return self.inventory[oldest.species].dequeue()

	def dequeue_type(self, species): # implements dequeue_dog, dequeue_cat :)
		if species not in self.inventory:
			raise WrongTypeError('AnimalShelter does not have animal {0}'.format(species))
		return self.inventory[species].dequeue()

# Let's test it!
shelter = AnimalShelter('cat', 'dog', 'rhino')

print("Let's welcome: billy, daphnie, ace, and charles!")
shelter.enqueue(Animal('billy', 'dog'))
shelter.enqueue(Animal('daphnie', 'cat'))
shelter.enqueue(Animal('ace', 'rhino'))
shelter.enqueue(Animal('charles', 'dog'))
try:
	shelter.enqueue(Animal('mickey', 'mouse'))
except WrongTypeError as err:
	print(err)

print('''Mario's Animal Shelter:
cat:   [daphnie]
dog:   [billy, charles]
rhino: [ace]''')

print('Goodbye {0}!'.format(shelter.dequeue_any().name))
print('Goodbye {0}!'.format(shelter.dequeue_any().name))
print('Goodbye {0}!'.format(shelter.dequeue_type('dog').name))
print('Goodbye {0}!'.format(shelter.dequeue_type('rhino').name))

try:
	shelter.dequeue_any()
except EmptyQueueError as err:
	print(err)

try:
	shelter.dequeue_type('dog')
except EmptyQueueError as err:
	print(err)
