from PygameManager import PygameManager
from QueueStepper import QueueStepper
import pygame

pygameManager = PygameManager(pygame)
pygameManager.setup()

queueStepper = QueueStepper("Chapters.json", pygame)

programmAktiv = True

while programmAktiv and not queueStepper.isEndReached():
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                programmAktiv = False
            if event.key == pygame.K_a:
                queueStepper.nextStep()
    pygameManager.clockTick()
pygameManager.teardown()