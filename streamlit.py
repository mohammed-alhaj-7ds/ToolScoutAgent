import streamlit as st
from src.workflow import Workflow
from PIL import Image
import time

# 🟢 Page setup
st.set_page_config(
    page_title="ToolScoutAgent",
    page_icon="🤖",
    layout="wide"
)

st.markdown(
    "<h1 style='text-align: center;'>🤖 ToolScoutAgent</h1>",
    unsafe_allow_html=True
)

st.markdown("""
<p style='text-align: center; font-size:16px;'>
AI-powered agent to discover, analyze, and recommend developer tools.  
Enter your query below to get developer-focused insights.
</p>
""", unsafe_allow_html=True)

# Sidebar settings
st.sidebar.header("⚙️ Settings")
num_results = st.sidebar.slider("Number of tools to display", 1, 10, 5)

workflow = Workflow()

# User input
query = st.text_input("🔍 Enter your developer tool query:", "")

if st.button("Search") and query.strip():
    placeholder = st.empty()
    with st.spinner("🔄 Searching and analyzing tools..."):
        try:
            result = workflow.run(query.strip())
            placeholder.empty()
            st.success(f"Results for: **{query}**")

            for i, company in enumerate(result.companies[:num_results], 1):
                # Card container
                with st.container():
                    st.markdown(f"### {i}. 🏢 {company.name}")
                    col1, col2 = st.columns([2, 3])

                    with col1:
                        st.markdown(f"🌐 **Website:** [{company.website}]({company.website})" if company.website else "N/A")
                        st.markdown(f"💰 **Pricing:** {company.pricing_model or 'Unknown'}")
                        st.markdown(f"📖 **Open Source:** {'✅' if company.is_open_source else '❌'}")
                        st.markdown(f"🔌 **API:** {'✅' if company.api_available else '❌'}")
                    
                    with col2:
                        st.markdown(f"🛠️ **Tech Stack:** {', '.join(company.tech_stack[:5]) or 'N/A'}")
                        st.markdown(f"💻 **Language Support:** {', '.join(company.language_support[:5]) or 'N/A'}")
                        st.markdown(f"🔗 **Integrations:** {', '.join(company.integration_capabilities[:4]) or 'N/A'}")
                        st.markdown(f"📝 **Description:** {company.description or 'N/A'}")

                    st.markdown("---")
                    time.sleep(0.1)  # slight delay for smooth UI

            # Recommendations card
            if result.analysis:
                st.markdown("## 💡 Developer Recommendations")
                st.text_area("Copyable Recommendations", value=result.analysis, height=180)

        except Exception as e:
            st.error(f"⚠️ An error occurred: {e}")

st.markdown("""
---
Developed by **Mohammed Alhaj** | [GitHub Repository](https://github.com/mohammed-alhaj-7ds/ToolScoutAgent)
""")
