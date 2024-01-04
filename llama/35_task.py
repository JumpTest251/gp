def rgb_to_hsv(r, g, b):
    """
    Write a function to convert rgb color to hsv color.

    assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)       
    """
    r /= 255
    g /= 255
    b /= 255
    cmax = max(r, g, b)
    cmin = min(r, g, b)
    delta = cmax - cmin
    hue = None
    saturation = None
    value = None
    if delta == 0:
        hue = 0.0
    elif cmax == r:
        hue = ((g - b) / delta + (g < b)) % 6
    elif cmax == g:
        hue = (b - r) / delta + 2
    else:
        hue = (r - g) / delta + 4
    saturation = delta / cmax if cmax != 0 else 0.0
    value = cmax * 100.0
    return hue, saturation, value