from lxml.etree import Element



def strike(metrics, strikeIndex, strikeRes, subfolder, glyphs):

    height =          round( (metrics['height'] / metrics['unitsPerEm']) * 128 )
    width =           round( (metrics['width'] / metrics['unitsPerEm']) * 128 )

    horiBearingX =    round( (metrics['xMin'] / metrics['unitsPerEm']) * 128 )
    horiBearingY =    round( (metrics['yMin'] / metrics['unitsPerEm']) * 128 )
    horiAdvance =     width

    vertBearingX =    round( (metrics['xMin'] / metrics['unitsPerEm']) * 128 )
    vertBearingY =    round( (metrics['yMin'] / metrics['unitsPerEm']) * 128 )
    vertAdvance =     height


    # start of strikes
    # (which we're fudging right now)
    # ------------------------------------------------------------
    strike = Element("strikedata", {"index": strikeIndex})

    for g in glyphs['img']:

        # you only put them in if there's an actual image
        if g.imagePath:

            # format 18 for big metrics and PNG data.
            bitmapTable = Element("cbdt_bitmap_format_18", {"name": g.codepoints.name() })

            glyphMetrics = Element("BigGlyphMetrics")
            glyphMetrics.append(Element("height",          {"value": str(height) }))
            glyphMetrics.append(Element("width",           {"value": str(width) }))
            glyphMetrics.append(Element("horiBearingX",    {"value": str(horiBearingX) }))
            glyphMetrics.append(Element("horiBearingY",    {"value": str(horiBearingY) }))
            glyphMetrics.append(Element("horiAdvance",     {"value": str(horiAdvance) }))
            glyphMetrics.append(Element("vertBearingX",    {"value": str(vertBearingX) }))
            glyphMetrics.append(Element("vertBearingY",    {"value": str(vertBearingY) }))
            glyphMetrics.append(Element("vertAdvance",     {"value": str(vertAdvance) }))

            bitmapTable.append(glyphMetrics)


            rawImageData = Element("rawimagedata")

            with open(g.imagePath[subfolder], "rb") as read_file:
                pngHexdump = read_file.read().hex()

            rawImageData.text = pngHexdump

            bitmapTable.append(rawImageData)

            strike.append(bitmapTable)

    return strike




def cbdt(metrics, glyphs):
    """
    Generates and returns a glyf table with dummy data.
    """

    cbdt = Element("CBDT")

    cbdt.append(Element("header", {"version": "3.0"})) # hard-coded



    # get basic strike information.

    for g in glyphs['img']:
        if g.imagePath:
            firstGlyphWithStrikes = g
            break


    # iterate over each strike.

    strikeIndex = 0

    for formatName, format in firstGlyphWithStrikes.imagePath.items():
        if formatName.split('-')[0] == "png":
            strikeRes = formatName.split('-')[1]
            cbdt.append(strike(metrics, str(strikeIndex), strikeRes, formatName, glyphs))
            strikeIndex += 1



    return cbdt
