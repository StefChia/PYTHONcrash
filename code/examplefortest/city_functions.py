
def get_city_country(city, country, population=''):
    """Return a neatly City, Country string"""
    if population:
        string = f'{city.title()}, {country.title()} - population: {population}'
        return string
    else:
        string = f'{city}, {country}'
        return string.title()
