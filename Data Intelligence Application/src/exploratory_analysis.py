"""
Exploratory Data Analysis Module
Provides automated EDA capabilities
"""

import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, List, Any
import plotly.express as px
import plotly.graph_objects as go


class ExploratoryAnalysis:
    """Automated Exploratory Data Analysis"""

    def __init__(self, df: pd.DataFrame):
        """
        Initialize EDA module

        Args:
            df: DataFrame to analyze
        """
        self.df = df
        self.numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        self.categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
        self.datetime_cols = df.select_dtypes(include=['datetime64']).columns.tolist()

    def show_overview(self):
        """Display dataset overview"""
        st.markdown("### Dataset Information")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Rows", f"{self.df.shape[0]:,}")
        with col2:
            st.metric("Total Columns", self.df.shape[1])
        with col3:
            st.metric("Memory Usage", f"{self.df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
        with col4:
            duplicates = self.df.duplicated().sum()
            st.metric("Duplicate Rows", duplicates)

        st.markdown("---")

        # Column types
        st.markdown("### Column Types")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Numeric Columns", len(self.numeric_cols))
        with col2:
            st.metric("Categorical Columns", len(self.categorical_cols))
        with col3:
            st.metric("Datetime Columns", len(self.datetime_cols))

        # Show column details
        st.markdown("### Column Details")

        column_info = pd.DataFrame({
            'Column': self.df.columns,
            'Type': self.df.dtypes.astype(str),
            'Non-Null Count': self.df.count(),
            'Null Count': self.df.isnull().sum(),
            'Null %': (self.df.isnull().sum() / len(self.df) * 100).round(2),
            'Unique Values': [self.df[col].nunique() for col in self.df.columns]
        })

        st.dataframe(column_info, use_container_width=True)

        # Data sample
        st.markdown("### Data Sample")
        st.dataframe(self.df.head(10), use_container_width=True)

    def show_statistics(self):
        """Display statistical summary"""
        st.markdown("### Statistical Summary")

        if self.numeric_cols:
            # Descriptive statistics
            st.markdown("#### Numeric Columns Statistics")
            stats_df = self.df[self.numeric_cols].describe().T
            stats_df['missing'] = self.df[self.numeric_cols].isnull().sum()
            stats_df['missing_pct'] = (stats_df['missing'] / len(self.df) * 100).round(2)

            st.dataframe(stats_df, use_container_width=True)

            # Distribution plots
            st.markdown("#### Distribution Overview")

            n_cols = min(3, len(self.numeric_cols))
            cols = st.columns(n_cols)

            for idx, col in enumerate(self.numeric_cols[:n_cols]):
                with cols[idx % n_cols]:
                    fig = px.histogram(
                        self.df,
                        x=col,
                        title=f'{col} Distribution',
                        nbins=30
                    )
                    fig.update_layout(height=300, showlegend=False)
                    st.plotly_chart(fig, use_container_width=True)

        else:
            st.info("No numeric columns found in dataset")

        # Categorical statistics
        if self.categorical_cols:
            st.markdown("#### Categorical Columns Statistics")

            cat_stats = []
            for col in self.categorical_cols:
                cat_stats.append({
                    'Column': col,
                    'Unique Values': self.df[col].nunique(),
                    'Most Frequent': self.df[col].mode()[0] if len(self.df[col].mode()) > 0 else None,
                    'Frequency': self.df[col].value_counts().iloc[0] if len(self.df[col]) > 0 else 0,
                    'Missing': self.df[col].isnull().sum(),
                    'Missing %': f"{self.df[col].isnull().sum() / len(self.df) * 100:.2f}"
                })

            cat_df = pd.DataFrame(cat_stats)
            st.dataframe(cat_df, use_container_width=True)

    def show_data_quality(self):
        """Display data quality report"""
        st.markdown("### Data Quality Assessment")

        # Missing data analysis
        st.markdown("#### Missing Data Analysis")

        missing_data = pd.DataFrame({
            'Column': self.df.columns,
            'Missing Count': self.df.isnull().sum(),
            'Missing Percentage': (self.df.isnull().sum() / len(self.df) * 100).round(2)
        })
        missing_data = missing_data[missing_data['Missing Count'] > 0].sort_values(
            'Missing Percentage', ascending=False
        )

        if len(missing_data) > 0:
            st.dataframe(missing_data, use_container_width=True)

            # Missing data visualization
            fig = px.bar(
                missing_data,
                x='Column',
                y='Missing Percentage',
                title='Missing Data by Column',
                labels={'Missing Percentage': 'Missing %'},
                color='Missing Percentage',
                color_continuous_scale='Reds'
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.success("✅ No missing data found!")

        # Duplicate analysis
        st.markdown("#### Duplicate Rows Analysis")
        duplicates = self.df.duplicated().sum()

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Duplicate Rows", duplicates)
        with col2:
            st.metric("Duplicate Percentage", f"{duplicates / len(self.df) * 100:.2f}%")

        if duplicates > 0:
            st.warning(f"⚠️ Found {duplicates} duplicate rows")
            if st.button("Show Duplicate Rows"):
                st.dataframe(self.df[self.df.duplicated(keep=False)], use_container_width=True)

        # Outlier detection
        st.markdown("#### Outlier Detection (IQR Method)")

        if self.numeric_cols:
            outlier_summary = []

            for col in self.numeric_cols:
                Q1 = self.df[col].quantile(0.25)
                Q3 = self.df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR

                outliers = self.df[(self.df[col] < lower_bound) | (self.df[col] > upper_bound)]

                outlier_summary.append({
                    'Column': col,
                    'Outlier Count': len(outliers),
                    'Outlier %': f"{len(outliers) / len(self.df) * 100:.2f}",
                    'Lower Bound': f"{lower_bound:.2f}",
                    'Upper Bound': f"{upper_bound:.2f}"
                })

            outlier_df = pd.DataFrame(outlier_summary)
            outlier_df = outlier_df[outlier_df['Outlier Count'] > 0]

            if len(outlier_df) > 0:
                st.dataframe(outlier_df, use_container_width=True)
            else:
                st.success("✅ No significant outliers detected!")

        # Data type consistency
        st.markdown("#### Data Type Consistency")

        type_issues = []
        for col in self.df.columns:
            if self.df[col].dtype == 'object':
                # Check if column should be numeric
                try:
                    pd.to_numeric(self.df[col], errors='coerce')
                    non_numeric = self.df[col][pd.to_numeric(self.df[col], errors='coerce').isna()].count()
                    if non_numeric < len(self.df) * 0.1:  # Less than 10% non-numeric
                        type_issues.append({
                            'Column': col,
                            'Current Type': 'object',
                            'Suggested Type': 'numeric',
                            'Reason': f'{non_numeric} non-numeric values'
                        })
                except:
                    pass

        if type_issues:
            st.warning("⚠️ Potential data type issues detected:")
            st.dataframe(pd.DataFrame(type_issues), use_container_width=True)
        else:
            st.success("✅ Data types appear consistent!")

    def show_correlations(self):
        """Display correlation analysis"""
        st.markdown("### Correlation Analysis")

        if len(self.numeric_cols) < 2:
            st.warning("Need at least 2 numeric columns for correlation analysis")
            return

        # Correlation matrix
        corr_matrix = self.df[self.numeric_cols].corr()

        st.markdown("#### Correlation Matrix")

        # Heatmap
        fig = px.imshow(
            corr_matrix,
            labels=dict(color="Correlation"),
            x=corr_matrix.columns,
            y=corr_matrix.columns,
            color_continuous_scale='RdBu_r',
            aspect='auto',
            zmin=-1,
            zmax=1
        )
        fig.update_layout(height=600)
        st.plotly_chart(fig, use_container_width=True)

        # Strong correlations
        st.markdown("#### Strong Correlations (|r| > 0.7)")

        strong_corr = []
        for i in range(len(corr_matrix.columns)):
            for j in range(i+1, len(corr_matrix.columns)):
                corr_val = corr_matrix.iloc[i, j]
                if abs(corr_val) > 0.7:
                    strong_corr.append({
                        'Variable 1': corr_matrix.columns[i],
                        'Variable 2': corr_matrix.columns[j],
                        'Correlation': f"{corr_val:.3f}",
                        'Strength': 'Strong Positive' if corr_val > 0 else 'Strong Negative'
                    })

        if strong_corr:
            st.dataframe(pd.DataFrame(strong_corr), use_container_width=True)
        else:
            st.info("No strong correlations found (|r| > 0.7)")

        # Scatter plot matrix for top correlated pairs
        if strong_corr and len(strong_corr) > 0:
            st.markdown("#### Scatter Plots of Top Correlated Pairs")

            top_pair = strong_corr[0]
            var1 = top_pair['Variable 1']
            var2 = top_pair['Variable 2']

            fig = px.scatter(
                self.df,
                x=var1,
                y=var2,
                title=f'{var1} vs {var2} (r = {top_pair["Correlation"]})',
                trendline="ols"
            )
            st.plotly_chart(fig, use_container_width=True)

    def show_distributions(self):
        """Display distribution analysis"""
        st.markdown("### Distribution Analysis")

        if not self.numeric_cols:
            st.warning("No numeric columns found for distribution analysis")
            return

        # Select column
        selected_col = st.selectbox("Select Column", self.numeric_cols)

        if selected_col:
            col1, col2 = st.columns(2)

            with col1:
                # Histogram
                st.markdown("#### Histogram")
                fig = px.histogram(
                    self.df,
                    x=selected_col,
                    nbins=30,
                    title=f'Distribution of {selected_col}'
                )
                st.plotly_chart(fig, use_container_width=True)

                # Box plot
                st.markdown("#### Box Plot")
                fig = px.box(
                    self.df,
                    y=selected_col,
                    title=f'Box Plot: {selected_col}'
                )
                st.plotly_chart(fig, use_container_width=True)

            with col2:
                # Statistics
                st.markdown("#### Distribution Statistics")

                stats = {
                    'Mean': self.df[selected_col].mean(),
                    'Median': self.df[selected_col].median(),
                    'Mode': self.df[selected_col].mode()[0] if len(self.df[selected_col].mode()) > 0 else None,
                    'Std Dev': self.df[selected_col].std(),
                    'Variance': self.df[selected_col].var(),
                    'Skewness': self.df[selected_col].skew(),
                    'Kurtosis': self.df[selected_col].kurtosis(),
                    'Min': self.df[selected_col].min(),
                    'Max': self.df[selected_col].max(),
                    'Range': self.df[selected_col].max() - self.df[selected_col].min()
                }

                stats_df = pd.DataFrame(list(stats.items()), columns=['Statistic', 'Value'])
                st.dataframe(stats_df, use_container_width=True)

                # Interpretation
                st.markdown("#### Interpretation")

                skew = self.df[selected_col].skew()
                if abs(skew) < 0.5:
                    skew_interp = "approximately symmetric"
                elif skew > 0:
                    skew_interp = "right-skewed (positive skew)"
                else:
                    skew_interp = "left-skewed (negative skew)"

                st.info(f"The distribution is **{skew_interp}** with skewness = {skew:.2f}")

        # Categorical distributions
        if self.categorical_cols:
            st.markdown("---")
            st.markdown("### Categorical Variable Distributions")

            selected_cat = st.selectbox("Select Categorical Column", self.categorical_cols)

            if selected_cat:
                value_counts = self.df[selected_cat].value_counts()

                col1, col2 = st.columns(2)

                with col1:
                    # Bar chart
                    fig = px.bar(
                        x=value_counts.index,
                        y=value_counts.values,
                        title=f'Distribution of {selected_cat}',
                        labels={'x': selected_cat, 'y': 'Count'}
                    )
                    st.plotly_chart(fig, use_container_width=True)

                with col2:
                    # Pie chart
                    fig = px.pie(
                        values=value_counts.values,
                        names=value_counts.index,
                        title=f'Proportion of {selected_cat}'
                    )
                    st.plotly_chart(fig, use_container_width=True)
