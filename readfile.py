class g_lll:
  ##creates a new node, also pushes if head given
  def __init__(self, var, right, head = None):
    self.next_node = None
    self.var = var
    self.right = right
    if head:
      self.next_node = head
    return

  def print_all(self):
    print("'" + self.var + "'  '" + self.right + "'")

    if self.next_node:
      self.next_node.print_all()


def read_file(file_name):
  f = open(file_name)
  grammer_name = f.readline()
  line = f.readline()
  start = 0
  head = None
  while line:
    var = line[0]
    start = 3
    for i in range(2, len(line)):
      if line[i] == '|' or i+1 == len(line):
        head = g_lll(var, line[start:i], head)
        start = i+2
    line = f.readline()
#  head.print_all()
  f.close()
  return head

def main():
  #print('anbn')
  anbn = read_file('anbn.txt')

  #print('\n\n palendrome')
  palen = read_file('palendrome.txt')

  #print('\n\n aibjck')
  abc = read_file('aibjck.txt')

if __name__ == '__main__':
  main()








