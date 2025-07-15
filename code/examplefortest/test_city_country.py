
from city_functions import get_city_country

def test_city_country_2names():
    """Test if city_country function works for arguments like: Santiago, Cile"""
    output = get_city_country('Santiago','Cile')
    assert output == 'Santiago, Cile'

def test_city_country_population():
    """Test if city_country function works for arguments like: Santiago, Cile, 500000"""
    output = get_city_country('Santiago','Cile',500000)
    assert output == 'Santiago, Cile - population: 500000'