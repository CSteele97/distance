import math

def compute_distance(point1, point2):
    """ 
    Compute the distance between two points.
    
    The points should be given as a tuple with an x and a y coordinate.
    The function returns the distance which is computed by Pythagoras.
    """
    return math.sqrt((point1[0] - point2[1]) **2
                     + (point1[1] - point2[1]) **2)

point1 = (0, 0)
point2 = (1, 1)
print(compute_distance(point1, point2))
 