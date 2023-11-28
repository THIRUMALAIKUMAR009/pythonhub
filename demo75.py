try:
    a=int(input())
    b=int(input())
except valueError as e:
    print("value Error",e)  
except Exception:
    print("something Worng")
finally:
    print("Done")
