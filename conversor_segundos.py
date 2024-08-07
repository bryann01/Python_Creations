print("bem vindo(a)", end="\n")
print ("~" * 55)

segundos = input("Digite alguns segundos: ")
segundos_total = int(segundos)

semanas = segundos_total // 604800
horas = segundos_total // 3600
segundos_restantes = segundos_total % 3600
minutos = segundos_restantes // 60
segundos_fim = segundos_restantes % 60

print(segundos_total, "segundos", semanas, "semanas", horas, "horas", minutos, "minutos", segundos_fim, "segundos")
print("fim do programa", end="\n" + "~" * 55)

