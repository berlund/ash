# Auto screen capture for Google Maps

## Prerequisites

### Virtual Env
Although not strictly needed, it is recommended to run this script in virtual env.

```bash
> pip3.7 install virtualenv
> virtualenv env
> source env/bin/activate
```

If you are done, you can leave your virtual env running

```bash
deactivate
```

### Python dependencies
Install Python dependencies with
```
> pip install -r requirements.txt
```

### Selenium drivers
Place the latest version of [geckodriver](https://github.com/mozilla/geckodriver/releases) or
[chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads), depending on what browser you will use.

Place the drivers in the `bin` folder or make them available in you `PATH`.

## Usage

* Choose Google Maps area in a web browser and set it in `screenshot.py`
* Set the right schedule in `timer.py`
* Run it with `python timer.py`, alternatively run `./run.sh`