from geopy.geocoders import Nominatim
from math import pi

class different_city_pattern(pattern):
  def __init__(self):
    super().__init__()


  def do_stuff(self, cards: list[str], transactions: dict, transaction_id: list[str]):
      for i in range(1, len(transactions)):
          address2 = "Российская Федерация, " + transactions[i]['city'] 
          address1 = "Российская Федерация, " + transactions[i-1]['city'] 
          geolocator = Nominatim(user_agent="Tester")
          location2 = geolocator.geocode(address2)
          location1 = geolocator.geocode(address1)
          delta = (transactions[i]['date'] - transactions[i-1]['date'])
          delta = delta.total_seconds()
          r = 6371000
          dlat = (location2.latitude - location1.latitude)*(pi*r/180)
          dlon = (location2.longitude - location1.longitude)*(pi*r/180)
          dist = (dlat**2+dlon**2)**0.5
          if r/delta > 350:
              transactions[i]['fraud_pattern'] = 'different_city'
