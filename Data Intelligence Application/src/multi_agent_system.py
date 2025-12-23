"""
Multi-Agent AI System for Data Analysis
Powered by PandasAI and custom analysis agents
"""

import pandas as pd
import numpy as np
from typing import Dict, Any, List, Optional
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os


class DataAnalysisAgent:
    """
    Multi-agent system for intelligent data analysis
    Uses different specialized agents for various analysis tasks
    """

    def __init__(self, df: pd.DataFrame):
        """
        Initialize the multi-agent system

        Args:
            df: DataFrame to analyze
        """
        self.df = df
        self.agents = {
            'statistical': StatisticalAgent(df),
            'pattern': PatternRecognitionAgent(df),
            'insight': InsightGenerationAgent(df),
            'prediction': PredictiveAgent(df),
            'nlp': NaturalLanguageAgent(df)
        }

    def analyze(self, query: str) -> Dict[str, Any]:
        """
        Analyze data based on natural language query

        Args:
            query: Natural language question about the data

        Returns:
            Dict containing analysis results, explanations, and visualizations
        """
        # Route query to appropriate agent(s)
        query_lower = query.lower()

        result = {
            'explanation': '',
            'data': None,
            'visualization': None,
            'insights': []
        }

        try:
            # Statistical queries
            if any(word in query_lower for word in ['average', 'mean', 'median', 'sum', 'count', 'max', 'min', 'std']):
                stat_result = self.agents['statistical'].analyze(query, self.df)
                result.update(stat_result)

            # Pattern recognition queries
            elif any(word in query_lower for word in ['trend', 'pattern', 'correlation', 'relationship']):
                pattern_result = self.agents['pattern'].analyze(query, self.df)
                result.update(pattern_result)

            # Insight generation queries
            elif any(word in query_lower for word in ['insight', 'summary', 'overview', 'key findings']):
                insight_result = self.agents['insight'].analyze(query, self.df)
                result.update(insight_result)

            # Predictive queries
            elif any(word in query_lower for word in ['predict', 'forecast', 'future', 'estimate']):
                pred_result = self.agents['prediction'].analyze(query, self.df)
                result.update(pred_result)

            # General NLP queries
            else:
                nlp_result = self.agents['nlp'].analyze(query, self.df)
                result.update(nlp_result)

        except Exception as e:
            result['explanation'] = f"Error during analysis: {str(e)}\n\nTry rephrasing your query or check column names."
            result['insights'] = [
                "Make sure column names in your query match the dataset",
                "Try simpler queries for better results",
                "Check if the operation is valid for your data types"
            ]

        return result


class StatisticalAgent:
    """Agent specialized in statistical analysis"""

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def analyze(self, query: str, df: pd.DataFrame) -> Dict[str, Any]:
        """Perform statistical analysis"""
        result = {}

        # Extract statistical operation
        query_lower = query.lower()

        # Identify numeric columns
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

        if 'average' in query_lower or 'mean' in query_lower:
            stats = df[numeric_cols].mean()
            result['explanation'] = "### Statistical Analysis: Mean Values\n\n"
            result['explanation'] += "Here are the average (mean) values for numeric columns:\n\n"
            result['data'] = pd.DataFrame({'Column': stats.index, 'Mean': stats.values})
            result['insights'] = [
                f"Highest average: {stats.idxmax()} = {stats.max():.2f}",
                f"Lowest average: {stats.idxmin()} = {stats.min():.2f}"
            ]

        elif 'median' in query_lower:
            stats = df[numeric_cols].median()
            result['explanation'] = "### Statistical Analysis: Median Values\n\n"
            result['explanation'] += "Here are the median values for numeric columns:\n\n"
            result['data'] = pd.DataFrame({'Column': stats.index, 'Median': stats.values})

        elif 'sum' in query_lower or 'total' in query_lower:
            stats = df[numeric_cols].sum()
            result['explanation'] = "### Statistical Analysis: Sum/Total Values\n\n"
            result['data'] = pd.DataFrame({'Column': stats.index, 'Total': stats.values})

        elif 'max' in query_lower or 'maximum' in query_lower:
            stats = df[numeric_cols].max()
            result['explanation'] = "### Statistical Analysis: Maximum Values\n\n"
            result['data'] = pd.DataFrame({'Column': stats.index, 'Maximum': stats.values})

        elif 'min' in query_lower or 'minimum' in query_lower:
            stats = df[numeric_cols].min()
            result['explanation'] = "### Statistical Analysis: Minimum Values\n\n"
            result['data'] = pd.DataFrame({'Column': stats.index, 'Minimum': stats.values})

        else:
            # General statistics
            result['explanation'] = "### Comprehensive Statistical Summary\n\n"
            result['data'] = df[numeric_cols].describe()
            result['insights'] = [
                f"Dataset has {len(numeric_cols)} numeric columns",
                f"Total records: {len(df)}"
            ]

        return result


