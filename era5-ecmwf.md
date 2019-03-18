- Create login credentials
- Accept license term: http://apps.ecmwf.int/datasets/licences/copernicus/

- Go to [https://api.ecmwf.int/v1/key/]
It will show something like this:

```
{
    "url"   : "https://api.ecmwf.int/v1",
    "key"   : "XXXXXXXXXXXXXXXXXXXXXX",
    "email" : "john.smith@example.com"
}
```

Copy this content to `$HOME/.ecmwfapirc`



Install the python 3 ECMWF API:


```
pip3 install --user https://software.ecmwf.int/wiki/download/attachments/56664858/ecmwf-api-client-python.tgz
```
