import os
import sys
import pygame

pygame.init()

#  Color constants for testing
RED = (255, 0, 0)
WHITE = (240, 240, 240)

#############
#  CLASSES  #
#############
    
class Idm:
    """
    IDM is the class for the main application
    """
    def __init__(self, path):
        self.path = path 
        self.dir_list, self.image_list = list_files(self.path)
        self.width = 800
        self.height = 600
        self.window = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        self.caption = "IDM"
        self.theme = {
                "color0" : (80, 80, 80),
                "color1" : (250, 250, 250)
                }
        self.selected_directory = 0
        self.selected_image = 0

    def setup(self):
        """
        setup function is ran once at the startup
        """
        pygame.display.set_caption(self.caption)
        pygame.key.set_repeat()

    def handle_keyboard(self):
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.selected_directory -= 1
            if self.selected_directory < 0:
                self.selected_directory = 0
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.selected_directory += 1
            if self.selected_directory > len(self.dir_list):
                self.selected_directory = len(self.dir_list) - 1
        # TODO: ajouter une touche pour revenir à la première image d'un répertoire

    def draw(self):
        """
        draw is run at each frame, ideally, 
        it would be run at each image change
        """
        #  self.window.fill(RED)
        draw_left_menu(self.window, self.theme["color0"], self.path, self.selected_directory)
        draw_image_list(self.window, self.theme["color0"], self.image_list, self.selected_image)
        pygame.display.flip()

    def run(self):
        """
        run launch the application and contain
        the main loop
        """
        running = True
        self.setup()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
            self.handle_keyboard()
            self.draw()

#   TODO: il vaudrait mieux créer une classe Directory qui contiendrait la liste d'image et l'image sélectionnée
#   pour garder en mémoire l'image sélectionnée quand on change de répertoire

class Image:
    """
    Image class contains all variables needed
    to display easily an image
    """
    def __init__(self, path):
        self.path = path
        self.file = pygame.image.load(self.path)
        self.rect = self.file.get_rect()
        self.is_selected = False

    def draw(self):
        """
        to simplify image display
        """
        window.blit(self.file, self.rect)


###########
#  MODEL  #
###########

def list_files(path):
    """
    create lists of directories and files in order,
    like 'tree' command line function
    """
    filenames = []
    dirnames  = []
    for root, dirs, files in os.walk(path):
        path = root.split(os.sep)
        dirnames.append(len(path) * ' ' + os.path.basename(root))
        for name in files:
            if name.endswith(".jpg"):
                filenames.append(len(path) * ' ' + name)
    return dirnames, filenames


################
#  CONTROLLER  #
################


##########
#  VIEW  #
##########

# TODO: déplacer toutes les fonctions dans la classe Idm

def draw_left_menu(surface, color, path, selected_directory):
    """
    The left menu displays all directories names,
    which structure the presentation
    """
    width, height = pygame.display.get_window_size()
    left_menu_rect = pygame.Rect(0, 0, 200, height)
    pygame.draw.rect(surface, color, left_menu_rect)
    dirnames, filenames = list_files(path)
    ypos = 20
    dir_number = 0
    for dirname in dirnames:
        text_rect = draw_text(surface, dirname, 10, 10, ypos)
        # TODO: dessiner un plus beau rectangle pour le répertoire sélectionné
        if dir_number == selected_directory:
            pygame.draw.rect(surface, RED, text_rect, width = 1)
        ypos += 16
        dir_number += 1


def draw_image_list(surface, color, image_list, selected_image):
    """
    The image list is displayed at the bottom of the screen, 
    and displays all file names contained in the selected directory.
    The selected image is highlighted.
    """
    width, height = pygame.display.get_window_size()
    image_list_rect = pygame.Rect(200, height - 100, width - 200 , 100)
    pygame.draw.rect(surface, color, image_list_rect)
    xpos = image_list_rect.left + 10
    ypos = image_list_rect.centery
    for image_name in image_list:
        draw_text(surface, image_name, 10, xpos, ypos)
        xpos += len(image_name) * 4 


def draw_image(image):
    """
    Displays the selected image on the main part of the screen
    """
    pass
    

font_name = pygame.font.match_font('Hack')
def draw_text(surface, text, size, x, y):
    """
    To simplify text display
    """
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midleft = (x, y)
    surface.blit(text_surface, text_rect)
    return text_rect

if __name__ == "__main__":
    #  if len(sys.argv) == 1:
    #      path = os.getcwd()
    #  elif len(sys.argv) > 1:
    #      path = sys.argv[1]
    path = "/home/antharia/Dev/python/idm/presentation" # DEBUG
    app = Idm(path)
    app.run()
