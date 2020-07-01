import urllib.request
estados = ["ac", "al", "ap", "am" ,"ba" ,"ce", "df", "es", "go","ma", "mt" ,"ms", "mg" ,"pa" ,"pb" ,"pr", "pe", "pi", "rj", "rn", "rs", "ro", "rr", "sc", "sp", "se", "to"]
partidos = ["avante", "cidadania", "dc", "dem", "mdb","novo", "patriota","pcb", "pcdob" ,"pco", "pdt", "phs", "pl", "pmb", "pmn", "pode", "pp","ppl","pors","prp","prtb","psb","psc","psd","psdb","psl","psol","pstu","pt","ptb","ptc","pv","rede","republicanos","solidariedade"]
part_lenth = len(partidos) 
est_lenth = len(estados)
for cont in range (0,part_lenth):
    for cont2 in range (0,est_lenth):
        nome = partidos[cont] + "_" + estados[cont2]+".zip"
        url = "http://agencia.tse.jus.br/estatistica/sead/eleitorado/filiados/uf/filiados_" + nome
        print (url)
        try: 
            urllib.request.urlretrieve(url,nome)
            print("Ok")
        except:
            print("Deu Erro")
            pass