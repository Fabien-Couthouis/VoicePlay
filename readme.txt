R�alis� par Fabien Couthouis - Stagiaire Conseil Digital Cov�a, �t� 2019

VoicePlay est un petit utilitaire pour r�aliser une synth�se vocale � partir de texte (Text2Speech) et lire
les sons ainsi cr�es. VoicePlay a �t� utilis� pour r�aliser les tests utilisateurs Voicebot prise de rdv en Juillet 2019
__________________________________________________________________________

Intructions :

-sounds est un dossier contenant tous les sons devant �tre jou�s par Voiceplay. Chaque nom fichier doit �tre pr�c�d�
par un num�ro (ex 1xxxx.mp3) pour �tre reconnu par Voiceplay. Ce num�ro permet d'organiser les sons et correspond au num�ro
de la ligne dans la grille dans laquelle sont pr�sent�s les sons.

- ibm-credentials.env est un fichier r�cup�r� via la console IBM Watson. Il contient les informations n�cessaires �
l'utilisation de l'API Text2Speech (cl� + url). La cl� utilis�e dans VoicePlay m'apparient. Il est possible qu'il faille
la remplacer en cas d'erreur.

- GenerateVoice.py permet de faire le liens avec l'api IBm

- main.py est le fichier principal de l'application

- generate_executable.bat est un petit script permettant de g�n�rer l'ex�cutable du logiciel. Attention, il faut imp�rativement
qu'une version de python 3 soit install�e sur le poste


