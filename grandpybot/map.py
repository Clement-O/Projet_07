from googlemaps import client, geocoding

from config import Config

""" Module to get coordinates of a given address. """

gm_client = client.Client(key=Config.GOOGLE_API_KEY)


def get_coordinates(address):
    """
    Get coordinates.
    :param address: Returned address from 'input.get_address()'
    :return: A set of coordinates
    """
    geocode_result = geocoding.geocode(gm_client, address)
    if geocode_result:
        coordinates = {
            "address": address,
            "street": "",
            "city": "",
            "formatted_address": geocode_result[0]['formatted_address'],
            "lat": geocode_result[0]['geometry']['location']['lat'],
            "lng": geocode_result[0]['geometry']['location']['lng'],
            "place_id": geocode_result[0]['place_id'],
            "status": "OK"
        }
        # If the first component of an address is a locality (city).
        if geocode_result[0]['address_components'][0]['types'] == [
                'locality', 'political']:
            coordinates['city'] = geocode_result[0]['address_components'][0][
                'long_name']
        # Else look for a street.
        else:
            for item in geocode_result[0]['address_components']:
                if item['types'] == ['route']:
                    coordinates['street'] = item['long_name']
        return coordinates
    else:
        coordinates = {"status": "FAIL"}
        return coordinates
