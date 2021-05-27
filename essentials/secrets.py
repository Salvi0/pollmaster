class Secrets:
    def __init__(self):
        self.dbl_token = ''  # DBL token (only needed for public bot)
        self.mongo_db = 'mongodb+srv://modmail:luna@cluster0.wlkwe.mongodb.net/'
        self.bot_token = 'NjQ0MjY0NTk4OTcwODI2NzUy.XcxgKg.ouBiu0_3Rn9qmb4TcK2-XmhRGvg' # official discord bot token
        self.mode = 'development' # or production

SECRETS = Secrets()
