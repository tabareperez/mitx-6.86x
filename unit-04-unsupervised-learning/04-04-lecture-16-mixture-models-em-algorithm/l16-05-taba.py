import math

p_values = [.5, .5]
sigma_sq_values = [4, 4]
x_values = [.2, -.9, -1, 1.2, 1.8]
mu_values = [-3, 2]

def N(j,i):
    val=( 1/math.sqrt(2*math.pi*sigma_sq_values[j-1]) )*math.exp(
        -((x_values[i-1]-mu_values[j-1])**2)/(2*sigma_sq_values[j-1]) )
    return val


def p(j,i):
    val=p_values[j-1]*N(j,i)/( p_values[0]*N(1,i)+p_values[1]*N(2,i))
    return val

print(p(1,1))
print(p(1,2))
print(p(1,3))
print(p(1,4))
print(p(1,5))

print ("------")

print(p(2,1))
print(p(2,2))
print(p(2,3))
print(p(2,4))
print(p(2,5))

print ("------")

# Verificación, todos deberían sumar 1

print(p(1,1) + p(2,1))
print(p(1,2) + p(2,2))
print(p(1,3) + p(2,3))
print(p(1,4) + p(2,4))
print(p(1,5) + p(2,5))


def est_p(j):
    val = sum([p(1, i) for i in range(1, len(x_values)+1)])/len(x_values)
    return val

def est_mu(j):
    val = sum([p(1, i)*x_values[i-1] for i in range(1, len(x_values)+1)]) / sum([p(1, i) for i in range(1, len(x_values)+1)])
    return val

def est_sigma_sq(j):
    val = sum([p(1, i)*((x_values[i-1]-est_mu(j))**2) for i in range(1, len(x_values)+1)]) / sum([p(1, i) for i in range(1, len(x_values)+1)])
    return val


print ("est p1:")
print (est_p(1))

print ("est mu1:")
print (est_mu(1))

print ("est sigma sq 1:")
print (est_sigma_sq(1))
