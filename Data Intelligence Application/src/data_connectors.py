"""
Data Connectors Module
Handles connections to various data sources
"""

import pandas as pd
import numpy as np
import io
import requests
from typing import Optional, Dict, Any
import sqlite3
from pathlib import Path


class DataConnector:
    """Handle connections to multiple data sources"""

    def __init__(self):
        self.supported_formats = ['csv', 'xlsx', 'xls', 'json', 'parquet']

    def load_file(self, uploaded_file) -> pd.DataFrame:
        """
        Load data from uploaded file

        Args:
            uploaded_file: Streamlit UploadedFile object

        Returns:
            pd.DataFrame: Loaded dataframe
        """
        file_extension = uploaded_file.name.split('.')[-1].lower()

        if file_extension == 'csv':
            df = pd.read_csv(uploaded_file)
        elif file_extension in ['xlsx', 'xls']:
            df = pd.read_excel(uploaded_file)
        elif file_extension == 'json':
            df = pd.read_json(uploaded_file)
        elif file_extension == 'parquet':
            df = pd.read_parquet(uploaded_file)
        else:
            raise ValueError(f"Unsupported file format: {file_extension}")

        return df

    def load_from_database(
        self,
        db_type: str,
        host: str,
        port: int,
        database: str,
        username: str,
        password: str,
        query: str
    ) -> pd.DataFrame:
        """
        Load data from database

        Args:
            db_type: Type of database (PostgreSQL, MySQL, SQLite, SQL Server)
            host: Database host
            port: Database port
            database: Database name
            username: Database username
            password: Database password
            query: SQL query to execute

        Returns:
            pd.DataFrame: Query results
        """
        try:
            if db_type == "PostgreSQL":
                import psycopg2
                conn = psycopg2.connect(
                    host=host,
                    port=port,
                    database=database,
                    user=username,
                    password=password
                )
                df = pd.read_sql_query(query, conn)
                conn.close()

            elif db_type == "MySQL":
                import pymysql
                conn = pymysql.connect(
                    host=host,
                    port=port,
                    database=database,
                    user=username,
                    password=password
                )
                df = pd.read_sql_query(query, conn)
                conn.close()

            elif db_type == "SQLite":
                conn = sqlite3.connect(database)
                df = pd.read_sql_query(query, conn)
                conn.close()

            elif db_type == "SQL Server":
                import pyodbc
                conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={host},{port};DATABASE={database};UID={username};PWD={password}'
                conn = pyodbc.connect(conn_str)
                df = pd.read_sql_query(query, conn)
                conn.close()

            else:
                raise ValueError(f"Unsupported database type: {db_type}")

            return df

        except ImportError as e:
            raise ImportError(f"Required database driver not installed: {str(e)}")
        except Exception as e:
            raise Exception(f"Database connection error: {str(e)}")

    def load_from_api(
        self,
        url: str,
        method: str = "GET",
        auth_type: str = "None",
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None
    ) -> pd.DataFrame:
        """
        Load data from REST API

        Args:
            url: API endpoint URL
            method: HTTP method (GET, POST)
            auth_type: Authentication type
            headers: Request headers
            params: Request parameters

        Returns:
            pd.DataFrame: API response data
        """
        try:
            if headers is None:
                headers = {}

            if method == "GET":
                response = requests.get(url, headers=headers, params=params)
            elif method == "POST":
                response = requests.post(url, headers=headers, json=params)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            response.raise_for_status()

            # Try to parse JSON response
            data = response.json()

            # Convert to DataFrame
            if isinstance(data, list):
                df = pd.DataFrame(data)
            elif isinstance(data, dict):
                # Check if there's a data key
                if 'data' in data:
                    df = pd.DataFrame(data['data'])
                elif 'results' in data:
                    df = pd.DataFrame(data['results'])
                else:
                    df = pd.DataFrame([data])
            else:
                raise ValueError("Unable to parse API response to DataFrame")

            return df

        except requests.exceptions.RequestException as e:
            raise Exception(f"API request error: {str(e)}")
        except Exception as e:
            raise Exception(f"Error loading data from API: {str(e)}")

    def load_sample_data(self, dataset_name: str) -> pd.DataFrame:
        """
        Load sample datasets for demonstration

        Args:
            dataset_name: Name of sample dataset

        Returns:
            pd.DataFrame: Sample dataset
        """
        if dataset_name == "iris":
            # Iris dataset
            from sklearn.datasets import load_iris
            iris = load_iris()
            df = pd.DataFrame(iris.data, columns=iris.feature_names)
            df['species'] = iris.target
            df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

        elif dataset_name == "titanic":
            # Titanic dataset (synthetic)
            np.random.seed(42)
            n_passengers = 500

            df = pd.DataFrame({
                'PassengerId': range(1, n_passengers + 1),
                'Survived': np.random.choice([0, 1], n_passengers, p=[0.62, 0.38]),
                'Pclass': np.random.choice([1, 2, 3], n_passengers, p=[0.24, 0.21, 0.55]),
                'Sex': np.random.choice(['male', 'female'], n_passengers, p=[0.65, 0.35]),
                'Age': np.random.normal(30, 14, n_passengers).clip(0.5, 80),
                'SibSp': np.random.choice([0, 1, 2, 3, 4], n_passengers, p=[0.68, 0.23, 0.06, 0.02, 0.01]),
                'Parch': np.random.choice([0, 1, 2, 3], n_passengers, p=[0.76, 0.13, 0.08, 0.03]),
                'Fare': np.random.lognormal(3, 1, n_passengers),
                'Embarked': np.random.choice(['S', 'C', 'Q'], n_passengers, p=[0.72, 0.19, 0.09])
            })

        elif dataset_name == "sales":
            # Sales dataset (synthetic)
            np.random.seed(42)
            n_records = 1000

            products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
            regions = ['North', 'South', 'East', 'West', 'Central']
            dates = pd.date_range('2023-01-01', periods=n_records, freq='D')

            df = pd.DataFrame({
                'Date': np.random.choice(dates, n_records),
                'Product': np.random.choice(products, n_records),
                'Region': np.random.choice(regions, n_records),
                'Quantity': np.random.randint(1, 100, n_records),
                'Unit_Price': np.random.uniform(10, 500, n_records),
                'Discount': np.random.uniform(0, 0.3, n_records)
            })

            df['Revenue'] = df['Quantity'] * df['Unit_Price'] * (1 - df['Discount'])
            df['Date'] = pd.to_datetime(df['Date'])

        elif dataset_name == "customers":
            # Customer analytics dataset (synthetic)
            np.random.seed(42)
            n_customers = 800

            df = pd.DataFrame({
                'Customer_ID': range(1, n_customers + 1),
                'Age': np.random.normal(40, 15, n_customers).clip(18, 80),
                'Gender': np.random.choice(['M', 'F', 'Other'], n_customers, p=[0.48, 0.48, 0.04]),
                'Income': np.random.lognormal(10.5, 0.5, n_customers),
                'Total_Purchases': np.random.poisson(15, n_customers),
                'Avg_Purchase_Value': np.random.uniform(20, 500, n_customers),
                'Customer_Lifetime': np.random.randint(1, 120, n_customers),  # months
                'Satisfaction_Score': np.random.uniform(1, 5, n_customers),
                'Churn_Risk': np.random.choice(['Low', 'Medium', 'High'], n_customers, p=[0.6, 0.3, 0.1])
            })

        else:
            raise ValueError(f"Unknown sample dataset: {dataset_name}")

        return df

    def export_data(
        self,
        df: pd.DataFrame,
        file_path: str,
        format: str = 'csv'
    ) -> str:
        """
        Export dataframe to file

        Args:
            df: DataFrame to export
            file_path: Export file path
            format: Export format (csv, xlsx, json, parquet)

        Returns:
            str: Path to exported file
        """
        try:
            if format == 'csv':
                df.to_csv(file_path, index=False)
            elif format == 'xlsx':
                df.to_excel(file_path, index=False)
            elif format == 'json':
                df.to_json(file_path, orient='records', indent=2)
            elif format == 'parquet':
                df.to_parquet(file_path, index=False)
            else:
                raise ValueError(f"Unsupported export format: {format}")

            return file_path

        except Exception as e:
            raise Exception(f"Export error: {str(e)}")
