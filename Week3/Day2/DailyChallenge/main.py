# Week3 Day2
# Dmitry Dubrov
# Daily Challenge : Pagination
# Instructions :
# Create a class to handle paginated content in a website. 
# A pagination is used to divide long lists of content in a series of pages.
class Pagination() :
    def __init__(self, in_items = None, in_pageSize = 10):
        self.items = in_items
        self.pageSize = in_pageSize
        #info about q-ty of pages
        self.pagenumber = 0
        self.page_info = {"first":0,"last":0,"all":[]}
    
    def add_page_info(self) :
        #find first page, last and list of pages
        first_page = 1 if len(self.items) > 0 else 0
        last_page = int(len(self.items)//self.pageSize) + (1 if len(self.items)%self.pageSize > 0 else 0)
        page_list = [i for i in range(first_page, last_page+1)]
        #save to main class atrib
        self.page_info["first"] = first_page
        self.page_info["last"] = last_page
        self.page_info["all"] = page_list
        self.pagenumber = first_page
        s ="s" if last_page > 1 else ""
        print(f'Text will be splited to {self.page_info["last"]} page{s}.')
      
    def getVisibleItems(self) :
        start_letter = ((self.pagenumber-1)*self.pageSize) if ((self.pagenumber-1)*self.pageSize) <= len(self.items) else len(self.items)
        last_letter = (start_letter + self.pageSize) if (start_letter + self.pageSize) <= len(self.items) else len(self.items)
        
        print(self.items[start_letter:last_letter])
     
    def prevPage(self) :
        self.pagenumber = (self.pagenumber - 1) if self.pagenumber >= 2 else 1 
        return self
    
    def nextPage(self) :
        self.pagenumber = (self.pagenumber + 1) if self.pagenumber < self.page_info.get("last") else self.page_info.get("last") 
        return self
    
    
    def firstPage(self) :
        self.pagenumber = self.page_info.get("first")
        return self
    
    
    def lastPage(self) :
        self.pagenumber = self.page_info.get("last")
        return self
    
    def goToPage(self, num) :
        if num in self.page_info.get("all"):
            self.pagenumber = num
        elif num > self.page_info.get("last"):
            self.pagenumber = self.page_info.get("last")
        elif num < self.page_info.get("first"):
            self.pagenumber = self.page_info.get("first")
        else: 
            print("Wrong page")    
        return self
    
    def cur_page(self) :
        print(self.pagenumber)
        
    # Drivers
alphabetList = list("abcdefghijklmnopqrstuvwxyz")

x = Pagination(alphabetList, 6)

x.add_page_info()
x.getVisibleItems()
x.nextPage().nextPage()
x.getVisibleItems()

x.prevPage()
x.getVisibleItems()

x.goToPage(4)
x.getVisibleItems()
x.cur_page()