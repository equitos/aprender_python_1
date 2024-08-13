#cria planilhas

from basic import *
import sqlite3
import os


class sql:
    def __init__(self, conexao):
        self.conexao = conexao
        self.cursor = self.conexao.cursor()

    def where_is(cursor, tabela, coluna, valor):
        achar = cursor.execute(f'''
        select 0
        from {tabela}
        where {coluna} = ?               
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
            '''),(valor, id,)
            cursor.connection.commit()

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
        for player in self.player:
            try:
                self.cursor.execute(f"""
                CREATE TABLE {player} (id TEXT PRIMARY KEY, {lista})
                """)
                self.conexao.commit()
            except:
                "erro de criação"




a = panilha(get_conexao.conexao_step(), get_lista_player())
a.new_panilha(get_lista_paramitos())
p = get_lista_player()
p = p[0]
cursor_a = a.get_curso()

sql.add_valor(cursor_a, p, 0, 'vida', 100)


