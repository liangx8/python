import pcbnew    
unit=1000000
if __name__=="__main__":
    org='/home/arm/git/kicad/stm-esc/stm-esc.kicad_pcb'
    pcb=pcbnew.LoadBoard(org)
    ms = pcb.GetModules()
    rowi=0
    coli=0
    incrment=20 * unit

    for m in ms:
        pos = m.GetPosition()
        pos.x=coli * incrment
        pos.y=rowi * incrment
        m.SetPosition(pos)
        coli = coli + 1
        if coli > 8:
            coli = 0
            rowi = rowi + 1

    pcb.Save(org)
