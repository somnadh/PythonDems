def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

print("First Call",add(12,14,18))
print("second Call",add(14,7858,158,12,14,18))