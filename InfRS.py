import csv
from company import Company

class IRS(): #Class: Information Retrieval System

    def exit(self):#santiago
        return 0

    def __init__(self): #initializ list-- Santiago Areliz
        self.list_companies = []

    def load_data_csv(self,file):#-- Santiago Areliz
        with open(file, mode ='r')as file:#opens csv file 
            csvFile = csv.reader(file)#set csvreader 
            for lines in csvFile:#for loop to read lines in csv file
                #print(lines[1])  #see output to test code
                
                rank = lines[0]      #set rank variables             
                company = lines[1]#set company variables 
                ticker = lines[2]#set ticker variables 
                sector = lines[3]#set sector variables 
                country = lines[24]  #set variables               
                #print(lines[1])#test code
                company = Company(rank, company, ticker, sector, country) #create company objects that holds 
                self.list_companies.append(company)# append csv to list

    def write_back(self, csv): #by: Elizabeth Suarez
        janklist = []
        with open(csv, "r") as file: #open csv file 
            for line in file: #add lines into array
                janklist.append(line)
                break 
        with open(csv, "w") as file:
            file.write(janklist[0])
            file.write("\n")    
            for object in self.list_items:
                file.write(str(object.rank))
                file.write(",")
                file.write(object.company)
                file.write(",")
                file.write(object.ticker)
                file.write(",")
                file.write(object.sector)
                file.write(",")
                k = 0
                for k in range(20):
                    file.write(",")
                file.write(object.country)
                file.write("\n")
    
    def add_singular(self, additem): #by: Elizabeth Suarez
        self.list_companies.append(additem)

        #for testing purposes only:
        #i=0
        #for i in range(1):
        #   print("add singular:", self.list)
        
    def delete_singular(self, con): #by: Elizabeth Suarez
        o = 0
        for item in self.list_companies:
            if (con.company.lower() == item.company.lower()):
               self.list_items.pop(o) 
            o+=1

        
    def search_by_rank(self, item_rank): #-santiago areliz
        """Return an item object matching the given rank, or None if not found."""
        for item in self.list_companies:#loops through list
            if (item.rank == item_rank):#compaires item we are trying to find
                return item#if ite is found return item
        return None#if item is not found return none
    
    def search_top_companies(self, top):#-- santiago areliz
        for item in self.list_companies:#loops through list
            if (item.rank <= top):#checks if items in list are less than or equal to item input
                return item #returns items that are less than the input to return list of top# companies 
        return None#if the number is not in list return none

    def searchby_companyname(self, company_name): # Ximena Montes
            for object in self.list_companies: #access list_comp
                if object.company.lower() ==  company_name.lower().strip(): #strip , lower
                    return object                   #return the obj     
            return "Error"                                                                 
                
    def return_rank(self, search_num):  # Ximena Montes
            if search_num.rank:          #Searching for num
                return search_num.rank #return the rank
            else: # If else then return the message error
                return "Error"
            
            
    def return_ticker(self, company_name): #Ximena Montes
            if company_name.ticker: #searching for ticker access first 
                return company_name.ticker #return ticker vvv else errors
            else:
                return "Error"

    def return_sector(self, num): #Ximena Montes
            if num.sector: #returning sector, if its something else return the error.
                return num.sector
            else:
                return "Error"
         
    def return_country(self, identifier): #Ximena Montes
            if identifier.country:  #looking for countries, returning country, if not error message. 
                return identifier.country 
            else:                       
                return "Error" 
  
    def searchby_countries(self, countries): #by: Elizabeth Suarez
        for object in self.list_countries:
            if object.country.lower() == countries.lower().strip():
                return object
        return "Error" 

    def __str__(self): #Elizabeth
        return f"Item(rank = {self.rank}, company = {self.company} , ticker= {self.ticker}, sector= {self.sector}, country= {self.country})"
