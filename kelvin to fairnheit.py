k=int(input())
f=0
try:
    if k<0:
        raise Exception
    else:
        f=((k-273.15)*(9/5))+32
except Exception:
    f="VERY COOL! \nENTER THE TEMPRATURE ABOVE 0 KELVIN"
finally:
    print(f)