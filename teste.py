import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configuração da tela
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Entrada de Números")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 128, 255)

# Fonte
font = pygame.font.Font(None, 50)

class TextInput:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 80, 80)
        self.font = font
        self.text_color = BLACK
        self.bg_color = WHITE
        self.text = ""
        self.active = False  # Indica se o campo está ativo para entrada

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Ativa o campo se o clique ocorrer dentro do retângulo
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                # Remove o último caractere
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN:
                # Finaliza a entrada de número
                return self.text
            else:
                # Adiciona o caractere digitado
                self.text += event.unicode
        return None

    def draw(self, screen):
        # Desenha o campo de texto
        pygame.draw.rect(screen, self.bg_color, self.rect)
        # Renderiza o texto
        text_surface = self.font.render(self.text, True, self.text_color)
        screen.blit(text_surface, (self.rect.x + 30, self.rect.y + 25))
        # Desenha a borda para indicar atividade
        pygame.draw.rect(screen, BLUE if self.active else BLACK, self.rect, 2)


class ArrayInput:
    def __init__(self):
        self.numbers = []  # Armazena os números inseridos
        self.text_input = TextInput(200, 250)

    def add_number(self, number):
        if number.isdigit():  # Verifica se é um número válido
            self.numbers.append(int(number))  # Adiciona ao array
        return number

    def display_numbers(self, screen):
        # Exibe os números na tela dentro de retângulos na horizontal
        x_position = 50  # Começo da posição no eixo X
        y_position = 350  # Posição fixa no eixo Y (não será alterada)
        box_width = 80  # Largura da caixinha
        box_height = 80  # Altura da caixinha

        for num in self.numbers:
            # Desenha o retângulo
            pygame.draw.rect(screen, BLUE, (x_position, y_position, box_width, box_height))  # Cor azul para o retângulo
            # Renderiza o número dentro do retângulo
            number_text = font.render(str(num), True, WHITE)  # Cor branca para o texto
            screen.blit(number_text, (x_position + (box_width - number_text.get_width()) // 2, y_position + (box_height - number_text.get_height()) // 2))
            
            x_position += 100  # Espaça as caixinhas horizontalmente

    def handle_events(self, event):
        number = self.text_input.handle_event(event)
        if number is not None:
            self.add_number(number)
            self.text_input.text = ""  # Limpa o campo após inserir o número


# Instância da classe que controla os números
array_input = ArrayInput()

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        array_input.handle_events(event)

    # Preenche o fundo
    screen.fill(WHITE)

    # Desenha o campo de texto
    array_input.text_input.draw(screen)

    # Exibe os números inseridos
    array_input.display_numbers(screen)

    # Atualiza a tela
    pygame.display.flip()

pygame.quit()
sys.exit()
