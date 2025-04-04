# Programa de MicroSev

import sqlite3
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.post("/incluir_produto")
def adicionar_produto():
    return {"produto"}

@app.get("/consultar_estoque")
def revisar_estoque():
    #try:
    con = sqlite3.connect("/home/ijovem02/hackers/database/mercado.db")
    cur = con.cursor()
    cur.execute(" select id, codigo, nome, quantidade from produtos  "  )
    rows=cur.fetchall()
    con.close
    return {rows}
    #except:
        #return False

    
@app.put("/alterar_produto")
def alterar_produto(id: int,codigo: str, nome:str):
    try:
        con = sqlite3.connect("/home/ijovem02/hackers/database/mercado.db")
        cur = con.cursor()
        cur.execute(""" update  produtos set codigo=?, nome=? where id=?  """ ,   (codigo, nome, id ) ) 
        con.commit()
        con.close
        return {True}
    except:
        return False

