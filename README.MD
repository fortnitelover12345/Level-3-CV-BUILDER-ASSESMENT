Set-ExecutionPolicy Unrestricted -Scope Process ;  .venv/Scripts/activate ; cd launchpad ;  py manage.py runserver
Get-ChildItem -Path . -Filter "desktop.ini" -Recurse -Force -ErrorAction SilentlyContinue | Remove-Item -Force

 Launchpad CVS
Created by Karamveer Singh
## How to Run Launchpad CVS?
Insert these following commands at the **root** of the directory.

First create a virtual environment:
`
py -m venv .venv
`\
Next install the following frameworks & libraries:
> [!TIP]
> The "--upgrade pip" may not be necessary if already to date.
```
py -m pip install django
py -m pip install Pillow
py -m pip install --upgrade pip
```
Once those are installed use the connected command to run:
> [!Note]
> The "Set-ExecutionPolicy" is only there because powershell disables scripts by default. It will only give temporary access while launching.
```
Set-ExecutionPolicy RemoteSigned -Scope Process ; 
.venv/Scripts/activate ; 
cd clarity ; 
py manage.py runserver 6464
```
Now everything should be complete and you can go to the following link: 
[Local Host](http://127.0.0.1:8000/)