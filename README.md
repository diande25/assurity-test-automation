# assurity-test-automation

Assurity test automation is intended to be the Automated Regression for TM Sandbox API using Behavioral Data Driven approach.
This is a Hybrid Test Automation Framework that uses Robot Framework and Python as its main testing framework and language. 

## Getting Started

### Prerequisites

1. Any Integrated Development Environment(IDE) for Python is installed in your machine (PyCharm, Visual Studio, IntelliJ and others).
2. Clone working assurity-test-automation repository [here](https://github.com/diande25/assurity-test-automation)
```
git clone https://github.com/diande25/assurity-test-automation.git
```

### Installing
1. Download and Install [Python 3.7x](https://www.python.org/downloads/)
2. Install [pip](https://pip.pypa.io/en/stable/installing/#do-i-need-to-install-pip)
```
python get-pip.py
```
3. Install needed python modules
```
cd \path-to\assurity-test-automation\requirements
pip install -r requirements.txt
```

For Windows 10 x64, necessary modules and libraries are already included in assurity-test-automation venv folder. 
Just activate the virtual env in machine. 

Install virtualenv via pip
```
pip install virtualenv
```

Activate virtualenv
```
virtualenv venv
. .\venv\Scripts\activate.bat
```
To deactivate virtualenv
```
. .\venv\Scripts\deactivate.bat
```

## Running the tests

3 Ways to Execute the Test.

**1. Running via Terminal**

*   Go to the working directory of assurity-test-automation
```    
cd \path-to\assurity-test-automation
```
*   Enter the following command in terminal:
```
robot -d assurity\api\testresults assurity\api\testcases\UAT_TMSandbox.robot
```

**2. Running via IDE (PyCharm) - External Tools**
*  To execute single test case
*     Go to Pycharm Preferences -> Tools -> External Tools
*     Create Tool
        - Name: Run Selected Test Case
        - Program: C:\Users\path-to\assurity-test-automation\venv\Scripts\robot.bat
        - Argument: -d \path-to\assurity\api\testresults --test "$SelectedText$" $FileDir$
        - Working Directory: $ProjectFileDir
        
*  To execute entire test suite
*     Go to Pycharm Preferences -> Tools -> External Tools
*     Create Tool
          - Name: Run Entire Test Suite
          - Program: C:\Users\path-to\assurity-test-automation\venv\Scripts\robot.bat
          - Argument: -d \path-to\assurity\api\testresults $FileDir$
          - Working Directory: $ProjectFileDir$

        
 **Execution Steps:**
  *  For Single test case
```
Highlight a test case -> right click -> External Tools > Run Selected Test Case
```

 * For All test cases
 ```
Highlight any test case -> right click -> External Tools > Run All Test Case on File
```

**3. Running in Jenkins (Continuous Integration)**

* To be added...

## Built With

* [Robot Framework](http://robotframework.org/) - Automation Framework
* [PyCharm](https://www.jetbrains.com/pycharm/) - IDE
* [Python](https://www.python.org/) - Programming Language
* [Behavioral Driven Development](https://en.wikipedia.org/wiki/Behavior-driven_development) - Approach for API testing

## Contributing to the Repository

Do you intend to add a new feature or change an existing one?

* Open a new Pull Request and put a description that clearly defines what will be the changes for.
* Make sure you're not directly pushing to the master branch by using a fork of your own branch

## Authors

* **Diana I. De Chavez** - *Initial work* -

See also the list of [contributors](https://github.com/diande25/assurity-test-automationn/contributors) who participated in this project.

