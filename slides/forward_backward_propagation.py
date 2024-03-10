# Initialisierung der Gewichte und Bias
w11, w12, w21, w22, w31, w32 = 0.5, -1, 1.5, -2, 1, -1
b1, b2, b3 = 0, 0.5, -1.5
x1, x2 = 1, 2
y_tatsaechlich = 1

# Vorwärtspropagation
z1 = w11*x1 + w12*x2 + b1
z2 = w21*x1 + w22*x2 + b2
y_vorhergesagt = w31*z1 + w32*z2 + b3
print('y_vorhergesagt', y_vorhergesagt)

# Berechnung des Verlustes
verlust = 0.5 * (y_vorhergesagt - y_tatsaechlich)**2

# Rückwärtspropagation (Gradientenberechnung für eine der Gewichte als Beispiel)
# Gradient des Verlustes in Bezug auf y_vorhergesagt
dL_dy = y_vorhergesagt - y_tatsaechlich

# Gradient des Verlustes in Bezug auf w31 (als Beispiel)
dL_dw31 = dL_dy * z1

print(verlust, dL_dy, dL_dw31)

