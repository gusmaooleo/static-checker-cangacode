'''
Orquestrador __main__ do static-checker.
'''
from syntax.controller import Controller
from utils.fileLoader import fileLoader

if __name__ == "__main__":
    path = fileLoader()
    controller = Controller(path)
    controller.run()
