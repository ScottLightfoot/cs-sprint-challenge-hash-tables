# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    d = {}
    for i in files:
        f = i.split('/')
        if f[-1] in d:
            d[f[-1]].append(i)
        else:
            d[f[-1]] = [i]
    out = []
    for i in queries:
        if i in d:
            out.extend(d[i])

    return out


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
