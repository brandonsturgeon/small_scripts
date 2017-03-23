import requests

a = requests.get("https://gist.githubusercontent.com/brandonsturgeon/e66fc426ce298970cc0f777e73ceb5d8/raw/7104ab3f11ba119205077505d9f37bb79ae751cb/emojis1")
emojis = a.text.encode('utf-8')

spl = emojis.split(" ")

spl = ['"{}"'.format(a) for a in spl]

print ",\n".join(spl)
