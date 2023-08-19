#### A simple blog api project built using python's fastApi framework.

### Steps to run this project locally:

##### Requirements:
* Python3
* Pip3


##### Installation (macOS):

```bash
$ brew install python3
```

Pip3 is installed with Python3

To install virtualenv via pip run:
```bash
$ pip3 install virtualenv
```

##### Usage
Creation of virtualenv:
```bash
$ virtualenv -p python3 <desired-path>
```

Activate the virtualenv:
```bash
$ source <desired-path>/bin/activate
```

Deactivate the virtualenv:
```bash
$ deactivate
```

After activating virtualenv, inside project's root directory, run below commands:
```bash
$ pip install requirements.txt
```

```bash
$ uvicorn main:app --reload
``` 
or 
```bash
$ python main.py
```

####  Then view your project running locally on: http://127.0.0.1:8080