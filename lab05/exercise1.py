chain = "X-DSPAM-Confidence:0.8475"

uno = chain.find(":")
print("Inicia en el Indice: "+ str(uno))

dos = chain.find("5")
print("Termina en: "+ str(dos))

last = len(chain)
substring = chain[uno+1:last]
tipo = float(substring)

print(tipo)
print(type(tipo))