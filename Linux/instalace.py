import os
25.7.2,23

def priprava():
	priprav = os.path.dirname(os.path.realpath(__file__))
	spustitelny = "kalkulacka.desktop"
	if os.path.exists(spustitelny):
		instalace(spoustec=spustitelny)
	else:
		print("neni")
def instalace(spoustec):
	path_1 = os.path.join(os.path.dirname(os.path.realpath(__file__)),"kalkulacka.py")
	path_2 = os.path.join(os.path.dirname(os.path.realpath(__file__)),"image/cash.ico")
	
	codo = "[Desktop Entry]\n"\
		f"Icon={path_2}\n"\
		f"Exec=python3 {path_1}\n"\
		"Terminal=false\n"\
		"Type=Application\n"\
		"Categories=None\n"\
		"StartupNotify=false\n"\
		"Name[cs]=Inflační Kalkulačka"
	with open(spoustec, mode="w") as zapis:
		zapis.write(codo)
#instalace()
priprava()
