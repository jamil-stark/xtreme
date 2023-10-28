test_input = input()
n, m = map(int, test_input.split('\n')[0].split(' '))
dictionary = []
for i in range(n):
    dictionary.append(input())

blended = []
for i in range(m):
    blended.append(input())

prefixes = {}
suffixes = {}
for word in dictionary:
    for i in range(3, len(word)):
        prefix = word[:i]
        suffix = word[-i:]
        if prefix not in prefixes:
            prefixes[prefix] = []
        if suffix not in suffixes:
            suffixes[suffix] = []
        prefixes[prefix].append(word)
        suffixes[suffix].append(word)
    
    if len(word) == 3:
        prefix = word[:3]
        suffix = word[-3:]
        if prefix not in prefixes:
            prefixes[prefix] = []
        if suffix not in suffixes:
            suffixes[suffix] = []
        prefixes[prefix].append(word)
        suffixes[suffix].append(word)

for word in blended:
    prefix = word[:3]
    suffix = word[-3:]
    if prefix not in prefixes or suffix not in suffixes:
        print('none')
    elif len(prefixes[prefix]) > 1 or len(suffixes[suffix]) > 1:
        print('ambiguous')
    else:
        print(prefixes[prefix][0], suffixes[suffix][0])
