for i in range(8):
    num = (i+1) % 2 + 1
    num1 = (i) % 2 + 1
    print(f'$$ arr[{i}] \\oplus 3 + \\mathrm{{0x30}} = {num1} \\oplus 3 + \\mathrm{{0x30}} = \\mathrm{{0x3{num}}} = \\texttt{{\'{num}\'}} $$')
