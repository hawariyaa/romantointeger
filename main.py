
class sloution:
    def romantointerger(self,s : str )->int:
# besically this means the input is a string and the output is an interger
# if largest to smallest add them up
# if smallest to larges subtruct the samllest form the largest
# we are going to use a hash table
# you have to make sure to respect the constraint 
         roman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
                }

         result = 0
         for index in range(len(s)):
             if index + 1 < len(s) and roman[s[index]] < roman[s[index + 1]]:
                 if (s[index] == "I" and (s[index + 1] == "V" or s[index + 1] == "X")) or (s[index] == "x" and (s[index + 1] == "L" or s[index + 1] == "C")) or (s[index] == "C" and (s[index + 1] == "D" or s[index + 1] == "M")):
                       result -= roman[s[index]]
                 else:
                    return print("invalid number!")
             else:
                    result += roman[s[index]]

         return result

answer = sloution()
new = answer.romantointerger("DM")
print(new)

