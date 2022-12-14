import random

class Game:
    def __init__(self, key, snake):
        self.array_game = []
        self.key = key
        self.snake = snake
        self.game_run = True
        self.compteur_key = 0
        
        # Génére les jarres.
        self.generate_jarres()
        
        
        while(self.game_run == True):
            self.run()
        
    # Lance le jeu.    
    def run(self):
        self.userChoice()        
    
    # Génère les jarres en fonction du level.
    def generate_jarres(self):
        for i in range(self.snake):
            self.array_game.append("snake")
            
        for i in range(self.key):
            self.array_game.append("key")
            
        self.randomJarres()
            
        
    # Mélange le tableau.
    def randomJarres(self):
        random.shuffle(self.array_game)
           
    # Récupère le choix de l'utilisateur et fait une action.
    def userChoice(self):
        print("5 jarres sont devant vous !")
        inputUser = int(input("Quelle jarre voulez ouvrir ? "))
        
        if (inputUser > 5 or inputUser < 1):
           print("Entrer une jarre valide !")
        else:        
            if (self.array_game[inputUser - 1] == "snake"):
                print("Cette jarre contient un serpent !")
                
                # Retire une clé
                self.compteur_key = self.compteur_key - 1
                
                print("Vous avez " + str(self.compteur_key) + " clés")
                
                self.randomJarres()
            else:
                print("Cette jarre contient une clé !")
                
                # Ajoute une clé
                self.compteur_key = self.compteur_key + 1
                
                print("Vous avez " + str(self.compteur_key) + " clés")
                
                self.randomJarres()
                
        if (self.compteur_key == 3):
            print("Tu deviens roi du temple")
            self.game_run = False
        elif (self.compteur_key < 0):
            print("Vous avez perdu ...")
            self.game_run = False
            
        
            
            
# Affiche le menu de séléction pour l'utilisateur.    
def print_menu():
    menu_options = {
    1: "Level 1 (1 serpent, 4 clés)",
    2: "Level 2 (2 serpents, 3 clés)",
    3: "Level 3 (4 serpents, 1 clé)",
    4: "Exit",
    }
    
    for key in menu_options.keys():
        print(key, menu_options[key])
    

# Tant que vrai affiche le menu.
while(True):
    print_menu()
    level = int(input("Enter votre choix: "))
    
    if (level > 4 or level < 1):
        print("Enter une options valide !")
    elif (level == 1):
        game = Game(4, 1)
        exit()
    elif (level == 2):
        game = Game(3, 2)
        exit()
    elif (level == 3):
        game = Game(1, 4)
        exit()
    elif (level == 4):
        exit()
    