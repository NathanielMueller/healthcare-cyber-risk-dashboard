# 🏥 Healthcare Cyber Risk Intelligence Dashboard
**Author:** Nathaniel Mueller  
📍 *Built with Python, Pandas, Plotly, Streamlit, and Jupyter Notebook*

---

## 📘 Overview
The **Healthcare Cyber Risk Intelligence Dashboard** is a data-driven web application designed to analyze and visualize healthcare data breaches reported to the **U.S. Department of Health & Human Services (HHS) Office for Civil Rights (OCR)**.  

This project combines **cybersecurity intelligence**, **data analytics**, and **interactive visualization** to uncover patterns, trends, and vulnerabilities across the U.S. healthcare system.  
It was built to simulate a real-world intelligence dashboard—offering actionable insights into where, how, and why healthcare data breaches occur.

---

## 💡 Key Features
- **Interactive Filtering:** Filter by *Year*, *Breach Type*, and *State* to isolate specific patterns.  
- **Executive-Level Insights:** Automated summary highlighting top breach category and severity trends.  
- **Trend Analysis:** Visualizes breach growth and changes over time with dynamic line charts.  
- **Geographic Mapping:** Choropleth map visualizing the spread of incidents across the U.S.  
- **Top Entities View:** Identifies healthcare organizations with the most reported breaches.  
- **Custom Theme Design:** Professional dark–blue UI inspired by Homeland Security and HHS branding.  

---

## 🧠 Analytical Workflow
1. **Data Acquisition:**  
   - Raw dataset obtained from the **HHS OCR Breach Portal** (public data on U.S. healthcare breaches).  

2. **Data Cleaning & Transformation:**  
   - Conducted in **Jupyter Notebook** using **Pandas** and **NumPy**.  
   - Removed duplicates, standardized column names, and derived new metrics (e.g., breach counts, YOY trends).  

3. **Exploratory Analysis:**  
   - Analyzed distributions and correlations using **Matplotlib** and **Seaborn**.  .  

4. **Dashboard Development:**  
   - Built with **Streamlit** and **Plotly Express** for interactivity.  
   - Added sidebar filters, tabs, and tooltips to guide exploration.  

5. **UI/UX & Theming:**  
   - Customized **HTML/CSS** styling for a modern, data-security aesthetic.  
   - Rounded cards, shadowed graphs, and clean spacing to enhance readability.  

6. **Deployment:**  
   - Tested locally using **VS Code**.  
   - Deployable via **Streamlit Cloud** or **GitHub Pages (static screenshots)**.  

---

## 🧰 Tools, Libraries & Technologies Used
| Category | Tools & Libraries |
|-----------|------------------|
| **Programming Language** | Python 3 |
| **Data Handling** | Pandas · NumPy |
| **Visualization** | Plotly Express · Matplotlib · Seaborn |
| **Web Framework** | Streamlit |
| **Development Environment** | Jupyter Notebook · VS Code |
| **Frontend Customization** | HTML · CSS |
| **Version Control** | Git · GitHub |
| **Data Source** | [HHS OCR Breach Portal](https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf) |

---

## 🎨 Design Focus
**Theme:** Custom Homeland Security–inspired design with a modern, data-centric interface.  
**Focus Areas:**  
- Data Analytics  
- Cyber Threat Intelligence  
- Interactive Visualization  
- Human-Centered Design  

---

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/NathanielMueller/healthcare-cyber-risk-dashboard.git
2. Navigate into the folder:
    cd healthcare-cyber-risk-dashboard
3. Install dependencies:
    pip install -r requirements.txt
4. Run the dashboard:
    streamlit run app.py

--

## 📊 Data Source
U.S. Department of Health & Human Services – Office for Civil Rights (OCR) Breach Portal
https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf

--

## 📊 Screenshots
screenshots/breach_trends.png
screenshots/dashboard_overview.png
screenshots/entities.png
screenshots/map_view.png

## 👤 Author
Nathaniel Mueller
🎓 M.S. Information Systems (Business Analytics) — California State University, Fullerton
🔗 LinkedIn https://www.linkedin.com/in/nathaniel-mueller/