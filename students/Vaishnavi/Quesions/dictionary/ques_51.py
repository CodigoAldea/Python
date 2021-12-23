a = ["S001", "S002", "S003", "S004"] 
b = ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] 
c = [85, 98, 89, 92]

r= [{x : {y : z}} for (x,y,z) in zip(a,b,c)]
print ( r )