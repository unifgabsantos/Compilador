import json
class Token(object):
  '''Class for create your Token'''
  def __init__(self, type, value,commentary):
      self.type = type
      self.value = value
      self.commentary = commentary
  def __str__(self):
      return f"<{self.type},{self.value}>"
  def __repr__(self):
      return self.__str__()
  def help(self):
      return self.commentary
def readTokenFile(path:str)->list:
    '''Function for read file with yours tokens.'''
    file = open(path,"r",encoding="utf-8")
    payload = json.loads(file.read())
    file.close()
    return payload
def createTokens(payloads:list)->list:
    '''Function for create yours Token.'''
    tokens = []
    for token in payloads:
        tokens.append(Token(token["Type"],token["Value"],token["Commentary"]))
    return tokens
def main():
    tokens = createTokens(readTokenFile("Tokens.json"))
    for token in tokens:
        print(token)
main()