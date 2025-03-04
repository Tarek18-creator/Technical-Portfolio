import requests
import pandas as pd
from odf.opendocument import OpenDocumentSpreadsheet
from odf.table import Table, TableRow, TableCell
from odf.text import P


def main():
    # Ask the user for their preferences
    preferences = get_user_preferences()

    # Fetch the list of houses from the API
    houses = fetch_houses()

    # Filter the houses based on the user's preferences
    filtered_houses = filter_houses(houses, preferences)

    # Generate the recommendations table, ordered by preference
    recommended_houses = generate_recommendations(filtered_houses)

    # Save the table to an ODS (OpenDocument Spreadsheet) file
    save_to_ods(recommended_houses)

    print("Recommendations have been saved in the file 'recommendations.ods'")


def get_user_preferences():
    # Ask the user for their preferences
    print("What are your preferences for buying a house?")
    print("1. Price and Capacity")
    print("2. Price and Size")
    print("3. Price and Location")
    print("4. Price and Bedrooms")

    option = input("Please select an option (1-4): ")

    if option == "1":
        price = int(input("What is your maximum budget? "))
        capacity = int(input("What is the minimum capacity you need (in square feet)? "))
        return {"type": "price_capacity", "price": price, "capacity": capacity}

    elif option == "2":
        price = int(input("What is your maximum budget? "))
        size = int(input("What is the minimum size you want (in square feet)? "))
        return {"type": "price_size", "price": price, "size": size}

    elif option == "3":
        price = int(input("What is your maximum budget? "))
        location = input("Which location do you prefer for the house? ")
        return {"type": "price_location", "price": price, "location": location}

    elif option == "4":
        price = int(input("What is your maximum budget? "))
        bedrooms = int(input("How many bedrooms do you need at a minimum? "))
        return {"type": "price_bedrooms", "price": price, "bedrooms": bedrooms}

    else:
        print("Invalid option, please try again.")
        return get_user_preferences()


def fetch_houses():
    # Make a request to the API to get the list of houses
    response = requests.get("http://localhost:5000/houses")
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching houses from the API.")
        return []


def filter_houses(houses, preferences):
    filtered = []

    for house in houses:
        if preferences["type"] == "price_capacity":
            if house["price"] <= preferences["price"] and house["capacity"] >= preferences["capacity"]:
                filtered.append(house)

        elif preferences["type"] == "price_size":
            if house["price"] <= preferences["price"] and house["capacity"] >= preferences["size"]:
                filtered.append(house)

        elif preferences["type"] == "price_location":
            if house["price"] <= preferences["price"] and preferences["location"].lower() in house["location"].lower():
                filtered.append(house)

        elif preferences["type"] == "price_bedrooms":
            if house["price"] <= preferences["price"] and house["bedrooms"] >= preferences["bedrooms"]:
                filtered.append(house)

    return filtered


def generate_recommendations(filtered_houses):
    # Create a list of recommendations ordered by price (ascending) and capacity (descending)
    recommendations = sorted(filtered_houses, key=lambda x: (x["price"], -x["capacity"]))

    # Convert the filtered houses into a pandas DataFrame for easy handling
    df = pd.DataFrame(recommendations)

    # Return the recommendations as a sorted DataFrame
    return df


def save_to_ods(df):
    # Create a new OpenDocument Spreadsheet (ODS) file
    ods = OpenDocumentSpreadsheet()

    # Create a table in the spreadsheet
    table = Table(name="Recommendations")

    # Create the header row with column names
    header_row = TableRow()
    for col in df.columns:
        cell = TableCell()
        cell.addElement(P(text=col))
        header_row.addElement(cell)
    table.addElement(header_row)

    # Add each row of data for the recommended houses
    for _, row in df.iterrows():
        table_row = TableRow()
        for value in row:
            cell = TableCell()
            cell.addElement(P(text=str(value)))
            table_row.addElement(cell)
        table.addElement(table_row)

    # Add the table to the ODS document
    ods.spreadsheet.addElement(table)

    # Save the ODS file
    ods.save("recommendations.ods")


if __name__ == "__main__":
    main()
