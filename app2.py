import streamlit as st
from PIL import Image

st.set_option('deprecation.showPyplotGlobalUse', False)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

def resize_image(image, size):
    # Resize the image while maintaining the aspect ratio
        image.thumbnail(size)
        return image

# Home page
def home():
    st.title("Welcome to My Personal Profile")
    
    col1, col2 = st.columns([2, 3])
    
    with col1:
        st.image("images/profile_picture.jpg", caption="Olasunkanmi Felix Oyadokun", width=200)
    
    with col2:
        st.markdown("<p style='text-align: justify; font-family: Arial, sans-serif;'><strong>Introduction:</strong></p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: justify; font-family: Arial, sans-serif;'>Welcome to my personal profile. I'm passionate about leveraging technology to solve problems and create innovative solutions.</p>", unsafe_allow_html=True)

        st.markdown("<p style='text-align: justify; font-family: Arial, sans-serif;'><strong>Professional Statement:</strong></p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: justify; font-family: Arial, sans-serif;'>I'm a data scientist, software engineer and researcher with expertise in data science, data analytics, web development, machine learning and research. I enjoy building scalable applications and exploring the latest technologies.</p>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<p style='text-align: justify; font-family: Arial, sans-serif;'><strong>Featured Projects:</strong></p>", unsafe_allow_html=True)

    # Projects section
    #st.header("Projects")
    projects = [
    {
        'name': 'Rainfall Analysis',
        'image': 'images/rain.jpg',
        'link': 'https://github.com/Olasunkii/wine-clasification'
    },
    {
        'name': 'Movie Recommender',
        'image': 'images/movies.jpg',
        'link': 'https://github.com/Olasunkii/wine-clasification'
    },
    {
        'name': 'Sentiment Analysis',
        'image': 'images/twiter.jpg',
        'link': 'https://github.com/Alaine911/TeamNM2/blob/master/Advanced_Classification_TeamNM2%20attempt%20(1).ipynb'
    },
    {
        'name': 'Wine Classification',
        'image': 'images/wine.jpg',
        'link': 'https://github.com/Olasunkii/wine-clasification'
    },
    {
        'name': 'Heart Disease',
        'image': 'images/heart.jpg',
        'link': 'https://github.com/Olasunkii/heart-disease'
    },
    {
        'name': 'Bulldozer Pred',
        'image': 'images/buldozer.jpg',
        'link': 'https://github.com/Olasunkii/Bulldozer_Price_Predition'
    },
    {
        'name': 'Language Id',
        'image': 'images/language.jpg',
        'link': 'https://github.com/Olasunkii/language_identification/blob/main/Language_Classification.ipynb'
    },
    # Add more projects here
]

    project_columns = st.columns(4)
    for i, project in enumerate(projects):
        with project_columns[i % 4]:
            image = Image.open(project['image'])
            resized_image = resize_image(image, (200, 200))
            st.image(resized_image, use_column_width=True)
            
            # Adjust the markdown style
            markdown_text = f"<p style='text-align:center; font-size:13px; color:#454545;'><a href='{project['link']}' target='_blank'>{project['name']}</a></p>"
            st.markdown(markdown_text, unsafe_allow_html=True)


    research = [
        
        {
            'name': 'AES for file security',
            'image': 'images/file_security.jpg',
            'link': 'https://www.irejournals.com/formatedpaper/17038321.pdf'
        },
        {
            'name': 'Building blocks of CNN',
            'image': 'images/cnn.jpg',
            'link': 'https://www.irejournals.com/formatedpaper/1703854.pdf'
        },
        {
            'name': 'Secured communication using MAES',
            'image': 'images/comm.jpg',
            'link': 'https://github.com/Olasunkii/Bulldozer_Price_Predition'
        },
        {
            'name': 'Curbing wastage of electricity',
            'image': 'images/electric.jpg',
            'link': 'https://www.academia.edu/41771948/CURBING_THE_WASTE_OF_ELECTRICAL_ENERGY_IN_NIGERIA-A_CASE_STUDY_OF_FEDERAL_UNIVERSITY_OF_TECHNOLOGY_MINNA?auto=download'
        },
        # Add more projects here
    ]
    st.markdown("---")
    st.markdown("<p style='text-align: justify; font-family: Arial, sans-serif;'><strong>Research Works:</strong></p>", unsafe_allow_html=True)

    project_columns = st.columns(4)
    for i, project in enumerate(research):
        with project_columns[i % 4]:
            image = Image.open(project['image'])
            resized_image = resize_image(image, (200, 200))
            st.image(resized_image, use_column_width=True)
            # Adjust the markdown style
            markdown_text = f"<p style='text-align:center; font-size:13px; color:#454545;'><a href='{project['link']}' target='_blank'>{project['name']}</a></p>"
            st.markdown(markdown_text, unsafe_allow_html=True)
    
    st.markdown("---")

    
    col3, col4 = st.columns(2)
    with col3:
        st.write("Skills:")
        st.markdown(
            "- Python\n"
            "- Machine Learning\n"
            "- Statistical Analysis"
            "- Web Development\n"
            "- HTML/CSS\n"
              "- JavaScript\n"
            
        )

    with col4:
        st.write("Testimonials:")
        st.write("Kolawole Ridwan, Team Lead (Team 11) Explore AI Academy")
        st.markdown(
            "> \"Olasunkanmi's technical skills and dedication to delivering high-quality code were impressive. He consistently exceeded our expectations.\""
        )



