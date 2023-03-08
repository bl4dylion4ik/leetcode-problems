from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    d = {}
    for i in nums:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1

    bucket_list = [[] for i in range(len(nums))]

    print(d)

    # store the numbers in the bucket list using the count as the index
    for num, count in d.items():
        bucket_list[count - 1].append(
            num)  # we subtract 1 since, the smallest index in our list "0" corresponds to the smallest possible count which is "1"
    print(bucket_list)

    # unpack the bucket list into a new list
    results = []
    for bucket in bucket_list:
        results.extend(bucket)

    print(results)

    # fetch the top k elements by iterating through the list in reverse (since we want the max count)
    topk = []
    for i in range(-1, -(k + 1), -1):  # we add 1 to k, since we k+1 will not be included
        topk.append(results[i])
    return topk
    # return list({k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}.keys())[:k]


print(topKFrequent(nums = [1,1,1,2,2,3, 2, 4], k = 2))