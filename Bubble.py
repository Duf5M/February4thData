def sort():
    for x in range(0, length-1):
        for y in range(x+1, length):
            if M[x] > M[y]:
                M[x], M[y] = M[y], M[x]
