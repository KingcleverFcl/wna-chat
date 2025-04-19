import os
import databases

DATABASE_URL = os.getenv("DATABASE_URL")

db = databases.Database(DATABASE_URL)
