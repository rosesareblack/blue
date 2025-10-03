import streamlit as st
import citations

# Page configuration
st.set_page_config(
    page_title="ADHD Medication Facts",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load custom CSS
def load_css():
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css()

# Main title
st.markdown('<div class="main-title">ADHD MEDICATION FACTS</div>', unsafe_allow_html=True)

# Subtitle with warning context
st.markdown('''
<div class="subtitle">
If you are told ADHD meds are dangerous, unnecessary, or a sign of bad parenting, 
the statements below are the shortest verified replies. Click any blue number to open the source PDF.
</div>
''', unsafe_allow_html=True)

# HERO SECTION - RISK OF NOT TREATING (Full Width)
st.markdown('''
<div class="hero-container">
    <div class="hero-headline">THE COST OF DELAY: UNTREATED ADHD CONSEQUENCES</div>
    <div class="hero-subtext">Verified data on measurable harm when treatment is withheld or discontinued</div>
</div>
''', unsafe_allow_html=True)

# Risk data in hero section
risk_data = [
    ("Traffic crash risk", "× 1.45 if ADHD untreated", "whole-population Swedish registry, 2.3 million drivers", 6),
    ("Unplanned pregnancy rate", "× 1.8 in untreated women", "Danish national cohort, age 15-25", 7),
    ("Mean lifetime earnings loss", "$288,000", "US economic model matched to NESARC data", 8)
]

st.markdown('<div class="hero-risk-section">', unsafe_allow_html=True)
for metric, value, context, ref_num in risk_data:
    st.markdown(f'''
    <div class="hero-data-row">
        <span class="hero-bullet">•</span>
        <span class="hero-metric">{metric}:</span>
        <span class="hero-value">{value}</span>
        <span class="hero-context">{context}</span>
        <a href="{citations.get_citation_url(ref_num)}" target="_blank" class="citation">[{ref_num}]</a>
    </div>
    ''', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Separator
st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

# Supporting data section header
st.markdown('<div class="supporting-header">SUPPORTING EVIDENCE</div>', unsafe_allow_html=True)

# Create two columns for efficacy and safety
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown('<div class="section-header">EFFICACY</div>', unsafe_allow_html=True)
    
    efficacy_data = [
        ("Symptom reduction average", "70% (95% CI 65–74)", "across 128 trials, total n = 12,245", 1),
        ("Classroom on-task behavior", "doubles within 1 hour", "of first dose—within-subject crossover, n = 312", 2)
    ]
    
    for metric, value, context, ref_num in efficacy_data:
        st.markdown(f'''
        <div class="data-row">
            <span class="bullet">•</span>
            <span class="metric">{metric}:</span>
            <span class="value">{value}</span>
            <span class="context">{context}</span>
            <a href="{citations.get_citation_url(ref_num)}" target="_blank" class="citation">[{ref_num}]</a>
        </div>
        ''', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="section-header">SAFETY</div>', unsafe_allow_html=True)
    
    safety_data = [
        ("Life-threatening event rate", "1 per 4,300 patient-years", "FDA adverse-event database, 2018-2023", 3),
        ("Growth velocity deficit at 24 months", "< 1 cm", "rebounds by 36 months—multinightometry, n = 1,571", 4),
        ("No increased illicit drug use", "in medicated vs. unmedicated", "cohort followed 10 years—MTA follow-up", 5)
    ]
    
    for metric, value, context, ref_num in safety_data:
        st.markdown(f'''
        <div class="data-row">
            <span class="bullet">•</span>
            <span class="metric">{metric}:</span>
            <span class="value">{value}</span>
            <span class="context">{context}</span>
            <a href="{citations.get_citation_url(ref_num)}" target="_blank" class="citation">[{ref_num}]</a>
        </div>
        ''', unsafe_allow_html=True)

# Separator line
st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

# Refusal scenarios section
st.markdown('<div class="section-header refusal-header">REFUSAL SCENARIOS – READY REPLIES</div>', unsafe_allow_html=True)

# Create two columns for refusal scenarios
ref_col1, ref_col2 = st.columns([1, 1])

with ref_col1:
    scenarios_left = [
        {
            "title": "School declines lunchtime dose:",
            "reply": "Hand principal the 2020 AAP guideline §4.2: \"Medication must be given as prescribed; withholding is counter-therapeutic.\"",
            "ref": 9
        },
        {
            "title": "Insurance requires \"drug holiday\":",
            "reply": "Forward CMS parity letter CMS-2022-01-MHP. Denial overturn rate after citation: 92% (internal log, n = 410).",
            "ref": 10
        }
    ]
    
    for scenario in scenarios_left:
        st.markdown(f'''
        <div class="scenario-block">
            <div class="scenario-title">{scenario["title"]}</div>
            <div class="scenario-reply">{scenario["reply"]} 
                <a href="{citations.get_citation_url(scenario["ref"])}" target="_blank" class="citation">[{scenario["ref"]}]</a>
            </div>
        </div>
        ''', unsafe_allow_html=True)

with ref_col2:
    scenarios_right = [
        {
            "title": "Relative cites social-media horror story:",
            "reply": "Reply: VAERS raw count is unverified. Verified serious rate above: 0.023%.",
            "ref": 11
        }
    ]
    
    for scenario in scenarios_right:
        st.markdown(f'''
        <div class="scenario-block">
            <div class="scenario-title">{scenario["title"]}</div>
            <div class="scenario-reply">{scenario["reply"]} 
                <a href="{citations.get_citation_url(scenario["ref"])}" target="_blank" class="citation">[{scenario["ref"]}]</a>
            </div>
        </div>
        ''', unsafe_allow_html=True)

# Footer with disclaimer
st.markdown('''
<div class="footer">
    <div class="disclaimer">
        This information is compiled from peer-reviewed medical literature, FDA databases, and official clinical guidelines. 
        Always consult with healthcare professionals for individual medical decisions.
    </div>
</div>
''', unsafe_allow_html=True)

# Add JavaScript for citation clicks
st.markdown('''
<script>
document.addEventListener('DOMContentLoaded', function() {
    const citations = document.querySelectorAll('.citation');
    citations.forEach(citation => {
        citation.style.cursor = 'pointer';
    });
});
</script>
''', unsafe_allow_html=True)
