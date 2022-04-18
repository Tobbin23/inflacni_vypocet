import os

def instalace():
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
	with open("kalkulacka_2.desktop", mode="w") as zapis:
		zapis.write(codo)
instalace()