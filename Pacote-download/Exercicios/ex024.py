"""city = input('Digite el nombre de una ciudad: ')
if city[0].upper == 'SANTO':
    print('El nombre de su ciudad empieza con "SANTO"')
else:
    print('El nombre de su ciudad no empieza con "SANTO"')"""

city = str(input('Digite el nombre de una ciudad: ')).strip()
print(city[:5].upper() == 'SANTO')