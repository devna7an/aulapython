import hashlib
import random
def criptografar(chave):
    #eu alterei o codigo
    a = random.randint(1, 100000000)
    crip=chave
    senha = crip[1] + str(a)
    objsenha = hashlib.sha512(senha.encode())
    hexsenha = objsenha.hexdigest()
    crip[1] = hexsenha
    return crip
def entrada():
    saida = []
    usuario = input("digite o seu nome")
    senha = input("digite a sua senha")
    saida.append(usuario)
    saida.append(senha)
    return saida
if __name__ == "__main__":
    print(criptografar(entrada()))
    
   
    
    
    
    
