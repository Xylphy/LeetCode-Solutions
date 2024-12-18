#
# @lc app=leetcode id=535 lang=python
#
# [535] Encode and Decode TinyURL
#

# @lc code=start
class Codec:

    def __init__(self):
        self.long_url = {}
        self.shortUrl = "http://tinyurl.com/"
        self.counter = 0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        short_url = self.shortUrl + str(self.counter)
        self.long_url[short_url] = longUrl
        self.counter += 1
        return short_url
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.long_url.get(shortUrl, "")
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# @lc code=end

