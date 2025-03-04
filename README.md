# WEB SCRAPER

#### Video Demo:  <https://www.youtube.com/watch?v=zpEBHo44BYE>

#### Description:

Main Application
The main application is a Python script that serves as the core of the house recommendation system. It utilizes several libraries to handle data processing, API interactions, and file generation.
User Interaction
The script begins by prompting the user for their house-buying preferences. Users can choose from four options:
Price and Capacity
Price and Size
Price and Location
Price and Bedrooms
Based on the user's selection, the script collects specific criteria such as maximum budget, minimum capacity, preferred location, or number of bedrooms.
Data Retrieval and Processing
After gathering user preferences, the script fetches house data from a local API (running on http://localhost:5000). It then filters the houses based on the user's criteria. The filtering process considers factors like price, capacity, size, location, and number of bedrooms, depending on the user's chosen preference type.
Recommendation Generation
The filtered houses are then sorted to generate recommendations. The sorting prioritizes houses with lower prices and higher capacities, creating a balance between affordability and spaciousness.
Output Generation
Finally, the script creates an OpenDocument Spreadsheet (ODS) file named "recommendations.ods" to present the recommendations in a tabular format. This file can be easily opened with various spreadsheet applications, providing a user-friendly way to view and compare the recommended houses.
API Description
The API used in this project is a Flask-based application that manages a simple in-memory database of houses. Here's an overview of its functionality:
Data Structure
The API maintains a list of 10 sample houses, each with properties such as ID, price, capacity, location, number of bedrooms and bathrooms, garage availability, and proximity to the beach.
Endpoints
GET /houses: Retrieves all houses in the database.
GET /houses/<house_id>: Fetches a specific house by its ID.
POST /houses: Adds a new house to the database.
PUT /houses/<house_id>: Updates information for a specific house.
DELETE /houses/<house_id>: Removes a house from the database.
Features
The API uses JSON for data exchange, making it easy to integrate with various client applications.
It includes basic error handling, such as returning appropriate status codes for not found or invalid requests.
The POST route automatically generates a unique ID for new houses.
Libraries Used
The project utilizes several Python libraries to achieve its functionality:
requests: For making HTTP requests to the API.
pandas: For data manipulation and analysis.
odf.opendocument: Part of the odfpy library, used for creating OpenDocument files.
odf.table and odf.text: Also from odfpy, used for creating tables and text elements in the ODS file.
Flask: Used in the API to create a web server and define routes.
jsonify: A Flask helper for creating JSON responses.
This house recommendation system showcases a practical application of data processing, API integration, and file generation in Python. It provides a user-friendly interface for house hunters to find properties that match their specific criteria, demonstrating how programming can be used to solve real-world problems in the real estate domain.
