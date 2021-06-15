# PROGRAMA DE EJEMPLO PARA TRAER LAS ESTADISTICAS ACTUALES DE CASOS COVID EN EL MUNDO
# AUTOR : CESAR MAYTA
# VERSION : 1.0
# FECHA : 19/02/2021
import matplotlib.pyplot as plt
import urllib.request
import json
# peru - chile - argentina - colombia - ecuador - brazil - bolivia
datos = urllib.request.urlopen('https://api.covid19api.com/country/peru/status/confirmed?from=2020-03-01T00:00:00Z&to=2020-08-02T00:00:00Z').read().decode()
casos = json.loads(datos)

data = {}
cont = 1
for caso in casos:
    nuevoDato = {cont:caso['Cases']}
    data.update(nuevoDato)
    cont += 1   
print(data)

names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots()
axs.plot(names, values)
fig.suptitle('Casos confirmados de covid en Perú')
plt.show()