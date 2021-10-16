import pyautogui
import time
from pynput.mouse import Button, Controller as MouseController
import pydirectinput as pdi

questAccepted = False
questDone = False
questTurnedIn = False

mouse = MouseController()


def AcceptQuest():
    global questAccepted
    global questDone
    availableCoordinates = pyautogui.locateOnScreen('Available_Not_Selected.png', confidence=.7)
    print(availableCoordinates)
    time.sleep(0.5)
    if availableCoordinates:
        pyautogui.click(availableCoordinates)
        time.sleep(0.5)
        mouse.press(Button.left)
        mouse.release(Button.left)
    time.sleep(0.5)
    questCoordinates = pyautogui.locateOnScreen('Quest_Available.png', confidence=.7)
    print(questCoordinates)
    if questCoordinates:
        pyautogui.moveTo(questCoordinates)
        time.sleep(0.5)
        mouse.press(Button.left)
        mouse.release(Button.left)
    else:
        questAccepted = True
        questDone = False
        inProgressCoordinates = pyautogui.locateOnScreen('In_Progress.png', confidence=.7)
        print(inProgressCoordinates)
        if inProgressCoordinates:
            pyautogui.moveTo(inProgressCoordinates)
            time.sleep(0.5)
            mouse.press(Button.left)
            mouse.release(Button.left)
        return
    time.sleep(0.5)
    acceptCoordinates = pyautogui.locateOnScreen('Accept_Quest.png', confidence=.85)
    pyautogui.moveTo(acceptCoordinates)
    time.sleep(0.5)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.5)
    for i in range(8):
        pdi.press(" ")
        time.sleep(0.5)
    inProgressCoordinates = pyautogui.locateOnScreen('In_Progress.png', confidence=.85)
    if inProgressCoordinates:
        pyautogui.moveTo(inProgressCoordinates)
        time.sleep(0.5)
        mouse.press(Button.left)
        mouse.release(Button.left)
    questAccepted = True
    questDone = False
    time.sleep(0.5)
    pdi.press('l')


def CheckIfQuestDone():
    global questDone
    time.sleep(1)
    print("checking if quest done")
    completedCoordinates = pyautogui.locateOnScreen('Quest_Completed.png', confidence=.9)
    print(completedCoordinates)
    if completedCoordinates:
        questDone = True
    else:
        questDone = False


def TurnInQuest():
    print("turning in")
    rewardCoordinates = pyautogui.locateOnScreen('Quest_Reward.png', confidence=.7)
    if rewardCoordinates:
        pyautogui.moveTo(rewardCoordinates)
        time.sleep(0.5)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(1)
        pdi.press(" ")
        pdi.press(" ")
        pdi.press(" ")
        pdi.press(" ")
        time.sleep(1)
        pdi.press('l')
    global questAccepted
    global questDone
    questAccepted = False
    questDone = False


if __name__ == "__main__":
    while True:
        AcceptQuest()
        print(questAccepted)
        while questDone is False and questAccepted is True:
            CheckIfQuestDone()
            print(questDone, questAccepted)
        TurnInQuest()



