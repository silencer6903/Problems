def topKFrequent(nums: list[int], k: int) -> list[int]:
    res = {}

    for i, v in enumerate(nums):
        res[v] = res.setdefault(v, 0) + 1  # Add count values to dict with nums list keys

    return   [*dict(sorted(res.items(), key=lambda s: s[1], reverse=True)).keys()][:k] #Convert to convert to convert...


s= [1,1,1,2,2,3]
print(topKFrequent(s, 2))
