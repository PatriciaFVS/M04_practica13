from animal import animal as an
from vehicle import vehicle as ve
from school import school as sc


""" De la clase animal """
panda = an("mamífer" , "4", "Haribo", "2" , "blanc i negre" , "gran")
panda.salutacio()
panda.setName("T'challa")""" De la clase vehicle"""
panda.salutacio()

koala = an("mamífer" , "4", "Kali", "10" , "gris" , "mitjà")
panda.salutacio()
panda.setSize("petit")
panda.salutacio()
""" ---- ----"""

""" De la clase vehicle"""
ferrari = ve("Ferrari", "345556SHA", "300.000", "0 km", "vermell","mitjà")
ferrari.parts()
ferrari.setPrice("299.500")
ferrari.parts()

twingo = ve("Twingo", "345556CLA", "30.000", "30.000 km", "gris" ,"petit")
twingo.parts()
twingo.setKm("10.500 km")
twingo.parts()
""" ---- ----"""

""" De la clase school"""
jaumebalmes = sc("10000", "100", "6", "2", "300 euros ", "si")
jaumebalmes.info()
jaumebalmes.setPreumatri("400 euros")
jaumebalmes.info()

joandaustria = sc("20000", "200", "6", "3", "200 euros ", "no")
joandaustria.info()
joandaustria.setExtraescolars("sí")
joandaustria.info()
""" ---- ----"""

