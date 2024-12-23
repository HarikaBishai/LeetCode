

class Codec:

    def __init__(self):
        self.id = 1
        self.urlMap = {}
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        currId = self.id
        shortUrl = ''
        chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

        while currId > 0:
            shortUrl += chars[currId%62]
            currId = currId // 62

        self.urlMap[shortUrl[::-1]] = longUrl
        self.id += 1

        return shortUrl[::-1]
        


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """

        return self.urlMap[shortUrl]
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))