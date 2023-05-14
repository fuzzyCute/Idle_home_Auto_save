# Building the project

## Virtual environment
You can create a python virtual environment to avoid "contaminating"
your system install of python with unnecessary dependencies.
```sh
python -m venv .venv
```
Once it’s been created, every time you want to start working in the virtual environment:
```sh
source .venv/Scripts/activate 
```
You can choose not to use a virtual environment, but in that case,
you need to make sure to have python and pip installed,
and have the Scripts folder of your main python install in the PATH env variable.

## Build project with dependencies (once)
```sh
pip install .
```

## Compile binary
```sh
pip install pyinstaller
pyinstaller auto_save.spec
```
The built binary will be generated in `dist/auto_save.exe`

## Sign binary

### Install Windows SDK (once)
Download and run the [Windows SDK installer](https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/).
For signing the .exe, you only actually need the component called "**App Certification Kit**", but feel free to keep the others components checked too.

### Generate certificate (once)
```ps
New-SelfSignedCertificate -Type CodeSigning -Subject "E=your@email.com,CN=www.yourname.com" -CertStoreLocation "cert:\CurrentUser\My"
```
Don’t forget to replace the placeholder email and domain name with your own...!

### Sign binary (every time you build the .exe)
```ps
 & "C:\Program Files (x86)\Windows Kits\10\App Certification Kit\signtool.exe" sign /fd SHA256 /n "www.yourname.com" /t http://timestamp.digicert.com .\dist\auto_save.exe
```
Don’t forget to replace the placeholder domain name with the one provided during certificate generation.
