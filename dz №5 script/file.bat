@echo off
md newDir
cd newDir
py -m venv venv
call ".\venv\Scripts\activate"
pip install django
django-admin startproject projectNew .
pip freeze > requirements.txt