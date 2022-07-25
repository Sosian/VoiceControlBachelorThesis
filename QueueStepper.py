import json


class QueueStepper:
    def __init__(self, path, pygame): 
        self.pygame = pygame   
        self.currentStepIndex = 0
        self.currentChapterIndex = 0
        self.endReached = False
        
        chaptersFile = open(path)
        chaptersJson = json.load(chaptersFile)
        self.chapters = chaptersJson["chapters"]
        self.currentChapter = self.chapters[self.currentChapterIndex]
        self.currentSteps = self.currentChapter["steps"]
        
    def nextStep(self):
        currentStep = self.currentSteps[self.currentStepIndex]

        if (currentStep["stepFunction"] == "Music"):
            self.pygame.mixer.music.load(currentStep["file"])
            self.pygame.mixer.music.play(currentStep["loops"],0.0)
        if (currentStep["stepFunction"] == "Sound"):
            sound = self.pygame.mixer.Sound(currentStep["file"])
            sound.play()
        if (currentStep["stepFunction"] == "StopMusic"):
            self.pygame.mixer.music.stop()
            self.pygame.mixer.music.unload()

        self.currentStepIndex = self.currentStepIndex + 1
        if (self.currentStepIndex == len(currentStep)):  
            self.currentChapterIndex = self.currentChapterIndex + 1
            if (self.currentChapterIndex == len(self.chapters)):
                self.endReached = True    
            else:
                self.currentChapter = self.chapters[self.currentChapterIndex]
                self.currentSteps = self.currentChapter["steps"]
    
    def isEndReached(self):
        return self.endReached