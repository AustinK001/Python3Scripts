def rotate(): 
    array = [1,23,423,234]
    return [list(x) for x in zip(*array)[::-1]]
