import xml.etree.ElementTree as etree

import pytest

from shp_learning import main


@pytest.fixture
def create_xml() -> etree.Element:
    xml_string: str = '<?xml version="1.0" encoding="UTF-8"?>' \
        '<kml xmlns="http://www.opengis.net/kml/2.2">' \
        '<Document>' \
        '  <Placemark>' \
        '    <name>1</name>' \
        '    <description>狛江駅北口\n狛江市役所前</description>' \
        '    <styleUrl>#m_ylw-pushpin</styleUrl>' \
        '    <LineString>' \
        '      <tessellate>1</tessellate>' \
        '      <coordinates>' \
        '        139.5773785398502,35.63317469234866,0 139.5783391581343,35.63395289893936,0 139.5783635194075,35.63400605957735,0' \
        '      </coordinates>' \
        '    </LineString>' \
        '  </Placemark>' \
        '</Document>' \
        '</kml>'

    element = etree.fromstring(xml_string)
    yield element


def test_get_description(create_xml):
    element = create_xml.find(f"./{{{main.NAME_SPACE['kml']}}}Document/{{{main.NAME_SPACE['kml']}}}Placemark")
    assert main.get_description(element) == ('狛江駅北口', '狛江市役所前')


def test_get_polyline(create_xml):
    element = create_xml.find(f"./{{{main.NAME_SPACE['kml']}}}Document/{{{main.NAME_SPACE['kml']}}}Placemark")
    assert main.get_polyline(element) == '139.5773785398502,35.63317469234866,0 ' \
        '139.5783391581343,35.63395289893936,0 ' \
        '139.5783635194075,35.63400605957735,0'
