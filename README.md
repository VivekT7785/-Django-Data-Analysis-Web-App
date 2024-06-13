# Django Data Analysis Web App

## Overview

This Django-based web application allows users to upload CSV files, perform data analysis using pandas and numpy, and visualize the results and visualizations on the web interface. The project aims to provide a user-friendly platform for data exploration, enabling users to gain insights from their data quickly and effectively.

## Features

- **CSV File Upload**: Users can upload CSV files through a simple and intuitive interface.
- **Data Analysis**: The application performs data analysis tasks such as calculating summary statistics (mean, median, standard deviation), identifying missing values, and generating histograms for numerical columns.
- **Interactive Visualizations**: Users can explore their data visually through dynamically generated histograms.
- **User-Friendly Interface**: The entire user interface is designed to be intuitive and user-friendly, making it accessible to users with varying levels of technical expertise.
- **Flexibility and Scalability**: The application is designed to be flexible and scalable, allowing for easy integration of additional features and functionalities in the future.

## Setup Instructions

1. **Clone the Repository**: 
   ```
   git clone https://github.com/VivekT7785/-Django-Data-Analysis-Web-App
   ```

2. **Navigate to the Project Directory**:
   ```
   cd django-data-analysis-web-app
   ```

3. **Create a Virtual Environment**:
   ```
   python3 -m venv venv
   ```

4. **Activate the Virtual Environment**:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

5. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```

6. **Run Migrations**:
   ```
   python manage.py migrate
   ```

7. **Start the Development Server**:
   ```
   python manage.py runserver
   ```

8. **Access the Application**:
   Open your web browser and navigate to `http://127.0.0.1:8000/` to access the application.

## Technologies Used

- Python
- Django
- pandas
- numpy
- matplotlib


