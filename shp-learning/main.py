#!/usr/bin/env python

import xml.etree.ElementTree as etree
from typing import Dict


def main():
    name_space: Dict[str, str] = {'kml': 'http://www.opengis.net/kml/2.2'}
    name_space_uri: str = 'http://www.opengis.net/kml/2.2'

    tree = etree.parse('kml/komae_bus.kml')
    root = tree.getroot()

    placemarks = root.findall(f"./{{{name_space_uri}}}Document/{{{name_space_uri}}}Placemark")
    for i, placemark in enumerate(placemarks):
        print(f"{i+1}番目の区間")
        print(placemark.find('kml:description', name_space).text)

        print(f"{i+1}番目のpoliline")
        print(placemark.find('kml:LineString/kml:coordinates', name_space).text)


if __name__ == "__main__":
    main()
