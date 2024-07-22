import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "24715632"))
    API_HASH = os.environ.get("API_HASH", "dc1320bd5c50d6834a5abe2e343b0bee")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7269198396:AAFKKvA7u_oTIWYZwvqYCBAAZLKnM49tRwM")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "6648168722")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://uhdprime:uhdprime@cluster0.ry5y4yk.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQF5IXAADlgaGdzQdKlVEMK5UPm1ngACni1JYFrSb191tDVX2-lQtdSdXB4lXBW0p6NOABOapDC595UvRyI73-yHnfA7HC3O9CcbgCe_NBIiXL19cvzJX9c3WxQt5YFDiFii0BrVhDh_rHX5kig5PpjpH72azdRvseOc0J7nEGsCvXZhHLYvoRQAtjntRXSu9p5q8xbKBhdsJuWI_qNA9wgsH-BfOIc2O3knGgSdtUFPylRvC42FjKkajYIH2znF9mC8sU4T7rQW-Hmd_yHvuPvGfSpC2bR6Cqz-GqiVDe5o5BMgyNQQr3PRTfbBcdFlLFXiI6h8H2RkETdAbDrIxdpi9FOzQgAAAAGMQwESAA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1002055068009"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "orgpostforwardbot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
