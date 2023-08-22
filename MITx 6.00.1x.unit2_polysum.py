import math
def polysum(n, s):
    perimeter = n*s
    x = math.tan(math.pi/n)
    sqr_perimeter = perimeter**2
    area_polygon = (0.25*perimeter*s)/x
    ans = sqr_perimeter + area_polygon
    return round(ans,4)