#MontyPythonErrorListener.py

# Clase para tratar erros de sintaxe durante o parse do código Monty Python
from antlr4.error.ErrorListener import ErrorListener # Importar a interface ErrorListener

class MontyPythonErrorListener(ErrorListener): # Definimos a classe herdando de ErrorListener
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e): # Sobrescrever o método para tratamento de erros
        print(f"Erro de Sintaxe na linha {line}:{column} - {msg}") # Exibimos mensagem de erro
