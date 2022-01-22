colors = ['black', 'white']
sizes = ['S', 'M', 'L']

for result in (f'{c},{s}' for c in colors for s in sizes):
    print(result)