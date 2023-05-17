# stuff to run always here such as class/def
def sum(a,b) :
    s = a + b
    print(s)
    return s

def main():
    pass

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   sum(3,4)
   main()


