# myapp/views.py
from django.shortcuts import render
from .forms import CSVUploadForm
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            # Handle the uploaded file
            df = handle_uploaded_file(csv_file)
            # Perform basic data analysis tasks
            first_rows = df.head()
            summary_stats = df.describe()
            missing_values = df.isnull().sum()
            # Generate histograms for numerical columns
            histograms = generate_histograms(df)
            return render(request, 'analysis.html', {'first_rows': first_rows,
                                                     'summary_stats': summary_stats,
                                                     'missing_values': missing_values,
                                                     'histograms': histograms})
    else:
        form = CSVUploadForm()
    return render(request, 'upload.html', {'form': form})

def generate_histograms(df):
    histograms = {}
    numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns
    for column in numerical_columns:
        plt.figure(figsize=(8, 6))
        df[column].plot(kind='hist', bins=20, color='skyblue', edgecolor='black')
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.grid(True)
        # Save the plot to a bytes object
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        # Encode the bytes object as a base64 string
        plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
        histograms[column] = plot_base64
        plt.close()
    return histograms


def handle_uploaded_file(f):
    # Read the CSV file using pandas
    df = pd.read_csv(f)
    return df
    
