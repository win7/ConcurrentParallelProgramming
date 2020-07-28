
t_s = [29.3398, 27.2986, 28.0637]
t_p = [17.9250, 19.2626, 21.6766]

promedio_t_s = sum(t_s) / len(t_s)
promedio_t_p = sum(t_p) / len(t_p)

speedup = promedio_t_s / promedio_t_p

print("Speepup: {}".format(speedup))