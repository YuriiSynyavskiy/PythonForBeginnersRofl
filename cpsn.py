def count_positives_sum_negatives(arr):
    pos = [cnt for cnt in arr if cnt > 0]
    neg = [sm for sm in arr if sm < 0]
    return [len(pos), sum(neg)] if not arr == [] else []