base_value = float(input("Introdueix un preu: "))
iva = float(input("Introdueix el IVA a aplicar: "))

final_value = base_value * iva / 100 + base_value

print(f"Preu base: {base_value} €")
print(f"IVA: {iva} %")
print(f"Preu final: {final_value} €")