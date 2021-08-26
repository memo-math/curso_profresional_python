
def make_repeater_of(n):

    def repeater(string):
        assert type(string) == str, "Solo puedes utilizar cadenas"
        return string*n
    
    return repeater

def run():
    repeat5 = make_repeater_of(5)
    repeat2 = make_repeater_of(2)
    print(repeat5('Memo'))
    print(repeat2('perro'))

if __name__=='__main__':
    run()