# document-uploader

Simple document uploader using [PyDrive](https://pypi.org/project/PyDrive/) library


Install dependecies:
```
pipenv install --deploy
```

\
`upload_list.json` example:
```
{
    "files": [
        {
            "fileName": "main.pdf"
        }
    ]
}
```

Usage:
```
python main.py
```


In order to use this project, you may need to [configure](https://pythonhosted.org/PyDrive/quickstart.html) your Google APIs console, and put into project folder `client_secrets.json`


