#Merge two dictionaries.

dict1 = {  'richu': 5, 'ammu': 7, 'Joy' : 10 }
dict2 = {'Aadil': 8,'ammu': 20,'Mark' : 11 }
dict3 = {**dict1 , **dict2}
print(dict3)