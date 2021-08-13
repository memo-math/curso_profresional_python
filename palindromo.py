
def is_palindrome(string: str) -> bool:
    """ Regresa el booleano que representa si la cadena de caracteres
    ingresada es palindromo o no """
    string = string.replace(" ", "").lower()
    return string == string[::-1]

def run():
    print(is_palindrome(1000)) #va aventar error con mypy

if __name__=='__main__':
    run()
