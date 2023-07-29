def mergeAlternately( word1 ="", word2=""):
        length = min(len(word1) , len(word2))
        result = ''
        for x in range(length):
                result+=word1[x]+word2[x]

        result += word1[length:]+word2[length:]        
        return result        


print(mergeAlternately('acegik' , 'bd'))