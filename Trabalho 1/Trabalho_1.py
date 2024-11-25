import pygame
import sys

# Inicializa o Pygame
pygame.init()

#cores do jogo
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (33, 90, 54)
LIGHT_GREEN = (125, 255, 95)
YELLOW = (250, 216, 17)
RED = (249, 17, 17)
ORANGE = (250, 124, 17)

# Configuração da tela
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("TRABALHO de AED II")
font = pygame.font.Font("minha_fonte.ttf", 25)
small_font = pygame.font.Font("minha_fonte.ttf", 15)
clock = pygame.time.Clock()

# Define a classe do Botão
class Button:
    def __init__(self, x, y, width, height, text, color, text_color):
        self.rect = pygame.Rect(x, y, width, height) # desenha o botão
        self.color = color # cor do botão
        self.text = text # texto sobre o botão
        self.text_color = text_color
        self.font = font # fonte do texto (global)

    def draw_button(self, screen):
        # Desenha o retângulo do botão, recebendo a tela, a cor, o retangulo e raio da borda 5
        pygame.draw.rect(screen, self.color, self.rect, border_radius= 5)
        
        # Renderiza e desenha o texto centralizado no botão
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
        
    def is_clicked(self, mouse_pos):
        # Verifica se o botão foi clicado
        return self.rect.collidepoint(mouse_pos)

#para inserir inputs na tela
class TextInput:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 80, 80) # desenha a área do input na tela
        self.text = "" # texto da área
        self.active = False # só ativa hora que clicar nele
        self.font_size = 36  # Tamanho inicial da fonte

        # Carrega a fonte customizada (minha-fonte.ttf)
        self.font_path = "minha_fonte.ttf"  # Caminho da fonte customizada
        self.font = pygame.font.Font(self.font_path, self.font_size)

    def handle_event(self, event):
        # essa função controla os eventos que acontecem com o input de texto
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos) # ativa a caixa de input (fica azul)
        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE: # apaga o texto
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER: # isso confirma o texto e envia para o array
                return self.text
            else:
                self.text += event.unicode # isso incrementa o caractere inserido no texto a ser exibido

    def draw(self, screen):
        # Calcula o tamanho da fonte baseado no comprimento do texto
        max_font_size = 36  # Tamanho máximo da fonte
        min_font_size = 18  # Tamanho mínimo da fonte

        text_length = len(self.text)
        # Ajusta o tamanho da fonte baseado no comprimento do texto
        if text_length == 0:
            self.font_size = max_font_size
        else:
            # Calcula o novo tamanho da fonte
            self.font_size = max(min_font_size, max_font_size - (text_length * 2))

        # Atualiza a fonte com o novo tamanho
        self.font = pygame.font.Font(self.font_path, self.font_size)

        # Desenha o campo de texto
        pygame.draw.rect(screen, WHITE, self.rect)
        text_surface = self.font.render(self.text, True, BLACK)

        # Centraliza o texto dentro do campo de entrada
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

        pygame.draw.rect(screen, BLUE if self.active else BLACK, self.rect, 2, border_radius= 5)

class Text:
    def __init__(self, text, x, y):
        """
        Inicializa o texto.
        :param text: O texto que será exibido.
        :param x: Posição X na tela.
        :param y: Posição Y na tela.
        :param font_size: Tamanho da fonte.
        :param color: Cor do texto (RGB).
        """
        self.text = text
        self.x = x
        self.y = y
        self.color = BLACK
        self.font_size = 36
        self.font_path = "minha_fonte.ttf"  # Caminho da fonte customizada
        self.font = pygame.font.Font(self.font_path, self.font_size)

    def draw(self, screen):
        """
        Renderiza e desenha o texto na tela.
        :param screen: Superfície do Pygame onde o texto será desenhado.
        """
        # Renderiza o texto
        text_surface = self.font.render(self.text, True, self.color)
        # Desenha o texto na posição especificada
        screen.blit(text_surface, (self.x, self.y))
    
