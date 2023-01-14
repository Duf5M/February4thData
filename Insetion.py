def sort():
    for i in range(1, length):
        position = i
        current = M[i]
        while position > 0 and M[position - 1] > current:
            M[position] = M[position - 1]
            position -= 1
        M[position] = current
