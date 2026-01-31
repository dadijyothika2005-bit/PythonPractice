def merge_dicts_strings(a, b):
    merged = a.copy()  
    for key, value in b.items():
        if key in merged:
            merged[key] += value  
        else:
            merged[key] = value
    return merged
a = {'x': 'Hello ', 'y': 'World'}
b = {'y': '!', 'z': 'Python'}
print(merge_dicts_strings(a, b))


