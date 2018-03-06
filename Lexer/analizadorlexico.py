import ply.lex as lex
import re
import codecs
import os
import sys



reservadas =['EMPEZAR','FIN','SI','ENTONCES','MIENTRAS','HAGA','LLAMADO','CONSTANTE','VARIABLE','PROCEDIMIENTO','SALIDA','ENTRADA','SINO']

tokens = reservadas+['IDENTIFICADOR','NUMERO','SUMA','MENOS','MULT','DIVISION','ODD','ASIGNACION','DIFERENTE','MENOR','MENORIGUAL','MAYOR','MAYORIGUAL','PARENTIZQ','PARENTDER','COMA','PUNTOYCOMA','PUNTO','ACTUALIZAR'] 



t_ignore = '\t'
t_SUMA =  r'\+'
t_MENOS = r'\-'
t_MULT = r'\*'
t_DIVISION = r'/'
t_ODD = r'ODD'
t_ASIGNACION = r'<-'
t_DIFERENTE = r'<>'
t_MENOR = r'<'
t_MENORIGUAL = r'<='
t_MAYOR = r'>'
t_MAYORIGUAL = r'>='
t_PARENTIZQ = r'\('
t_PARENTDER = r'\)'
t_COMA = r','
t_PUNTOYCOMA = r';'
t_PUNTO = r'\.'
t_ACTUALIZAR = r':='


def t_IDENTIFICADOR(t):
    r'[[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
    return t


#reconocer y obviar comentarios
def t_COMENTARIO(t):
    r'\#.*'
    pass

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return (t)

def t_newline(t):
    r'\n+'
    #t.lexer.lineno += len(t.value)

def t_error(t):
    print ("Caracter Ilegal'%s'" % t.value[0])
    t.lexer.skip(1)


    




fp = codecs.open("archivo.alexis","r","utf-8")
cadena = fp.read()
fp.close()

analizador = lex.lex()
analizador.input(cadena)

while True:
    tok = analizador.token()
    if not tok : break
    print (tok)

    
