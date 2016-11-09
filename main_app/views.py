from django.shortcuts import render


# Create your views here.
def index(request):

	return render(request, 'index.html', {'treasures': treasures})






class Treasure:
	def __init__(self, name, value, material, location):
		self.name = name
		self.value = value
		self.material = material
		self.location = location


treasures = [
	Treasure('Gold Nugget', 500.00, 'gold', 'Boobs inc.'),
	Treasure('Silver Nugget', 40.05, 'silver', 'Acme'),
	Treasure('Nickel', 0, 'tin', 'Spam inc.')
]