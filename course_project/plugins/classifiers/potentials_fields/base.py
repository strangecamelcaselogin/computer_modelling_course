def sq_dist(x, y):
    """ Квадрат дистанции """
    return sum((xi - yi)**2 for xi, yi in zip(x, y))
