from mediawiki import MediaWiki
import re

from grandpybot.response import format_response

""" Module to get the wiki infos of a coordinates set. """

wikipedia = MediaWiki(lang='fr')


def get_infos(coordinates):
    """
    Get wiki infos.
    :param coordinates: Address coordinates
    :return: A formatted response or an error
    """
    page_list = wikipedia.geosearch(latitude=coordinates['lat'],
                                    longitude=coordinates['lng'],
                                    radius=10000,
                                    results=50)

    if page_list:
        # If user's input looking for a city
        if coordinates['city'] and coordinates['city'] in page_list:
            summary = wikipedia.page(title=coordinates['city']).summary
            return format_response(coordinates, coordinates['city'], "EXACT",
                                   summary)
        # Else look for the exact place or street
        else:
            # Regex to search part of the address in the wiki page list.
            # Useful only for common / generic places. Ex: "Mairie Paris".
            address = coordinates['address'].split()
            if len(address) > 1:
                regex_address = r'\b({}[\D]+{})'.format(address[0], address[1])
            else:
                regex_address = r'\b({})'.format(address[0])

            for title in page_list:
                # Search part of the address in the wiki page list.
                if re.match(regex_address, title, flags=re.IGNORECASE):
                    summary = wikipedia.page(title=title).summary
                    return format_response(coordinates, title, "EXACT",
                                           summary)
                # Otherwise look for street in the wiki page list.
                elif coordinates['street'] in title:
                    summary = wikipedia.page(title=title).summary
                    return format_response(coordinates, title, "NEAR",
                                           summary)
            # Else take the closest page from the address (first result).
            else:
                summary = wikipedia.page(title=page_list[0]).summary
                return format_response(coordinates, page_list[0], "NEAR",
                                       summary)
    else:
        response = {"status": "FAIL"}
        return response
