from InfRS import IRS

def main():
    Inventory = IRS()
    #Inventory.load_data("fortune1000_2024.csv")
    Inventory.load_data_csv("fortune1000_2024.csv")

    company1 = str(input("Enter a Company Name: "))
    object = Inventory.searchby_companyname(company1)

    if object:
        print (f"Rank: {object.rank}, Company: {object.company}, Ticker:{object.ticker} Sector:{object.sector} Country:{object.country}")
    else:
        print("Item not found. :'(")


if __name__ == "__main__":
    main()