from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "22359038"))
    API_HASH = getenv("API_HASH", "b3901895dc193c30c808ba4f1b550ed0")
    BOT_TOKEN = getenv("BOT_TOKEN", "5918634201:AAH0xZTz2BkmjCT3P_KbfDPNDnsX_JBatYM")
    FSUB = getenv("FSUB", "REQUSET_ACCEPT_BOT")
    CHID = int(getenv("CHID", "-1001745001470"))
    SUDO = list(map(int, getenv("SUDO", "5531461861 1878911986").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Bastin:Bastin@cluster0.irj81sj.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
