# check byte 模版
def check_byte(octet):  
    if not octet: return False  
    if not octet.isdigit(): return False  
    if len(octet) > 1 and octet[0] == '0': return False 
    return 0 <= int(octet) <= 255

def validateIP(ipaddr): 
    octets = ipaddr.split('.')  
    if len(octets) != 4: return False 
    for octet in octets:
        if not check_byte(octet): return False
    return True

# Test cases
print(validateIP('192.168.0.1'))   # True
print(validateIP('0.0.0.0'))       # True
print(validateIP('123.24.59.99'))   # True
print(validateIP('192.168.123.456')) # False
print(validateIP('12.34.56.oops'))  # False
print(validateIP('1.2.3.4.5'))      # False
print(validateIP('123.235.153.425')) # False
