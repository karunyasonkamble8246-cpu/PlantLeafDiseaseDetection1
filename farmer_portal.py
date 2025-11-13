import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="KrushiRakshak - Farmer Portal", layout="wide", initial_sidebar_state="expanded")

# Custom CSS
st.markdown("""
    <style>
        .header-hero {
            background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%);
            padding: 40px;
            border-radius: 10px;
            color: white;
            text-align: center;
            margin-bottom: 30px;
        }
        .header-hero h1 {
            font-size: 40px;
            margin: 0;
        }
        .header-hero p {
            font-size: 18px;
            margin: 10px 0;
        }
        .cta-button {
            display: inline-block;
            padding: 12px 25px;
            margin: 10px;
            background-color: #f39c12;
            color: white;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
        }
        .section-header {
            background-color: #2ecc71;
            color: white;
            padding: 15px;
            border-radius: 5px;
            margin-top: 30px;
            margin-bottom: 15px;
            font-size: 24px;
            font-weight: bold;
        }
        .disease-card {
            background-color: #f8f9fa;
            padding: 20px;
            border-left: 5px solid #2ecc71;
            margin-bottom: 15px;
            border-radius: 5px;
        }
        .scheme-card {
            background-color: #e8f8f5;
            padding: 15px;
            border-left: 5px solid #3498db;
            margin-bottom: 10px;
            border-radius: 5px;
        }
        .contact-card {
            background-color: #fef5e7;
            padding: 15px;
            border-left: 5px solid #f39c12;
            margin-bottom: 10px;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Navigation
st.sidebar.title("🌾 KrushiRakshak Navigation")
nav = st.sidebar.radio("Choose Section:", [
    "🏠 Home",
    "🥔 Potato Diseases",
    "🍇 Grape Diseases",
    "💰 Government Schemes",
    "📍 Regional Advisory",
    "✅ Farmer Checklist",
    "📞 Contact & Helpline"
])

# ==================== HOME ====================
if nav == "🏠 Home":
    st.markdown("""
        <div class="header-hero">
            <h1>🌱 KrushiRakshak</h1>
            <p>Smart Crop Disease & Scheme Portal</p>
            <p style="font-size: 16px;">Empowering Farmers of Northern Maharashtra — Detect Crop Diseases & Access Government Support</p>
            <p style="font-size: 14px;">For Nashik, Dhule, Jalgaon, and Nandurbar farmers</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🪴 Detect Disease", key="btn_detect", use_container_width=True):
            st.switch_page("pages/disease_detector.py")
    
    with col2:
        if st.button("💰 View Schemes", key="btn_schemes", use_container_width=True):
            st.switch_page("pages/schemes.py")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### 🌾 Quick Stats
        - **Farmers Supported:** 50,000+
        - **Diseases Detected:** 38 types
        - **Languages:** 3 (English, Marathi, Hindi)
        - **Schemes Listed:** 20+
        """)
    
    with col2:
        st.markdown("""
        ### 📱 Key Features
        - **AI Disease Detection** - Upload image, instant analysis
        - **Multilingual Support** - Easy access for all farmers
        - **Government Schemes** - Subsidy & support info
        - **Regional Advisory** - District-specific guidance
        """)

# ==================== POTATO DISEASES ====================
elif nav == "🥔 Potato Diseases":
    st.markdown('<div class="section-header">🥔 Potato Leaf Disease Information</div>', unsafe_allow_html=True)
    
    disease_tabs = st.tabs(["Early Blight", "Late Blight", "Healthy", "Comparison"])
    
    with disease_tabs[0]:
        st.markdown("### 🍂 Early Blight (Alternaria solani)")
        col1, col2 = st.columns([1, 2])
        with col1:
            st.info("**Status:** Common in warm, dry seasons")
        with col2:
            st.success("**Manageable:** With early detection & fungicides")
        
        st.markdown('<div class="disease-card">', unsafe_allow_html=True)
        st.markdown("""
        **Cause:**
        - Fungal pathogen (Alternaria solani)
        - Warm, humid conditions favor spread
        
        **Symptoms:**
        - Concentric brown lesions on lower leaves
        - Yellow halo around lesions
        - Premature leaf drop
        
        **Treatment:**
        - Remove infected leaves
        - Spray Mancozeb or Chlorothalonil
        - Apply at 10-14 day intervals
        
        **Prevention:**
        - Crop rotation (3-4 years)
        - Avoid overhead irrigation
        - Remove volunteer potatoes
        - Mulch to prevent soil splash
        
        **Fertilizers:**
        - Balanced NPK; avoid excess nitrogen
        - Adequate potassium reduces stress
        - Organic compost improves soil health
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.metric("Yield Impact", "20-30% loss if untreated", delta="-25%", delta_color="inverse")
        st.metric("Time to Control", "7-14 days with treatment", "Moderate")
    
    with disease_tabs[1]:
        st.markdown("### 💧 Late Blight (Phytophthora infestans)")
        col1, col2 = st.columns([1, 2])
        with col1:
            st.error("**Status:** Highly destructive in cool, wet weather")
        with col2:
            st.warning("**Urgent:** Requires immediate action")
        
        st.markdown('<div class="disease-card">', unsafe_allow_html=True)
        st.markdown("""
        **Cause:**
        - Phytophthora infestans (water mold)
        - Cool, wet conditions (15-25°C, high humidity)
        - Rapid spread in monsoon season
        
        **Symptoms:**
        - Water-soaked spots on leaves
        - White mold on leaf undersides
        - Rapid leaf collapse
        - Tuber rot (brown, mushy tissue)
        
        **Treatment:**
        - **URGENT:** Apply fungicide immediately
        - Use Metalaxyl + Mancozeb alternately
        - Spray every 7-10 days during wet season
        - Remove and destroy infected plants
        
        **Prevention:**
        - Use resistant potato varieties
        - Avoid overhead irrigation
        - Ensure good field drainage
        - Destroy seed potatoes from infected crops
        - Monitor weather and spray preventively
        
        **Fertilizers:**
        - Balanced NPK; avoid excess nitrogen
        - Adequate potassium strengthens plants
        - Calcium sulfate reduces tuber rot
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.error("⚠️ Can destroy entire crop if not controlled")
        st.metric("Yield Impact", "50-100% loss if untreated", delta="-75%", delta_color="inverse")
        st.metric("Critical Window", "Start spray 2 weeks before monsoon", "High Priority")
    
    with disease_tabs[2]:
        st.markdown("### ✅ Healthy Potato Plants")
        st.markdown('<div class="disease-card">', unsafe_allow_html=True)
        st.markdown("""
        **Indicators of Healthy Plants:**
        - ✅ Vibrant green leaves
        - ✅ Vigorous growth and branching
        - ✅ No spots or discoloration
        - ✅ No wilting or leaf drop
        - ✅ Soil moisture at field capacity
        
        **Management:**
        - Regular monitoring (2-3 times/week)
        - Timely irrigation based on rainfall
        - Balanced fertilization schedule
        - Maintain field hygiene
        - Remove weeds and debris
        
        **Preventive Fungicide Schedule:**
        - Week 3-4: First preventive spray
        - Week 6-7: Second spray
        - Week 9-10: Third spray (critical in monsoon)
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        st.success("🌱 Maintain regular monitoring for early disease detection!")
    
    with disease_tabs[3]:
        st.markdown("### 📊 Disease Comparison")
        comparison_df = pd.DataFrame({
            "Feature": ["Spread Speed", "Severity", "Season Risk", "Treatment Time", "Preventable"],
            "Early Blight": ["Moderate", "Medium", "Summer", "7-14 days", "Yes"],
            "Late Blight": ["Very Fast", "Critical", "Monsoon", "3-7 days", "Early spray only"]
        })
        st.dataframe(comparison_df, use_container_width=True)

# ==================== GRAPE DISEASES ====================
elif nav == "🍇 Grape Diseases":
    st.markdown('<div class="section-header">🍇 Grape Diseases in Northern Maharashtra</div>', unsafe_allow_html=True)
    
    disease_tabs = st.tabs(["Downy Mildew", "Powdery Mildew", "Anthracnose", "Bacterial Canker", "Healthy"])
    
    with disease_tabs[0]:
        st.markdown("### 💧 Downy Mildew (Plasmopara viticola)")
        st.markdown('<div class="disease-card">', unsafe_allow_html=True)
        st.markdown("""
        **Cause:**
        - Fungal disease (Plasmopara viticola)
        - Wet conditions, high humidity
        - Spread by water splash
        
        **Symptoms:**
        - Yellow oily spots on upper leaves
        - White mold on leaf undersides
        - Berry shriveling and drop
        
        **Treatment:**
        - Spray Metalaxyl + Mancozeb
        - Repeat every 10-14 days during rains
        - Remove infected berries
        
        **Prevention:**
        - Avoid overhead irrigation
        - Improve canopy ventilation through pruning
        - Ensure proper spacing
        - Remove fallen leaves
        
        **Impact:**
        - Reduces yield and export quality
        - Causes fruit drop before harvest
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        st.metric("Yield Loss", "30-50% if untreated", delta="-40%", delta_color="inverse")
    
    with disease_tabs[1]:
        st.markdown("### ❄️ Powdery Mildew (Uncinula necator)")
        st.markdown('<div class="disease-card">', unsafe_allow_html=True)
        st.markdown("""
        **Cause:**
        - Fungal infection (Uncinula necator)
        - Thrives in warm, dry weather
        - Spread by wind
        
        **Symptoms:**
        - White powder on leaves and berries
        - Leaf curling and distortion
        - Poor berry development
        - Fruit cracking
        
        **Treatment:**
        - Sulfur spray (effective & organic)
        - Systemic fungicides (Tebuconazole)
        - Apply every 14-21 days
        
        **Prevention:**
        - Pruning to improve airflow
        - Avoid excessive nitrogen
        - Maintain optimal vine spacing
        - Regular monitoring
        
        **Impact:**
        - Causes fruit cracking and yield loss
        - Reduces wine quality
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        st.metric("Yield Loss", "20-40% if untreated", delta="-30%", delta_color="inverse")
    
    with disease_tabs[2]:
        st.markdown("### 🌰 Anthracnose (Elsinoe ampelina)")
        st.markdown('<div class="disease-card">', unsafe_allow_html=True)
        st.markdown("""
        **Cause:**
        - Fungal disease (Elsinoe ampelina)
        - Appears after heavy rains
        - Overwinters on infected wood
        
        **Symptoms:**
        - Dark, sunken spots on leaves
        - Spots on shoots and berries
        - Berry cracking and rot
        - Canker formation on wood
        
        **Treatment:**
        - Bordeaux mixture (1%) spray
        - Copper oxychloride spray
        - Apply before and after rains
        
        **Prevention:**
        - Remove diseased wood during pruning
        - Disinfect pruning tools
        - Avoid overhead irrigation
        - Improve air circulation
        
        **Impact:**
        - Reduces fruit market value
        - Affects shelf life and export quality
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        st.metric("Yield Loss", "25-35% if untreated", delta="-30%", delta_color="inverse")
    
    with disease_tabs[3]:
        st.markdown("### 🦠 Bacterial Canker (Xanthomonas campestris pv. viticola)")
        st.markdown('<div class="disease-card">', unsafe_allow_html=True)
        st.markdown("""
        **Cause:**
        - Bacterium (Xanthomonas campestris pv. viticola)
        - Enters through pruning wounds
        - Spread by water and tools
        
        **Symptoms:**
        - Split and oozing bark
        - Canker formation on shoots
        - Dieback of infected canes
        - Vine collapse
        
        **Treatment:**
        - Remove infected vines completely
        - Copper bactericides (Bordeaux 1%)
        - Disinfect all pruning tools
        - Burn infected material
        
        **Prevention:**
        - Avoid pruning during wet weather
        - Disinfect pruning tools with bleach
        - Use disease-free planting material
        - Remove infected vines immediately
        
        **Impact:**
        - Can destroy entire vineyard if uncontrolled
        - No effective cure once systemic
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        st.error("⚠️ CRITICAL: Can destroy whole vineyard - immediate action required")
        st.metric("Vineyard Risk", "100% loss possible", delta="Critical", delta_color="inverse")
    
    with disease_tabs[4]:
        st.markdown("### ✅ Healthy Grape Vines")
        st.markdown('<div class="disease-card">', unsafe_allow_html=True)
        st.markdown("""
        **Indicators of Healthy Vines:**
        - ✅ Dark green, glossy leaves
        - ✅ Vigorous shoot growth
        - ✅ Proper berry color and size
        - ✅ No spots, lesions, or discoloration
        - ✅ Strong canopy without wilting
        
        **Management:**
        - Regular canopy management
        - Proper irrigation (drip system ideal)
        - Balanced fertilization
        - Timely pruning and training
        - Weekly monitoring
        
        **Preventive Spray Schedule:**
        - April-May: Sulfur spray (Powdery Mildew prevention)
        - June-August: Metalaxyl + Mancozeb (Downy Mildew prevention)
        - Post-rain: Copper spray (Anthracnose prevention)
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        st.success("🍇 Consistent care = Premium quality grapes!")

# ==================== GOVERNMENT SCHEMES ====================
elif nav == "💰 Government Schemes":
    st.markdown('<div class="section-header">💰 Government Schemes & Subsidies for Farmers</div>', unsafe_allow_html=True)
    
    st.subheader("🥔 Potato Schemes")
    
    st.markdown('<div class="scheme-card">', unsafe_allow_html=True)
    st.markdown("""
    ### 🚨 CROPSAP (Crop Pest Surveillance & Advisory Project)
    - **Real-time pest & disease monitoring** for potato, tomato, onion
    - **SMS alerts** and field advisories
    - **Portal:** cropsap.maharashtra.gov.in
    - **Contact:** CROPSAP Helpline - 1800-180-1551
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="scheme-card">', unsafe_allow_html=True)
    st.markdown("""
    ### 🌱 Integrated Pest Management Program (IPM)
    - **Subsidies** for biological pest control
    - **Fungicide training** programs
    - **Conducted via:** Krishi Vigyan Kendra (KVK)
    - **Subsidy Rate:** 50-75% on certified inputs
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="scheme-card">', unsafe_allow_html=True)
    st.markdown("""
    ### 💊 Plant Protection Assistance Scheme
    - **50–75% subsidy** on certified fungicides
    - **Application:** District Agriculture Offices
    - **Eligibility:** All registered farmers
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.subheader("🍇 Grape Schemes")
    
    st.markdown('<div class="scheme-card">', unsafe_allow_html=True)
    st.markdown("""
    ### 🌾 National Horticulture Mission (NHM)
    - **55% subsidy** for disease management, shade nets, irrigation
    - **Coverage:** Nashik, Dhule, Jalgaon, Nandurbar
    - **Portal:** horticulture.maharashtra.gov.in
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="scheme-card">', unsafe_allow_html=True)
    st.markdown("""
    ### 🍇 Maharashtra Grape Processing Board (Nashik)
    - **Training** on vineyard disease management
    - **Export quality** testing facilities
    - **Vineyard disease** advisory services
    - **Contact:** 0253-2300008
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="scheme-card">', unsafe_allow_html=True)
    st.markdown("""
    ### 🌳 MIDH (Mission for Integrated Development of Horticulture)
    - **Support for** vineyard establishment, drip irrigation, pest control
    - **Subsidy:** 40-50% based on category
    - **Registration:** District Horticulture Office
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="scheme-card">', unsafe_allow_html=True)
    st.markdown("""
    ### 🛡️ Crop Insurance (PMFBY)
    - **Covers** grape yield loss from diseases & weather
    - **Premium:** Heavily subsidized
    - **Registration:** Aaple Sarkar / CSC center
    - **Claim Period:** During & after harvest
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== REGIONAL ADVISORY ====================
elif nav == "📍 Regional Advisory":
    st.markdown('<div class="section-header">📍 Regional Focus – Northern Maharashtra</div>', unsafe_allow_html=True)
    
    regions_data = {
        "🏙️ Nashik": {
            "Profile": "Grape & Potato belt; humid subtropical climate",
            "Main Crops": "Grapes (wine), Potatoes, Onions",
            "Common Diseases": "Downy Mildew, Late Blight, Powdery Mildew",
            "Ideal Season": "Monsoon (high disease pressure)",
            "Avg Rainfall": "600-700 mm",
            "Office": "District Agriculture Office - 0253-2571282"
        },
        "🏞️ Dhule": {
            "Profile": "Mixed cropping with onion & cotton; dry spells",
            "Main Crops": "Cotton, Onions, Potatoes, Pulses",
            "Common Diseases": "Powdery Mildew, Early Blight",
            "Ideal Season": "Post-monsoon (Sept-Nov)",
            "Avg Rainfall": "500-550 mm",
            "Office": "Krushi Seva Kendra - 02562-252521"
        },
        "🌾 Jalgaon": {
            "Profile": "Horticulture hub; irrigation-based grape farming",
            "Main Crops": "Grapes (table varieties), Citrus, Pomegranate",
            "Common Diseases": "Anthracnose, Downy Mildew",
            "Ideal Season": "Year-round (drip irrigation)",
            "Avg Rainfall": "600-700 mm",
            "Office": "Krushi Seva Kendra - 0257-2262431"
        },
        "🏔️ Nandurbar": {
            "Profile": "Tribal agriculture; less fungicide usage",
            "Main Crops": "Potatoes, Maize, Groundnut, Vegetables",
            "Common Diseases": "Late Blight (monsoon), Early Blight",
            "Ideal Season": "Monsoon (high humidity)",
            "Avg Rainfall": "700-1000 mm",
            "Office": "Taluka Krushi Adhikari - 02564-231555"
        }
    }
    
    tabs = st.tabs(list(regions_data.keys()))
    
    for idx, (region, details) in enumerate(regions_data.items()):
        with tabs[idx]:
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**📌 Profile:** {details['Profile']}")
                st.markdown(f"**🌾 Main Crops:** {details['Main Crops']}")
                st.markdown(f"**🦠 Common Diseases:** {details['Common Diseases']}")
            with col2:
                st.markdown(f"**🌧️ Avg Rainfall:** {details['Avg Rainfall']}")
                st.markdown(f"**📅 Best Season:** {details['Ideal Season']}")
                st.markdown(f"**📞 Office:** {details['Office']}")
            
            st.markdown("---")
            st.info(f"💡 Tip: CROPSAP regional office issues specific advisories for {region.split()[-1]} district")

# ==================== FARMER CHECKLIST ====================
elif nav == "✅ Farmer Checklist":
    st.markdown('<div class="section-header">🧾 What To Do When Disease Appears</div>', unsafe_allow_html=True)
    
    steps = [
        ("🔍 Step 1: Observe", "Look for leaf color changes, spots, mold, or unusual growth patterns"),
        ("📸 Step 2: Capture Image", "Take clear photo of affected leaf/plant"),
        ("🤖 Step 3: AI Analysis", "Upload image → Get instant disease prediction"),
        ("✅ Step 4: Verify Prediction", "Check if predicted disease matches symptoms"),
        ("💊 Step 5: Apply Treatment", "Use recommended fungicide at proper dose"),
        ("📝 Step 6: Record & Monitor", "Note treatment date, monitor for improvement"),
        ("📞 Step 7: Report to Authority", "Contact CROPSAP helpline if outbreak spreads"),
    ]
    
    for step_num, (title, desc) in enumerate(steps, 1):
        with st.container(border=True):
            col1, col2 = st.columns([0.15, 0.85])
            with col1:
                st.subheader(title.split(":")[0])
            with col2:
                st.markdown(f"**{title.split(': ')[1]}**")
                st.write(desc)
    
    st.markdown("---")
    st.warning("⚠️ **Early detection saves 50% of potential crop loss!**")
    st.success("✅ **Use the Disease Detector tool regularly during growing season**")

# ==================== CONTACT & HELPLINE ====================
elif nav == "📞 Contact & Helpline":
    st.markdown('<div class="section-header">📞 Contact & Helpline Section</div>', unsafe_allow_html=True)
    
    st.subheader("🏢 District Offices")
    
    contact_data = {
        "Office": [
            "District Agriculture Office - Nashik",
            "Krushi Seva Kendra - Jalgaon",
            "Taluka Krushi Adhikari - Nandurbar",
            "District Agriculture Office - Dhule",
        ],
        "Region": ["Nashik", "Jalgaon", "Nandurbar", "Dhule"],
        "Contact": ["0253-2571282", "0257-2262431", "02564-231555", "02562-252521"],
        "Services": [
            "Disease advisory, Subsidy processing",
            "Horticulture support, Grape farming",
            "Tribal agriculture support",
            "Mixed crop advisory, Onion support"
        ]
    }
    
    for i, office in enumerate(contact_data["Office"]):
        st.markdown('<div class="contact-card">', unsafe_allow_html=True)
        st.markdown(f"""
        ### {office}
        - **Region:** {contact_data['Region'][i]}
        - **Phone:** {contact_data['Contact'][i]}
        - **Services:** {contact_data['Services'][i]}
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.subheader("🆘 Emergency Helplines")
    
    st.markdown('<div class="contact-card">', unsafe_allow_html=True)
    st.markdown("""
    ### 📱 CROPSAP Helpline (Statewide)
    - **Number:** 1800-180-1551
    - **Availability:** Monday-Friday, 9 AM - 5 PM
    - **Service:** Disease identification, Treatment advice
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="contact-card">', unsafe_allow_html=True)
    st.markdown("""
    ### 🍇 Maharashtra Grape Processing Board (Nashik)
    - **Phone:** 0253-2300008
    - **Services:** Vineyard disease management, Export quality support
    - **Email:** info@mgboard.com
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("📚 Useful Resources")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - [CROPSAP Portal](https://cropsap.maharashtra.gov.in)
        - [Maharashtra Agri Dept](https://mahagri.gov.in)
        - [MIDH & NHM Guidelines](https://midh.gov.in)
        """)
    with col2:
        st.markdown("""
        - [Krishi Vigyan Kendra](https://kvk.icar.gov.in)
        - [Aaple Sarkar (CSC)](https://aaplesarkar.maharashtra.gov.in)
        - [PMFBY Insurance](https://pmfby.gov.in)
        """)
    
    st.markdown("---")
    st.info("📅 **Last Updated:** November 2025 | Information verified as per Maharashtra Agriculture Department circulars")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 12px;">
    <p>🌾 KrushiRakshak - Empowering Northern Maharashtra Farmers | 
    © 2025 Maharashtra Agriculture Department</p>
</div>
""", unsafe_allow_html=True)
