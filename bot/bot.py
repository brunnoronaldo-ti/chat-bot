import random
import unicodedata
#versão 0.1
#funções: conversa básica
#implementação futura: jogos/mini-games

class Bot:

    def normalizar(self, texto):
        texto = texto.lower()
        texto = unicodedata.normalize("NFD", texto)
        texto = "".join(
            c for c in texto if unicodedata.category(c) != "Mn"
        )
        return texto

    def __init__(self):
        self.intents = {
            "jogar_forca": {
                "palavras": [
                    "vamos jogar forca",
                    "jogar forca",
                    "bora jogar forca",
                    "forca"
                ],
                "acao": "forca",
                "tipo": "acao"
            },

            "despedida": {
                "palavras": [
                    "tchau", "ate mais", "falou",
                    "ate logo", "ate a proxima"
                ],
                "respostas": [
                    "Até mais 👋",
                    "Falou!",
                    "Volta depois 😄"
                ],
                "tipo": "resposta"
            },

            "agradecimento": {
                "palavras": [
                    "obrigado", "obrigada", "valeu",
                    "brigadao", "brigadinha"
                ],
                "respostas": [
                    "De nada! 😊",
                    "Por nada! 😄",
                    "Sempre às ordens! 😉"
                ],
                "tipo": "resposta"
            },

            "saudacao": {
                "palavras": [
                    "oi", "ola", "e ai", "fala",
                    "bom dia", "boa tarde", "boa noite",
                    "salve", "ei", "eai"
                ],
                "respostas": [
                    "Olá 😄",
                    "E aí! Tudo bem?",
                    "Fala comigo 😎"
                ],
                "tipo": "resposta"
            }
        }

        # prioridade
        self.ordem_intents = [
            "jogar_forca",
            "despedida",
            "agradecimento",
            "saudacao"
        ]

        self.acoes = {
            "forca": self.jogar_forca
        }

        self.estado = "idle"


    def responder(self, mensagem):
        mensagem = self.normalizar(mensagem)

        if self.estado == "idle":
            if "jogar forca" in mensagem:
                self.estado = "jogando_forca"
                return "🎮 Beleza! Pensei numa palavra. Manda uma letra."
        if self.estado == "jogando_forca":
            return self.processar_forca(mensagem)

        for nome in self.ordem_intents:
            intent = self.intents[nome]
            palavras = [self.normalizar(p) for p in intent["palavras"]]

            if any(p in mensagem for p in palavras):

                if intent["tipo"] == "resposta":
                    return random.choice(intent["respostas"])

                if intent["tipo"] == "acao":
                    return self.acoes[intent["acao"]]()

        return "Ainda não sei responder isso 😅"

    def jogar_forca(self):
        return "🎮 Iniciando o jogo da forca..."
