while True:
    try:
        n = int(input())
        k = 1
        only_one = 1
        while True:
            if only_one % n == 0:
                print(k)
                break
            else:
                only_one *= 10
                only_one += 1
                k += 1
    except:
        break