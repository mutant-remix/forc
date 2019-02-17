from lxml.etree import Element


def head(m, created):

    head = Element("head")

    head.append(Element("tableVersion", {'value': '1.0'})) # hard-coded
    head.append(Element("fontRevision", {'value': str(m['metadata']['headVersion'])}))

    head.append(Element("checkSumAdjustment", {'value': '0'})) # TTX changes this at compilation
    head.append(Element("magicNumber", {'value': '0x5f0f3cf5'})) # hard-coded

    head.append(Element("flags", {'value': '00000000 00001011'})) # hard-coded

    head.append(Element("unitsPerEm", {'value': str(m['metrics']['unitsPerEm'])}))
    head.append(Element("created", {'value': created}))
    head.append(Element("modified", {'value': 'Mon Dec 11 13:45:00 2018'})) # TTX changes this at compilation

    head.append(Element("xMin", {'value': str(m['metrics']['xMin']) }))
    head.append(Element("yMin", {'value': str(m['metrics']['yMin']) }))
    head.append(Element("xMax", {'value': str(m['metrics']['xMax']) }))
    head.append(Element("yMax", {'value': str(m['metrics']['yMax']) }))

    head.append(Element("macStyle", {'value': '00000000 00000000'})) # hard-coded. Must agree with os2's fsType.
    head.append(Element("lowestRecPPEM", {'value': str(m['metrics']['lowestRecPPEM']) }))

    head.append(Element("fontDirectionHint", {'value': '2'})) # hard-coded
    head.append(Element("indexToLocFormat", {'value': '0'})) # not important, hard-coded
    head.append(Element("glyphDataFormat", {'value': '0'})) # not important, hard-coded

    return head
