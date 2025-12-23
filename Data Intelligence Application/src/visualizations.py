"""
Visualization Engine Module
Advanced interactive visualizations
"""

import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from typing import Optional, List


class VisualizationEngine:
    """Advanced visualization creation engine"""

    def __init__(self, df: pd.DataFrame):
        """
        Initialize visualization engine

        Args:
            df: DataFrame to visualize
        """
        self.df = df
        self.numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        self.categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
        self.datetime_cols = df.select_dtypes(include=['datetime64']).columns.tolist()

    def create_visualization(self, viz_type: str):
        """
        Create specified visualization type

        Args:
            viz_type: Type of visualization to create
        """
        if viz_type == "Line Chart":
            self.create_line_chart()
        elif viz_type == "Bar Chart":
            self.create_bar_chart()
        elif viz_type == "Scatter Plot":
            self.create_scatter_plot()
        elif viz_type == "Box Plot":
            self.create_box_plot()
        elif viz_type == "Histogram":
            self.create_histogram()
        elif viz_type == "Heatmap":
            self.create_heatmap()
        elif viz_type == "Pie Chart":
            self.create_pie_chart()
        elif viz_type == "Area Chart":
            self.create_area_chart()
        elif viz_type == "3D Scatter":
            self.create_3d_scatter()
        elif viz_type == "Pair Plot":
            self.create_pair_plot()

    def create_line_chart(self):
        """Create interactive line chart"""
        st.subheader("Line Chart")

        col1, col2 = st.columns(2)

        with col1:
            x_col = st.selectbox("X-axis", self.df.columns.tolist(), key="line_x")

        with col2:
            y_cols = st.multiselect(
                "Y-axis (can select multiple)",
                self.numeric_cols,
                default=self.numeric_cols[0] if self.numeric_cols else None,
                key="line_y"
            )

        if x_col and y_cols:
            color_col = st.selectbox(
                "Color by (optional)",
                [None] + self.categorical_cols,
                key="line_color"
            )

            fig = go.Figure()

            for y_col in y_cols:
                if color_col:
                    for category in self.df[color_col].unique():
                        df_filtered = self.df[self.df[color_col] == category]
                        fig.add_trace(go.Scatter(
                            x=df_filtered[x_col],
                            y=df_filtered[y_col],
                            mode='lines+markers',
                            name=f'{y_col} - {category}'
                        ))
                else:
                    fig.add_trace(go.Scatter(
                        x=self.df[x_col],
                        y=self.df[y_col],
                        mode='lines+markers',
                        name=y_col
                    ))

            fig.update_layout(
                title=f'Line Chart: {", ".join(y_cols)} vs {x_col}',
                xaxis_title=x_col,
                yaxis_title='Value',
                hovermode='x unified',
                height=600
            )

            st.plotly_chart(fig, use_container_width=True)

    def create_bar_chart(self):
        """Create interactive bar chart"""
        st.subheader("Bar Chart")

        col1, col2 = st.columns(2)

        with col1:
            x_col = st.selectbox(
                "X-axis (Category)",
                self.categorical_cols + self.numeric_cols,
                key="bar_x"
            )

        with col2:
            y_col = st.selectbox(
                "Y-axis (Value)",
                self.numeric_cols,
                key="bar_y"
            )

        if x_col and y_col:
            agg_func = st.selectbox(
                "Aggregation Function",
                ["sum", "mean", "count", "median", "min", "max"],
                key="bar_agg"
            )

            color_col = st.selectbox(
                "Color by (optional)",
                [None] + self.categorical_cols,
                key="bar_color"
            )

            # Aggregate data
            if color_col:
                df_agg = self.df.groupby([x_col, color_col])[y_col].agg(agg_func).reset_index()
                fig = px.bar(
                    df_agg,
                    x=x_col,
                    y=y_col,
                    color=color_col,
                    title=f'Bar Chart: {agg_func.title()} of {y_col} by {x_col}',
                    barmode='group'
                )
            else:
                df_agg = self.df.groupby(x_col)[y_col].agg(agg_func).reset_index()
                fig = px.bar(
                    df_agg,
                    x=x_col,
                    y=y_col,
                    title=f'Bar Chart: {agg_func.title()} of {y_col} by {x_col}'
                )

            fig.update_layout(height=600)
            st.plotly_chart(fig, use_container_width=True)

    def create_scatter_plot(self):
        """Create interactive scatter plot"""
        st.subheader("Scatter Plot")

        col1, col2 = st.columns(2)

        with col1:
            x_col = st.selectbox("X-axis", self.numeric_cols, key="scatter_x")

        with col2:
            y_col = st.selectbox("Y-axis", self.numeric_cols, key="scatter_y")

        if x_col and y_col:
            col1, col2, col3 = st.columns(3)

            with col1:
                color_col = st.selectbox(
                    "Color by (optional)",
                    [None] + self.categorical_cols + self.numeric_cols,
                    key="scatter_color"
                )

            with col2:
                size_col = st.selectbox(
                    "Size by (optional)",
                    [None] + self.numeric_cols,
                    key="scatter_size"
                )

            with col3:
                show_trendline = st.checkbox("Show Trendline", value=False)

            fig = px.scatter(
                self.df,
                x=x_col,
                y=y_col,
                color=color_col,
                size=size_col,
                title=f'Scatter Plot: {y_col} vs {x_col}',
                trendline="ols" if show_trendline else None,
                hover_data=self.df.columns.tolist()
            )

            fig.update_layout(height=600)
            st.plotly_chart(fig, use_container_width=True)

            # Show correlation if both are numeric
            if x_col in self.numeric_cols and y_col in self.numeric_cols:
                corr = self.df[x_col].corr(self.df[y_col])
                st.info(f"📊 Correlation coefficient: {corr:.3f}")

    def create_box_plot(self):
        """Create box plot"""
        st.subheader("Box Plot")

        col1, col2 = st.columns(2)

        with col1:
            y_col = st.selectbox("Value Column", self.numeric_cols, key="box_y")

        with col2:
            x_col = st.selectbox(
                "Group by (optional)",
                [None] + self.categorical_cols,
                key="box_x"
            )

        if y_col:
            color_col = st.selectbox(
                "Color by (optional)",
                [None] + self.categorical_cols,
                key="box_color"
            )

            fig = px.box(
                self.df,
                x=x_col,
                y=y_col,
                color=color_col,
                title=f'Box Plot: {y_col}' + (f' by {x_col}' if x_col else ''),
                points="outliers"
            )

            fig.update_layout(height=600)
            st.plotly_chart(fig, use_container_width=True)

    def create_histogram(self):
        """Create histogram"""
        st.subheader("Histogram")

        col1, col2 = st.columns(2)

        with col1:
            x_col = st.selectbox("Column", self.numeric_cols, key="hist_x")

        with col2:
            nbins = st.slider("Number of Bins", min_value=10, max_value=100, value=30, key="hist_bins")

        if x_col:
            color_col = st.selectbox(
                "Color by (optional)",
                [None] + self.categorical_cols,
                key="hist_color"
            )

            marginal = st.selectbox(
                "Marginal Plot",
                [None, "box", "violin", "rug"],
                key="hist_marginal"
            )

            fig = px.histogram(
                self.df,
                x=x_col,
                color=color_col,
                nbins=nbins,
                marginal=marginal,
                title=f'Distribution of {x_col}'
            )

            fig.update_layout(height=600)
            st.plotly_chart(fig, use_container_width=True)

            # Show statistics
            st.markdown("#### Statistics")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Mean", f"{self.df[x_col].mean():.2f}")
            with col2:
                st.metric("Median", f"{self.df[x_col].median():.2f}")
            with col3:
                st.metric("Std Dev", f"{self.df[x_col].std():.2f}")
            with col4:
                st.metric("Skewness", f"{self.df[x_col].skew():.2f}")

    def create_heatmap(self):
        """Create correlation heatmap"""
        st.subheader("Correlation Heatmap")

        if len(self.numeric_cols) < 2:
            st.warning("Need at least 2 numeric columns for correlation heatmap")
            return

        # Select columns
        selected_cols = st.multiselect(
            "Select Columns (leave empty for all numeric columns)",
            self.numeric_cols,
            default=self.numeric_cols[:min(10, len(self.numeric_cols))],
            key="heatmap_cols"
        )

        if selected_cols:
            corr_matrix = self.df[selected_cols].corr()

            fig = px.imshow(
                corr_matrix,
                labels=dict(color="Correlation"),
                x=corr_matrix.columns,
                y=corr_matrix.columns,
                color_continuous_scale='RdBu_r',
                aspect='auto',
                zmin=-1,
                zmax=1,
                text_auto='.2f'
            )

            fig.update_layout(
                title='Correlation Heatmap',
                height=600
            )

            st.plotly_chart(fig, use_container_width=True)

    def create_pie_chart(self):
        """Create pie chart"""
        st.subheader("Pie Chart")

        if not self.categorical_cols:
            st.warning("No categorical columns available for pie chart")
            return

        col = st.selectbox("Category Column", self.categorical_cols, key="pie_col")

        if col:
            value_counts = self.df[col].value_counts()

            # Option to limit categories
            top_n = st.slider(
                "Show Top N Categories",
                min_value=3,
                max_value=min(20, len(value_counts)),
                value=min(10, len(value_counts)),
                key="pie_top"
            )

            value_counts = value_counts.head(top_n)

            fig = px.pie(
                values=value_counts.values,
                names=value_counts.index,
                title=f'Distribution of {col} (Top {top_n})'
            )

            fig.update_layout(height=600)
            st.plotly_chart(fig, use_container_width=True)

    def create_area_chart(self):
        """Create area chart"""
        st.subheader("Area Chart")

        col1, col2 = st.columns(2)

        with col1:
            x_col = st.selectbox("X-axis", self.df.columns.tolist(), key="area_x")

        with col2:
            y_cols = st.multiselect(
                "Y-axis (can select multiple)",
                self.numeric_cols,
                default=self.numeric_cols[:min(3, len(self.numeric_cols))],
                key="area_y"
            )

        if x_col and y_cols:
            # Sort by x
            df_sorted = self.df.sort_values(x_col)

            fig = go.Figure()

            for y_col in y_cols:
                fig.add_trace(go.Scatter(
                    x=df_sorted[x_col],
                    y=df_sorted[y_col],
                    mode='lines',
                    name=y_col,
                    fill='tonexty' if y_cols.index(y_col) > 0 else 'tozeroy',
                    stackgroup='one'
                ))

            fig.update_layout(
                title=f'Area Chart: {", ".join(y_cols)} vs {x_col}',
                xaxis_title=x_col,
                yaxis_title='Value',
                hovermode='x unified',
                height=600
            )

            st.plotly_chart(fig, use_container_width=True)

    def create_3d_scatter(self):
        """Create 3D scatter plot"""
        st.subheader("3D Scatter Plot")

        if len(self.numeric_cols) < 3:
            st.warning("Need at least 3 numeric columns for 3D scatter plot")
            return

        col1, col2, col3 = st.columns(3)

        with col1:
            x_col = st.selectbox("X-axis", self.numeric_cols, key="3d_x")

        with col2:
            y_col = st.selectbox("Y-axis", self.numeric_cols, key="3d_y")

        with col3:
            z_col = st.selectbox("Z-axis", self.numeric_cols, key="3d_z")

        if x_col and y_col and z_col:
            color_col = st.selectbox(
                "Color by (optional)",
                [None] + self.categorical_cols + self.numeric_cols,
                key="3d_color"
            )

            size_col = st.selectbox(
                "Size by (optional)",
                [None] + self.numeric_cols,
                key="3d_size"
            )

            fig = px.scatter_3d(
                self.df,
                x=x_col,
                y=y_col,
                z=z_col,
                color=color_col,
                size=size_col,
                title=f'3D Scatter: {x_col}, {y_col}, {z_col}'
            )

            fig.update_layout(height=700)
            st.plotly_chart(fig, use_container_width=True)

    def create_pair_plot(self):
        """Create pair plot matrix"""
        st.subheader("Pair Plot Matrix")

        if len(self.numeric_cols) < 2:
            st.warning("Need at least 2 numeric columns for pair plot")
            return

        # Select columns (limit to prevent performance issues)
        selected_cols = st.multiselect(
            "Select Columns (max 5 recommended)",
            self.numeric_cols,
            default=self.numeric_cols[:min(4, len(self.numeric_cols))],
            key="pair_cols"
        )

        if selected_cols and len(selected_cols) >= 2:
            color_col = st.selectbox(
                "Color by (optional)",
                [None] + self.categorical_cols,
                key="pair_color"
            )

            if len(selected_cols) > 5:
                st.warning("⚠️ Selecting more than 5 columns may impact performance")

            with st.spinner("Generating pair plot..."):
                fig = px.scatter_matrix(
                    self.df,
                    dimensions=selected_cols,
                    color=color_col,
                    title='Pair Plot Matrix'
                )

                fig.update_layout(height=800)
                st.plotly_chart(fig, use_container_width=True)
