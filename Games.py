import pygame
# from pygame.locals import *

from Player import Player
from Ball import Ball


class Game:

    def __init__(self, display_surf):
        self.__running = True
        self.__display_surf = display_surf
        self.__size = self.__weight, self.__height = 800, 600

    def __on_init(self):
        pygame.init()
        # self.__display_surf = pygame.display.set_mode(
        # self.__size, pygame.HWSURFACE|pygame.DOUBLEBUF)
        self.__running = True
        pygame.display.set_caption("Ping-Pong", "Pong.ico")
        self.__p1 = Player(3, self.__height/2, 'Player 1')
        self.__p2 = Player(777, self.__height/2, 'Player 2')
        self.__ball = Ball((self.__weight/2, self.__height/2), 12)
        self.__playing = 0    # ball ready
        self.__color_white = (255, 255, 255)
        self.__color_black = (0, 0, 0)
        self.__clock = pygame.time.Clock()
        self.__font = pygame.font.SysFont('Arial Black', 30)
        self.__space_txt = 'Press Space to Begin'
        self.__space_txt_surf = self.__font.render(
            self.__space_txt, False, self.__color_white)
        self.__pause_txt = 'Press Esc to Continue'
        self.__pause_txt_surf = self.__font.render(
            self.__pause_txt, False, self.__color_white)
        self.__pause_continue_txt = 'Continue'
        self.__pause_continue_txt_surf = self.__font.render(
            self.__pause_continue_txt, False, self.__color_white)
        self.__pause_restart_txt = 'Restart'
        self.__pause_restart_txt_surf = self.__font.render(
            self.__pause_restart_txt, False, self.__color_white)
        self.__pause_exit_txt = 'Exit'
        self.__pause_exit_txt_surf = self.__font.render(
            self.__pause_exit_txt, False, self.__color_white)
        self.__counter = 0
        self.__paused = False
        self.__options = 0
        self.__txt_scoreboard = '{} x {}'.format(
            self.__p1.get_score(), self.__p2.get_score())
        self.__txt_surf_Scoreboard = self.__font.render(
            self.__txt_scoreboard, False, self.__color_white)
        self.__config = {'max_points': 2}
        self.__txt_Winner = '{} Won!'.format('')
        self.__txt_surf_Winner = self.__font.render(
            self.__txt_Winner, False, self.__color_white)

    def __move_players(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.__p1.move_up()
        if pressed[pygame.K_s]:
            self.__p1.move_down()
        if pressed[pygame.K_UP]:
            self.__p2.move_up()
        if pressed[pygame.K_DOWN]:
            self.__p2.move_down()

    def __pause(self):
        pygame.draw.rect(
            self.__display_surf, self.__color_white, pygame.Rect(
                self.__weight/2-112, self.__height/2-142, 224, 284))
        pygame.draw.rect(
            self.__display_surf, self.__color_black, pygame.Rect(
                self.__weight/2-110, self.__height/2-140, 220, 280))
        # continue
        self.__display_surf.blit(self.__pause_continue_txt_surf, (self.__weight/2 - self.__font.size(self.__pause_continue_txt)[0]/2 + 12, self.__height/2 - self.__font.size(self.__pause_restart_txt)[1] - self.__font.size(self.__pause_continue_txt)[1] - 10))  # noqa
        # restart
        self.__display_surf.blit(self.__pause_restart_txt_surf, (self.__weight/2 - self.__font.size(self.__pause_continue_txt)[0]/2 + 12, self.__height/2 - self.__font.size(self.__pause_restart_txt)[1]/2))  # noqa
        # exit
        self.__display_surf.blit(self.__pause_exit_txt_surf, (self.__weight/2 - self.__font.size(self.__pause_continue_txt)[0]/2 + 12, self.__height/2 + self.__font.size(self.__pause_restart_txt)[1] + 10))  # noqa
        # option arrow
        if self.__options == 0:
            arrow_y = self.__height/2 - self.__font.size(self.__pause_continue_txt)[1] - self.__font.size(self.__pause_continue_txt)[1] + 2  # noqa
        elif self.__options == 1:
            arrow_y = self.__height/2 - self.__font.size(self.__pause_restart_txt)[1]/2 + 12  # noqa
        elif self.__options == 2:
            arrow_y = self.__height/2 + self.__font.size(self.__pause_exit_txt)[1] + self.__font.size(self.__pause_exit_txt)[1]/2 + 2  # noqa
        self.__draw_arrow(self.__display_surf, self.__color_white, (self.__weight/2 - 90), arrow_y)  # noqa
        # Scoreboard
        self.__display_surf.blit(self.__txt_surf_Scoreboard, (self.__weight/2 - self.__font.size(self.__txt_scoreboard)[0]/2, 10))  # noqa

    def __game_won(self):
        pygame.draw.rect(self.__display_surf, self.__color_white, pygame.Rect(self.__weight/2-127, self.__height/2-142, 254, 284))  # noqa
        pygame.draw.rect(self.__display_surf, self.__color_black, pygame.Rect(self.__weight/2-125, self.__height/2-140, 250, 280))  # noqa
        # winner
        self.__display_surf.blit(self.__txt_surf_Winner, (self.__weight/2 - self.__font.size(self.__txt_Winner)[0]/2, self.__height/2 - self.__font.size(self.__pause_restart_txt)[1] - self.__font.size(self.__pause_continue_txt)[1] - 10))  # noqa
        # restart
        self.__display_surf.blit(self.__pause_restart_txt_surf, (self.__weight/2 - self.__font.size(self.__pause_continue_txt)[0]/2 + 12, self.__height/2 - self.__font.size(self.__pause_restart_txt)[1]/2))  # noqa
        # exit
        self.__display_surf.blit(self.__pause_exit_txt_surf, (self.__weight/2 - self.__font.size(self.__pause_continue_txt)[0]/2 + 12, self.__height/2 + self.__font.size(self.__pause_restart_txt)[1] + 10))  # noqa
        # option arrow
        if self.__options == 0:
            arrow_y = self.__height/2 - self.__font.size(self.__pause_restart_txt)[1]/2 + 12  # noqa
        elif self.__options == 1:
            arrow_y = self.__height/2 + self.__font.size(self.__pause_exit_txt)[1] + self.__font.size(self.__pause_exit_txt)[1]/2 + 2  # noqa
        self.__draw_arrow(self.__display_surf, self.__color_white, (self.__weight/2 - 90), arrow_y)  # noqa
        # Scoreboard
        self.__display_surf.blit(self.__txt_surf_Scoreboard, (self.__weight/2 - self.__font.size(self.__txt_scoreboard)[0]/2, 10))  # noqa

    def __draw_arrow(self, display_surf, color, x, y):
        pygame.draw.polygon(display_surf, color, [
            (x, y), (x+15, y+10), (x, y+20), (x+5, y+10)])

    def __track_ball(self):
        if self.__playing == 1:  # playing
            if (self.__ball.get_x() - self.__ball.get_radius()) <= (self.__p1.get_x() + self.__p1.get_weight()):  # noqa
                if not self.__ball.colide_player1(self.__p1):
                    self.__playing = 2   # unreachable
            elif (self.__ball.get_x() + self.__ball.get_radius()) >= self.__p2.get_x():  # noqa
                if not self.__ball.colide_player2(self.__p2):
                    self.__playing = 2     # unreachable
        else:
            if (self.__ball.get_x() + self.__ball.get_radius()) < 0:
                self.__ball = Ball((self.__weight/2, self.__height/2), 12)
                self.__playing = 0    # ball left screen, reset to center
                self.__p1.reset_y(self.__height/2)
                self.__p2.reset_y(self.__height/2)
                self.__p2.inc_score()
                self.__counter = 0
                self.__txt_scoreboard = '{} x {}'.format(self.__p1.get_score(), self.__p2.get_score())  # noqa
                self.__txt_surf_Scoreboard = self.__font.render(self.__txt_scoreboard, False, self.__color_white)  # noqa
            elif self.__weight < (self.__ball.get_x() - self.__ball.get_radius()):  # noqa
                self.__ball = Ball((self.__weight/2, self.__height/2), 12)
                self.__playing = 0    # ball left screen, reset to center
                self.__p1.reset_y(self.__height/2)
                self.__p2.reset_y(self.__height/2)
                self.__p1.inc_score()
                self.__counter = 0
                self.__txt_scoreboard = '{} x {}'.format(self.__p1.get_score(), self.__p2.get_score())  # noqa
                self.__txt_surf_Scoreboard = self.__font.render(self.__txt_scoreboard, False, self.__color_white)  # noqa
            if self.__p1.get_score() >= self.__config['max_points']:
                self.__playing = 3
                self.__txt_Winner = '{} Won!'.format(self.__p1.get_name())
                self.__txt_surf_Winner = self.__font.render(self.__txt_Winner, False, self.__color_white)  # noqa
                self.__options = 0
            elif self.__p2.get_score() >= self.__config['max_points']:
                self.__playing = 3
                self.__txt_Winner = '{} Won!'.format(self.__p2.get_name())
                self.__txt_surf_Winner = self.__font.render(self.__txt_Winner, False, self.__color_white)  # noqa
                self.__options = 0

    def __on_event(self, event):
        if event.type == pygame.QUIT:
            self.__running = False
        elif not self.__paused:
            if event.type == pygame.KEYDOWN:
                if self.__playing != 3:
                    if event.key == pygame.K_SPACE:
                        if self.__playing == 0:     # ball ready
                            self.__playing = 1      # playing
                            self.__ball.start()
                    if event.key == pygame.K_ESCAPE:
                        self.__paused = True
                else:
                    if event.key == pygame.K_DOWN:
                        self.__options = (self.__options + 1) % 2
                    elif event.key == pygame.K_UP:
                        self.__options = (self.__options - 1) % 2
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:  # noqa
                        if self.__options == 0:
                            self.__running = False
                            self.on_execute()
                        elif self.__options == 1:
                            self.__running = False
                    elif event.key == pygame.K_ESCAPE:
                        self.__running = False
        else:
            if event.type == pygame.KEYDOWN:
                if self.__playing != 3:
                    if event.key == pygame.K_ESCAPE:
                        self.__paused = not self.__paused
                    elif event.key == pygame.K_DOWN:
                        self.__options = (self.__options + 1) % 3
                    elif event.key == pygame.K_UP:
                        self.__options = (self.__options - 1) % 3
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:  # noqa
                        if self.__options == 0:
                            self.__paused = False
                        elif self.__options == 1:
                            self.__running = False
                            self.on_execute()
                        elif self.__options == 2:
                            self.__running = False

    def __on_loop(self):
        self.__move_players()
        self.__ball.move()
        self.__track_ball()

    def __on_render(self):
        """Draw screen objects"""
        self.__display_surf.fill((0, 0, 0))
        # Player 1 (Left)
        pygame.draw.rect(self.__display_surf, self.__color_white, pygame.Rect(self.__p1.get_x(), self.__p1.get_y(), self.__p1.get_weight(), self.__p2.get_height()))  # noqa
        # Player 2 (Right)
        pygame.draw.rect(self.__display_surf, self.__color_white, pygame.Rect(self.__p2.get_x(), self.__p2.get_y(), self.__p1.get_weight(), self.__p2.get_height()))  # noqa
        # Net
        pygame.draw.line(self.__display_surf, self.__color_white, (self.__weight/2 - 1, 0), (self.__weight/2 - 1, self.__height), 2)  # -> Rect  # noqa
        # Ball
        pygame.draw.circle(self.__display_surf, self.__color_white, (int(self.__ball.get_x()), int(self.__ball.get_y())), self.__ball.get_radius(), self.__ball.get_radius())  # noqa
        # Start Text
        if self.__playing == 0 and not self.__paused:
            # ScoreBoard
            self.__display_surf.blit(self.__txt_surf_Scoreboard, (self.__weight/2 - self.__font.size(self.__txt_scoreboard)[0]/2, 10))  # noqa
            # Blink:
            self.__counter = (self.__counter + 1) % 60
            if self.__counter < 30:
                self.__display_surf.blit(self.__space_txt_surf, (self.__weight/2 - self.__font.size(self.__space_txt)[0]/2, self.__height/4))  # noqa
        # Paused Text
        elif self.__paused:
            self.__pause()
        # Game Won
        elif self.__playing == 3:
            self.__game_won()
        # Update screen
        pygame.display.update()
        self.__clock.tick(60)

    def on_execute(self):

        if self.__on_init() is False:
            self.__running = False

        while (self.__running):
            for event in pygame.event.get():
                self.__on_event(event)
            if not self.__paused and self.__playing != 0 and self.__playing != 3:  # noqa
                self.__on_loop()
            self.__on_render()


if __name__ == "__main__":
    pygame.init()
    display_surf = pygame.display.set_mode((800, 600), pygame.HWSURFACE | pygame.DOUBLEBUF)  # noqa
    game = Game(display_surf)
    game.on_execute()
