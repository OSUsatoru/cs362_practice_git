def cal_cube(n):
    try:
        if n>=0:
            return n*n*n
        else:
            return "Negative value"
    except:
        return "Invalid input"