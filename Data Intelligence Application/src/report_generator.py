"""
Automated Report Generator Module
Creates comprehensive analysis reports
"""

import pandas as pd
import numpy as np
from datetime import datetime
from typing import List, Dict, Any


class ReportGenerator:
    """Generate comprehensive data analysis reports"""

    def __init__(self, df: pd.DataFrame):
        """
        Initialize report generator

        Args:
            df: DataFrame to analyze
        """
        self.df = df
        self.numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        self.categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
        self.datetime_cols = df.select_dtypes(include=['datetime64']).columns.tolist()
        self.generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def generate_report(
        self,
        sections: List[str],
        format: str = "HTML"
    ) -> str:
        """
        Generate comprehensive report

        Args:
            sections: List of sections to include
            format: Output format (HTML, Markdown, PDF)

        Returns:
            str: Generated report content
        """
        if format == "HTML":
            return self._generate_html_report(sections)
        elif format == "Markdown":
            return self._generate_markdown_report(sections)
        else:
            return self._generate_markdown_report(sections)

    def _generate_html_report(self, sections: List[str]) -> str:
        """Generate HTML format report"""
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Data Analysis Report</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 40px;
            background-color: #f5f5f5;
            color: #333;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            padding: 40px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #34495e;
            margin-top: 30px;
            border-left: 4px solid #3498db;
            padding-left: 15px;
        }}
        h3 {{
            color: #7f8c8d;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }}
        th {{
            background-color: #3498db;
            color: white;
        }}
        tr:nth-child(even) {{
            background-color: #f2f2f2;
        }}
        .metric {{
            display: inline-block;
            background-color: #ecf0f1;
            padding: 15px 25px;
            margin: 10px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }}
        .metric-value {{
            font-size: 24px;
            font-weight: bold;
            color: #2c3e50;
        }}
        .metric-label {{
            font-size: 14px;
            color: #7f8c8d;
        }}
        .insight {{
            background-color: #e8f5e9;
            padding: 15px;
            margin: 10px 0;
            border-left: 4px solid #4caf50;
            border-radius: 3px;
        }}
        .warning {{
            background-color: #fff3cd;
            padding: 15px;
            margin: 10px 0;
            border-left: 4px solid #ffc107;
            border-radius: 3px;
        }}
        .footer {{
            margin-top: 50px;
            padding-top: 20px;
            border-top: 1px solid #ddd;
            color: #7f8c8d;
            font-size: 12px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Data Analysis Report</h1>
        <p><strong>Generated:</strong> {self.generated_at}</p>
        <p><strong>Dataset:</strong> {len(self.df)} rows × {len(self.df.columns)} columns</p>
"""

        for section in sections:
            if section == "Executive Summary":
                html += self._html_executive_summary()
            elif section == "Data Overview":
                html += self._html_data_overview()
            elif section == "Statistical Analysis":
                html += self._html_statistical_analysis()
            elif section == "Data Quality Assessment":
                html += self._html_data_quality()
            elif section == "Correlation Analysis":
                html += self._html_correlation_analysis()
            elif section == "Key Insights":
                html += self._html_key_insights()
            elif section == "Visualizations":
                html += self._html_visualizations()
            elif section == "Recommendations":
                html += self._html_recommendations()

        html += f"""
        <div class="footer">
            <p>Report generated by Data Intelligence App on {self.generated_at}</p>
        </div>
    </div>
</body>
</html>
"""
        return html

    def _generate_markdown_report(self, sections: List[str]) -> str:
        """Generate Markdown format report"""
        md = f"""# 📊 Data Analysis Report

**Generated:** {self.generated_at}

**Dataset:** {len(self.df)} rows × {len(self.df.columns)} columns

---

"""

        for section in sections:
            if section == "Executive Summary":
                md += self._md_executive_summary()
            elif section == "Data Overview":
                md += self._md_data_overview()
            elif section == "Statistical Analysis":
                md += self._md_statistical_analysis()
            elif section == "Data Quality Assessment":
                md += self._md_data_quality()
            elif section == "Correlation Analysis":
                md += self._md_correlation_analysis()
            elif section == "Key Insights":
                md += self._md_key_insights()
            elif section == "Recommendations":
                md += self._md_recommendations()

        md += f"\n\n---\n\n*Report generated by Data Intelligence App on {self.generated_at}*\n"
        return md

    # HTML Section Generators

    def _html_executive_summary(self) -> str:
        """Generate executive summary section (HTML)"""
        total_missing = self.df.isnull().sum().sum()
        missing_pct = (total_missing / (len(self.df) * len(self.df.columns)) * 100)

        html = """
        <h2>Executive Summary</h2>
        <div>
"""
        html += f"""
            <div class="metric">
                <div class="metric-label">Total Records</div>
                <div class="metric-value">{len(self.df):,}</div>
            </div>
            <div class="metric">
                <div class="metric-label">Total Features</div>
                <div class="metric-value">{len(self.df.columns)}</div>
            </div>
            <div class="metric">
                <div class="metric-label">Numeric Columns</div>
                <div class="metric-value">{len(self.numeric_cols)}</div>
            </div>
            <div class="metric">
                <div class="metric-label">Categorical Columns</div>
                <div class="metric-value">{len(self.categorical_cols)}</div>
            </div>
            <div class="metric">
                <div class="metric-label">Missing Data</div>
                <div class="metric-value">{missing_pct:.2f}%</div>
            </div>
        </div>
"""
        return html

    def _html_data_overview(self) -> str:
        """Generate data overview section (HTML)"""
        html = "<h2>Data Overview</h2>\n"

        # Column information
        html += "<h3>Column Information</h3>\n<table>\n"
        html += "<tr><th>Column</th><th>Type</th><th>Non-Null</th><th>Unique</th><th>Sample</th></tr>\n"

        for col in self.df.columns[:20]:  # Limit to first 20 columns
            dtype = str(self.df[col].dtype)
            non_null = self.df[col].count()
            unique = self.df[col].nunique()
            sample = str(self.df[col].iloc[0]) if len(self.df) > 0 else "N/A"

            html += f"<tr><td>{col}</td><td>{dtype}</td><td>{non_null:,}</td><td>{unique:,}</td><td>{sample[:50]}</td></tr>\n"

        html += "</table>\n"
        return html

    def _html_statistical_analysis(self) -> str:
        """Generate statistical analysis section (HTML)"""
        if not self.numeric_cols:
            return "<h2>Statistical Analysis</h2>\n<p>No numeric columns available for analysis.</p>\n"

        html = "<h2>Statistical Analysis</h2>\n"
        html += "<h3>Descriptive Statistics</h3>\n<table>\n"

        stats = self.df[self.numeric_cols].describe()
        html += "<tr><th>Statistic</th>" + "".join([f"<th>{col}</th>" for col in stats.columns]) + "</tr>\n"

        for idx in stats.index:
            html += f"<tr><td><strong>{idx}</strong></td>"
            for col in stats.columns:
                html += f"<td>{stats.loc[idx, col]:.2f}</td>"
            html += "</tr>\n"

        html += "</table>\n"
        return html

    def _html_data_quality(self) -> str:
        """Generate data quality section (HTML)"""
        html = "<h2>Data Quality Assessment</h2>\n"

        # Missing data
        missing = self.df.isnull().sum()
        missing_cols = missing[missing > 0]

        if len(missing_cols) > 0:
            html += '<div class="warning">\n'
            html += f"<strong>⚠️ Missing Data Found</strong><br>\n"
            html += f"Total missing values: {missing_cols.sum():,}<br>\n"
            html += f"Affected columns: {len(missing_cols)}\n"
            html += "</div>\n"

            html += "<h3>Missing Data by Column</h3>\n<table>\n"
            html += "<tr><th>Column</th><th>Missing Count</th><th>Missing %</th></tr>\n"

            for col in missing_cols.index:
                pct = (missing_cols[col] / len(self.df) * 100)
                html += f"<tr><td>{col}</td><td>{missing_cols[col]:,}</td><td>{pct:.2f}%</td></tr>\n"

            html += "</table>\n"
        else:
            html += '<div class="insight">✅ No missing data found!</div>\n'

        # Duplicates
        duplicates = self.df.duplicated().sum()
        if duplicates > 0:
            html += f'<div class="warning">⚠️ Found {duplicates:,} duplicate rows ({duplicates/len(self.df)*100:.2f}%)</div>\n'
        else:
            html += '<div class="insight">✅ No duplicate rows found!</div>\n'

        return html

    def _html_correlation_analysis(self) -> str:
        """Generate correlation analysis section (HTML)"""
        if len(self.numeric_cols) < 2:
            return "<h2>Correlation Analysis</h2>\n<p>Need at least 2 numeric columns for correlation analysis.</p>\n"

        html = "<h2>Correlation Analysis</h2>\n"

        corr_matrix = self.df[self.numeric_cols].corr()

        # Find strong correlations
        strong_corr = []
        for i in range(len(corr_matrix.columns)):
            for j in range(i+1, len(corr_matrix.columns)):
                corr_val = corr_matrix.iloc[i, j]
                if abs(corr_val) > 0.7:
                    strong_corr.append({
                        'var1': corr_matrix.columns[i],
                        'var2': corr_matrix.columns[j],
                        'corr': corr_val
                    })

        if strong_corr:
            html += "<h3>Strong Correlations (|r| > 0.7)</h3>\n<table>\n"
            html += "<tr><th>Variable 1</th><th>Variable 2</th><th>Correlation</th><th>Strength</th></tr>\n"

            for corr in strong_corr:
                strength = "Strong Positive" if corr['corr'] > 0 else "Strong Negative"
                html += f"<tr><td>{corr['var1']}</td><td>{corr['var2']}</td><td>{corr['corr']:.3f}</td><td>{strength}</td></tr>\n"

            html += "</table>\n"
        else:
            html += "<p>No strong correlations found (|r| > 0.7)</p>\n"

        return html

    def _html_key_insights(self) -> str:
        """Generate key insights section (HTML)"""
        html = "<h2>Key Insights</h2>\n"

        insights = self._generate_insights()

        for insight in insights:
            html += f'<div class="insight">{insight}</div>\n'

        return html

    def _html_visualizations(self) -> str:
        """Generate visualizations section (HTML)"""
        html = "<h2>Visualizations</h2>\n"
        html += "<p><em>Note: Interactive visualizations are available in the main application.</em></p>\n"
        return html

    def _html_recommendations(self) -> str:
        """Generate recommendations section (HTML)"""
        html = "<h2>Recommendations</h2>\n"

        recommendations = self._generate_recommendations()

        html += "<ul>\n"
        for rec in recommendations:
            html += f"<li>{rec}</li>\n"
        html += "</ul>\n"

        return html

    # Markdown Section Generators

    def _md_executive_summary(self) -> str:
        """Generate executive summary section (Markdown)"""
        total_missing = self.df.isnull().sum().sum()
        missing_pct = (total_missing / (len(self.df) * len(self.df.columns)) * 100)

        md = f"""## Executive Summary

- **Total Records**: {len(self.df):,}
- **Total Features**: {len(self.df.columns)}
- **Numeric Columns**: {len(self.numeric_cols)}
- **Categorical Columns**: {len(self.categorical_cols)}
- **Missing Data**: {missing_pct:.2f}%

"""
        return md

    def _md_data_overview(self) -> str:
        """Generate data overview section (Markdown)"""
        md = "## Data Overview\n\n### Column Information\n\n"
        md += "| Column | Type | Non-Null | Unique |\n"
        md += "|--------|------|----------|--------|\n"

        for col in self.df.columns[:20]:
            dtype = str(self.df[col].dtype)
            non_null = self.df[col].count()
            unique = self.df[col].nunique()
            md += f"| {col} | {dtype} | {non_null:,} | {unique:,} |\n"

        md += "\n"
        return md

    def _md_statistical_analysis(self) -> str:
        """Generate statistical analysis section (Markdown)"""
        if not self.numeric_cols:
            return "## Statistical Analysis\n\nNo numeric columns available for analysis.\n\n"

        md = "## Statistical Analysis\n\n### Descriptive Statistics\n\n"

        stats = self.df[self.numeric_cols].describe()
        md += stats.to_markdown() + "\n\n"

        return md

    def _md_data_quality(self) -> str:
        """Generate data quality section (Markdown)"""
        md = "## Data Quality Assessment\n\n"

        # Missing data
        missing = self.df.isnull().sum()
        missing_cols = missing[missing > 0]

        if len(missing_cols) > 0:
            md += f"⚠️ **Missing Data Found**: {missing_cols.sum():,} total missing values in {len(missing_cols)} columns\n\n"
        else:
            md += "✅ **No missing data found!**\n\n"

        # Duplicates
        duplicates = self.df.duplicated().sum()
        if duplicates > 0:
            md += f"⚠️ **Duplicates Found**: {duplicates:,} duplicate rows ({duplicates/len(self.df)*100:.2f}%)\n\n"
        else:
            md += "✅ **No duplicate rows found!**\n\n"

        return md

    def _md_correlation_analysis(self) -> str:
        """Generate correlation analysis section (Markdown)"""
        if len(self.numeric_cols) < 2:
            return "## Correlation Analysis\n\nNeed at least 2 numeric columns for correlation analysis.\n\n"

        md = "## Correlation Analysis\n\n"

        corr_matrix = self.df[self.numeric_cols].corr()

        # Find strong correlations
        strong_corr = []
        for i in range(len(corr_matrix.columns)):
            for j in range(i+1, len(corr_matrix.columns)):
                corr_val = corr_matrix.iloc[i, j]
                if abs(corr_val) > 0.7:
                    strong_corr.append(f"- **{corr_matrix.columns[i]}** ↔ **{corr_matrix.columns[j]}**: {corr_val:.3f}")

        if strong_corr:
            md += "### Strong Correlations (|r| > 0.7)\n\n"
            md += "\n".join(strong_corr) + "\n\n"
        else:
            md += "No strong correlations found (|r| > 0.7)\n\n"

        return md

    def _md_key_insights(self) -> str:
        """Generate key insights section (Markdown)"""
        md = "## Key Insights\n\n"

        insights = self._generate_insights()

        for insight in insights:
            md += f"- {insight}\n"

        md += "\n"
        return md

    def _md_recommendations(self) -> str:
        """Generate recommendations section (Markdown)"""
        md = "## Recommendations\n\n"

        recommendations = self._generate_recommendations()

        for rec in recommendations:
            md += f"- {rec}\n"

        md += "\n"
        return md

    # Helper Methods

    def _generate_insights(self) -> List[str]:
        """Generate data insights"""
        insights = []

        insights.append(f"Dataset contains {len(self.df):,} records and {len(self.df.columns)} features")

        # Numeric insights
        if self.numeric_cols:
            for col in self.numeric_cols[:3]:
                mean_val = self.df[col].mean()
                std_val = self.df[col].std()
                insights.append(f"**{col}**: Mean = {mean_val:.2f}, Std Dev = {std_val:.2f}")

        # Categorical insights
        if self.categorical_cols:
            for col in self.categorical_cols[:2]:
                n_unique = self.df[col].nunique()
                insights.append(f"**{col}**: {n_unique} unique values")

        # Missing data insight
        missing_pct = (self.df.isnull().sum().sum() / (len(self.df) * len(self.df.columns)) * 100)
        if missing_pct > 5:
            insights.append(f"⚠️ Significant missing data: {missing_pct:.2f}% of total values")

        return insights

    def _generate_recommendations(self) -> List[str]:
        """Generate recommendations"""
        recommendations = []

        # Missing data recommendation
        missing = self.df.isnull().sum()
        missing_cols = missing[missing > 0]
        if len(missing_cols) > 0:
            recommendations.append(f"Address missing data in {len(missing_cols)} columns using imputation or removal")

        # Duplicates recommendation
        duplicates = self.df.duplicated().sum()
        if duplicates > 0:
            recommendations.append(f"Remove or investigate {duplicates:,} duplicate rows")

        # Outliers recommendation
        if self.numeric_cols:
            recommendations.append("Investigate outliers in numeric columns using IQR or Z-score methods")

        # Data type recommendation
        recommendations.append("Validate data types for all columns and convert where necessary")

        # Analysis recommendations
        if len(self.numeric_cols) >= 2:
            recommendations.append("Perform correlation analysis to identify relationships between variables")

        if self.categorical_cols and self.numeric_cols:
            recommendations.append("Conduct group-by analysis to understand patterns across categories")

        recommendations.append("Create visualizations to better understand data distributions and patterns")

        return recommendations
