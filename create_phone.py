def create_phone_number(n):
    return f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"


def create_phone_number(n):
    f = "".join(map(str, n[0:3]) )
    s = "".join(map(str, n[3:6]) )
    t = "".join(map(str, n[6:10]) )
    return "("+f+") "+ s +"-"+t