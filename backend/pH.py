#Get user pH
def ph(area):
    d={"Rice":5.6,"Sugar Cane":5.5,"Oak":5.6,"Wasteland":5.5,"Forest":4.2,"Build-up":4.3,"Cotton":6.25,"Fruits":3.5,"Tea":7,"Vegetables":6.5,"Cashew":6.5,"Apples":6.5,"Rubber":5.25,"Soybean":6.5,"Wheat":6.5}
    ph = eval(input("Enter the pH level:"))
    field_type = input("Enter what the field is used for:")
    if ph > d[field_type] :
        if ph-d[field_type]>=1:
            print("You loose on more than '10%-50%' of your yield")
            print("You should use :- Ammonium sulfate , Elemental sulfur , 	Sulfur-coated urea , Aluminum.\n In the concentration of 75:150:75:15 per acre.")
            print("Ammonium sulfate = ", area*75 ," pounds.\n","Elemental sulfur = ", area*150 ," pounds.\n","sulfur-coated = ", area*75 ," pounds.\n","Aluminum = ", area*15 ," pounds.\n")
        else:
            print("You loose on more than '1%' of your yield")
            print("Just use organic matter and you are good to go.")
    elif d[field_type] > ph:
        if d[field_type]-ph >= 1:
            print("You loose on more than '10%-50%' of your yield")
            print("You should use :- Agricultural lime, Dolomitic lime, Wood ash, Gypsum, Calcium carbonate.\n In the concentration of 3000:3000:750:750:750 per acre.")
            print("Agricultural lime = ", area*3000 ," pounds.\n","Dolomitic lime = ", area*3000 ," pounds.\n","Wood ash = ", area*750 ," pounds.\n","Gypsum = ", area*750 ," pounds.\n","Calcium carbonate = ", area*750 ," pounds.\n")
        else:
            print("You loose on more than '1%' of your yield")
            print("Just use organic matter and you are good to go.")
    else:
        print("You have the perfect concentration for the soil.")
def main():
    file_path = 'Data.csv'
    area = eval(input("Enter the area of your field in acre"))
    ph(area)

#Enter the function
if __name__ == "__main__":
    main()
