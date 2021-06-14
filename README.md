# PythonAPITest
 Simple API Tests using Python. Python, Pytest, Docker, Requests, etc. 

# Run Locally
## Install Docker
https://www.docker.com/products/docker-desktop
## Install Visual Studio Code
https://code.visualstudio.com/download
### Setup Visual Studio Code
Extensions to install
- Name: **Remote Development**
    Id: ms-vscode-remote.vscode-remote-extensionpack
##### Building and runnning test framework
1. Open Visual Studio Code
2. File -> Open
3. Navigate to the cloned directory, and open it
4. When prompted **Folder contains a dev container configuration file. Reopen folder to develop in a container.** click on **Reopen in Container**

The required images, will then be either downloaded or built.  This will take a little while depending on your network speed and machines performance.  
Once this is completed, the framework should be ready to run tests.  

## Running tests in Terminal to generate a html report under reports
pytest -v --no-summary --html=/workspace/reports/report.html --self-contained-html pythonapi

## Better report using Allure
Only an examle in test_pet.py

# Generrate nunit XML report to supprt Calliope dashboard
Pytest is not supported by Calliope. So install pytest-nunit so can import result to dashboard.
pip3 install pytest-nunit
pytest pythonapi/tests -v --nunit-xml=APItest-results.xml

# Example Jenkinsfile to add a job to run in Docker
test.Jenkinsfile