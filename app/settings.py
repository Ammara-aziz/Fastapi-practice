from starlette.config import Config
from starlette.datastructures import Secret

try:
    config = Config(".env")
except FileNotFoundError:
    config = Config()

DATABASE_URL = config("DATABASE_URL", cast=Secret)

TEST_DATABASE_URL = config("TEST_DATABASE_URL", cast=Secret)

# postgresql://Lahore_owner:************@ep-rough-frost-a5qautsv.us-east-2.aws.neon.tech/FastApiproj?sslmode=require