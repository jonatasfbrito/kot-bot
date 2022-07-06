import requests
import json

class Funcoes():



	def mensagem_autodestrutiva(txt):
		url = "https://www.invertexto.com/ajax/mensagem-autodestrutiva.php"
		post = {"msg":f"{txt}","autodestroy":1440}
		res = requests.post(url, data=post).json()
		ide = res["linkId"]
		sct = res["secret"]
		finalLink = f"https://www.invertexto.com/?key={sct}&id={ide}"
		finalText = f"""
		Mensagem gerada com sucesso!

Link: {finalLink}
Obs: Caso não lida, a mensagem se autodestruirá em 24 horas.
		"""
		return finalText




	def numero_extenso(num):
		url = "https://www.invertexto.com/ajax/numeros-por-extenso.php"
		post = {"numero":f"{num}"}
		res = requests.post(url, data=post).text
		txt = f"""
*Número:* {num}

*Extenso:* {res}
		"""
		return txt





	def gerar_pessoas():
		url = "https://www.4devs.com.br/ferramentas_online.php"
		post = {"acao":"gerar_pessoa","sexo":"I","pontuacao":"S","idade":"0","cep_estado":"","txt_qtde":"1","cep_cidade":""}
		res = requests.post(url, data=post).json()
		return res