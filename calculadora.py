def somar(a: int, b: int) -> int:
#Função que recebe dois números inteiros e retorna sua soma.
  
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Ambas as entradas devem ser números inteiros.")
    return a + b
