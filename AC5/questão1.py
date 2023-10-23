def progressão_númerica(n):
    for x in range(1 ,n + 1):
        print(x , fim = "\n")
        if x == n:
            break
        else:
            for y in range(1 , n + 1):
                if x >= y:
                    print(y, fim= "")

progressão_númerica(20)