def about():
    st.title("About Me")
    st.markdown("<h2 style='font-size: 16px; font-weight: bold;'>Work Experience</h2>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='font-size: 16px; font-weight: bold;'>Data Science Internship</h3>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 14px;'>Explore AI, July 2022 - Present</p>", unsafe_allow_html=True)
    st.markdown("<ul style='font-size: 14px;'>"
            "<li>Contributed 70% to successful completion of Thames rainfall project</li>"
            "<li>Completed projects on sentiment analysis and recommendation systems</li>"
            "<li>Learnt geospatial analysis to give my team edge over other competitors</li>"
            "</ul>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='font-size: 16px; font-weight: bold;'>Data Analysis Intern</h3>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 14px;'>Natview Foundation for Technology, July 2022 - February 2023</p>", unsafe_allow_html=True)
    st.markdown("<ul style='font-size: 14px;'>"
            "<li>Contributed 60% to successful completion of group project.</li>"
            "<li>Selected as best group in EDA with python and selected as presenter in the group.</li>"
            "<li>Selected among the 5 best presenter in bicycle analysis project</li>"
            "<li>Involvement in successful completion of various projects</li>"
            "</ul>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='font-size: 16px; font-weight: bold;'>Lecturer</h3>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 14px;'>NISMS, September 2016 - May 2023</p>", unsafe_allow_html=True)
    st.markdown("<ul style='font-size: 14px;'>"
                "<li>Improved the accuracy and speed of computing student results by over 50%</li>"
                "<li>Graduated over 100 National Diploma students</li>"
                "<li>Supervised 36 student projects</li>"
                "</ul>", unsafe_allow_html=True) 
       
    st.markdown("---")

    st.markdown("<h2 style='font-size: 16px; font-weight: bold;'>Education</h2>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='font-size: 16px; font-weight: bold;'>Master of Engineering in Electronics and Communications Engineering</h3>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 14px;'>Nigerian Defence Academy, October 2017 - September 2021</p>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='font-size: 16px; font-weight: bold;'>Bachelor of Engineering in Electrical and Computer Engineering</h3>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 14px;'>Federal University of Technology, Minna, January 2009 - April 2014</p>", unsafe_allow_html=True)
    
    st.markdown("---")

    st.markdown("<h2 style='font-size: 16px; font-weight: bold;'>Membership & Licenses</h2>", unsafe_allow_html=True)
    
    st.markdown("<ul style='font-size: 14px;'>"
                "<li>Member, International Association of Engineers</li>"
                "<li>Member, International Society for Data Science and Analytics</li>"
                "<li>Chartered Project Management Professional, The Chartered</li>"
                "</ul>", unsafe_allow_html=True)
    
    st.markdown("---")

    st.markdown("<h2 style='font-size: 16px; font-weight: bold;'>Courses/Certificates</h2>", unsafe_allow_html=True)
    
    st.markdown("<ul style='font-size: 14px;'>"
                "<li>Data Science Fellow, Natview Foundation for Technology</li>"
                "<li>AWS Machine Learning Foundation, Udacity</li>"
                "<li>Python for Data Science, IBM</li>"
                "<li>Data Analysis With Python, IBM</li>"
                "<li>Data Visualization With Python, IBM</li>"
                "<li>Data Privacy Fundamental, IBM</li>"
                "<li>Soft Skills Training, Jobberman</li>"
                "</ul>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("<h2 style='font-size: 16px; font-weight: bold;'>Skills</h2>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='font-size: 16px; font-weight: bold;'>IT Skills</h3>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 14px;'>Statistical Analysis, Machine Learning, Data Visualization, Python, Data Wrangling, Problem-solving, Geospatial analysis</p>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='font-size: 16px; font-weight: bold;'>Soft Skills</h3>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 14px;'>Abstract, Communication, Critical Thinking, Collaboration, Adaptability, Curiosity</p>", unsafe_allow_html=True)
    

    st.markdown("---")

    st.markdown("<h2 style='font-size: 16px; font-weight: bold;'>Conference, Seminars, and Presentations</h2>", unsafe_allow_html=True)
    
    st.markdown("<ul style='font-size: 14px;'>"
                "<li>Demystifying the Rainfall Data Problems, Explore AI Academy, 2023</li>"
                "<li>Movies Recommender System, Explore AI Academy, 2022</li>"
                "<li>Spain Rainfall Electricity, Explore AI Academy, 2022</li>"
                "<li>Analyzing Health Care Financing, Amina J.M. Lab, 2022</li>"
                "<li>Analyzing Financial Data for Fraud Detection, Amina J.M Lab, 2022</li>"
                "<li>Kaduna State Health Integrated Supervision Support System, Amina J.M. Lab, 2022</li>"
                "<li>Analyzing Employees Life’s Quality, Amina J.M Lab, 2022</li>"
                "</ul>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("<h2 style='font-size: 16px; font-weight: bold;'>Volunteering</h2>", unsafe_allow_html=True)
    
    st.markdown("<ul style='font-size: 14px;'>"
                "<li>Data Collector for out-of-school survey, Kaduna State Government, 2022</li>"
                "<li>Bio data capturing and collection for disabled adults and children below 6 years, Kaduna State Government, 2022</li>"
                "<li>ICT Officer, Living Faith Foundation, 2016</li>"
                "</ul>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("<h2 style='font-size: 16px; font-weight: bold;'>Hobbies and Interests</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 14px;'>Data science programming, playing adventure and mission games, watching Discovery Channel</p>", unsafe_allow_html=True)



import base64

def download():
    cv_file_path = "docs/cv.pdf"  # Replace with the actual file path of your CV
    
    with open(cv_file_path, "rb") as file:
        cv_data = file.read()
        cv_base64 = base64.b64encode(cv_data).decode("utf-8")
        cv_size = len(cv_data)
    
    st.title("Download my CV")
    st.markdown(f"<p style='font-size: 16px;'>Click the button below to download my CV.</p>", unsafe_allow_html=True)
    
    # Create a download link for the CV
    href = f"<a href='data:application/pdf;base64,{cv_base64}' download='cv.pdf'>Download CV ({cv_size} bytes)</a>"
    st.markdown(href, unsafe_allow_html=True)

# Main app

# Contact page
def contact():
    st.title("Contact Me")
    
    st.markdown("<h3 style='font-size: 20px; font-weight: bold;'>Email</h3>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 16px;'>olasunkanmifelix@yahoo.com</p>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='font-size: 20px; font-weight: bold;'>Mobile</h3>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 16px;'>+2347066722345</p>", unsafe_allow_html=True)

# Sidebar navigation
pages = {
    "Home": home,
    "About": about,
    "Download": download,
    "Contact": contact
}

# Set up sidebar
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Run selected page
pages[selection]()
