data = {'name': 'Jordan',
        'age': 12,
        'job': 'pyton programmer'}
print(data['name'], data['job'])
print('')

data = {'name': ['Jordan','Pavel'],
        'age': (12,21),
        'job': 'pyton programmers'}
print(data['name'][0], data['job'][-1])