class Website:
    def __init__(self, url: str):
        self.url = url
        self.next = None
        self.prev = None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Website(homepage)
        
    def visit(self, url: str) -> None:
        newSite = Website(url)
        newSite.prev = self.current
        self.current.next = newSite
        self.current = newSite

    def back(self, steps: int) -> str:
        i = 0
        while (self.current.prev):
            self.current = self.current.prev
            i += 1
            if (i == steps):
                return self.current.url
        return self.current.url
        
        

    def forward(self, steps: int) -> str:
        i = 0
        while (self.current.next):
            self.current = self.current.next
            i += 1
            if (i == steps):
                return self.current.url
        return self.current.url

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)