from robocorp.tasks import task
from robocorp import browser

@task
def Level_II_robot():
    open_robotsparebinindustries()

def open_robotsparebinindustries():
    browser.goto("https://robotsparebinindustries.com/#/robot-order")
   
