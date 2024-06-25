fruits = ["apple", "orange", "apple", "mango", "banana", "apple"]
uniquefruits = set(fruits)
print(uniquefruits)

overseafruits = {"apple", "orange", "mango", "banana", "grapes"}
localfruits = {"durian", "rambutan", "cempedak", "banana", "mogosteen"}
print(overseafruits.union(localfruits))
print(overseafruits.intersection(localfruits))
print(overseafruits.difference(localfruits))

fruits = ["apple", "orange", "apple", "mango", "banana", "apple"]
uniquefruits = set(fruits)
print(uniquefruits)

overseafruits = {"apple", "orange", "mango", "banana", "grapes"}
localfruits = {"durian", "rambutan", "cempedak", "banana", "mogosteen"}
print(overseafruits.union(localfruits))
print(overseafruits.intersection(localfruits))
print(overseafruits.difference(localfruits))

favoritefruits = {"durian", "rambutan", "mangosteen"}
print(favoritefruits.issubset(localfruits))
print(localfruits.issuperset(favoritefruits))
print(favoritefruits.isdisjoint(overseafruits))

emailcontent = """n a larger sense, the civil rights movement in the United States refers to the long history of social and political activity seeking full civil rights and legal equality for all Americans, although usually the term focuses on the struggle for racial equality for African Americans.  Milestone Supreme Court rulings include Plessy v. Ferguson in 1896, which upheld “separate but equal” racial segregation, and Brown v. Board of Education in 1954, which overturned the earlier decision.  Brown v. Board of Education opened the door for the major civil rights activities of the 1950s and 1960s, as well as major legislative achievements such as the Civil Rights Act of 1964, the Voting Rights Act of 1965, and the Fair Housing Act of 1968."""

words = emailcontent.split()
print(len(words), "total")

word_set = set(words)
print(len(word_set), "unique")

print(f"difference:{len(words) - len(word_set)}")

cleanwords = []
for word in words:
    word = word.replace(".","") #method replace takes 2 argument, first find, second is to replace
    word = word.replace(",","")
    word = word.lower()
    cleanwords.append(word)

unique_w = set(cleanwords)
print(unique_w)
print(len(unique_w),"unique clean words")
    
