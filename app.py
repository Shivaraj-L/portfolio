import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import json
from PIL import Image, ImageDraw

# Set page configuration
st.set_page_config(page_title="Data Engineer Portfolio", page_icon=":bar_chart:", layout="wide")

# Function to load and make the profile picture round
def load_round_profile_pic(filepath: str):
    # Open the image and ensure it has an alpha channel for transparency
    img = Image.open(filepath).convert("RGBA")
    width, height = img.size

    # Create a circular mask
    mask = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, width, height), fill=255)

    # Apply the mask to the image
    img.putalpha(mask)

    return img
# Load assets
profile_pic = load_round_profile_pic("logo.jpg")# Load a Lottie animation for header if you want
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_coding = load_lottiefile("coding.json")  # You can download a lottie file or use URL

# --- Styling ---
def inject_custom_css():
    st.markdown("""
    <style>
    /* Customizing text colors */
    h1, h2, h3 {
        color: #0E5EC5;
    }
    p, li {
        color: #5A5A5A;
    }
    /* Button styles */
    div.stButton > button {
        background-color: #0E5EC5;
        color: white;
        border-radius: 10px;
    }
    /* Form styling */
    input, textarea {
        border-radius: 8px;
        padding: 8px;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

inject_custom_css()

# --- HEADER SECTION ---
with st.container():
    col1, col2 = st.columns((2, 3))
    with col1:
        st.image(profile_pic, width=200)
    with col2:
        st.title("Shivaraj L")
        st.subheader("Data Engineer | RPA Developer | Big Data Enthusiast ")
        st.write("🚀 I design and build robust, scalable, and secure data infrastructures that empower businesses to unlock the power of their data.")
        st.lottie(lottie_coding, height=200, key="coding")

# --- TABS SECTION ---
tabs = st.tabs(["About", "Skills", "Projects", "Contact"])

# --- ABOUT ---
with tabs[0]:
    st.header("About Me 🧑‍💻")
    st.write("""
    I am a passionate **Data Engineer** with over **X+ years** of experience in building scalable data solutions. 
    Skilled in **data modeling**, **ETL development**, and **cloud platforms** like AWS, Azure, and GCP.

    I focus on delivering **high-performance**, **cost-optimized**, and **maintainable** data systems that power real-time analytics and machine learning solutions.
    """)

# --- SKILLS ---
with tabs[1]:
    st.header("Skills 🛠️")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Programming Languages")
        st.write("""
        - Python (Pandas, PySpark)
        - SQL (T-SQL, PL/SQL)
        - Java Basics
        """)
    with col2:
        st.subheader("Big Data & ETL Tools")
        st.write("""
        - Apache Spark, Kafka
        - Airflow, dbt
        - Hadoop, Flink
        """)
    with col3:
        st.subheader("Cloud & DevOps")
        st.write("""
        - AWS (Glue, Redshift, S3)
        - Azure Data Factory
        - Docker, Terraform
        """)

# --- PROJECTS ---
with tabs[2]:
    st.header("Projects 🚀")

    # First Row (3 projects side-by-side)
    with st.container():
        project_col1, project_col2, project_col3 = st.columns(3)

        with project_col1:
            st.subheader("Real-Time Analytics Platform")
            st.write("**Tech Stack**: Kafka, Spark Streaming, AWS Redshift")
            st.write("""
            - Built a real-time pipeline processing over 10M events/day.
            - Enabled live dashboards for business KPIs.
            """)
            st.markdown("[GitHub Repository](https://github.com/yourusername/project1)")

        with project_col2:
            st.subheader("Automated Data Warehouse")
            st.write("**Tech Stack**: dbt, Snowflake, Airflow")
            st.write("""
            - Designed a modular and automated data warehouse with version control.
            - Reduced manual data processing time by 60%.
            """)
            st.markdown("[GitHub Repository](https://github.com/yourusername/project2)")

        with project_col3:
            st.subheader("Streaming Data Ingestion")
            st.write("**Tech Stack**: AWS Kinesis, Lambda, DynamoDB")
            st.write("""
            - Designed an event-driven serverless architecture.
            - Reduced system latency by 45%.
            """)
            st.markdown("[GitHub Repository](https://github.com/yourusername/project3)")

    st.write("")  # Add some space

    # Second Row (New project below)
    with st.expander("See more projects"):
        with st.container():
            project_col4, empty_col1, empty_col2 = st.columns([1, 0.5, 0.5])

            with project_col4:
                st.subheader("Data Lakehouse Architecture")
                st.write("**Tech Stack**: Delta Lake, Azure Data Lake, Databricks")
                st.write("""
                - Architected a scalable Lakehouse solution combining structured and unstructured data.
                - Improved data access efficiency by 30%.
                """)
                st.markdown("[GitHub Repository](https://github.com/yourusername/project4)")
            with st.container():
                project_col5, empty_col1, empty_col2 = st.columns([1, 0.5, 0.5])

                with project_col5:
                    st.subheader("Data Lakehouse Architecture")
                    st.write("**Tech Stack**: Delta Lake, Azure Data Lake, Databricks")
                    st.write("""
                    - Architected a scalable Lakehouse solution combining structured and unstructured data.
                    - Improved data access efficiency by 30%.
                    """)
                    st.markdown("[GitHub Repository](https://github.com/yourusername/project4)")


# --- CERTIFICATIONS AND CONTACT ---
with tabs[3]:
    # st.header("Certifications 📜")
    # st.write("""
    # - Google Professional Data Engineer
    # - AWS Certified Data Analytics – Specialty
    # - Azure Data Engineer Associate
    # """)

    st.header("Contact Me 📫")
    contact_form = """
    <form action="https://formsubmit.co/shivaraja261@gmail.com" method="POST">
         <input type="text" name="name" placeholder="Your Name" required><br><br>
         <input type="email" name="email" placeholder="Your Email" required><br><br>
         <textarea name="message" placeholder="Your Message Here" required></textarea><br><br>
         <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
    st.markdown("Or connect with me on [LinkedIn](https://www.linkedin.com/in/yourlinkedin/)", unsafe_allow_html=True)

# --- FOOTER ---
st.write("---")
st.write("Made with ❤️ using Streamlit | © 2025 Shivaraj")
