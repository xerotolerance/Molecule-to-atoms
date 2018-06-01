def parse_molecule(formula):
    atoms, inner = {}, {}
    elm, multstr ='', ''
    sem=0

    for i in range(len(formula)):
        letr, nextletr = formula[i], formula[i+1] if i+1 < len(formula) else ''
        
        if letr.isalpha() and sem >= 0:
            elm+=letr
        elif letr in '([{':
            if sem == 0:
                inner = parse_molecule(formula[i+1:])
            sem -= 1
        elif letr in '}])':
            sem += 1
            if sem > 0:
                return atoms
        
        if sem < 0: continue
        
        if letr.isdigit():
            multstr += str(letr)
            if not nextletr.isdigit():
                if inner != {}:
                    for item in inner:
                        atoms[item] = inner[item] * int(multstr) if item not in atoms else atoms[item] + inner[item] * int(multstr)
                    inner = {}
                elif elm != '':
                    atoms[elm] = int(multstr) if elm not in atoms else atoms[elm] + int(multstr)
                    elm = ''
                multstr=''
        
        if not (nextletr.islower() or nextletr.isdigit()):
            if inner != {}:
                for item in inner:
                    atoms[item] = inner[item] if item not in atoms else atoms[item] + inner[item]
                inner = {}
            elif elm != '':
                atoms[elm] = 1 if elm not in atoms else atoms[elm] + 1
                elm = ''
    return atoms
