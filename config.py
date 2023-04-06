import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "16445683"))
  API_HASH = os.environ.get("API_HASH", "d0852e13eee2389ff2d9183b00649547")
  BOT_TOKEN = os.getenv("BOT_TOKEN", "6264339891:AAHOaAyEFg3s4Rbl62adJtc3E9GfRg5TsNQ")
  STRINGSESSION = os.environ.get("STRINGSESSION", "BQD68PMAsUuiQekNe2Hug_bY4aLd7P0qBjB5C4nqnrlyZNl1k-8S01TL_-Hu6ayW0zSBZj31Ej74AsHCzUpudoKsMJ7chBQUBGpk8X7zzw0qHlrTRr4_tNY16lL8p64lD_EI3aU8AUKukeF3z3OtEPYhXkDr-11kFSTvcKWsl10HmQJunfUixERT6EMDCAJ0jGF-4CyIp3KVaRHjjJ0AhCiHonK1F59fqW032-pStVV08iHwuA3sFmaouJWt_Wq3AREn7O6SUxf_e-V7Um9FMd-8qebY6H_5bz2zgBnCh6VYPlOv9SoWkSHoKqWWtaix1KValRzrvgnZLPxEeIHyIOUdisTuwQAAAAFm2wNIAA")
  OWNER_ID = int(os.environ.get("OWNER_ID", "5651594253"))
  DATABASE_CHANNELS = os.environ.get("DATABASE_CHANNELS", ["-1001863769271"])
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://herokudeploye:herokudeploye@cluster0.m9r3mk8.mongodb.net/?retryWrites=true&w=majority")
  DELETE_DELAY = int(os.environ.get("DELETE_DELAY", 600))
  SUBSCRIPTION_TIME = int(os.getenv("SUBSCRIPTION_TIME", "31"))
  FORCESUB_CHANNEL = os.getenv("FORCESUB_CHANNEL", -100)
  OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "J_shree_ram")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "BetterFiltersV5_Bot")
