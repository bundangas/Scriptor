import random
from templates import (
    INTRODUCAO_TEMPLATES, 
    DESENVOLVIMENTO1_TEMPLATES, 
    DESENVOLVIMENTO2_TEMPLATES, 
    CONCLUSAO_TEMPLATES,
    CONECTIVOS
)

class RedacaoGenerator:
    @staticmethod
    def get_random_conectivo(tipo):
        return random.choice(CONECTIVOS[tipo])

    @staticmethod
    def gerar_introducao():
        template = random.choice(INTRODUCAO_TEMPLATES)
        return template.format(
            cenário="{cenário - ex: brasileiro atual/contemporâneo/global}",
            tema="{tema da redação}",
            contexto_atual="{contextualização do tema}"
        )

    @staticmethod
    def gerar_desenvolvimento1():
        template = random.choice(DESENVOLVIMENTO1_TEMPLATES)
        conectivo = RedacaoGenerator.get_random_conectivo('causa_consequencia')
        return template.format(
            argumento_principal="{seu primeiro argumento}",
            evidencia_exemplo="{exemplo ou evidência que comprova seu argumento}",
            consequencia_impacto="{consequência ou impacto do seu argumento}",
            conectivo=conectivo,
            analise_critica="{sua análise crítica}"
        )

    @staticmethod
    def gerar_desenvolvimento2():
        template = random.choice(DESENVOLVIMENTO2_TEMPLATES)
        conectivo = RedacaoGenerator.get_random_conectivo('adicao')
        return template.format(
            segundo_argumento="{seu segundo argumento}",
            evidencia_exemplo2="{exemplo ou evidência que comprova seu segundo argumento}",
            consequencia_impacto2="{consequência ou impacto do seu segundo argumento}",
            conectivo=conectivo,
            analise_critica2="{sua análise crítica}"
        )

    @staticmethod
    def gerar_conclusao():
        template = random.choice(CONCLUSAO_TEMPLATES)
        return template.format(
            retomada_tema="{retomada do tema principal}",
            agente_proposta1="{quem deve agir - ex: o governo/a sociedade}",
            acao_proposta1="{ação proposta - ex: implemente políticas públicas}",
            agente_proposta2="{segundo agente - ex: as instituições de ensino}",
            acao_proposta2="{segunda ação proposta}",
            objetivo_impacto="{objetivo final da proposta}"
        )

    @staticmethod
    def gerar_redacao_completa():
        return {
            'introducao': RedacaoGenerator.gerar_introducao(),
            'desenvolvimento1': RedacaoGenerator.gerar_desenvolvimento1(),
            'desenvolvimento2': RedacaoGenerator.gerar_desenvolvimento2(),
            'conclusao': RedacaoGenerator.gerar_conclusao()
        }