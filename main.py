import json
import funcs

mMaxSac = int(input('Masse supporté par le sac: '))

objFile = open("./obj.json", "r")

objlist = json.loads(objFile.read())

