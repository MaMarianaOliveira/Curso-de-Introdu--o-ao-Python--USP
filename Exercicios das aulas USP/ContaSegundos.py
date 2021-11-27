segundos_str = input("Por favor, coloque o número de segundos que deseja converter:")
total_segs = int(segundos_str)

hora = total_segs // 3600
segs_rest = total_segs % 3600
minutos = segs_rest // 60
segs_rest_final = segs_rest % 60


print ( hora, "horas," , minutos, "minutos e ", segs_rest_final, "segundos.")