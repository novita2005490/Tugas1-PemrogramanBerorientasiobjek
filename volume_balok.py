print('Program menghitung luas, volume, dan keliling balok')
p = int(input('masukan panjang balok: '))
l = int(input('masukan lebar balok: '))
t = int(input('masukan tinggi balok: '))
 

def volume(p,l,t):
    V = p * l * t
    return V
 
 
print('Jadi balok dengan ukuran panjang:{}, lebar:{}, tinggi:{} \nMempunyai volume:{} '.format(p,l,t,volume(p,l,t)))