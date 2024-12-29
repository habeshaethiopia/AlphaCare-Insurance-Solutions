import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import io
import requests
import zipfile
import chardet

class DataLoader:
    def __init__(self, link):
        """
        Initializes the DataLoader with a Google Drive link to the zip file.
        
        Args:
            link (str): The Google Drive link to the zip file.
        """
        self.link = link
        self.file_id = self.extract_file_id(link)
        self.download_url = f'https://drive.google.com/uc?id={self.file_id}&export=download'

    def extract_file_id(self, link):
        """
        Extracts the file ID from the Google Drive link.
        
        Args:
            link (str): The Google Drive link to the zip file.
        
        Returns:
            str: The file ID.
        """
        return link.split('/')[-2]

    def load_data_from_drive_zip(self):
        """
        Loads data from a zip file on Google Drive containing a text file with pipe-separated data.
        
        Returns:
            pandas.DataFrame: The data as a pandas DataFrame.
        """
        try:
            # Download the zip file
            response = requests.get(self.download_url)
            response.raise_for_status()  # Raise an exception for bad responses
            
            # Extract the zip file
            with zipfile.ZipFile(io.BytesIO(response.content)) as z:
                # Assuming there is only one file in the zip
                file_name = z.namelist()[0]
                with z.open(file_name) as f:
                    # Detect the encoding
                    result = chardet.detect(f.read())
                    encoding = result['encoding']
                    f.seek(0)
                    # Load the data into a pandas DataFrame
                    data = pd.read_csv(f, sep='|', encoding=encoding)
            return data
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
