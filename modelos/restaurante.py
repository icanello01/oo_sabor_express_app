class restaurante:
    def __init__(self, nome=None, categoria=None):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

restaurante_praca = restaurante('Praça', 'Brasileira')
restaurante_pizza = restaurante('Pizzalia', 'Italiana')

restaurantes = [restaurante_praca, restaurante_pizza]

print (vars (restaurante_praca)) 
print (vars (restaurante_pizza))