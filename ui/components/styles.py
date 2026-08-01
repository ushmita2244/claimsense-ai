import streamlit as st


def load_css():

    st.markdown(
        """
<style>

/* ===========================
Main App
=========================== */

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    max-width:1200px;
}

/* ===========================
Hero Card
=========================== */

.hero{

background:linear-gradient(
135deg,
#0F6CBD,
#2E8BFF
);

border-radius:22px;

padding:24px 34px;

color:white;

box-shadow:
0px 16px 32px rgba(0,0,0,0.15);

margin-bottom:28px;

}

/* ===========================
Hero Text
=========================== */

.hero-title{

font-size:42px;

font-weight:700;

margin-bottom:8px;

}

.hero-subtitle{

font-size:20px;

opacity:0.95;

margin-bottom:20px;

}

.hero-description{

font-size:16px;

line-height:1.5;

opacity:0.92;

}

/* ===========================
Section Heading
=========================== */

.section-title{

font-size:34px;

font-weight:700;

margin-top:20px;

margin-bottom:20px;

}

/* ===========================
Feature Cards
=========================== */

.feature{

background:white;

border-radius:18px;

padding:25px;

border:1px solid #E8EEF7;

transition:0.3s;

min-height:170px;

box-shadow:
0px 6px 20px rgba(0,0,0,0.05);

}

.feature:hover{

transform:translateY(-6px);

border:1px solid #0F6CBD;

box-shadow:
0px 14px 28px rgba(15,108,189,0.18);

}

/* ===========================
Feature Icon
=========================== */

.feature-icon{

font-size:34px;

margin-bottom:10px;

}

/* ===========================
Feature Title
=========================== */

.feature-title{

font-size:22px;

font-weight:600;

margin-bottom:10px;

}

/* ===========================
Feature Description
=========================== */

.feature-desc{

color:#666;

font-size:15px;

line-height:1.7;

}

/* =======================================================
Chat Messages
======================================================= */


.ai-message{

background:#FCFCFD;

border:1px solid #E7EAF3;

border-radius:18px;

padding:22px;

margin-top:8px;

box-shadow:
0 6px 18px rgba(15,23,42,0.08);

}

.user-message{

background:#F5F9FF;

border:1px solid #D6E9FF;

border-radius:18px;

padding:22px;

margin-top:8px;

}

/* =======================================================
AI Insights
======================================================= */

.metric-card{

background:linear-gradient(
180deg,
#FFFFFF,
#F8FAFC
);

border:1px solid #E6EDF8;

border-radius:14px;

padding:16px;

text-align:center;

box-shadow:
0 4px 14px rgba(15,23,42,0.05);

margin-bottom:14px;

transition:all .2s ease;

}

.metric-card:hover{

transform:translateY(-3px);

box-shadow:
0 12px 24px rgba(37,99,235,0.12);

border-color:#BFDBFE;

}

.metric-title{

font-size:12px;

letter-spacing:.3px;

text-transform:uppercase;

font-weight:600;

color:#64748B;

margin-bottom:10px;

}

.metric-value{

font-size:22px;

font-weight:700;

color:#0F172A;

}

</style>
        """,
        unsafe_allow_html=True,
    )