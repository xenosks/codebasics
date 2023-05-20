def digital_root(n):
    x = sum(int(i) for i in str(n))
    if x > 9:
       return digital_root(x)
    else:
        return x


def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))