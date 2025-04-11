from deep_translator import GoogleTranslator

def traduzir_palavra(palavra):
    tradutor = GoogleTranslator(source='en', target='pt')
    return tradutor.translate(palavra)

palavra = input("Digite uma palavra em inglês: ")
traducao = traduzir_palavra(palavra)

print(f"A palavra '{palavra}' significa '{traducao}' em português.")
