import streamlit as st
import pandas as pd
import os
from Controllers.scraper import search_products
from Pipelines.data_pipeline import DataPipeline
from Agents.Agent_feedback import recommend_best_deal_with_ai

# 🧱 Page setup
st.set_page_config(page_title="Amazon Scraper", page_icon="🛍️", layout="centered")

with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Title
st.markdown('<div class="title">🛍️ Amazon Product Scraper</div>', unsafe_allow_html=True)

# Input Section
st.markdown('<div class="section-title">🔎 Search for a product</div>', unsafe_allow_html=True)
product_name = st.text_input("Enter the product name:", placeholder="e.g. MacBook, Headphones...")

# Scrape button
if st.button("Scrape Product Data"):
    if not product_name.strip():
        st.warning("⚠️ Please enter a valid product name.")
    else:
        filename = f"{product_name}.csv"
        pipeline = DataPipeline(csv_filename=filename)

        try:
            search_products(product_name, data_pipeline=pipeline)
            pipeline.close_pipeline()

            if os.path.exists(filename):
                df = pd.read_csv(filename)
                st.success("Scraping completed successfully!")
                st.markdown('<div class="section-title">🗂️ Scraped Product List</div>', unsafe_allow_html=True)
                st.dataframe(df)

                st.download_button("📥 Download CSV", df.to_csv(index=False), file_name=filename, mime="text/csv")
            else:
                st.warning("⚠️ No results found.")
        
        except ValueError as ve:
            st.error(f"❌ Error: {ve}")
        except Exception as e:
            st.error(f"⚠️ Unexpected error: {e}")

# Divider
st.markdown("---")

# AI Recommendation Section
if product_name and os.path.exists(f"{product_name}.csv"):
    st.markdown('<div class="section-title">🤖 Ask the AI agent for the best deal</div>', unsafe_allow_html=True)

    if st.button("🧠 Recommend the best product"):
        with st.spinner("The AI agent is thinking..."):
            product, reason = recommend_best_deal_with_ai(f"{product_name}.csv")
            st.success(f"🌟 **Recommended product:** {product}")
            st.info(f"💬 **Why:** {reason}")



# Optional Footer
st.markdown("""---  
<center><small>Built with ❤️ using Python, Streamlit, and LLM Agents</small></center>""", unsafe_allow_html=True)

