from faker import Faker

fake = Faker()
Faker.seed(0)

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
        person = dict(first_name=first_name, last_name = last_name, latitude =latitude, longitude =longitude, county = county, country = country, timezone =  timezone) 
        users.append(person)
    return users
    
if __name__ == "__main__":
    print(generate())