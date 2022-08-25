class Response():
    status_txt: str
    long_url: str
    short_url: str

    def __init__(self, status_txt: str, long_url: str, short_url: str) -> None:
        self.status_txt = status_txt
        self.long_url = long_url
        self.short_url = short_url
