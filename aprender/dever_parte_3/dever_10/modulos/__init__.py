class carro:
    def __init__(self, km_litro, tanque_max, litro_no_tanque=0):
        self._km_litro = km_litro
        self._tanque_max = tanque_max
        self._litro_no_tanque = litro_no_tanque

        if self._litro_no_tanque > self._tanque_max:
            print("\033[31mERRO NOS PARAMETOS CARRO\033[m")
            exit()

    def nivelTanque(self):
        print(self._litro_no_tanque)

    def abastecer(self, n_litros):
        total_litros = self._litro_no_tanque + n_litros
        if total_litros > self._tanque_max:
            print("seu tanque não cabe essa quantidade de litros")
        else:
            self._litro_no_tanque = total_litros

    def ver_carro(self):
        print(f"km por litro: {self._km_litro}")
        print(f"maximo do tanque: {self._tanque_max}")
        print(f"litros no tanque: {self._litro_no_tanque}")

    def ver_tanque(self):
        return self._litro_no_tanque

    def andar(self, km):
        litros_total = self._km_litro * km
        if litros_total > self._litro_no_tanque:
            print("não tem combutivel o suficiente")
        else:
            print(f"seu carro gastou {litros_total} litros")
            self._litro_no_tanque - litros_total

