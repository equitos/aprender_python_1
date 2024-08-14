#cria planilhas

import sqlite3
import os


class sql:
    def __init__(self, conexao):
        self.conexao = conexao
        self.cursor = self.conexao.cursor()

    def where_is(cursor, tabela, key, valor):
        achar = cursor.execute(f'''
        select 0
        from {tabela}
        where {key} = ?               
        ''', (valor,))

        achar = achar.fetchall()

        for i in achar:
            achar = True
            break
        if achar != True:
            achar = False

        return achar

    def add_valor(cursor, tabela, id, key, valor):

        achar_ = sql.where_is(cursor, tabela, 'id', id)

        if achar_ == False:
            cursor.execute(f'''
            INSERT INTO {tabela} (id) VALUES (?)
            ''', (id,))
            cursor.connection.commit()
        else:
            cursor.execute(f'''
            update {tabela}
            set {key} = ?
            where id = ?               
            ''',(valor, id,))
            cursor.connection.commit()
        
    def get_valor(cursor, tabela, id, key):
        valor = cursor.execute(f'''
        select 0
        from {tabela}
        where {key} = ?               
        ''', (valor,))

        valor = valor.fetchall()
        valor = valor[0]
        print(valor)


class panilha:        
    def __init__(self, conexao, player):
        self.player = player
        self.conexao = sqlite3.connect(conexao)
        self.cursor = self.conexao.cursor()

    def get_curso(self):
        return self.cursor
    
    def get_conexao(self):
        return self.conexao

    def new_panilha(self, lista):
        if lista != 'nan':
            for player in self.player:
                try:
                    self.cursor.execute(f"""
                    CREATE TABLE {player} (id TEXT PRIMARY KEY, {lista})
                    """)
                    self.conexao.commit()
                except:
                    "erro de criação"