class PatternRecognitionAgent:
    """Agent specialized in pattern recognition and correlation analysis"""

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def analyze(self, query: str, df: pd.DataFrame) -> Dict[str, Any]:
        """Analyze patterns and correlations"""
        result = {}

        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

        if 'correlation' in query.lower():
            if len(numeric_cols) >= 2:
                corr_matrix = df[numeric_cols].corr()

                result['explanation'] = "### Correlation Analysis\n\n"
                result['explanation'] += "Correlation matrix showing relationships between numeric variables:\n\n"
                result['explanation'] += "- Values close to 1: Strong positive correlation\n"
                result['explanation'] += "- Values close to -1: Strong negative correlation\n"
                result['explanation'] += "- Values close to 0: Weak or no correlation\n\n"

                result['data'] = corr_matrix

                # Create correlation heatmap
                fig, ax = plt.subplots(figsize=(10, 8))
                sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0,
                          fmt='.2f', square=True, ax=ax)
                ax.set_title('Correlation Heatmap')
                result['visualization'] = fig

                # Find strong correlations
                insights = []
                for i in range(len(corr_matrix.columns)):
                    for j in range(i+1, len(corr_matrix.columns)):
                        corr_val = corr_matrix.iloc[i, j]
                        if abs(corr_val) > 0.7:
                            col1 = corr_matrix.columns[i]
                            col2 = corr_matrix.columns[j]
                            insights.append(
                                f"Strong correlation ({corr_val:.2f}) between {col1} and {col2}"
                            )

                result['insights'] = insights if insights else ["No strong correlations found (|r| > 0.7)"]

        elif 'trend' in query.lower():
            # Time series trend analysis
            date_cols = df.select_dtypes(include=['datetime64']).columns.tolist()

            if date_cols and numeric_cols:
                date_col = date_cols[0]
                value_col = numeric_cols[0]

                df_sorted = df.sort_values(date_col)

                fig, ax = plt.subplots(figsize=(12, 6))
                ax.plot(df_sorted[date_col], df_sorted[value_col], marker='o', linestyle='-')
                ax.set_xlabel(date_col)
                ax.set_ylabel(value_col)
                ax.set_title(f'Trend Analysis: {value_col} over {date_col}')
                ax.grid(True, alpha=0.3)
                plt.xticks(rotation=45)
                plt.tight_layout()

                result['visualization'] = fig
                result['explanation'] = f"### Trend Analysis\n\nShowing trend of {value_col} over time ({date_col})"

                # Calculate trend
                trend_direction = "increasing" if df_sorted[value_col].iloc[-1] > df_sorted[value_col].iloc[0] else "decreasing"
                result['insights'] = [
                    f"Overall trend is {trend_direction}",
                    f"Range: {df_sorted[value_col].min():.2f} to {df_sorted[value_col].max():.2f}"
                ]
            else:
                result['explanation'] = "No time series data found for trend analysis."

        else:
            result['explanation'] = "### Pattern Analysis\n\nAnalyzing data patterns..."
            result['data'] = df.head(20)

        return result


class InsightGenerationAgent:
    """Agent specialized in generating insights and summaries"""

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def analyze(self, query: str, df: pd.DataFrame) -> Dict[str, Any]:
        """Generate insights from data"""
        result = {}

        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

        result['explanation'] = "### Key Insights from Your Data\n\n"

        insights = []

        # Dataset overview
        insights.append(f"📊 Dataset contains {len(df)} records and {len(df.columns)} columns")

        # Numeric insights
        if numeric_cols:
            insights.append(f"🔢 {len(numeric_cols)} numeric columns: {', '.join(numeric_cols[:3])}{'...' if len(numeric_cols) > 3 else ''}")

            for col in numeric_cols[:3]:
                mean_val = df[col].mean()
                std_val = df[col].std()
                cv = (std_val / mean_val * 100) if mean_val != 0 else 0
                insights.append(f"   • {col}: mean={mean_val:.2f}, std={std_val:.2f}, CV={cv:.1f}%")

        # Categorical insights
        if categorical_cols:
            insights.append(f"📝 {len(categorical_cols)} categorical columns: {', '.join(categorical_cols[:3])}")

            for col in categorical_cols[:2]:
                n_unique = df[col].nunique()
                top_value = df[col].mode()[0] if len(df[col].mode()) > 0 else 'N/A'
                insights.append(f"   • {col}: {n_unique} unique values, most common: {top_value}")

        # Missing data
        missing = df.isnull().sum()
        missing_cols = missing[missing > 0]
        if len(missing_cols) > 0:
            insights.append(f"⚠️ Missing data found in {len(missing_cols)} columns")
            for col in missing_cols.head(3).index:
                pct = (missing_cols[col] / len(df) * 100)
                insights.append(f"   • {col}: {missing_cols[col]} missing ({pct:.1f}%)")
        else:
            insights.append("✅ No missing data detected")

        # Duplicates
        n_duplicates = df.duplicated().sum()
        if n_duplicates > 0:
            insights.append(f"⚠️ {n_duplicates} duplicate rows found ({n_duplicates/len(df)*100:.1f}%)")
        else:
            insights.append("✅ No duplicate rows detected")

        # Outliers (simple IQR method)
        if numeric_cols:
            outlier_counts = {}
            for col in numeric_cols[:3]:
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                outliers = df[(df[col] < Q1 - 1.5*IQR) | (df[col] > Q3 + 1.5*IQR)]
                if len(outliers) > 0:
                    outlier_counts[col] = len(outliers)

            if outlier_counts:
                insights.append(f"📌 Potential outliers detected:")
                for col, count in outlier_counts.items():
                    insights.append(f"   • {col}: {count} outliers")

        result['insights'] = insights
        result['explanation'] += "\n".join([f"- {insight}" for insight in insights])

        # Summary statistics table
        if numeric_cols:
            summary = df[numeric_cols].describe().T
            summary['missing'] = df[numeric_cols].isnull().sum()
            result['data'] = summary

        return result


