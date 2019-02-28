from lxml.etree import Element

def gasp():
    """
    Create a really basic gasp table.
    """

    gasp = Element("gasp")

    gasp.append(Element("gaspRange", {'rangeMaxPPEM': '65535'
                                     ,'rangeGaspBehavior': '0x0f'
                                     }))

    return gasp