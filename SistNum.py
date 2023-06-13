def baseChanger_dec_all(num, base):
    if num == 0:
        return "0"

    digitos_base = []

    while num > 0:
        residuo = num % base
        digitos_base.append(str(residuo))
        num = num // base

    return "".join(digitos_base[::-1])  

def baseChanger_dec_bin(num):
    return baseChanger_dec_all(num,2)

def baseChanger_dec_hex(num):
    return baseChanger_dec_all(num,16)

def baseChanger_dec_oct(num):
    return baseChanger_dec_all(num,8)


#Pasaje de Cualquier Base a Decimal

def baseChanger_all_dec(num, base):
    digitos = list(str(num))
    digitos.reverse()
    resultado = 0
    for i in range(len(digitos)):
        valor = int(digitos[i], base)
        resultado += valor * (base ** i)

    return resultado

def baseChanger_bin_dec(num):
    return baseChanger_all_dec(num,2)

def baseChanger_hex_dec(num):
    return baseChanger_all_dec(num,16)

def baseChanger_oct_dec(num):
    return baseChanger_all_dec(num,8)


#Pasaje de Binario a Octal y Hexadecimal

def baseChanger_bin_to_oct_and_hex(num,base):
    if base==8:
        return baseChanger_dec_oct(baseChanger_bin_dec(num))
    elif base==16:
        return baseChanger_dec_hex(baseChanger_bin_dec(num))  

def baseChanger_bin_oct(num):
    return baseChanger_bin_to_oct_and_hex(num,8)

def baseChanger_bin_hex(num):
    return baseChanger_bin_to_oct_and_hex(num,16)


#Pasaje de Octal a Binario y Hexadecimal

def baseChanger_oct_to_bin_and_hex(num,base):
    if base==2:
        return baseChanger_dec_bin(baseChanger_oct_dec(num))
    elif base==16:
        return baseChanger_dec_hex(baseChanger_oct_dec(num))
    
def baseChanger_oct_bin(num):
    return baseChanger_oct_to_bin_and_hex(num,2)

def baseChanger_oct_hex(num):
    return baseChanger_oct_to_bin_and_hex(num,16)


#Pasaje de Hexadecimal a Binario y Octal

def baseChanger_hex_to_bin_and_oct(num,base):
    if base==2:
        return baseChanger_dec_bin(baseChanger_hex_dec(num))
    elif base==8:
        return baseChanger_dec_oct(baseChanger_hex_dec(num))
        
def baseChanger_hex_bin(num):
    return baseChanger_hex_to_bin_and_oct(num,2)

def baseChanger_hex_oct(num):
    return baseChanger_hex_to_bin_and_oct(num,8)