import os
class Configuration:
  MONGO_DB = os.environ.get("MONGO_DB", "db")
  MONGO_URI = os.environ.get("MONGO_URI", "mongodb://user:password@localhost/db")
  SECONDS = int(os.environ.get("SECONDS", "30"))