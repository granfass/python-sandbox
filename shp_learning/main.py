#!/usr/bin/env python

import xml.etree.ElementTree as etree
from typing import Dict, List

NAME_SPACE: Dict[str, str] = {'kml': 'http://www.opengis.net/kml/2.2'}


def get_description(element: etree.Element) -> (str, str):
    busstops: List[str] = element.find('kml:description', NAME_SPACE).text.split()
    return busstops[0], busstops[1]


def main():
    tree = etree.parse('kml/komae_bus.kml')
    root = tree.getroot()

    placemarks = root.findall(f"./{{{NAME_SPACE['kml']}}}Document/{{{NAME_SPACE['kml']}}}Placemark")
    for i, placemark in enumerate(placemarks):
        start_busstop, end_busstop = get_description(placemark)
        print(f'{i + 1}番目の発バス停：{start_busstop}')
        print(f'{i + 1}番目の着バス停：{end_busstop}')

        print(f"{i+1}番目のpoliline")
        print(placemark.find('kml:LineString/kml:coordinates', NAME_SPACE).text)


if __name__ == "__main__":
    main()
