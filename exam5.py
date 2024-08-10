def prime(x,y):
    prime_list = []
    for i in range(x,y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
                else:
                    prime_list.append(i)
    return prime_list

start_range = 2
end_range = 9

lst = prime(start_range, end_range)
if len(lst) == 0:
    print(" ")
else:
    print(" ", lst)