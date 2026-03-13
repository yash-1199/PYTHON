def read_file(fileName):
    with open(fileName,'r')  as f:
        return f.read()

def write_file(fileName,text):
    with open(fileName,'w') as f:
         f.write(text)

def append_file(fileName,text):
    with open(fileName,'a') as f:
         f.write(text)

def count_lines(fileName):
    with open(fileName,'r') as f:
       return len(f.readlines())
    

