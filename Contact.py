#x=open("C:\\Users\\DELL PC\\Desktop\\Python playground\\ContactBook\\CONTACT-Book.txt","x")

def cBookadd(c_name,c_phno):
    cb_add=open("C:\\Users\\DELL PC\\Desktop\\Python playground\\ContactBook\\CONTACT-Book.txt","a")
    
    cb_add.write( "\n",c_name+": "+str(c_phno))
    cb_add.close()


def cBook_read():
    c_open=open("C:\\Users\\DELL PC\\Desktop\\Python playground\\ContactBook\\CONTACT-Book.txt","r")
    for lines in c_open.readlines():
        print(lines)
    c_open.close()


def cSerch(line):
     n=1
     
     c_opens=open("C:\\Users\\DELL PC\\Desktop\\Python playground\\ContactBook\\CONTACT-Book.txt","r")
     if n==1:
        for lines in c_opens:
            l=len(lines)
            if (line in lines) and (len(line)==(l-13)) :
                print(lines)
                n-=1
            

     else:
        c_opens.close()
        print("S")
           
        
            
        
            
     
    
     
     




   
        
         

     







user_Choice=input("Want to 'Add-contact' OR 'Read-Contact' (add or read): ").lower()
if user_Choice=="add":
    c_name=input("Enter the name :")
    c_phno=int(input("Enter the phno:"))
    cBookadd(c_name,c_phno)
elif user_Choice=="read":
    cBook_read()
elif user_Choice=="serch":
    line=input("Enter the name: ")
    cSerch(line)