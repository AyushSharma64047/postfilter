import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "6019847133"))
  API_HASH = os.environ.get("API_HASH", "34a0b2551aacd866c3729f7044525353")
  BOT_TOKEN = os.getenv("BOT_TOKEN", "6019847133:AAHFcXabIXDJvERwbWfsBtOJf_X2XfHB6Rg")
  STRINGSESSION = os.environ.get("STRINGSESSION", "BQD68PMAsUuiQekNe2Hug_bY4aLd7P0qBjB5C4nqnrlyZNl1k-8S01TL_-Hu6ayW0zSBZj31Ej74AsHCzUpudoKsMJ7chBQUBGpk8X7zzw0qHlrTRr4_tNY16lL8p64lD_EI3aU8AUKukeF3z3OtEPYhXkDr-11kFSTvcKWsl10HmQJunfUixERT6EMDCAJ0jGF-4CyIp3KVaRHjjJ0AhCiHonK1F59fqW032-pStVV08iHwuA3sFmaouJWt_Wq3AREn7O6SUxf_e-V7Um9FMd-8qebY6H_5bz2zgBnCh6VYPlOv9SoWkSHoKqWWtaix1KValRzrvgnZLPxEeIHyIOUdisTuwQAAAAFm2wNIAA")
  OWNER_ID = int(os.environ.get("OWNER_ID", "1413071149"))
  DATABASE_CHANNELS = os.environ.get("DATABASE_CHANNELS", ["-1001898364516"])
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://herokudeploye:herokudeploye@cluster0.m9r3mk8.mongodb.net/?retryWrites=true&w=majority")
  DELETE_DELAY = int(os.environ.get("DELETE_DELAY", "600"))
  SUBSCRIPTION_TIME = int(os.getenv("SUBSCRIPTION_TIME", "360"))
  FORCESUB_CHANNEL = os.getenv("FORCESUB_CHANNEL", "-1001557431626")
  OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "sigma_male_007")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "Auto_Post_Filter_Bot")
