#Enter modules
import requests
import csv
def redcon(file_path,state):
    soil = ""
    with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["State"]==state:
                    soil = row["Soil"]
    return soil
def main():
    file_path = 'Data.csv'  # Replace with the path to your CSV file
    state = input("Enter the state name: ")
    Best_Crop= redcon(file_path, state)
    print("The best crop for you guys are: ",Best_Crop)

if __name__ == "__main__":
    main()
