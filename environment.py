import pygame
import sys
import random

''' TODO:
    - The agent is not respecting the grid
    - Figure out why it's being so slow
    - Have better understanding of agent's fitness
'''

class Agent:
    def __init__(self, size, rows):
        self.size = size
        self.rows = rows
        self.grid_size = size // rows
        self.x = self.grid_size * (rows // 2)
        self.y = self.grid_size * (rows // 2)
        self.color = (0, 255, 0) 
        self.directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        self.direction_idx = 0  

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.grid_size, self.grid_size))

    def decide_move(self, rewards):
        action = random.choice(['move forward', 'turn left', 'turn right'])

        if action == 'move forward':
            direction = self.directions[self.direction_idx]
            self.x += direction[0] * self.grid_size
            self.y += direction[1] * self.grid_size
        elif action == 'turn left':
            self.direction_idx = (self.direction_idx - 1) % 4
        elif action == 'turn right':
            self.direction_idx = (self.direction_idx + 1) % 4

        self.collect_rewards(rewards)

    def collect_rewards(self, rewards):
        for reward in rewards:
            if reward[0] == self.x and reward[1] == self.y:
                rewards.remove(reward)
                break

class Environment:
    def __init__(self, size, rows, num_rewards):
        pygame.init()
        self.size = size
        self.rows = rows
        self.num_rewards = num_rewards
        self.rewards_list = self.generate_rewards()
        self.agent = Agent(size, rows)
        self.window = pygame.display.set_mode((size, size))
        pygame.display.set_caption("Environment")

    def generate_rewards(self):
        grid_size = self.size // self.rows
        rewards_list = []
        while len(rewards_list) < self.num_rewards:
            x = random.randint(0, self.rows - 1) * grid_size
            y = random.randint(0, self.rows - 1) * grid_size
            rewards_list.append((x, y))
        return rewards_list

    def draw_grid(self):
        grid_size = self.size // self.rows
        for i in range(self.rows + 1):
            pygame.draw.line(self.window, (255, 255, 255), (i * grid_size, 0), (i * grid_size, self.size))
            pygame.draw.line(self.window, (255, 255, 255), (0, i * grid_size), (self.size, i * grid_size))
        for reward in self.rewards_list:
            pygame.draw.circle(self.window, (255, 0, 0), (reward[0] + grid_size // 2, reward[1] + grid_size // 2), grid_size // 4)
        self.agent.draw(self.window)

    def redraw(self):
        self.window.fill((0, 0, 0))
        self.draw_grid()
        pygame.display.update()

    def run(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.agent.decide_move(self.rewards_list)
            self.redraw()
            clock.tick(5)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    env = Environment(640, 32, 86)
    env.run()
