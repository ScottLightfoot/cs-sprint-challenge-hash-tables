def has_negatives(a):
    """
    YOUR CODE HERE
    """
    d = {}
    out = []
    for i in a:
        test = abs(i)
        # breakpoint()
        if abs(i) in d:
            out.append(abs(i))
        else:
            d[abs(i)] = 1
    return out



if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
