A function that will write a text file to your PC with your name:
  
#!/usr/bin/env python3

def put_a_name_to_file():
    f = open("name.txt" , "w+")
    f.write("Mehak Preet Singh")
    f.close()
    
if __name__ == "__main__":
    put_a_name_to_file()
