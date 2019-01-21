# track_and_trace_web_project


Šis projektas yra Kaunas Coding School Python kursų dalis

Kodų ant vaistų pakuočių keitimo programa. Nuskaitomas esantis ant vaistų dėžutės 2D kodas. Jame yra užkoduota informacija apie vaisto pavadinimą, gamybos serijos numeris, galiojimo data.

`New Product` mygtukas nukreipia į langą kuriame aprašoma su kokiu produktu bus dirbama.
`New Code` mygtukas nukreipia į langą kuriame įvedamas (nuskanuojamas) 2D kodas nuo vaisto pakuotės.

Duomenų bazėje patikrinama ar kodas nuskanuotas nuo produkto pakuotės yra autentiškas.
Kodas yra išskaidomas į [product_name], [product-batch], [expire_date] ir šie duomenys yra palyginami su `New Product` duomenimis. Jeigu duomenys iš `New Product` lango sutampa su duomenimis iš `New Code`lango yra sugeneruojamas naujas kodas `product_code`, o duomenys [product_name], [product-batch], [expire_date], [old_code], [new_code] yrašomi į duomenų bazę.

`new-code` sukurti reikalinga informacija: (seriją, pavadinimą, galiojimo datą. Apjungiant produkto pavadinimo ir galiojimo datos turi būtu sukuriamas produkto kodas (`code` + `pavadinimas` + `serija` + `galiojimo data` į vieną `new_code` 

## Diegimas
    
`pip install requirements.py`

## Naudojimas

`Create Account` mygtukas nukreipia į vartotojo registreacijos langą.
`Login` prijingia vartotoją kuris dirbs su produktu, o vartotojo duomenys bus įrašomi į duomenų bazę, kad būtų galima sekti kas sukūrė dirbo su produktu ir kas dalyvavo generuojant `new_code`.
`New Product` lange suvedama produkto duomenys.
`New Code` mygtukas nukreipia į langą kuriame įvedamas (nuskanuojamas) 2D kodas nuo vaisto pakuotės.


`code` reikalingi `new_code` generavimui saugomi `codes.txt` faile. Panaudojus `code` jis yra ištrinamas iš .txt failo.

Tarkime, jog turėjome du nepanaudotus kodus. 000000 ir 000001.
Sugeneravus vieną `new_code` `codes.txt` turinys turėtų pasikeisti į:
```txt
code
0000001
```
kitaip tariant, iš jo turėtų būti ištrinta  000000 eilutė.

Taip pat duomenų bazės eilutė pasipildo nauju įrašu :
`{['Morfin2018-12-212020-12/`000001`']}`


## Prisijungimas

Prisijungimui reikalinga registracija. `Create account` mygtukas nukreipia į registracijos langą.
