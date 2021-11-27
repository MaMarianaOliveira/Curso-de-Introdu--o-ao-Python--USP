segundos_str = input("Por favor, coloque o número de segundos que deseja converter:")
total_segs = int(segundos_str)

dia = total_segs // 86400
segs_dia = total_segs % 86400

hora = segs_dia // 3600
segs_rest = segs_dia % 3600
minutos = segs_rest // 60
segs_rest_final = segs_rest % 60


print ( dia, "dia (s)" , hora, "horas," , minutos, "minutos e ", segs_rest_final, "segundos.")