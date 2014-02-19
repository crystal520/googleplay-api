# separator used by search.py, categories.py, ...
SEPARATOR = "|"

LANG            = "en_US" # can be en_US, fr_FR, ...
ANDROID_ID      = "316ad35e91ceb3ae" # "xxxxxxxxxxxxxxxx"
GOOGLE_LOGIN    = "xxxxxx" # "username@gmail.com"
GOOGLE_PASSWORD = "xxxxxx"
AUTH_TOKEN      = None # "yyyyyyyyy"

# force the user to edit this file
if any([each == None for each in [ANDROID_ID, GOOGLE_LOGIN, GOOGLE_PASSWORD]]):
    raise Exception("config.py not updated")

