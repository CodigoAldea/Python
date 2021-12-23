from collections import defaultdict
a = {
  'Ora Mckinney': 8,
  'Theodore Hollandl': 7,
  'Mae Fleming': 7,
  'Mathew Gilbert': 8,
  'Ivan Little': 7,  
}

b = defaultdict(list)

for i,j in a.items():
    b[j].append(i)
print(b)