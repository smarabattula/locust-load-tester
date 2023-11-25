# locust_csc547
Clone the repo using git clone command or on editor

Then install required dependencies via pip install locust

Add locust installation path onto $PATH variables via:

`pip show locust | grep "Location"

export PATH=$PATH:"<output_from_above>"`
Run command `locust`

If it doesn't work, try `"c:\users\sasan\appdata\roaming\python\python311\scripts\locust.exe" -f stages.py`
Access via localhost:8089!

