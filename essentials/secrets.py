class Secrets:
    def __init__(self):
        self.dbl_token = ''  # DBL token (only needed for public bot)
        self.mongo_db = 'mongodb+srv://modmail:luna@cluster0.wlkwe.mongodb.net/'
        self.bot_token = 'NjkyODI0NTQ2MjQzNTEwNDMy.Xn0JIw.ySHCu_8ik8jzCzJp9TOs80z8nIs' # official discord bot token
        self.mode = 'development' # or production

SECRETS = Secrets()
