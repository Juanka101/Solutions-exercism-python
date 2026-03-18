def classify(n):
    if not isinstance(n, int):
        raise ValueError("Classification is only possible for positive integers.")

    if n <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    suma_divisores = 0
    for i in range(1, n):
        if n % i == 0:
            suma_divisores += i

    if suma_divisores == n:
        return "perfect"
    elif suma_divisores > n:
        return "abundant"
    else:
        return "deficient"

