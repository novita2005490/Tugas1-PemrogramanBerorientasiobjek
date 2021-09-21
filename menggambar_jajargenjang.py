n= input ("masukkan panjang : ")
tinggi= int( input ("masukkan tinggi:") )
a=1
while a<= tinggi:
        for i in range (1,n+1):
            if i==1:
                print (" " * (a+"*"))
                print ("*")
        else :
                print ("\n") 
a= a+1