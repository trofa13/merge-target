from django.shortcuts import render
from .models import Treasure


# Create your views here.
def index(request):
	treasures = Treasure.objects.all()

	return render(request, 'index.html', {'treasures': treasures})


def detail(request, treasure_id):
	treasure = Treasure.objects.get(id=treasure_id)
	return render(request, 'detail.html', {'treasure': treasure})



# class Treasure:
# 	def __init__(self, name, value, material, location):
# 		self.name = name
# 		self.value = value
# 		self.material = material
# 		self.location = location


# treasures = [
# 	Treasure('Gold Nugget', 500.00, 'gold', 'Boobs inc.'),
# 	Treasure('Silver Nugget', 40.05, 'silver', 'Acme'),
# 	Treasure('Nickel', 0, 'tin', 'Spam inc.')
# ]