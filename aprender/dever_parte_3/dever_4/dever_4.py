from modulos.humano import humano

humano = humano("Hiago", 16, 70, 170)

for i in range(humano.idade, 101):
    print(f"idade = {humano.idade} / altura = {humano.altura}")
    humano.envelhecer()

