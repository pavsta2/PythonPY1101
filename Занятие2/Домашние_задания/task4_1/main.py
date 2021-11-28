def len_points(pts: list) -> iter:
   for i in range(len(pts)-1):
       yield ((abs(pts[(i+1)][0] - pts[i][0])) ** 2 + (abs(pts[(i+1)][1] - pts[i][1])) ** 2) ** 0.5

def tasr_2(pts):

    return list(len_points(pts))


def tasr(pts):
    sum = 0
    for p in len_points(pts):
        sum += p
    return sum

if __name__ == "__main__":
    pts = [
        (3, 4),
        (4.5, 3),
        (2.1, -1),
        (6.8, -3),
        (1.4, 2.9)
    ]

    print(tasr(pts))
    print(tasr_2(pts))
    a = (i for i in range(1,10))
    print(next(len_points(pts)))

    my_gen = len_points(pts)
    print(next(my_gen))
    print(next(my_gen))


    print(type(len_points(pts)))
    print(next(len_points(pts)))
    print(next(len_points(pts)))