#para inserir Array
class ArrayInput:
    def __init__(self):
        self.numbers = [] # define os numeros do array
        self.text_input = TextInput(360, 190) # coloca o texto na tela

    def add_number(self, number): # verifica se a entrada do usuário é valida (int)
        if number.isdigit():
            self.numbers.append(int(number))

    def display_numbers(self, screen): 
        max_width = 700  # Largura máxima disponível na tela para os quadrados
        max_numbers = len(self.numbers)  # Total de números no array
        
        # Define tamanho dos quadrados e espaçamento com base no número de elementos
        if max_numbers > 0:
            circle_size = min(80, max_width // max_numbers - 10)  # Calcula tamanho dinâmico
            padding = 10  # Espaço fixo entre quadrados
        else:
            circle_size = 80
            padding = 20

        x_position = 50  # Posição inicial no eixo X

        for num in self.numbers:
            # Desenha o quadrado
            pygame.draw.rect(screen, LIGHT_GREEN, (x_position, 350, circle_size, circle_size), border_radius=5)

            # Renderiza o número com a fonte fixa
            number_text = font.render(str(num), True, WHITE)

            # Centraliza o texto dentro do quadrado
            text_rect = number_text.get_rect(center=(x_position + circle_size // 2, 350 + circle_size // 2))
            screen.blit(number_text, text_rect)

            # Move para o próximo quadrado
            x_position += circle_size + padding
            
    def handle_events(self, event): #controla os eventos da função que acontecem com o array
        number = self.text_input.handle_event(event)
        if number is not None:
            self.add_number(number)
            self.text_input.text = ""
            
    def selection_sort_visual(self, screen, clock):
        """
        Ordena os números usando Selection Sort, com visualização.
        """
        n = len(self.numbers)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                # Destaca o elemento sendo comparado
                screen.fill(WHITE)
                self._highlight_numbers(screen, i, j, min_index)
                pygame.display.flip()
                clock.tick(5)

                if self.numbers[j] < self.numbers[min_index]:
                    min_index = j

            # Troca os elementos com animação
            if i != min_index:
                self._swap_animation(screen, clock, i, min_index)

            # Atualiza a tela após a troca
            screen.fill(WHITE)
            self.display_numbers(screen)
            pygame.display.flip()
            clock.tick(10)
            # Realiza a troca no array após a animação
        self.numbers[i], self.numbers[j] = self.numbers[j], self.numbers[i]

    def _highlight_numbers(self, screen, i, j, min_index):
        """Destaca os números sendo comparados e o menor atual, com tamanho dinâmico de quadrados."""
        max_width = 700  # Largura máxima disponível para os quadrados
        max_numbers = len(self.numbers)  # Total de números no array

        # Calcula o tamanho dinâmico do quadrado
        if max_numbers > 0:
            circle_size = min(80, max_width // max_numbers - 10)  # Tamanho dinâmico
            padding = 10  # Espaço fixo entre quadrados
        else:
            circle_size = 80
            padding = 20

        x_position = 50  # Posição inicial no eixo X
        y_position = 350  # Altura fixa para exibição dos quadrados

        # Preenche o fundo
        screen.fill(WHITE)

        # Redesenha todos os números com estilos padrões ou destacados
        for index, num in enumerate(self.numbers):
            # Escolhe a cor do quadrado
            if index == min_index:
                color = RED  # Menor atual em vermelho
            elif index == i or index == j:
                color = ORANGE # Comparando os elementos i e j
            else:
                color = YELLOW  # Padrão para os demais

            # Desenha o quadrado
            pygame.draw.rect(screen, color, (x_position, y_position, circle_size, circle_size), border_radius=5)

            # Renderiza o número
            number_text = font.render(str(num), True, WHITE if color != WHITE else BLACK)
            text_rect = number_text.get_rect(center=(x_position + circle_size // 2, y_position + circle_size // 2))
            screen.blit(number_text, text_rect)

            # Move para o próximo quadrado
            x_position += circle_size + padding

        # Atualiza a tela
        pygame.display.flip()

    def _swap_animation(self, screen, clock, i, j):
        """Anima a troca de dois elementos, permitindo que os números acompanhem as caixas."""
        max_width = 700  # Largura máxima disponível para os quadrados
        max_numbers = len(self.numbers)  # Total de números no array

        # Calcula o tamanho dinâmico do quadrado
        if max_numbers > 0:
            circle_size = min(80, max_width // max_numbers - 10)  # Tamanho dinâmico
            padding = 10  # Espaço fixo entre quadrados
        else:
            circle_size = 80
            padding = 20

        # Calcula as posições iniciais
        x_start = 50 + i * (circle_size + padding)
        x_end = 50 + j * (circle_size + padding)
        y_position = 350

        # Configura a velocidade da troca
        swap_speed = 2  # Velocidade de movimento (ajustável)

        # Define as posições atuais
        current_x1, current_x2 = x_start, x_end

        # Anima até que ambos os elementos cheguem às suas posições finais
        while current_x1 != x_end or current_x2 != x_start:
            # Atualiza a posição do primeiro elemento
            if current_x1 != x_end:
                current_x1 += swap_speed if current_x1 < x_end else -swap_speed
                if (current_x1 > x_end and x_start < x_end) or (current_x1 < x_end and x_start > x_end):
                    current_x1 = x_end

            # Atualiza a posição do segundo elemento
            if current_x2 != x_start:
                current_x2 += swap_speed if current_x2 < x_start else -swap_speed
                if (current_x2 > x_start and x_end < x_start) or (current_x2 < x_start and x_end > x_start):
                    current_x2 = x_start

            # Redesenha a tela a cada passo da animação
            screen.fill(WHITE)  # Limpa a tela (ou ajuste a cor de fundo)
            self.display_numbers(screen)  # Exibe os números fixos na tela

            # Desenha os quadrados e números em movimento
            pygame.draw.rect(screen, RED, (current_x1, y_position, circle_size, circle_size), border_radius=5)
            pygame.draw.rect(screen, RED, (current_x2, y_position, circle_size, circle_size), border_radius=5)

            # Desenha os números dentro dos quadrados móveis
            number_text1 = font.render(str(self.numbers[i]), True, WHITE)
            number_text2 = font.render(str(self.numbers[j]), True, WHITE)

            # Centraliza os textos nos quadrados móveis
            text_rect1 = number_text1.get_rect(center=(current_x1 + circle_size // 2, y_position + circle_size // 2))
            text_rect2 = number_text2.get_rect(center=(current_x2 + circle_size // 2, y_position + circle_size // 2))

            screen.blit(number_text1, text_rect1)
            screen.blit(number_text2, text_rect2)

            # Atualiza a tela
            pygame.display.flip()
            clock.tick(60)  # Define o FPS

        # Realiza a troca no array após a animação
        self.numbers[i], self.numbers[j] = self.numbers[j], self.numbers[i]
        
    def heap_sort_visual(self, screen, clock):
        """
        Ordena os números usando Heap Sort, com visualização.
        """
        n = len(self.numbers)

        def heapify(n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and self.numbers[left] > self.numbers[largest]:
                largest = left
            if right < n and self.numbers[right] > self.numbers[largest]:
                largest = right

            if largest != i:
                # Chama a animação de troca
                self._swap_animation(screen, clock, i, largest)
                heapify(n, largest)

        # Construir o Max Heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        # Extração dos elementos
        for i in range(n - 1, 0, -1):
            self._swap_animation(screen, clock, 0, i)
            heapify(i, 0)

        # Atualiza o estado final na tela
        screen.fill(WHITE)
        self.display_numbers(screen)
        pygame.display.flip()
        clock.tick(10)
    
    def radix_sort_visual(self, screen, clock):
        """
        Ordena os números usando Radix Sort com animação.
        """
        # Função para obter o dígito em uma determinada posição (base 10)
        def get_digit(num, exp):
            return (num // exp) % 10

        # Função para realizar a contagem (counting sort) com base no dígito fornecido
        def counting_sort(exp):
            # Cria a lista de contagem (0-9)
            count = [0] * 10
            output = [0] * len(self.numbers)

            # Armazena a contagem das ocorrências dos dígitos
            for num in self.numbers:
                index = get_digit(num, exp)
                count[index] += 1

            # Altera count[i] para representar a posição final de cada dígito
            for i in range(1, 10):
                count[i] += count[i - 1]

            # Construa a saída com base na contagem
            for i in range(len(self.numbers) - 1, -1, -1):
                num = self.numbers[i]
                index = get_digit(num, exp)
                output[count[index] - 1] = num
                count[index] -= 1

            # Atualiza os números com a saída ordenada
            for i in range(len(self.numbers)):
                self.numbers[i] = output[i]

        max_num = max(self.numbers)  # Encontra o maior número
        exp = 1  # Começa a ordenar pelo dígito das unidades

        # Enquanto houver dígitos a serem processados
        while max_num // exp > 0:
            # Exibe o estado atual do array antes de cada passo
            screen.fill(WHITE)

            # Divida os números em baldes (de 0 a 9) para visualização
            buckets = [[] for _ in range(10)]  # Cria 10 baldes

            for num in self.numbers:
                index = get_digit(num, exp)
                buckets[index].append(num)

            # Ajuste os baldes para caber na tela de 800x600
            bucket_width = 60  # Reduzi a largura do balde
            bucket_spacing = 70  # Diminui o espaçamento entre os baldes
            max_buckets = 10  # Número máximo de baldes

            # Calcula o número de baldes a ser desenhado
            for i in range(10):
                bucket_x = 50 + i * bucket_spacing  # Ajusta a posição dos baldes
                if bucket_x + bucket_width > 800:  # Se o balde ultrapassar a tela, ajusta
                    break  # Sai do loop caso ultrapasse a largura da tela
                pygame.draw.rect(screen, BLUE, (bucket_x, 150, bucket_width, 180), border_radius= 5)  # Desenha o balde
                bucket_text = small_font.render(f'Balde {i}', True, BLACK)  # Fonte menor para o texto do balde
                screen.blit(bucket_text, (bucket_x + 10, 120))  # Exibe o texto do balde

                # Coloca os números nos baldes
                y_offset = 170
                for num in buckets[i]:
                    num_text = font.render(str(num), True, WHITE)
                    screen.blit(num_text, (bucket_x + 10, y_offset))  # Desenha o número
                    y_offset += 30

            # Exibe o array atual
            self.display_numbers(screen)

            pygame.display.flip()

            # Delay para manter os baldes visíveis por mais tempo
            pygame.time.delay(3000)  # Aguarda 1 segundo antes de continuar com o próximo passo

            # Realiza o counting sort com base no dígito atual
            counting_sort(exp)

            # Atualiza a tela após reorganizar os números
            screen.fill(WHITE)
            self.display_numbers(screen)  # Exibe o array atualizado
            pygame.display.flip()

            # Controla a velocidade da animação
            clock.tick(1)  # Espera para mostrar o estado

            exp *= 10  # Passa para o próximo dígito (decimais, centenas, etc.)

        # Exibe o array final ordenado
        screen.fill(WHITE)
        self.display_numbers(screen)
        pygame.display.flip()
        clock.tick(1)  # Espera um pouco para mostrar o array final

    
#Função da tela do Selection Sort
def selection_screen(screen):
    running = True
    text_over = Text("Insira um número inteiro e pressione ENTER",50, 100)
    back_button = Button(300, 500, 200, 50, "Back to Menu", BLACK, WHITE)
    go_button = Button(300, 440, 200, 50, "Go!", GREEN, WHITE)
    array_input = ArrayInput()

    # Acho q o erro tá aqui
    while running: # enquanto essa tela estiver sendo exibida
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # se eu clicar em quit, quita
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and go_button.is_clicked(event.pos): # 
                array_input.selection_sort_visual(screen, clock)    
            elif event.type == pygame.MOUSEBUTTONDOWN and back_button.is_clicked(event.pos): #     
                return "menu_screen"
            
            array_input.handle_events(event)
                    
        #desenha os elementos na tela de game
        screen.fill(WHITE)
        text_over.draw(screen)
        array_input.text_input.draw(screen)
        array_input.display_numbers(screen)
        go_button.draw_button(screen)
        back_button.draw_button(screen)
        
        pygame.display.flip()

#Função da tela do Radix Sort
def radix_screen(screen):
    running = True
    text_over = Text("Insira um número inteiro e pressione ENTER",50, 100)
    back_button = Button(300, 500, 200, 50, "Back to Menu", BLACK, WHITE)
    go_button = Button(300, 440, 200, 50, "Go!", GREEN, WHITE)
    array_input = ArrayInput()

    while running: # enquanto essa tela estiver sendo exibida
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # se eu clicar em quit, quita
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and go_button.is_clicked(event.pos): # 
                array_input.radix_sort_visual(screen, clock)
            elif event.type == pygame.MOUSEBUTTONDOWN and back_button.is_clicked(event.pos): # 
                return "menu_screen"
            array_input.handle_events(event)
                    
        #desenha os elementos na tela de game
        screen.fill(WHITE)
        go_button.draw_button(screen)
        back_button.draw_button(screen)
        text_over.draw(screen)
        array_input.text_input.draw(screen)
        array_input.display_numbers(screen)
        pygame.display.flip()

#Função da tela do Heap Sort
def heap_screen(screen):
    running = True
    text_over = Text("Insira um número inteiro e pressione ENTER",50, 50)
    back_button = Button(300, 500, 200, 50, "Back to Menu", BLACK, WHITE)
    go_button = Button(300, 440, 200, 50, "Go!", GREEN, WHITE)
    array_input = ArrayInput()

    while running: # enquanto essa tela estiver sendo exibida
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # se eu clicar em quit, quita
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and go_button.is_clicked(event.pos): # 
                array_input.heap_sort_visual(screen, clock)
            elif event.type == pygame.MOUSEBUTTONDOWN and back_button.is_clicked(event.pos): # 
                return "menu_screen"
            array_input.handle_events(event)
                    
        #desenha os elementos na tela de game
        screen.fill(WHITE)
        text_over.draw(screen)
        array_input.text_input.draw(screen)
        array_input.display_numbers(screen)
        go_button.draw_button(screen)
        back_button.draw_button(screen)
        pygame.display.flip()

#Função da tela inicial (menu)
def menu_screen(screen):
    #define botões do menu
    running = True
    selection_button = Button(300, 100, 200, 50, "Selection Sort", GREEN, WHITE)
    heap_button = Button(300, 200, 200, 50, "Heap Sort", GREEN, WHITE)
    radix_button = Button(300, 300, 200, 50, "Radix Sort", GREEN, WHITE)
    exit_button = Button(300, 400, 200, 50, "Exit", BLACK, WHITE)
    next_screen = None
    description_text = Text('Kauan Domingues de Souza - 170347', 100, 500)
    prof_text = Text('Prof. Dr. Reginaldo Massanobu Kuroshu', 100, 540)
    #enquanto o menu estiver rodando
    while running:
        for event in pygame.event.get():
            #se usuário dá quit, saia
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                #se clicou em start, vá para a tela game_screen
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if selection_button.is_clicked(event.pos):  #se o botão clicado foi Selection Sort, vá para essa tela
                    next_screen = "selection_screen"
                    running = False #sai do loop running
                    
                elif heap_button.is_clicked(event.pos):     #se o botão clicado foi Heap Sort, vá para essa tela
                    next_screen = "heap_screen"
                    running = False #sai do loop running
                
                elif radix_button.is_clicked(event.pos):    #se o botão clicado foi Radix Sort, vá para essa tela
                    next_screen = "radix_screen"
                    running = False #sai do loop running
                    
                    #se clicou em Exit, dá quit no jogo
                elif exit_button.is_clicked(event.pos):
                    pygame.quit()
                    sys.exit()

        #preenche a tela de menu com os elementos
        screen.fill(WHITE)
        selection_button.draw_button(screen)
        heap_button.draw_button(screen)
        radix_button.draw_button(screen)
        exit_button.draw_button(screen)
        description_text.draw(screen)
        prof_text.draw(screen)
        pygame.display.flip()
        
    #vai para outra tela após sair do loop running
    return next_screen

# Função principal para controlar o fluxo
def main_controller():
    screen_mapping = {
        "menu_screen": menu_screen,           #tela de menu (inicial)
        "selection_screen": selection_screen, #tela de Selection Sort
        "heap_screen": heap_screen,           #tela de Heap Sort
        "radix_screen": radix_screen          #tela de Radix Sort
    }
    current_screen = "menu_screen"            #tela atutal

    #essa função permite passar para a proxima tela, pegando screen (global) para desenhar a tela
    while True:
        next_screen = screen_mapping[current_screen](screen)
        if next_screen:
            current_screen = next_screen

# Executa o jogo
if __name__ == "__main__":
    main_controller()