def sort():
    for i in range(0, length):
        min_pos = i
        for j in range(i + 1, length):
            if M[j] < M[min_pos]:
                min_pos = j
        M[min_pos], M[i] = M[i], M[min_pos]
