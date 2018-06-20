import pygame
import Games


class App:

    __size = __weight, __height = 800, 600
    __display = None
    __display_surf = None
    __running = False
    __colors = {'white': (255, 255, 255), 'black': (0, 0, 0)}
    __clock = None
    __font = None
    __txt_Title = 'Ping Pong'
    __txt_New_Game = 'New Game'
    __txt_How_to_Play = 'How to Play'
    __txt_Exit = 'Exit'
    __options = 0
    __game = None

    @staticmethod
    def get_size(): return App.__size

    @staticmethod
    def get_weight(): return App.__weight

    @staticmethod
    def get_height(): return App.__height

    @staticmethod
    def __on_init():
        pygame.init()
        App.__running = True
        App.__display = pygame.display
        App.__display_surf = App.__display.set_mode(App.__size, pygame.HWSURFACE | pygame.DOUBLEBUF)  # noqa
        App.__display.set_caption("Ping-Pong")
        App.__clock = pygame.time.Clock()
        App.__font_Title = pygame.font.SysFont('Arial Black', 80)
        App.__font = pygame.font.SysFont('Arial Black', 40)
        App.__txt_surf_Title = App.__font_Title.render(App.__txt_Title, True, App.__colors['white'])  # noqa
        App.__txt_surf_New_Game = App.__font.render(App.__txt_New_Game, False, App.__colors['white'])  # noqa
        App.__txt_surf_How_to_Play = App.__font.render(App.__txt_How_to_Play, False, App.__colors['white'])  # noqa
        App.__txt_surf_Exit = App.__font.render(App.__txt_Exit, False, App.__colors['white'])  # noqa

    @staticmethod
    def __draw_arrow(display_surf, color, x, y):
        pygame.draw.polygon(display_surf, color, [(x, y), (x-8, y-16), (x+16, y), (x-8, y+16)])  # noqa

    @staticmethod
    def __on_event(event):
        if event.type == pygame.QUIT:
            App.__running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                App.__options = (App.__options + 1) % 3
            elif event.key == pygame.K_UP:
                App.__options = (App.__options - 1) % 3
            elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                if App.__options == 0:
                    App.__game = Games.Game(App.__display_surf)
                    App.__game.on_execute()
                elif App.__options == 1:
                    print("How to Play")
                elif App.__options == 2:
                    App.__running = False

    @staticmethod
    def __on_render():
        App.__display_surf.fill((0, 0, 0))
        # Title
        App.__display_surf.blit(App.__txt_surf_Title, (App.__weight/2 - App.__font_Title.size(App.__txt_Title)[0]/2, App.__height/4 - App.__font_Title.size(App.__txt_Title)[1]))  # noqa
        # New Game
        App.__display_surf.blit(App.__txt_surf_New_Game, (App.__weight/2 - App.__font.size(App.__txt_New_Game)[0]/2, App.__height/2 - App.__font.size(App.__txt_How_to_Play)[1]/2 - 20))  # noqa
        # How to Play
        App.__display_surf.blit(App.__txt_surf_How_to_Play, (App.__weight/2 - App.__font.size(App.__txt_How_to_Play)[0]/2, App.__height/2 + 20))  # noqa
        # Exit
        App.__display_surf.blit(App.__txt_surf_Exit, (App.__weight/2 - App.__font.size(App.__txt_Exit)[0]/2, App.__height/2 + App.__font.size(App.__txt_How_to_Play)[1]/2 + 60))  # noqa
        # Arrow
        if App.__options == 0:
            arrow_x = App.__weight/2 - App.__font.size(App.__txt_New_Game)[0]/2 - 30  # noqa
            arrow_y = App.__height/2 - App.__font.size(App.__txt_How_to_Play)[1]/2 + App.__font.size(App.__txt_New_Game)[1]/2 - 20  # noqa
        elif App.__options == 1:
            arrow_x = App.__weight/2 - App.__font.size(App.__txt_How_to_Play)[0]/2 - 30  # noqa
            arrow_y = App.__height/2 + App.__font.size(App.__txt_How_to_Play)[1] - 7  # + App.__font.size(App.__txt_How_to_Play)[1]/2 - 20  # noqa
        elif App.__options == 2:
            arrow_x = App.__weight/2 - App.__font.size(App.__txt_Exit)[0]/2 - 30  # noqa
            arrow_y = App.__height/2 + App.__font.size(App.__txt_How_to_Play)[1] + 20 + App.__font.size(App.__txt_Exit)[1]*3/4  # noqa

        App.__draw_arrow(App.__display_surf, App.__colors['white'], arrow_x, arrow_y)  # noqa
        # TODO
        App.__display.update()
        App.__clock.tick(30)

    def __on_cleanup():
        pygame.quit()

    @staticmethod
    def execute():

        if App.__on_init() is False:
            App.__running = False

        while (App.__running):
            for event in pygame.event.get():
                App.__on_event(event)
            App.__on_render()
        App.__on_cleanup()


if __name__ == "__main__":
    App.execute()
