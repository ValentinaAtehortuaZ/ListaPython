productos=[]
option=1


while(option !=0):
    producto={}
    option=int(input("Digite una option: "))
    if(option==1):
       producto['nombre']=input("Digite el nombre del producto")
       producto['codigo']=input("Digite el codigo del producto")
       producto['precio']=input("Digite el precio del producto")

       productos.append(producto)

    elif(option==2):
        print(productos)    
    elif(option==3):
        print("") 
    else: 
        print("")       