def topk(nums, k):
    if nums is None:
        return []
    if len(nums) == 0:
        return []
    if k > len(nums):
        return []
    if k <= 0:
        return []

    map = {}
    for num in nums:
        if num in map:
            map[num] = map[num]+1
        else:
            map[num] = 1

    result = []
    for m in map:
        result.append({'key': m, 'value': map[m]})

    def comp(x):
        return x['value']

    result.sort(key=comp, reverse=True)

    return[x['key'] for x in result][:k]

print(topk([1,2,3,1,5,5,5], 2))
