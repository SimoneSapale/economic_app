## Latvian Economy Data Visualization

This project is a Flask web application that visualizes Latvian GDP and inflation data using interactive charts. It demonstrates the use of Flask, SQLAlchemy, SQLite, and Plotly for data visualization.

## Prerequisites

- Docker and Docker Compose

## Project Structure

```
economic_app/
├── app/                     # Main application package
│   ├── __init__.py          # Flask application initialization
│   ├── models/              # Database models
│   │   └── database.py      # Database configuration and models
│   ├── routes.py            # Application routes
│   ├── static/              # Static files (CSS, JS)
│   │   └── css/
│   │       └── style.css    # Custom styling
│   └── templates/           # HTML templates
│       ├── gdp.html         # GDP visualization page
│       ├── index.html       # Home page
│       └── inflation.html   # Inflation visualization page
├── app.py                   # Application entry point
├── docker-compose.yml       # Docker Compose configuration
├── Dockerfile               # Docker configuration
├── instance/                # Instance folder for SQLite database
│   └── latvian_economy.db   # SQLite database file
└── requirements.txt         # Python dependencies
```

## Setup and Running

### Using Docker 

1. Clone the repository:
   ```bash
   git clone https://github.com/SimoneSapale/economic_app.git 
   cd latvian_economy_app
   ```

2. Build and run the Docker container:
   ```bash
   docker-compose up --build
   ```

3. Access the application in your browser at localhost if you can't access it there then use docker inspect on container and get the docker container ip address and use it instead of localhost:
   ```
   http://localhost:5000
   ```

## Usage

1. The home page displays options to view GDP or inflation data.
2. Click on "Skatīt IKP datus" to view GDP visualizations.
3. Click on "Skatīt inflācijas datus" to view inflation visualizations.
4. Use the sliders to filter data by year range.
5. Click "Pielietot" to apply the filter and update the visualizations.

## Technologies Used

- Flask: Web framework
- SQLAlchemy: ORM for database operations
- SQLite: Database engine
- Plotly: Interactive data visualizations
- Pandas: Data manipulation
- Docker: Containerization
