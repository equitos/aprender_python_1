import sqlite3
import os


class sqls:
    def __init__(self, conexao):
        self.conexao = conexao
        self.cursor = self.conexao.cursor()

    def sql_achar_valor_nome(self, valor, coluna):

        sql_achar = f"""
            select 0
            from dados_palavras
            where {coluna} = ?
            """

        resutado = self.cursor.execute(sql_achar, [valor])
        resutado = resutado.fetchall()
        print(resutado)
        if resutado not in [[], []]:
            return True
        else:
            return False


    def sql_colocar_valores(self,palavra, key, valor):
        achar = self.sql_achar_valor_nome(palavra, "palavra")
        print(achar)
        if achar == False:
                self.sql_colocar_valor = f"""
                insert into dados_palavras
                ({key}, n_palavras, palavra)
                values (?, ?, ?)
                """
                self.cursor.execute(self.sql_colocar_valor, (valor, 1, palavra))
        else:
            self.sql_colocar_valor = f"""
                update dados_palavras
                set {key} = ?
                where palavra = ?
                """
            self.cursor.execute(self.sql_colocar_valor, (valor, palavra))


        self.conexao.commit()


class dado_palavra:
    def __init__(self):
        self.conexao = sqlite3.connect('dados_palavras.db')
        self.cursor = self.conexao.cursor()
        try:
            self.cursor.execute("""CREATE TABLE dados_palavras (palavra TEXT PRIMARY KEY, n_palavras int,
                a INTEGER DEFAULT 0, b INTEGER DEFAULT 0, c INTEGER DEFAULT 0, d INTEGER DEFAULT 0, 
                e INTEGER DEFAULT 0, f INTEGER DEFAULT 0, g INTEGER DEFAULT 0, h INTEGER DEFAULT 0, 
                i INTEGER DEFAULT 0, j INTEGER DEFAULT 0, k INTEGER DEFAULT 0, l INTEGER DEFAULT 0, 
                m INTEGER DEFAULT 0, n INTEGER DEFAULT 0, o INTEGER DEFAULT 0, p INTEGER DEFAULT 0, 
                q INTEGER DEFAULT 0, r INTEGER DEFAULT 0, s INTEGER DEFAULT 0, t INTEGER DEFAULT 0, 
                u INTEGER DEFAULT 0, v INTEGER DEFAULT 0, w INTEGER DEFAULT 0, x INTEGER DEFAULT 0, 
                y INTEGER DEFAULT 0, z INTEGER DEFAULT 0)""")
            self.conexao.commit()
        except:
            "nan"
    def add_palavra(self, palavra):
        dic_palavra = palavras().dic_palavra(palavra)

        achar = sqls(self.conexao).sql_achar_valor_nome(palavra, "palavra")
        print(f"achar 1 = {achar}")
        if achar == False:
            for k, i in dic_palavra.items():
                try:
                    sqls(self.conexao).sql_colocar_valores(palavra, k, i)

                except TypeError as e:
                    print(f"error: {e}")

class palavras:
    def __init__(self):
        self.letras = "abcdefghijklmnopqrstuvwxyz"
    def dic_palavra(self, palavra):
        dic = {}
        palavra = palavra.lower()
        for i in palavra:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        return dic


a = dado_palavra()
a.add_palavra('palavras')
a.add_palavra('hiago')
a.add_palavra('rafael')
#a.add_palavra('palavras')
#a.add_palavra('palavras')
#a.add_palavra('Hiago')