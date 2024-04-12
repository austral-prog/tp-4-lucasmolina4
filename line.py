def line():
    print("TO DO")
    import math
coef_a= float(input("Ingrese el coeficiente A: "))
coef_b =float(input("Ingrese el coeficiente B: "))
coef_c =float(input("Ingrese el coeficiente C: "))
coef_d =float(input("Ingrese el coeficiente D: "))

print(f"El coeficiente A de su ecuación de la recta es:{coef_a}")
print(f"El coeficiente B de su ecuación de la recta es:{coef_b}")
print(f"El coeficiente X1 de su ecuación de la recta es:{coef_c}")
print(f"El coeficiente X2 de su ecuación de la recta es:{coef_d}")

print(f"Para la siguiente ecuacion:\n{coef_a}+{coef_b}")

P1=print(f"Dado los siguientes numeros:\n{coef_c, coef_a * coef_c + coef_b}")
P2=print(f"Dado los siguientes numeros:\n{coef_d, coef_a * coef_d + coef_b}")

print(f"La distancia entre ellos es:" ,math.dist([coef_c, coef_a * coef_c + coef_b ], [coef_d, coef_a * coef_d + coef_b]))


