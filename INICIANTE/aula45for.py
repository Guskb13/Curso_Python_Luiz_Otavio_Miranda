"""
Iteravel -> str, range, etc (__iter__)
Iterador -> quem sabe entrefgar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
texto = 'Luiz' #iteravel
iterador = iter(texto) #iterador

while True:    
    try:
        print(next(iterador))
    except StopIteration:
        break

