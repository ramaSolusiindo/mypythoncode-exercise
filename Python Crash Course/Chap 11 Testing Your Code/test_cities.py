import unittest
from city_function import get_city_country


class CitiesTestCase(unittest.TestCase):
    """ Test from city_function.py """
    def test_cities_country(self):
        formatted_name = get_city_country('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')

    def test_citise_country_population(self):
        formatted_name = get_city_country('santiago', 'chile', 'population = 5000000')
        self.assertEqual(formatted_name, 'Santiago, Chile - Population = 5000000')


if __name__ == '__main__':
    unittest.main()