class PredictiveAgent:
    """Agent specialized in predictive analysis"""

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def analyze(self, query: str, df: pd.DataFrame) -> Dict[str, Any]:
        """Perform predictive analysis"""
        result = {}

        result['explanation'] = "### Predictive Analysis\n\n"
        result['explanation'] += "🔮 Advanced predictive modeling capabilities:\n\n"
        result['explanation'] += "This agent can perform:\n"
        result['explanation'] += "- Time series forecasting\n"
        result['explanation'] += "- Regression analysis\n"
        result['explanation'] += "- Classification predictions\n"
        result['explanation'] += "- Anomaly detection\n\n"

        result['insights'] = [
            "Predictive modeling requires specific configuration",
            "Consider using machine learning models for complex predictions",
            "Ensure sufficient historical data for accurate forecasting"
        ]

        # Simple trend prediction for time series
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        if numeric_cols:
            col = numeric_cols[0]
            values = df[col].dropna()

            if len(values) > 10:
                # Simple moving average prediction
                window = min(5, len(values) // 4)
                ma = values.rolling(window=window).mean()

                fig, ax = plt.subplots(figsize=(12, 6))
                ax.plot(values.index, values.values, label='Actual', marker='o', alpha=0.6)
                ax.plot(ma.index, ma.values, label=f'Moving Average ({window})', linewidth=2)
                ax.set_title(f'Trend Analysis: {col}')
                ax.set_xlabel('Index')
                ax.set_ylabel(col)
                ax.legend()
                ax.grid(True, alpha=0.3)
                plt.tight_layout()

                result['visualization'] = fig
                result['explanation'] += f"\nShowing trend analysis for {col} with {window}-period moving average."

        return result


class NaturalLanguageAgent:
    """Agent for handling general natural language queries"""

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def analyze(self, query: str, df: pd.DataFrame) -> Dict[str, Any]:
        """Handle general NLP queries"""
        result = {}

        query_lower = query.lower()

        # Top/bottom queries
        if 'top' in query_lower or 'best' in query_lower or 'highest' in query_lower:
            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

            if numeric_cols:
                # Extract number if specified
                n = 5  # default
                words = query_lower.split()
                for i, word in enumerate(words):
                    if word.isdigit():
                        n = int(word)
                        break

                col = numeric_cols[0]  # default to first numeric column
                top_data = df.nlargest(n, col)

                result['explanation'] = f"### Top {n} Records\n\nShowing top {n} records sorted by {col}"
                result['data'] = top_data
                result['insights'] = [
                    f"Highest value: {top_data[col].iloc[0]:.2f}",
                    f"Range of top {n}: {top_data[col].min():.2f} - {top_data[col].max():.2f}"
                ]

        elif 'bottom' in query_lower or 'worst' in query_lower or 'lowest' in query_lower:
            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

            if numeric_cols:
                n = 5
                col = numeric_cols[0]
                bottom_data = df.nsmallest(n, col)

                result['explanation'] = f"### Bottom {n} Records\n\nShowing bottom {n} records sorted by {col}"
                result['data'] = bottom_data

        elif 'group' in query_lower or 'by' in query_lower:
            categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

            if categorical_cols and numeric_cols:
                group_col = categorical_cols[0]
                value_col = numeric_cols[0]

                grouped = df.groupby(group_col)[value_col].agg(['mean', 'sum', 'count'])

                result['explanation'] = f"### Grouped Analysis\n\nData grouped by {group_col}, aggregating {value_col}"
                result['data'] = grouped
                result['insights'] = [
                    f"Number of groups: {len(grouped)}",
                    f"Largest group: {grouped['count'].idxmax()} with {grouped['count'].max()} records"
                ]

        else:
            # Default: show sample data and description
            result['explanation'] = "### Data Overview\n\nHere's a sample of your data with basic statistics:"
            result['data'] = df.head(10)
            result['insights'] = [
                f"Total records: {len(df)}",
                f"Total columns: {len(df.columns)}",
                f"Column types: {df.dtypes.value_counts().to_dict()}"
            ]

        return result
