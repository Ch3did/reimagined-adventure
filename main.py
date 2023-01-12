import os
import urllib.request


class GetPoliticalParty:
    def __init__(self, estados, partidos):
        os.system("rm -r DadosEleitorais")
        os.system("mkdir DadosEleitorais")

        self.estados = estados
        self.partidos = partidos
        self.get_data()

    @classmethod
    def _make_url(cls, partido, estado):
        nome = partidos[partido] + "_" + estados[estado] + ".zip"
        url = (
            "http://agencia.tse.jus.br/estatistica/sead/eleitorado/filiados/uf/filiados_"
            + nome
        )
        return url, nome

    def _request_data(self, url, nome):
        try:
            urllib.request.urlretrieve(url, nome)
            print("Ok")
            return True
        except:
            print("Deu Erro")
            pass

    def get_data(self):
        part_lenth = len(partidos)
        est_lenth = len(estados)
        for partido in range(0, part_lenth):
            for estado in range(0, est_lenth):
                url, nome = self._make_url(partido=partido, estado=estado)
                if self._request_data(url, nome):
                    os.system("mv " + nome + " dados/")


if __name__ == "__main__":
    # Lista de Estados
    estados = [
        "ac",
        "al",
        "ap",
        "am",
        "ba",
        "ce",
        "df",
        "es",
        "go",
        "ma",
        "mt",
        "ms",
        "mg",
        "pa",
        "pb",
        "pr",
        "pe",
        "pi",
        "rj",
        "rn",
        "rs",
        "ro",
        "rr",
        "sc",
        "sp",
        "se",
        "to",
    ]

    # Lista de Partidos
    partidos = [
        "phs",
        "ppl",
        "prp",
        "avante",
        "cidadania",
        "dc",
        "dem",
        "mdb",
        "novo",
        "patriota",
        "pcb",
        "pcdob ",
        "pco",
        "pdt",
        "pl",
        "pmb",
        "pmn",
        "pode",
        "pp",
        "pros",
        "prtb",
        "psb",
        "psc",
        "psd",
        "psdb",
        "psl",
        "psol",
        "pstu",
        "pt",
        "ptb",
        "ptc",
        "pv",
        "rede",
        "republicanos",
        "solidariedade",
        "up",
    ]

    GetPoliticalParty(estados=estados, partidos=partidos)
