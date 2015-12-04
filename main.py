## CFG-Analyzer copyright (c) 2015 Gregory Gaston 
## MIT Liscense - See documentation at https://github/L0ntra/CFG-Analyzer

## Grammer Rules:
## 1. All runes must have a term. as the first char on the right hand side
## 2. No Var may have two rules with the same term. as the first symbol on 
##    the right hand side

## Encode the following languages:
## Have first line of the files be the languages of the grammer
## <<1>>
## {a^n#b^n | n > 0}
##  S: aAb
##  A: aAb | #
##
## <<2>>
## {w # (w^r) | w E{0,1)*}
## S: 0S0 | 1S1 | #
##
## <<3>>
## {(a^i)#(b^j)#(c^k)# | i = j and i, j, k > 0}
## S: aAb#cC
## A: aAb | #
## c: cC | #
##
## One other my choice


## Program functionality
## For grammer <<1>>
## String == aa#bb
## Push S
## Pop S
## PUSH aAb (top-> bottom)
## Pop a : remove 'a' from string : string == a#bb
## pop A
## push aAb (top-> bottom)
## pop a : remove 'a' from string : string == #bb
## pop A
## push #
## pop # : remove '#' from string : string == bb
## pop b : remove 'b' from string : string == b
## pop b : remove 'b' from string : string == ''
## Stack and string are empty : accept




import readfile

## Linear linked list used for stack
class lll:
  def __init__(self, data = None):
    self.data = data
    self.next_node = None
    if data == None:
      self.data = '$'

  def push(self, data):
    new_node = lll(data)
    new_node.next_node = self
    return new_node

  def pop(self):
    return (self.next_node, self.data)

  def print_all(self):
    print(self.data, end = ' ')
    if self.next_node:
      self.next_node.print_all()
    return None

def test():
  head = lll()
  i = 0
  print("\n<< Pushing Stack >>")
  while i < 10:
    head = head.push(i)
    print(i)
    i = i +1
  print("\n<< Stack Contents >>")
  head.print_all(); print()

  print("\n<< Popping Stack >>")
  while head:
    popped = head.pop()
    head = popped[0]
    print(popped[1])
  return


def main():

#  if input("Test?: ") == 'y':
#    test()

  accept = False
  while not accept:
    try:
      grammer_name, grammer = readfile.read_file(input("File name for grammer: "))
    except IOError:
      print("Invalid filename")
    else:
     accept = True

  verb = input("Verbouse Output? (y/n) ") == 'y'

  while 1:
    test_string = input('String to test: ')

    ##Push the string on to it's own stack
    input_string = lll()
    for i in range(len(test_string)-1, -1 , -1): ## this is kinda strange...
      input_string = input_string.push(test_string[i])

    stack = lll()
    stack = stack.push('S')
  
    if verb == True:
      print('Test String | Stack')
      input_string.print_all(); print('     ', end = ''); 
      stack.print_all(); print()
    while True:
      input_string, str_pop = input_string.pop()
      stack, stk_pop = stack.pop()
      s_result = None
      if(stk_pop != str_pop):
        s_result = grammer.search(stk_pop, str_pop)
        if s_result:
          for i in range(len(s_result)-1, 0, -1):#push all but first char
            stack = stack.push(s_result[i])
        else:
          good = False ##String is not part of language
          break
      if(stk_pop == str_pop) and (str_pop == '$'):
        good = True
        break
      if verb == True:
        input_string.print_all(); print('     ', end = ''); stack.print_all(); print()

    if good == True:
      print(test_string + ' is in the language of ' + grammer_name)
    else:
      print(test_string + ' is NOT in the language of ' + grammer_name)
    if input("Test another string? (y/n) ") != 'y':
      break





if __name__ == '__main__':
  main()
  
