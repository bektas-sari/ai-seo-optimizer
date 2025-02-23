
# AI SEO Optimizer

An AI-powered SEO analysis tool that helps optimize blog content using Google Trends data and advanced text analysis.

## Features

- Real-time SEO analysis of blog content
- Keyword density analysis and optimization suggestions
- Integration with Google Trends API for keyword popularity insights
- Word count analysis and recommendations
- Title length optimization
- Automated SEO recommendations based on content analysis

## Technologies Used

- Python 3.x
- Flask
- PyTrends
- Bootstrap 5
- HTML/CSS
- JavaScript

## Installation

1. Clone the repository
```bash
git clone https://github.com/bektas-sari/ai-seo-optimizer.git
cd ai-seo-optimizer
```

2. Create and activate a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install required packages
```bash
pip install -r requirements.txt
```

4. Set up environment variables
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
```

5. Run the application
```bash
flask run
```

The application will be available at `http://localhost:5000`

## Usage

1. Navigate to the homepage
2. Enter your blog content in the text area
3. Click "Analyze SEO"
4. Review the detailed analysis including:
   - Word count
   - Key terms
   - Google Trends analysis
   - SEO recommendations

## Project Structure

```
ai-seo-optimizer/
├── app.py              # Main Flask application
├── forms.py            # Form definitions
├── templates/          # HTML templates
│   ├── index.html     # Homepage template
│   └── result.html    # Results page template
├── static/            # Static files (CSS, JS)
├── requirements.txt   # Project dependencies
└── README.md         # Project documentation
```

## Error Handling

The application includes robust error handling for:
- Google Trends API rate limiting
- Network connection issues
- Invalid input validation
- API timeout management

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Contact

Bektas Sari - [LinkedIn](www.linkedin.com/in/bektas-sari) - bektas.sari@gmail.com

## License

This project is licensed under the MIT License - see the LICENSE file for details.
