capacity = 3
cache = {}
order = []


def put(key, value):
    global order
    if key in cache:
        cache[key] = value

        i = order.index(key)
        order = order[:i] + order[i+1:]
        order = [key] + order

    else:
        if len(cache) == capacity:
            old = order[-1]
            del cache[old]
            order = order[:-1]

        cache[key] = value
        order = [key] + order


def get(key):
    global order
    if key not in cache:
        return -1

    print(cache[key])

    i = order.index(key)
    order = order[:i] + order[i+1:]
    order = [key] + order

    print(order)


put(1, 10)
put(2, 20)
put(3, 30)

get(1)
get(1)

put(3, 40)

get(3)