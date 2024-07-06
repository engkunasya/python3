def isogram(sentence_split):
    alpha_list = list(map(list, sentence_split))
    alpha_set = list(map(set, sentence_split))
    
    not_iso = []
    _iso = []
    for i in range (len(alpha_list)):

            
            if len(alpha_list[i]) != len(alpha_set[i]):
                not_iso.append(["".join(alpha_list[i]) + " is not isogram."])

            else:
                 _iso.append(["".join(alpha_list[i]) + " is isogram."])
            

    return not_iso + _iso

   


sentence_split = input("Please enter the phrase: ").strip().upper().replace("-","").split()
print(isogram(sentence_split))

