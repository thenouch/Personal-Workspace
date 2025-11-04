"""
Kaggle Connector Module

This module provides functionality to securely load Kaggle credentials from a .env file
and download/load datasets without exposing credentials in the notebook.
"""

import os
import pandas as pd
import kaggle
from dotenv import load_dotenv
from pathlib import Path

class KaggleConnector:
    def __init__(self, env_path=None):
        """
        Initialize the KaggleConnector with credentials from .env file
        
        Args:
            env_path (str, optional): Path to the .env file. If None, looks in the workspace root.
        """
        # If no path provided, look for .env in the workspace root
        if env_path is None:
            workspace_root = Path(__file__).parent.parent
            env_path = workspace_root / '.env'
        
        # Load environment variables from .env file
        load_dotenv(env_path)
        
        # Set Kaggle credentials from environment variables
        os.environ['KAGGLE_USERNAME'] = os.getenv('kaggle_username')
        os.environ['KAGGLE_KEY'] = os.getenv('kaggle_key')
        
        # Verify credentials are available
        if not os.getenv('kaggle_username') or not os.getenv('kaggle_key'):
            raise ValueError("Kaggle credentials not found in .env file")
    
    def download_dataset(self, dataset, path=None, unzip=True):
        """
        Download a dataset from Kaggle
        
        Args:
            dataset (str): Kaggle dataset identifier (e.g., 'vijayuv/onlineretail')
            path (str, optional): Path to save the dataset
            unzip (bool): Whether to unzip the downloaded file
            
        Returns:
            str: Path to the downloaded dataset
        """
        # Authenticate with Kaggle
        kaggle.api.authenticate()
        
        # Download the dataset
        kaggle.api.dataset_download_files(
            dataset=dataset,
            path=path,
            unzip=unzip
        )
        
        return path
    
    def load_online_retail(self, file_path=None, dataset='vijayuv/onlineretail'):
        """
        Load the Online Retail dataset
        
        Args:
            file_path (str, optional): Path to the CSV file. If None, downloads from Kaggle.
            dataset (str): Kaggle dataset identifier
            
        Returns:
            pandas.DataFrame: The loaded dataset
        """
        # If no file path provided, download the dataset
        if file_path is None:
            download_path = 'online_retail_data'
            self.download_dataset(dataset, path=download_path, unzip=True)
            file_path = os.path.join(download_path, 'OnlineRetail.csv')
        
        # Load the dataset
        df = pd.read_csv(file_path, encoding='ISO-8859-1')
        return df
    

    def load_nba_players_dataset(self, file_path=None, dataset='yagizfiratt/nba-players-database'):
        """
        Load the Online Retail dataset
        
        Args:
            file_path (str, optional): Path to the CSV file. If None, downloads from Kaggle.
            dataset (str): Kaggle dataset identifier
            
        Returns:
            pandas.DataFrame: The loaded dataset
        """
        # If no file path provided, download the dataset
        if file_path is None:
            download_path = 'nba-players-database'
            self.download_dataset(dataset, path=download_path, unzip=True)
            file_path = os.path.join(download_path, 'PlayerIndex_nba_stats.csv')
        
        # Load the dataset
        df = pd.read_csv(file_path, encoding='ISO-8859-1')
        return df