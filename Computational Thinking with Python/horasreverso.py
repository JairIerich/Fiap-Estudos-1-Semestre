segundos = 87426

dias = segundos // (24 *3600)

segundosrest = segundos %(24 * 3600)

horas = segundosrest // 3600

minutos = segundosrest // 60

segundos2 = segundosrest %60

print(f"dias: {dias} horas: {horas} minutos: {minutos} segundos: {segundos2}")

