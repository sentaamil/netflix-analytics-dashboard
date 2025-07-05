# 🎬 Netflix Analytics Dashboard
(assets/banner.png)
<div align="center">

  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-1.25+-red.svg" alt="Streamlit">
  <img src="https://img.shields.io/badge/MySQL-8.0+-orange.svg" alt="MySQL">
  <img src="https://img.shields.io/badge/SQLAlchemy-2.0+-green.svg" alt="SQLAlchemy">
  <img src="https://img.shields.io/badge/Plotly-5.15+-purple.svg" alt="Plotly">
</div>

<div align="center">
  <h3>🚀 A fully interactive, Netflix-themed analytics dashboard built with Streamlit, MySQL, and modern data visualization libraries</h3>
</div>

---

## 🌟 **Project Overview**

This comprehensive Netflix Analytics Dashboard provides deep insights into Netflix's content library through an intuitive, dark-themed interface inspired by Netflix's own design language. Built with modern web technologies and robust database connectivity, it offers real-time data visualization and interactive filtering capabilities.

### 🎯 **Key Highlights**
- **🎨 Netflix-Inspired UI**: Authentic Netflix color scheme with red (#e50914) and black gradients
- **📊 Interactive Visualizations**: 8+ different chart types using Plotly and Matplotlib
- **🔐 Secure Database Connection**: MySQL integration with SQLAlchemy and environment variables
- **🔍 Advanced Filtering**: Multi-parameter filtering system for comprehensive data exploration
- **💻 Custom SQL Interface**: Built-in SQL query executor for advanced users
- **📱 Responsive Design**: Optimized for desktop and mobile viewing

---

## ✨ **Features**

### 🔧 **Technical Features**
- ✅ **MySQL Database Integration** using SQLAlchemy ORM
- ✅ **Secure Configuration** with `.env` file for database credentials
- ✅ **Real-time Data Processing** with Pandas for data manipulation
- ✅ **Interactive Charts** powered by Plotly and Matplotlib
- ✅ **Custom CSS Styling** with Netflix-themed dark mode
- ✅ **Error Handling** with comprehensive try-catch blocks
- ✅ **Data Validation** and preprocessing for clean visualizations

### 📈 **Dashboard Components**

#### 🎛️ **Filter Panel**
- **Content Type**: Movies vs TV Shows
- **Country**: Geographic content distribution
- **Release Year**: Temporal content filtering
- **Content Rating**: Age-appropriate content selection  
- **Title Search**: Fuzzy text search across all titles

#### 📊 **Visualization Suite**
1. **📈 Key Metrics Cards**: Total titles, movies, TV shows, and countries
2. **🍩 Content Type Distribution**: Interactive donut chart
3. **📅 Release Year Trends**: Time-series line chart showing content release patterns
4. **🎭 Top Genres**: Horizontal bar chart of most popular genres
5. **⭐ Rating Distribution**: Content rating breakdown by type
6. **🌍 Geographic Distribution**: Top countries by content volume
7. **📊 Content Categories**: Family-friendly vs intense content classification
8. **🔥 Content Addition Trends**: Monthly addition patterns over years
9. **📋 Interactive Data Table**: Sortable and filterable content preview

#### 💾 **SQL Interface**
- **Custom Query Executor**: Run SELECT queries directly from the dashboard
- **Real-time Results**: Instant table display of query results
- **Error Handling**: Comprehensive error messages for debugging

---

## 📚 **Dataset Information**

### 📄 **Source Dataset**
- **File**: `netflix_titles.csv`
- **Source**: Netflix content metadata (updated through 2021)
- **Size**: ~8,000+ titles across movies and TV shows
- **Format**: CSV with 12 primary columns

### 🗂️ **Data Schema**
```sql
CREATE TABLE netflix (
    show_id VARCHAR(10) PRIMARY KEY,
    type VARCHAR(10),
    title VARCHAR(255),
    director TEXT,
    cast TEXT,
    country VARCHAR(255),
    date_added DATE,
    release_year INT,
    rating VARCHAR(10),
    duration VARCHAR(15),
    listed_in TEXT,
    description TEXT
);
```

### 📊 **Key Data Fields**
| Column | Description | Example |
|--------|-------------|---------|
| `show_id` | Unique identifier | s1, s2, s3 |
| `type` | Content type | Movie, TV Show |
| `title` | Content title | "Stranger Things" |
| `director` | Director name(s) | "Christopher Nolan" |
| `cast` | Main cast members | "Leonardo DiCaprio, Marion Cotillard" |
| `country` | Production country | "United States" |
| `date_added` | Netflix addition date | "2021-01-01" |
| `release_year` | Original release year | 2020 |
| `rating` | Content rating | PG-13, TV-MA |
| `duration` | Runtime/seasons | "148 min", "3 Seasons" |
| `listed_in` | Genres | "Action, Thriller" |
| `description` | Plot summary | "A mind-bending thriller..." |

---

## 📁 **Project Structure**

```
netflix-analytics-dashboard/
├── 📁 app/
│   └── 📄 streamlit_dashboard.py      # Main dashboard application
├── 📁 data/
│   └── 📄 netflix_titles.csv         # Netflix dataset
├── 📁 database/
│   └── 📄 schemas.sql               # Database schema and setup
├── 📁 assets/
│   └── 📄 screenshots/              # Dashboard screenshots
├── 📄 .env                          # Environment variables (create this)
├── 📄 .env.example                  # Example environment file
├── 📄 requirements.txt              # Python dependencies
├── 📄 README.md                     # This file
└── 📄 setup.py                      # Package setup configuration
```

---

## 🚀 **Installation & Setup**

### 📋 **Prerequisites**
- Python 3.8 or higher
- MySQL 8.0 or higher
- pip (Python package manager)
- Git (for cloning the repository)

### 🔧 **Step 1: Clone the Repository**
```bash
git clone https://github.com/yourusername/netflix-analytics-dashboard.git
cd netflix-analytics-dashboard
```

### 🐍 **Step 2: Create Virtual Environment**
```bash
# Create virtual environment
python -m venv netflix_env

# Activate virtual environment
# On Windows:
netflix_env\Scripts\activate
# On macOS/Linux:
source netflix_env/bin/activate
```

### 📦 **Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

### 🗄️ **Step 4: Database Setup**

#### 4.1 Create MySQL Database
```sql
CREATE DATABASE netflix_db;
USE netflix_db;
```

#### 4.2 Create Table Schema
```sql
-- Run the contents of database/schemas.sql
SOURCE database/schemas.sql;
```

#### 4.3 Import Data
```bash
# Method 1: MySQL Command Line
mysql -u root -p netflix_db < data/netflix_titles.csv

# Method 2: MySQL Workbench
# Import wizard: Table Data Import Wizard
# Select netflix_titles.csv and map to netflix table
```

### 🔐 **Step 5: Environment Configuration**
Create a `.env` file in the project root:
```bash
# Database Configuration
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=your_username
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=netflix_db

# Optional: Application Configuration
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_HEADLESS=true
```

### ▶️ **Step 6: Run the Application**
```bash
streamlit run app/streamlit_dashboard.py
```

The dashboard will be available at `http://localhost:8501`

---

## 🖥️ **Usage Guide**

### 🎯 **Getting Started**
1. **Launch the Dashboard**: Open your browser to `http://localhost:8501`
2. **Explore Filters**: Use the sidebar to filter content by type, country, year, and rating
3. **Analyze Visualizations**: Interact with charts by hovering, clicking, and zooming
4. **Search Content**: Use the search bar to find specific titles
5. **Run Custom Queries**: Use the SQL interface for advanced data exploration

### 📊 **Dashboard Navigation**

#### 🔍 **Filter Panel (Sidebar)**
- **Content Type Filter**: Switch between Movies, TV Shows, or All content
- **Geographic Filter**: Select specific countries or regions
- **Temporal Filter**: Choose release years or year ranges
- **Rating Filter**: Filter by content ratings (G, PG, PG-13, R, etc.)
- **Text Search**: Search by title, director, or cast

#### 📈 **Main Dashboard**
- **Metrics Overview**: High-level statistics at the top
- **Content Distribution**: Visual breakdown of content types
- **Trend Analysis**: Time-series charts showing content patterns
- **Genre Analysis**: Popular genres and their distribution
- **Geographic Insights**: Content distribution by country
- **Content Quality**: Family-friendly vs mature content analysis

#### 💻 **SQL Interface**
- **Query Editor**: Text area for writing custom SQL queries
- **Execute Button**: Run queries against the Netflix database
- **Results Display**: Interactive table showing query results
- **Error Handling**: Clear error messages for debugging

### 🔥 **Advanced Features**

#### 📊 **Interactive Charts**
- **Zoom & Pan**: Navigate through large datasets
- **Hover Details**: Get detailed information on data points
- **Legend Interaction**: Click legend items to show/hide data series
- **Export Options**: Save charts as PNG or PDF (via browser)

#### 🎛️ **Advanced Filtering**
- **Multi-Select**: Combine multiple filter criteria
- **Real-time Updates**: Visualizations update instantly with filter changes
- **Filter Memory**: Dashboard remembers your filter preferences
- **Reset Options**: Clear all filters with a single click

---

## 🛠️ **Technical Implementation**

### 🏗️ **Architecture Overview**
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Streamlit     │    │   SQLAlchemy    │    │   MySQL         │
│   Frontend      │◄──►│   ORM Layer     │◄──►│   Database      │
│                 │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Plotly        │    │   Pandas        │    │   netflix       │
│   Visualization │    │   Data Proc.    │    │   Table         │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### 🔧 **Technology Stack**

#### 🖥️ **Frontend**
- **Streamlit**: Web application framework
- **Custom CSS**: Netflix-themed styling
- **Responsive Design**: Mobile-friendly interface

#### 📊 **Visualization**
- **Plotly**: Interactive charts and graphs
- **Matplotlib**: Statistical visualizations
- **Seaborn**: Advanced statistical plotting

#### 🗄️ **Backend**
- **SQLAlchemy**: Python SQL toolkit and ORM
- **MySQL Connector**: Database connectivity
- **Pandas**: Data manipulation and analysis

#### 🔐 **Security**
- **python-dotenv**: Environment variable management
- **SQL Injection Prevention**: Parameterized queries
- **Input Validation**: Data sanitization

### 📊 **Performance Optimizations**
- **Connection Pooling**: Efficient database connections
- **Data Caching**: Reduced database queries
- **Lazy Loading**: On-demand data loading
- **Optimized Queries**: Efficient SQL query structure

---

## 📱 **Screenshots**

### 🏠 **Main Dashboard**
![Main Dashboard](assets/screenshots/main_dashboard.png)

### 🔍 **Filter Panel**
![Filter Panel](assets/screenshots/filter_panel.png)

### 📊 **Visualizations**
![Visualizations](assets/screenshots/visualizations.png)

### 💻 **SQL Interface**
![SQL Interface](assets/screenshots/sql_interface.png)

---

## 🌐 **Deployment Options**

### ☁️ **Cloud Deployment**

#### 🚀 **Streamlit Cloud**
1. Push code to GitHub repository
2. Connect to Streamlit Cloud
3. Configure environment variables in Streamlit secrets
4. Deploy with automatic builds

#### 🐳 **Docker Deployment**
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8501

CMD ["streamlit", "run", "app/streamlit_dashboard.py"]
```

#### ☁️ **AWS/GCP/Azure**
- **EC2/Compute Engine**: Virtual machine deployment
- **ECS/Cloud Run**: Container-based deployment
- **RDS/Cloud SQL**: Managed database services

### 🏠 **Local Development**
```bash
# Development mode with auto-reload
streamlit run app/streamlit_dashboard.py --server.runOnSave=true

# Custom port
streamlit run app/streamlit_dashboard.py --server.port=8502
```

---

## 🧪 **Testing**

### 🔍 **Unit Tests**
```bash
# Run unit tests
python -m pytest tests/

# Run with coverage
python -m pytest tests/ --cov=app/
```

### 🧪 **Integration Tests**
```bash
# Test database connection
python tests/test_database.py

# Test data processing
python tests/test_data_processing.py
```

### 🌐 **UI Testing**
```bash
# Selenium tests for UI components
python tests/test_ui.py
```

---

## 🔧 **Troubleshooting**

### 🚨 **Common Issues**

#### 🔐 **Database Connection Issues**
```bash
# Check MySQL service status
sudo systemctl status mysql

# Test connection
mysql -u root -p -h localhost

# Verify credentials in .env file
```

#### 📦 **Package Installation Issues**
```bash
# Upgrade pip
pip install --upgrade pip

# Install specific versions
pip install streamlit==1.25.0

# Clear cache
pip cache purge
```

#### 🖥️ **Streamlit Issues**
```bash
# Clear Streamlit cache
streamlit cache clear

# Reset configuration
streamlit config show
```

### 🐛 **Debug Mode**
```bash
# Enable debug logging
export STREAMLIT_LOGGER_LEVEL=debug
streamlit run app/streamlit_dashboard.py
```

---

## 🚀 **Future Enhancements**

### 🔮 **Planned Features**
- [ ] **🤖 AI-Powered Recommendations**: ML-based content suggestions
- [ ] **📱 Mobile App**: React Native companion app
- [ ] **🔔 Real-time Notifications**: Content updates and alerts
- [ ] **👥 User Authentication**: Multi-user dashboard access
- [ ] **📊 Advanced Analytics**: Predictive analytics and forecasting
- [ ] **🎨 Custom Themes**: User-selectable color schemes
- [ ] **📤 Export Features**: PDF reports and data exports
- [ ] **🔗 API Integration**: RESTful API for external access

### 🛠️ **Technical Improvements**
- [ ] **⚡ Performance Optimization**: Faster load times
- [ ] **🔄 Real-time Updates**: Live data synchronization
- [ ] **🧪 A/B Testing**: Feature experimentation framework
- [ ] **📈 Monitoring**: Application performance monitoring
- [ ] **🔐 Enhanced Security**: OAuth2 authentication
- [ ] **🌍 Internationalization**: Multi-language support

---

## 🤝 **Contributing**

### 🛠️ **Development Setup**
```bash
# Fork the repository
git clone https://github.com/yourusername/netflix-analytics-dashboard.git

# Create feature branch
git checkout -b feature/your-feature-name

# Install development dependencies
pip install -r requirements-dev.txt

# Run pre-commit hooks
pre-commit install
```

### 📝 **Contribution Guidelines**
1. **🔍 Code Review**: All PRs require review
2. **✅ Testing**: Maintain test coverage above 80%
3. **📖 Documentation**: Update docs for new features
4. **🎨 Style**: Follow PEP 8 style guidelines
5. **🔒 Security**: Security-first development approach

### 🐛 **Bug Reports**
Please use the GitHub issue tracker for bug reports:
- **📋 Template**: Use the provided issue template
- **🔍 Details**: Include steps to reproduce
- **📊 Environment**: Specify OS, Python version, etc.
- **📸 Screenshots**: Include relevant screenshots

---

## 📜 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Netflix Analytics Dashboard

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🙏 **Acknowledgments**

### 📊 **Data Sources**
- **Netflix**: Original content metadata
- **Kaggle**: Dataset hosting and community
- **TMDb**: Additional movie information

### 🛠️ **Libraries & Tools**
- **Streamlit Team**: Amazing web framework
- **Plotly**: Interactive visualization library
- **Pandas**: Data manipulation powerhouse
- **SQLAlchemy**: Excellent ORM solution

### 🌟 **Inspiration**
- **Netflix**: UI/UX design inspiration
- **Modern Dashboard Design**: Contemporary web aesthetics
- **Data Visualization Best Practices**: Edward Tufte principles

---

## 📞 **Contact & Support**

### 👤 **Author**
- **Name**: Your Name
- **Email**: your.email@example.com
- **GitHub**: [@yourusername](https://github.com/yourusername)
- **LinkedIn**: [Your LinkedIn Profile](https://linkedin.com/in/yourprofile)

### 💬 **Support Channels**
- **🐛 Bug Reports**: [GitHub Issues](https://github.com/yourusername/netflix-analytics-dashboard/issues)
- **💡 Feature Requests**: [GitHub Discussions](https://github.com/yourusername/netflix-analytics-dashboard/discussions)
- **❓ Questions**: [Stack Overflow](https://stackoverflow.com/questions/tagged/netflix-dashboard)
- **📧 Email**: support@netflixdashboard.com

### 🌟 **Show Your Support**
If you found this project helpful, please consider:
- ⭐ **Starring** the repository
- 🍴 **Forking** for your own modifications
- 📢 **Sharing** with your network
- 🐛 **Reporting** issues and bugs
- 💡 **Suggesting** new features

---

<div align="center">
  <h3>🎬 Built with ❤️ for data enthusiasts and Netflix fans</h3>
  <p>© 2024 Netflix Analytics Dashboard. All rights reserved.</p>
</div>

---

*Last updated: July 2024*"# netflix-analytics-dashboard" 
