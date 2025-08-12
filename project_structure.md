# BluckBoster ETL Project Structure

```
bluckboster-etl-fuad-sam-lana-luca/
├── etl_process/
│   ├── config/
│   │   ├── __init__.py
│   │   ├── db_config.py                  # Database configuration
│   │   └── env_config.py                 # Environment configuration
│   ├── data/
│   │   ├── raw/                          # Raw extracted data
│   │   ├── processed/                    # Cleaned and joined data
│   │   └── output/                       # Final ETL outputs 
│   ├── src/
│   │   ├── extract/
│   │   │   ├── __init__.py
│   │   │   └── extract.py                # Raw data extraction functions
│   │   ├── transform/
│   │   │   ├── __init__.py
│   │   │   └── transform.py              # Data cleaning and joining
│   │   ├── load/
│   │   │   ├── __init__.py
│   │   │   └── load.py                   # Combined ETL functions (not needed)
│   │   ├── sql/
│   │   │   ├── film_actor_joins.sql      # Film -> film_actor -> actor
│   │   │   ├── rental_payment_joins.sql  # Film -> inventory -> rental -> payment
│   │   │   ├── customer_location_joins.sql # Customer -> address -> city -> country
│   │   │   └── staff_performance_joins.sql # Staff -> rental -> payment
│   │   └── utils/
│   │       ├── __init__.py
│   │       └── logging_utils.py          # Logging utilities
│   ├── notebooks/
│   │   ├── 01_data_exploration.ipynb     # Initial EDA
│   │   ├── 02_data_cleaning.ipynb        # Data quality analysis
│   │   ├── 03_film_analysis.ipynb        # Film/actor analysis
│   │   ├── 04_customer_analysis.ipynb    # Customer/location analysis
│   │   └── 05_revenue_analysis.ipynb     # Revenue/rental analysis
│   ├── scripts/
│   │   ├── __init__.py
│   │   └── run_etl.py                    # ETL execution script
│   ├── tests/
│   │   ├── unit_tests/
│   │   │   ├── test_extract.py           # Extract function tests
│   │   │   ├── test_transform.py         # Transform function tests
│   │   │   └── test_load.py              # Load function tests
│   │   └── run_tests.py
│   └── requirements-setup.txt
├── streamlit/
│   ├── app.py                            # Main Streamlit application
│   ├── pages/
│   │   ├── film_analysis.py              # Film/actor visualizations
│   │   ├── customer_analysis.py          # Customer/location maps
│   │   ├── revenue_analysis.py           # Revenue/rental charts
│   │   └── staff_analysis.py             # Staff performance charts
│   ├── components/
│   │   ├── charts.py                     # Reusable chart functions
│   │   └── maps.py                       # Map visualization functions
│   └── requirements.txt                  # Streamlit dependencies
├── images/
│   └── mainERD.png                       # Database ERD
├── presentation/
│   ├── slides.pptx                       # Presentation slides
│   └── assets/                           # Images/charts for presentation
├── README.md
├── goodpractice.md
└── project_structure.md
```

## Component Responsibilities

### ETL Process (`etl_process/`)
- **Extract** (`src/extract/`): Database connection and raw data extraction
- **Transform** (`src/transform/`): Data cleaning, joining, and validation
- **Load** (`src/load/`): Combined ETL pipeline functions
- **SQL** (`src/sql/`): SQL queries for specific joins
- **Notebooks** (`notebooks/`): Jupyter notebooks for analysis
- **Config** (`config/`): Database and environment configuration

### Streamlit App (`streamlit/`)
- **Main App**: Dashboard with navigation
- **Pages**: Separate pages for different analysis areas
- **Components**: Reusable visualization functions

### Data Analysis Areas

1. **Film Analysis**
   - Best/worst films by actor
   - Film ratings vs rental rates
   - Sequel analysis
   - Films by category/language/year

2. **Customer Analysis**
   - Customer location mapping
   - Geographic distribution analysis

3. **Revenue Analysis**
   - Highest selling movies
   - Revenue by category/time
   - Rental patterns

4. **Staff Analysis**
   - Staff performance metrics
   - Employee location analysis

### Required Database Joins
- Film → film_actor → actor
- Film → inventory → rental → payment
- Customer → address → city → country
- Staff → rental → payment