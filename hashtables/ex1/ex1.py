def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    out = None
    for i in range(length):
        if limit - weights[i] in weights[i+1:]:
            return([weights[i+1:].index(limit-weights[i]) + i + 1, i])


    return None
