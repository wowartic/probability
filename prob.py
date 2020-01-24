def probability(prob, times):
    count = 100 - ((prob ** times) * 100)
    print(count)


prob = 0.98
times = 100

probability(prob, times)
