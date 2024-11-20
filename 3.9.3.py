def max_product(n1, n2, n3, n4):
    result1 = n1 * n2
    result2 = n1 * n3
    result3 = n1 * n4
    result4 = n2 * n3
    result5 = n2 * n4
    result6 = n3 * n4
    return max(result1, result2, result3, result4, result5, result6)
