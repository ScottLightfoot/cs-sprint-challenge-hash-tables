def intersection(arrays):
    """
    YOUR CODE HERE
    """
    d = {}
    arrays = [set(i) for i in arrays]

    d = {}

    arrays.pop()
    for i in arrays:
        i = set(i)
        for j in i:
            if 



    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
