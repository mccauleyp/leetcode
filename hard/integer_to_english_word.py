'''
https://leetcode.com/problems/integer-to-english-words/
273. Integer to English Words
Hard

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"

Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
'''
class Solution:
    import re
    def numberToWords(self, num: int) -> str:
        def one_digit(num):
            digits = {'0':'', '1':'One', '2':'Two', '3':'Three', \
                      '4':'Four', '5':'Five', '6':'Six', '7':'Seven', \
                      '8':'Eight', '9':'Nine'}
            return digits[num]
        
        def two_digits(num):
            teens = {'10':'Ten', '11':'Eleven', '12':'Twelve', \
                     '13':'Thirteen', '14':'Fourteen', '15':'Fifteen', \
                     '16':'Sixteen', '17':'Seventeen', '18':'Eighteen', \
                     '19':'Nineteen'}
            tens = {'1':'', '2':'Twenty', '3':'Thirty', '4':'Forty', '5':'Fifty', \
                     '6':'Sixty', '7':'Seventy', '8':'Eighty', '9':'Ninety'}
        
            if num[0] == '0' or len(num) == 1:
                return one_digit(num[-1])
            else:
                if int(num) <= 19:
                    return teens[num]
                else:
                    return (tens[num[0]]+' '+one_digit(num[1])).strip()
        
        def three_digits(num):
            if len(num) == 1:
                return one_digit(num)
            elif num[0] == '0' or len(num) == 2:
                return two_digits(num[-2:])
            else:
                return (one_digit(num[0]) + ' Hundred ' + two_digits(num[1:])).strip()
        
        str_num = str(num)
        if str_num == '0': return 'Zero'
        
        powers_of_three = {0:'', 1:'Thousand', 2:'Million', 3:'Billion'}
        
        offset = len(str_num) % 3 
        if offset > 0:
            groups = [str_num[0:offset]] + re.findall("[0-9]{3}", str_num[offset:])
        else:
            groups = re.findall("[0-9]{3}", str_num)
        groups.reverse()
                
        output = '' 
        for i, group in enumerate(groups):
            append = three_digits(group)
            if append:
                output = three_digits(group)+' '+powers_of_three[i]+' '+output
            
        return output.strip()