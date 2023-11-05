
#   ~ PARCIAL Nº2 ~
#   Alumno: Ignacio Gómez Garcia

import Funciones
Funciones.clear_terminal()

print("\n ~ PARCIAL Nº2 ~\nMutantes:")
dna = []

# Se piden las bases nitrogenadas validando que sean de 6 caracteres y estos deben ser A,T,C o G:
for i in range(6):
    print("\nIngrese las secuencias de las bases nitrogenadas:")
    while True:
        nitrogenous_base = input(f"Secuencia base nitrogenda nº{i+1}: ").upper()
        if len(nitrogenous_base) != 6:
            print("Las bases deben ser de 6 caracteres.")
            continue
        else:
            for base in nitrogenous_base:
                if base not in "ATCG":
                    print("La base solo puede tener los caracteres A,R,C O G.")
                    break
            dna.append(nitrogenous_base)
        break

# Se llama a la funcion is_mutants (que esta en Funciones) para verificar si es mutante o no.
if Funciones.is_mutants(dna):
    print("\nEs mutante.")
else:
    print("\nNo es mutante.")

# se muestra la secuencia de ADN ingresada:
for i in range(len(dna)):
    for j in range(len(dna[i])):
        print(dna[i][j], end=" ")
    print() 