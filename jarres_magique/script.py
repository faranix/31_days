class Game:
    def __init__(self, key, snake):
        self.key = key
        self.snake = snake
        self.win = False
        
        while(self.win == False):
            self.run()
        
            
    def run(self):
        print("test")
        self.win = True
            
            
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
    