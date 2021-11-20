import os
import sys
import re
import shutil
from pathlib import Path


chemin = sys.argv[1]   #L'argument entré est le chemin à traiter

def traitement_jpg():
	
	print ("Nom des images:")
	
	#On liste les fichiers finissant par ".jpg" dans le chemin donné
	for images in os.listdir(chemin):
		if images.endswith(".jpg"):
			os.path.join(chemin, images)
			#On affiche seulement le nom de l'image sans l'extension
			file_name = Path(os.path.join(chemin, images)).stem
			print(file_name)
			#On copie les images trouvées dans le fichiers "images"
			shutil.copy(chemin+"/"+images, 'images')

def traitement_txt():

	print ("Recherche des fichiers texte:")

	#On liste les ficher finissant par ".txt" dans le chemin donné
	for file in os.listdir(chemin):
		if file.endswith(".txt"):
			#On affiche le fichier texte trouvé
			print(os.path.join(file))
       			
			#On fait une liste de chaque ligne du fichier trouvé
			with open(chemin+"/"+file) as fh:
 		 		string = fh.readlines()
   
			#Regex permettant de trouver les ip
			pattern =re.compile('''((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)''')
 
			
			valid =[]

 
			#On supprime les espaces en trop et on applique la regex à chaque ligne
			for line in string:
    				line = line.rstrip()
    				result = pattern.search(line)
 
				#Si la regex trouve une adresse ip alors on l'affiche 
    				if result:
      					valid.append(line)

			print("Valid IPs")
			print(valid)

def main():

	#On supprime le repertoire image si il existe déjà
	shutil.rmtree('images')
	#On créer le repertoire image
	os.mkdir('images')
	print ("mon ip:")
	#Variable contenant l'adresse ip de la machine
	ipv4 = os.popen('ip addr show eth0 | grep "\<inet\>" | awk \'{ print $2 }\' | awk -F "/" \'{ print $1 }\'').read().strip()
	print (ipv4)

	traitement_jpg()
	traitement_txt()
main()




