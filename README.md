# Setup
## Prerequisite
- docker
----------------------
This tool is developed using [linkedin scraper](https://github.com/joeyism/linkedin_scraper)
## Env setup
Build the image
```
./dev_build.sh
```
Start the container, note to modify the `dev_start.sh` script with the location of this repo which is going to be the persistent locaiton
```
./dev_start.sh
```
Enter the container
```
./dev_into.sh
```

## Inside the container

```
cd dev/webscraper
python3 linkedin_scraper.py
```

