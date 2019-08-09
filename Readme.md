Réalisé par Fabien Couthouis - Stagiaire Conseil Digital Covéa, été 2019

VoicePlay est un petit utilitaire pour réaliser une synthèse vocale à partir de texte (Text2Speech) et lire
les sons ainsi créés. VoicePlay a été utilisé pour réaliser les tests utilisateurs Voicebot prise de rdv en Juillet 2019
__________________________________________________________________________

## Instructions : ##

* sounds est un dossier à créer contenant tous les sons devant être joués par Voiceplay. Chaque nom fichier doit être précédé
par un numéro (ex 1xxxx.mp3) pour être reconnu par Voiceplay. Ce numéro permet d'organiser les sons et correspond au numéro
de la ligne dans la grille dans laquelle sont présentés les sons.

* ibm-credentials.env est un fichier récupéré via la console IBM Watson. Il contient les informations nécessaires à
l'utilisation de l'API Text2Speech (clé + url). La clé utilisée dans VoicePlay m'apparient. Il est possible qu'il faille
la remplacer en cas d'erreur.

* GenerateVoice.py permet de faire le liens avec l'api IBm

* main.py est le fichier principal de l'application

* generate_executable.bat est un petit script permettant de générer l'exécutable du logiciel. Attention, il faut impérativement
qu'une version de python 3 soit installée sur le poste


