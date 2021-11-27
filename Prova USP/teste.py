segundos_str= int (input("Por favor, entre com o número de segundos que deseja converter:"))

dia= segundos_str // 86400
segs_dia= segundos_str % 86400

hora= segs_dia // 3600
segs_rest= segs_dia % 3600
minutos= segs_rest // 60
segs_rest_final= segs_rest % 60

print(dia,"dias",hora,"horas,",minutos,"minutos e",segs_rest_final,"segundos.")