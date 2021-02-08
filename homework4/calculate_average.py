def cal_ave(n):
    try:
        return sum(n)/len(n)
    except ZeroDivisionError:
        return "Empty list"
    except:
        return "Invalid input"