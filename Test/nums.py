def modify(**kw):
    print(kw)
    kw['city'] = 'hello'
    kw['job'][0] = 100

nums = [3, 2, 1]
extra = {'city': 'Beijing', 'job': nums}

modify(**extra)
print(extra)
print(nums)
