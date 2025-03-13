from flask import render_template, jsonify
from app.models.database import GDP, Inflation, db
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go
import json

def register_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/gdp')
    def gdp_view():
        # Get GDP data from database
        gdp_records = GDP.query.all()
        years = [record.year for record in gdp_records]
        gdp_values = [record.gdp for record in gdp_records]
        
        # Create DataFrame for filtering capability
        df = pd.DataFrame({'Year': years, 'GDP (billion EUR)': gdp_values})
        
        # Create line chart
        fig_line = px.line(df, x='Year', y='GDP (billion EUR)', title='Latvian GDP Over Time')
        fig_line.update_layout(template='plotly_white')
        
        # Create bar chart
        fig_bar = px.bar(df, x='Year', y='GDP (billion EUR)', title='Latvian GDP by Year')
        fig_bar.update_layout(template='plotly_white')
        
        # Create histogram of GDP distribution
        fig_hist = px.histogram(df, x='GDP (billion EUR)', nbins=20, title='Distribution of Latvian GDP')
        fig_hist.update_layout(template='plotly_white')
        
        # Convert figures to JSON
        chart_line = json.dumps(fig_line, cls=plotly.utils.PlotlyJSONEncoder)
        chart_bar = json.dumps(fig_bar, cls=plotly.utils.PlotlyJSONEncoder)
        chart_hist = json.dumps(fig_hist, cls=plotly.utils.PlotlyJSONEncoder)
        
        # Get min and max years for the filter
        min_year = min(years)
        max_year = max(years)
        
        return render_template('gdp.html', chart_line=chart_line, chart_bar=chart_bar, 
                              chart_hist=chart_hist, min_year=min_year, max_year=max_year)
    
    @app.route('/gdp/data/<int:start_year>/<int:end_year>')
    def gdp_data(start_year, end_year):
        # Get filtered GDP data from the database
        gdp_records = GDP.query.filter(GDP.year >= start_year, GDP.year <= end_year).all()
        years = [record.year for record in gdp_records]
        gdp_values = [record.gdp for record in gdp_records]
        
        # Create DataFrame
        df = pd.DataFrame({'Year': years, 'GDP (billion EUR)': gdp_values})
        
        # Create line chart
        fig_line = px.line(df, x='Year', y='GDP (billion EUR)', title=f'Latvian GDP ({start_year}-{end_year})')
        fig_line.update_layout(template='plotly_white')
        
        # Create bar chart
        fig_bar = px.bar(df, x='Year', y='GDP (billion EUR)', title=f'Latvian GDP by Year ({start_year}-{end_year})')
        fig_bar.update_layout(template='plotly_white')
        
        # Create histogram of GDP distribution
        fig_hist = px.histogram(df, x='GDP (billion EUR)', nbins=20, title=f'Distribution of Latvian GDP ({start_year}-{end_year})')
        fig_hist.update_layout(template='plotly_white')
        
        # Convert figures to JSON
        chart_line = json.dumps(fig_line, cls=plotly.utils.PlotlyJSONEncoder)
        chart_bar = json.dumps(fig_bar, cls=plotly.utils.PlotlyJSONEncoder)
        chart_hist = json.dumps(fig_hist, cls=plotly.utils.PlotlyJSONEncoder)
        
        return jsonify({
            'chart_line': chart_line,
            'chart_bar': chart_bar,
            'chart_hist': chart_hist
        })
    
    @app.route('/inflation')
    def inflation_view():
        # Get inflation data from database
        inflation_records = Inflation.query.all()
        years = [record.year for record in inflation_records]
        inflation_values = [record.inflation for record in inflation_records]
        
        # Create DataFrame for filtering capability
        df = pd.DataFrame({'Year': years, 'Inflation (%)': inflation_values})
        
        # Create line chart
        fig_line = px.line(df, x='Year', y='Inflation (%)', title='Latvian Inflation Rate Over Time')
        fig_line.update_layout(template='plotly_white')
        
        # Create bar chart
        fig_bar = px.bar(df, x='Year', y='Inflation (%)', title='Latvian Inflation Rate by Year')
        fig_bar.update_layout(template='plotly_white')
        
        # Create histogram of inflation distribution
        fig_hist = px.histogram(df, x='Inflation (%)', nbins=20, title='Distribution of Latvian Inflation Rates')
        fig_hist.update_layout(template='plotly_white')
        
        # Convert figures to JSON
        chart_line = json.dumps(fig_line, cls=plotly.utils.PlotlyJSONEncoder)
        chart_bar = json.dumps(fig_bar, cls=plotly.utils.PlotlyJSONEncoder)
        chart_hist = json.dumps(fig_hist, cls=plotly.utils.PlotlyJSONEncoder)
        
        # Get min and max years for the filter
        min_year = min(years)
        max_year = max(years)
        
        return render_template('inflation.html', chart_line=chart_line, chart_bar=chart_bar, 
                              chart_hist=chart_hist, min_year=min_year, max_year=max_year)
    
    @app.route('/inflation/data/<int:start_year>/<int:end_year>')
    def inflation_data(start_year, end_year):
        # Get filtered inflation data from the database
        inflation_records = Inflation.query.filter(Inflation.year >= start_year, Inflation.year <= end_year).all()
        years = [record.year for record in inflation_records]
        inflation_values = [record.inflation for record in inflation_records]
        
        # Create DataFrame
        df = pd.DataFrame({'Year': years, 'Inflation (%)': inflation_values})
        
        # Create line chart
        fig_line = px.line(df, x='Year', y='Inflation (%)', title=f'Latvian Inflation Rate ({start_year}-{end_year})')
        fig_line.update_layout(template='plotly_white')
        
        # Create bar chart
        fig_bar = px.bar(df, x='Year', y='Inflation (%)', title=f'Latvian Inflation Rate by Year ({start_year}-{end_year})')
        fig_bar.update_layout(template='plotly_white')
        
        # Create histogram of inflation distribution
        fig_hist = px.histogram(df, x='Inflation (%)', nbins=20, title=f'Distribution of Latvian Inflation Rates ({start_year}-{end_year})')
        fig_hist.update_layout(template='plotly_white')
        
        # Convert figures to JSON
        chart_line = json.dumps(fig_line, cls=plotly.utils.PlotlyJSONEncoder)
        chart_bar = json.dumps(fig_bar, cls=plotly.utils.PlotlyJSONEncoder)
        chart_hist = json.dumps(fig_hist, cls=plotly.utils.PlotlyJSONEncoder)
        
        return jsonify({
            'chart_line': chart_line,
            'chart_bar': chart_bar,
            'chart_hist': chart_hist
        })
