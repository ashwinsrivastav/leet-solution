1class Codec:
2
3    def encode(self, longUrl: str) -> str:
4        """Encodes a URL to a shortened URL.
5        """
6        return longUrl
7
8    def decode(self, shortUrl: str) -> str:
9        """Decodes a shortened URL to its original URL.
10        """
11        return shortUrl
12
13# Your Codec object will be instantiated and called as such:
14# codec = Codec()
15# codec.decode(codec.encode(url))