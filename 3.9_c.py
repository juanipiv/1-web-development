def vec_product(x1, y1, z1, x2, y2, z2):
    """we are going to calculate the vectorial product of two given vectors
    x1 (int): first coordenate of the first vector
    y1 (int): second coordenate of the first vector
    z1 (int): third coordenate of the first vector
    x2 (int): first coordenate of the seconde vector
    y2 (int): second coordenate of the second vector
    z2 (int): third coordenate of the second vector
    output (int), (int), (int): coordinates of the result vector"""
    x = y1*z2 - z1y2
    y = z1*x2 - x1z2
    z = x1*y2 - y1x2
    
