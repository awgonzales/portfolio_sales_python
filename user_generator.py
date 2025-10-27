from faker import Faker
import requests as r

# CONSTSANTS

USER_URL = "https://randomuser.me/api/?nat=us&results="

Faker.seed(0)

fake = Faker()

def random_user(count:int = 100):
    """
    This creates 100 random users
    """
    users = []
    data = r.get(f"{USER_URL}{count}")
    results = data.json()
    for result in results['results']:
        last_name = result['name']['last']
        first_name = result['name']['first']
        region = fake.random_choices(elements =("Northeast", "Southeast", "Midwest", "Southwest", "West"), length = 1)
        sales =fake.random_int(min=100, max =10000)
        #city = result['location']['city']
        #state = result['location']['state']
        #latitude = result['location']['coordinates']['latitude']
        #longitude = result['location']['coordinates']['longitude']
        latitude, longitude, city, state , timezone = fake.local_latlng(country_code="US")
        photo = result['picture']['thumbnail']
        user = dict(first_name=first_name, last_name = last_name, region = region[0], sales = sales, city = city,
        state = state, latitude = float(latitude), 
        longitude = float(longitude), photo = photo)
        users.append(user)

    return users

def generate(count:int=10):
    """
    This function will generate users. (Default: 10)
    first_name
    last_name
    latitude
    longitude
    """
    users = []
    for _ in range(count):
        first_name = fake.first_name()
        last_name = fake.last_name()
        latitude, longitude, county, country, timezone = fake.local_latlng()
        print(first_name, last_name, latitude, longitude, county, county, timezone)
        person = dict(first_name=first_name, last_name = last_name, latitude =float(latitude), longitude =float(longitude), county = county, country = country, timezone =  timezone) 
        users.append(person)
    return users
    
if __name__ == "__main__":
    # generate()
    print(random_user(count = 10))