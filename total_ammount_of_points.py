def points(matches):
    total_points = 0
    for match in matches:
        x, y = match.split(":")
        x = int(x)
        y = int(y)
        if x > y:
            total_points += 3
        elif x == y:
            total_points += 1
    return total_points