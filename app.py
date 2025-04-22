import streamlit as st
from PIL import Image, ImageDraw
from streamlit_lottie import st_lottie
import json

# Set page configuration
st.set_page_config(
    page_title="Shivaraj L - Data Engineer Portfolio",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Function to load and make the profile picture round
def load_round_profile_pic(filepath: str):
    img = Image.open(filepath).convert("RGBA")
    width, height = img.size
    mask = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, width, height), fill=255)
    img.putalpha(mask)
    return img

# Load assets
profile_pic = load_round_profile_pic("logo.jpg")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_coding = load_lottiefile("coding.json")

# --- Styling that works for both light and dark themes ---
def inject_custom_css():
    st.markdown("""
    <style>
    /* Main container padding */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Headers with gradient text */
    h1, h2, h3 {
        background: -webkit-linear-gradient(#0E5EC5, #00C4FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.75rem;
    }
    
    /* Text that adapts to theme */
    p, li {
        color: var(--text-color);
    }
    
    /* Cards for projects */
    .project-card {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background-color: var(--background-secondary);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
        transition: transform 0.2s;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
    }
    
    /* Buttons */
    .stButton>button {
        border: none;
        background: linear-gradient(135deg, #0E5EC5, #00C4FF);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 0.5rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    /* Form styling */
    .stTextInput>div>div>input, 
    .stTextArea>div>div>textarea {
        background-color: var(--background-secondary);
        color: var(--text-color);
        border: 1px solid var(--border-color);
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        padding: 0.5rem 1rem;
        border-radius: 0.5rem;
        background-color: var(--background-secondary);
        transition: all 0.2s;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #0E5EC5, #00C4FF);
        color: white !important;
    }
    
    /* Custom CSS variables for theme adaptation */
    :root {
        --text-color: #5A5A5A;
        --background-secondary: #f0f2f6;
        --border-color: #e0e0e0;
    }
    
    [data-theme="dark"] {
        --text-color: #E0E0E0;
        --background-secondary: #2a2a2a;
        --border-color: #444;
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
        st.subheader("Senior Data Engineer | Cloud Specialist | Big Data Architect")
        st.write("""
        🚀 Transforming raw data into strategic assets through robust, scalable, and secure data infrastructure.
        Expertise in designing systems that enable data-driven decision making at scale.
        """)
        st_lottie(lottie_coding, height=200, key="coding")

# --- TABS SECTION ---
tabs = st.tabs(["📝 About", "🛠 Skills", "🚀 Projects", "📞 Contact"])

# --- ABOUT ---
with tabs[0]:
    st.header("Professional Profile")
    st.write("""
    I am a **Senior Data Engineer** with **5+ years** of experience in designing and implementing enterprise-grade data solutions. 
    My expertise spans the entire data lifecycle from ingestion to analytics, with a focus on **cloud-native architectures**, 
    **real-time processing**, and **data governance**.
    """)
    
    with st.expander("🔍 Detailed Background"):
        st.write("""
        ### Core Competencies:
        - **Data Architecture**: Designing scalable data lakes, warehouses, and lakehouses
        - **ETL/ELT Pipelines**: Building robust data pipelines with error handling and monitoring
        - **Cloud Platforms**: Certified in AWS and Azure data technologies
        - **DataOps**: Implementing CI/CD for data pipelines
        - **Performance Optimization**: Tuning queries and infrastructure for cost-efficiency
        
        ### Professional Philosophy:
        I believe in "data as a product" - treating data systems with the same care as customer-facing applications, 
        focusing on reliability, documentation, and ease of use for data consumers.
        """)

# --- SKILLS ---
with tabs[1]:
    st.header("Technical Expertise")
    
    with st.container():
        st.subheader("Core Technologies")
        cols = st.columns(4)
        with cols[0]:
            st.markdown("**Cloud Platforms**")
            st.markdown("""
            - AWS (Glue, Redshift, EMR)
            - Azure (Data Factory, Synapse)
            - GCP (BigQuery, Dataflow)
            - Databricks
            """)
        with cols[1]:
            st.markdown("**Big Data Tools**")
            st.markdown("""
            - Apache Spark
            - Kafka/Kinesis
            - Hadoop Ecosystem
            - Delta Lake/Iceberg
            """)
        with cols[2]:
            st.markdown("**Data Engineering**")
            st.markdown("""
            - Airflow/Luigi
            - dbt
            - Great Expectations
            - Prefect/Dagster
            """)
        with cols[3]:
            st.markdown("**Languages**")
            st.markdown("""
            - Python (Expert)
            - SQL (Advanced)
            - Scala/Java
            - Terraform
            """)
    
    #st.divider()
    
    # with st.container():
    #     st.subheader("Certifications")
    #     cert_cols = st.columns(3)
    #     with cert_cols[0]:
    #         st.markdown("""
    #         **AWS Certified**
    #         - Data Analytics Specialty
    #         - Solutions Architect
    #         """)
    #     with cert_cols[1]:
    #         st.markdown("""
    #         **Microsoft Certified**
    #         - Azure Data Engineer
    #         - Azure Solutions Architect
    #         """)
    #     with cert_cols[2]:
    #         st.markdown("""
    #         **Other Credentials**
    #         - Databricks Certified Engineer
    #         - Google Cloud Professional
    #         """)

# --- PROJECTS ---
with tabs[2]:
    st.header("Selected Projects")
    
    # Project 1
    with st.container():
        st.subheader("🔹 Enterprise Data Platform Modernization")
        cols = st.columns([3,1])
        with cols[0]:
            st.markdown("""
            **Client**: Fortune 500 Retail Company  
            **Role**: Lead Data Engineer  
            **Tech Stack**: AWS EMR, Glue, Redshift, Airflow, dbt  
            
            ### Achievements:
            - Migrated legacy on-premise data warehouse to cloud-native architecture
            - Implemented medallion architecture for incremental data quality
            - Reduced processing time by 65% while cutting costs by 40%
            - Established data governance framework with lineage tracking
            
            
            """)
        # with cols[1]:
        #     st.image("https://via.placeholder.com/300x200?text=Architecture+Diagram", use_container_width=True)
    #[View Case Study](#) | [GitHub Repository](#)
    st.divider()
    
    # Project 2
    with st.container():
        st.subheader("🔹 Real-Time Customer Analytics Pipeline")
        cols = st.columns([1,3])
        # with cols[0]:
        #     st.image("https://via.assets.so/img.jpg?width=300&height=200&text=Streaming+Diagram", use_container_width=True)
        with cols[0]:
            st.markdown("""
            **Client**: FinTech Startup  
            **Role**: Streaming Data Architect  
            **Tech Stack**: Kafka, Flink, DynamoDB, Lambda  
            
            ### Achievements:
            - Designed event-driven architecture processing 50M+ events/day
            - Implemented exactly-once processing semantics
            - Enabled real-time personalization features
            - Reduced alerting latency from hours to seconds
            """)
    
    st.divider()
    
    # Project 3
    with st.expander("➕ Additional Projects"):
        with st.container():
            st.subheader("🔹 Data Mesh Implementation POC")
            st.markdown("""
            **Organization**: Healthcare Provider  
            **Role**: Data Platform Engineer  
            **Tech Stack**: Kubernetes, S3, Spark, GraphQL  
            
            ### Key Contributions:
            - Designed domain-oriented data products
            - Implemented self-service data platform
            - Automated data product deployment
            """)
            
            st.subheader("🔹 MLOps Pipeline Automation")
            st.markdown("""
            **Organization**: AI Startup  
            **Role**: Data Infrastructure Engineer  
            **Tech Stack**: MLflow, Sagemaker, Step Functions  
            
            ### Key Contributions:
            - Automated feature store updates
            - Implemented model monitoring
            - Reduced deployment time by 75%
            """)

# --- CONTACT ---
with tabs[3]:
    st.header("Get In Touch")
    
    contact_cols = st.columns(2)
    with contact_cols[0]:
        st.subheader("Contact Form")
        contact_form = """
        <form action="https://formsubmit.co/shivaraja261@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your Name" required style="margin-bottom: 1rem; width: 100%; padding: 0.5rem; border-radius: 0.5rem; border: 1px solid var(--border-color); background-color: var(--background-secondary); color: var(--text-color);">
            <input type="email" name="email" placeholder="Your Email" required style="margin-bottom: 1rem; width: 100%; padding: 0.5rem; border-radius: 0.5rem; border: 1px solid var(--border-color); background-color: var(--background-secondary); color: var(--text-color);">
            <textarea name="message" placeholder="Your message here..." required style="margin-bottom: 1rem; width: 100%; padding: 0.5rem; border-radius: 0.5rem; border: 1px solid var(--border-color); background-color: var(--background-secondary); color: var(--text-color); height: 150px;"></textarea>
            <button type="submit" style="background: linear-gradient(135deg, #0E5EC5, #00C4FF); color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.5rem; cursor: pointer; transition: all 0.3s ease;">Send Message</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
    
    with contact_cols[1]:
        st.subheader("Connect With Me")
        st.markdown("""
        **📧 Email**: [shivaraja261@gmail.com](mailto:shivaraja261@gmail.com)  
        **💼 LinkedIn**: [linkedin.com/in/shivaraj-l](https://www.linkedin.com/in/shivaraj-l)  
        **🐙 GitHub**: [github.com/shivaraj-l](https://github.com/shivaraj-l)  
        **📱 Twitter**: [@shivaraj_l](https://twitter.com/shivaraj_l)  
        """)
        
        st.divider()
        
        st.subheader("Current Availability")
        st.markdown("""
        - **Location**: Remote or Bangalore, India
        - **Time Zone**: IST (UTC+5:30)
        """)

# --- FOOTER ---
st.divider()
footer_cols = st.columns(3)
with footer_cols[1]:
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <p>© 2025 Shivaraj L | Built with Streamlit</p>
        <p style="font-size: 0.8rem;">Last Updated: June 2025</p>
    </div>
    """, unsafe_allow_html=True)
