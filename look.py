def reverse_lookup(data, target):
    results = []
    for k, v in data.items():
        if v == target:
            results.append(k)
    return results
my_dict = {'saif':'I1','venky':'A2','sagar':'h7'}
print(reverse_lookup(my_dict, 'h7'))
