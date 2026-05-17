#ham tinh luy thua
#vi du
# 2^3 = 8
# 3^2 = 9
# def caculate_power(base_number(so dau),exponent(so mu)):
def calculate_power(base_number,exponent):
    #base_number * base_number *base_number
    result = 1
    for i in range(exponent):
        result = result * base_number
        #base_number = 2,exponent = 3
        # 1 * 2 = 2
        # 2 * 2 = 4
        # 4 * 2 = 8 (ngung khi du 3 lan lap)
    return result
print(calculate_power(2,3))