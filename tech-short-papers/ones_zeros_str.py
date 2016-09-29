'''
Given a string of letters, implement method that outputs string of 1's and 0's
of the same size corresponding to if a selected letter is in that position in
the input string. 
'''



def ones_zeros_str(string, selected_letter):
    """ ones_zeros_str """  # doc string ones_zeros_str.__doc__
    lst_hold = []
    for i in string:
        if i == selected_letter:
            #print(1)
            lst_hold.append('1')
        else:
            #print(0)
            lst_hold.append('0')
    output = ''.join(lst_hold)
    print(str(output))
          
string = "hello world my name is jasmine dumas"
selected_letter = "e"

ones_zeros_str(string, selected_letter)
