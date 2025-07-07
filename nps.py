from functools import wraps


def validar_nota(func):
    @wraps(func)
    def wrapper(self, nota):
        if not isinstance(nota, int):
            raise TypeError("A nota deve ser um número inteiro.")
        if nota < 0 or nota > 10:
            raise ValueError("A nota precisa ser entre 0 e 10.")
        return func(self, nota)
    return wrapper


class Nps:
    def __init__(self):
        self._notas = []

    @validar_nota
    def adicionar_nota(self, nota):
        self._notas.append(nota)

    @property
    def notas(self):
        """Retorna cópia das notas (encapsulamento)"""
        return self._notas.copy()

    def calcular_nps(self):
        if not self._notas:
            return 0.0

        detratores = [n for n in self._notas if n <= 6]
        promotores = [n for n in self._notas if n >= 9]

        perc_detratores = len(detratores) / len(self._notas) * 100
        perc_promotores = len(promotores) / len(self._notas) * 100

        return round(perc_promotores - perc_detratores, 2)

    def avaliar_classificacao(self):
        nps = self.calcular_nps()
        if nps < 0:
            return 'Zona Crítica'
        elif nps < 50:
            return 'Zona Neutra (Razoável)'
        elif nps < 75:
            return 'Zona de Qualidade (Muito bom)'
        else:
            return 'Zona de Excelência (Excelente)'

    def __len__(self):
        return len(self._notas)

    def __str__(self):
        return f"NPS atual: {self.calcular_nps()} - {self.avaliar_classificacao()}"

    def __repr__(self):
        return f"<Nps notas={self._notas}>"
