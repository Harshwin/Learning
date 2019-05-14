
def permute(letters):
    if len(letters) == 0:
        return ''
    else:
        permutations = ''
        for idx in range(len(letters)):
            otherPermutations = permute(letters[:idx] + letters[idx+1:])
            permutations += letters[idx] + otherPermutations

            #####
            # for (int j=0; j < otherPermutations.length(); j=j+inputs.length()-1)
            # allPermutations.add(otherPermutations.substring(j, j+inputs.length()-1))
            # if (allPermutations.size() == 0)
            #     permutations = inputs.charAt(i) + "";
            # for (String p: allPermutations)
            #     permutations = permutations + inputs.charAt(i) + p + "";
            ######

            # allpermuations = []
            # for j in range(0,len(otherPermutations )):
            #     allpermuations.append(otherPermutations[j:j+letters.__len__() -1])
            #
            # if allpermuations.__len__() == 0:
            #     permutations = letters[idx]
            # # for p in allpermuations:
            # #     permutations += letters[idx] + p
        return permutations




word = '123'
permutedString = permute(word)
print(permutedString)


