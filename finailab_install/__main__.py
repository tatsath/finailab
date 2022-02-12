import os

def main():
    print("Running Jupyter platform!") 
    
    out =str.rstrip(os.popen('python -m site --user-site').read())

    str_out = ""     
    # traverse in the string  
    for ele in out: 
        str_out += ele   
  

    filename =  os.path.join(str_out, "finailab_install", "jupyter_notebook_config.py")

    filename2 = filename.replace(os.sep, '/')    

    os.system("jupyter lab --config=" + filename2)
    

if __name__ == "__main__":
    main()


def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 

