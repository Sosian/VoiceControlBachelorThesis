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
        self.currentSteps = self.chapters[self.currentChapterIndex]["steps"]
        
    def nextStep(self):
        if (self.isLastStep() and self.isLastChapter()):
            self.endReached = True     
        else:
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

            if (self.isLastStep()):
                self.currentChapterIndex = self.currentChapterIndex + 1
                if (self.isLastChapter()):
                    self.endReached = True
                else:
                    self.currentSteps = self.chapters[self.currentChapterIndex]["steps"]
                    self.currentStepIndex = 0
    
    def isEndReached(self):
        return self.endReached

    def isLastStep(self):
        return (self.currentStepIndex == len(self.currentSteps))
    
    def isLastChapter(self):
        return (self.currentChapterIndex == len(self.chapters))