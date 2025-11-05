stopnie = (
 "Szeregowy",
 "Kapral",
 "Sierżancie",
 "Porucznik",
 "Kapitan",
 "Major",
 "Pułkownik",
)

#a = list(stopnie)
illosc_stopnii = len(stopnie)
Major_index = stopnie.index('Major')
if 'Pułkownik' in stopnie:
    Pulkownik_wstepowanie = 1
else:
    Pulkownik_wstepowanie = 0
print(illosc_stopnii , Major_index, Pulkownik_wstepowanie)

