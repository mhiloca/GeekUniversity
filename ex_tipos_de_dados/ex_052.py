aposta1 = float(input('Valor aposta: '))
aposta2 = float(input('Valor aposta: '))
aposta3 = float(input('Valor aposta: '))
tot_aposta = aposta1 + aposta2 + aposta3
per_aposta1 = round(((100 * aposta1) / tot_aposta), 2)
per_aposta2 = round(((100 * aposta2) / tot_aposta), 2)
per_aposta3 = round(((100 * aposta3) / tot_aposta), 2)
premio = float(input('Valor prêmio: '))
apostador_1 = premio * (per_aposta1 / 100)
apostador_2 = premio * (per_aposta2 / 100)
apostador_3 = premio * (per_aposta3 / 100)
print(f'Fulano que apostou R${aposta1:.2f} receberá R${apostador_1:.2f}')
print(f'Siclano que apostou R${aposta2:.2f} receberá R${apostador_2:.2f}')
print(f'Berltrano que apostou R${aposta3:.2f} receberá R${apostador_3:.2f}')
