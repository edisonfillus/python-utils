def primality(n):
    if (n < 2):
      return false
    elif (n == 2):
      return true
    elif (n % 2 == 0):
      return false

    sqrt = int(math.sqrt(n)+1)
    for i in range(3, sqrt, 2):
      if (n % i == 0):
        return false

    return true


primality(75)
