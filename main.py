from math import log2

wiederhole = True

while wiederhole:

    basis_netzt = input("Eingabe Basisnetz: ")
    arr_basis_netzt = basis_netzt.split(".")
    anz_subnetz =  int(input("Eingabe Menge an Netzen: "))

    log_anz_subnetz = log2(anz_subnetz)

    if log_anz_subnetz % 1 != 0:
        log_anz_subnetz = int(log_anz_subnetz + 1)
    else:
        log_anz_subnetz = int(log_anz_subnetz)

    host_anz_subnetz = 2**(8 - log_anz_subnetz)

    print("Anzahl der möglichen Hosts pro Netz: ", host_anz_subnetz - 2)
    print("Subnetzmaske der neuen Netze:" + "255.255.255." + str(256 - host_anz_subnetz) )

    for i in range(0, anz_subnetz):
        print(arr_basis_netzt[0] + "." + arr_basis_netzt[1] + "." + arr_basis_netzt[2] + "." + str(i * host_anz_subnetz))

    if input("Wiederholen? (y/n): ") == "n":
        wiederhole = False





