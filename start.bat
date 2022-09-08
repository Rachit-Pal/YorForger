@echo off
TITLE YorForger
:: Enables virtual env mode and then starts Yor
env\scripts\activate.bat && py -m YorForger
