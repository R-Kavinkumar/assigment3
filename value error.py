try:
    value=int(input())
    if value>100:
        raise ValueError
    else:
        out="without any error"
except ValueError:
    print("the number should be less than 100")
    out="with a error"
finally:
    print("the programm was processed succesfully",out)