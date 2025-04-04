def subtrair(b1,b2):
    return(b1-b2)

def somar(n1,n2):
    return(n1+n2)
    
    
def menu():
   
    print("1-somar ")
    print("2-subtrair ")
    print("3-multiplicar ")
    print("4-dividir ")
    print("5-sair ")
    try: 
        b = int(input("digite sua opção "))
        return b
    except:
        return 0
        

if __name__ == "__main__":
     while True:
          r=menu()
          if r == 0:
              print("opção invalida ")
          if r == 5: 
              break
          if r == 1:
              a = int(input("digite valor de n1 "))
              c = int(input("digite valor de n2 "))
              print(somar(a,c))
          if r == 2:
              b = int(input("digite valor de b1 "))
              c = int(input("digite valor de b2 "))
              print(subtrair(b,c))
          
               
            
              
          

