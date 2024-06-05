from collections import Counter
def frequencySort(s: str) -> str:
    freq = Counter(s)
    
    sorted_char = sorted(freq.items(), key = lambda x: x[1],reverse=True)
    
    return "".join([key * val for key,val in sorted_char])

print(frequencySort("banana"))

st = "banana"
freq_of_char = Counter(st)
print(freq_of_char)
dict_of_tuple_pair = freq_of_char.items()
print(dict_of_tuple_pair)
sorted_char = sorted(dict_of_tuple_pair, key = lambda x: x[1],reverse=True)    
print(sorted_char)
res = "".join([key * val for key,val in sorted_char])
print(res)