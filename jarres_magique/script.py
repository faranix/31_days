class Game:
    def __init__(self, key, snake):
        self.array_game = []
        self.key = key
        self.snake = snake
        self.game_run = True
        
        while(self.game_run == True):
            self.run()
        
            
    def run(self):
        self.generate_jarres()
        self.userChoice()        
    
    def generate_jarres(self):
        for i in range(self.snake):
            self.array_game.append("snake")
            
        for i in range(self.key):
            self.array_game.append("key")
            
    def userChoice(self):
        print("5 jarres sont devant vous !")
        inputUser = int(input("Quelle jarre voulez ouvrir ? "))
        
        if (self.array_game[inputUser] == "snake"):
            print("Cette jarre contient un serpent !")
            print("Perdu...")
            self.game_run = False
        else:
            print("Cette jarre contient une clé !")
            print("Gagner !")
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
    
    if (level > 4 | level < 1):
        level = int(input("Enter une options valide: "))
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
    