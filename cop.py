import streamlit as st
import pickle
import numpy as np
import sklearn
from streamlit_option_menu import option_menu
import re

import base64
from PIL import Image

# Functions

def predict_status(ctry,itmtp,aplcn,wth,prdrf,qtlg,cstlg,tknslg,slgplg,itmdt,itmmn,itmyr,deldtdy,deldtmn,deldtyr):

   #change the datatypes "string" to "int"
    itdd= int(itmdt)
    itdm= int(itmmn)
    itdy= int(itmyr)

    dydd= int(deldtdy)
    dydm= int(deldtmn)
    dydy= int(deldtyr) 

    #modelfile of the classification
    with open ("C:\Shubh Projects DS\Classification_model.pkl", "rb") as f:
        model_class=pickle.load(f)

    user_data= np.array([[ctry,itmtp,aplcn,wth,prdrf,qtlg,cstlg,tknslg,
                       slgplg,itdd,itdm,itdy,dydd,dydm,dydy]])
    
    y_pred= model_class.predict(user_data)

    if y_pred == 1:
        return 1
    else:
        return 0

def predict_selling_price(ctry,sts,itmtp,aplcn,wth,prdrf,qtlg,cstlg,
                   tknslg,itmdt,itmmn,itmyr,deldtdy,deldtmn,deldtyr):

    #change the datatypes "string" to "int"
    itdd= int(itmdt)
    itdm= int(itmmn)
    itdy= int(itmyr)

    dydd= int(deldtdy)
    dydm= int(deldtmn)
    dydy= int(deldtyr)

     #modelfile of the classification
    with open("C:\Shubh Projects DS\Regression_Model.pkl","rb") as f:
        model_regg=pickle.load(f)

    user_data= np.array([[ctry,sts,itmtp,aplcn,wth,prdrf,qtlg,cstlg,tknslg,
                       itdd,itdm,itdy,dydd,dydm,dydy]])
    
    y_pred= model_regg.predict(user_data)

    ac_y_pred= np.exp(y_pred[0])

    return ac_y_pred


# Set page title
st.write("""
<div style='text-align:center'>
    <h1 style='color:#ffa500;'>Industrial Copper Modeling Application</h1>
</div>
""", unsafe_allow_html=True)


# Define the sidebar menu
with st.sidebar:
    SELECT = option_menu(
        menu_title=None,
        options=["ABOUT", "PREDICT SELLING PRICE", "PREDICT STATUS"],
        default_index=1,
        orientation="vertical",
        styles={
            "container": {"padding": "0!important", "background-color": "white"},
            "icon": {"color": "black", "font-size": "20px"},
            "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px", "--hover-color": "#ffa500"},
            "nav-link-selected": {"background-color": "#ffa500"},
        }
    )
    
# About section
if SELECT == "ABOUT":
    st.write("""
    <div style='color: #8B4513;'>
        <p>In this machine learning project, the main objective is to predict the selling price and status of an item or product based on the provided values of specific features.</h2>
        <p>Predicting Selling Price: The project aims to build a model that can estimate the selling price of an item. This could be useful for various scenarios such as e-commerce platforms, real estate, or used car marketplaces. The model will take into account various features or attributes of the item, such as quantity, thickness, width, location, or any other relevant factors that influence the selling price.</p>
        <p>Predicting Status: Along with predicting the selling price, the project also focuses on predicting the status of the item. This refers to whether the item is likely to be sold or not. The model will consider the same set of features and use them to determine the likelihood of the item being sold based on historical data or patterns observed in the dataset. If it is sold, the status will be considered as "won", otherwise the status will be considered as "lost".</p>
    </div>
    """, unsafe_allow_html=True)


# Predict Status section
if SELECT == "PREDICT STATUS":
    st.header("PREDICT STATUS (Won / Lost)")
    st.write(" ")

    # Add custom CSS to style the font and input field colors
    st.markdown(
        """
        <style>
        /* Navy blue color for font */
        .st-ef {
            color: #000080 !important;
        }
        /* Light yellow color for input field */
        .st-at {
            background-color: #FFFFE0 !important;
        }
        /* Light yellow color for select input fields */
        .st-ah, .st-ai, .st-aj {
            background-color: #FFFFE0 !important;
        }
        </style>
        """
        , unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        country= st.number_input(label="**Enter the Value for COUNTRY**/ Min:25.0, Max:113.0")
        item_type= st.number_input(label="**Enter the Value for ITEM TYPE**/ Min:0.0, Max:6.0")
        application= st.number_input(label="**Enter the Value for APPLICATION**/ Min:2.0, Max:87.5")
        width= st.number_input(label="**Enter the Value for WIDTH**/ Min:700.0, Max:1980.0")
        product_ref= st.number_input(label="**Enter the Value for PRODUCT_REF**/ Min:611728, Max:1722207579")
        quantity_tons_log= st.number_input(label="**Enter the Value for QUANTITY_TONS (Log Value)**/ Min:-0.322, Max:6.924",format="%0.15f")
        customer_log= st.number_input(label="**Enter the Value for CUSTOMER (Log Value)**/ Min:17.21910, Max:17.23015",format="%0.15f")
        thickness_log= st.number_input(label="**Enter the Value for THICKNESS (Log Value)**/ Min:-1.71479, Max:3.28154",format="%0.15f") 

    with col2:
        selling_price_log= st.number_input(label="**Enter the Value for SELLING PRICE (Log Value)**/ Min:5.97503, Max:7.39036",format="%0.15f")
        item_date_day= st.selectbox("**Select the Day for ITEM DATE**",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
        item_date_month= st.selectbox("**Select the Month for ITEM DATE**",("1","2","3","4","5","6","7","8","9","10","11","12"))
        item_date_year= st.selectbox("**Select the Year for ITEM DATE**",("2020","2021"))
        delivery_date_day= st.selectbox("**Select the Day for DELIVERY DATE**",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
        delivery_date_month= st.selectbox("**Select the Month for DELIVERY DATE**",("1","2","3","4","5","6","7","8","9","10","11","12"))
        delivery_date_year= st.selectbox("**Select the Year for DELIVERY DATE**",("2020","2021","2022"))

    button = st.button(":violet[***PREDICT THE STATUS***]", use_container_width=True)

    if button:
        status = predict_status(country, item_type, application, width, product_ref, quantity_tons_log,
                                customer_log, thickness_log, selling_price_log, item_date_day,
                                item_date_month, item_date_year, delivery_date_day, delivery_date_month,
                                delivery_date_year)

        if status == 1:
            st.write("## :green[**The Status is WON**]")
        else:
            st.write("## :red[**The Status is LOST**]")
            
# Predict Selling Price section
if SELECT == "PREDICT SELLING PRICE":
    st.header("**PREDICT SELLING PRICE**")
    st.write(" ")

    # Add custom CSS to style the font and input field colors
    st.markdown(
        """
        <style>
        /* Navy blue color for font */
        .st-ef {
            color: #000080 !important;
        }
        /* Light yellow color for input field */
        .st-at {
            background-color: #FFFFE0 !important;
        }
        /* Light yellow color for select input fields */
        .st-ah, .st-ai, .st-aj {
            background-color: #FFFFE0 !important;
        }
        </style>
        """
        , unsafe_allow_html=True
    )


    col1, col2 = st.columns(2)

    with col1:
        country= st.number_input(label="**Enter the Value for COUNTRY**/ Min:25.0, Max:113.0")
        status= st.number_input(label="**Enter the Value for STATUS**/ Min:0.0, Max:8.0")
        item_type= st.number_input(label="**Enter the Value for ITEM TYPE**/ Min:0.0, Max:6.0")
        application= st.number_input(label="**Enter the Value for APPLICATION**/ Min:2.0, Max:87.5")
        width= st.number_input(label="**Enter the Value for WIDTH**/ Min:700.0, Max:1980.0")
        product_ref= st.number_input(label="**Enter the Value for PRODUCT_REF**/ Min:611728, Max:1722207579")
        quantity_tons_log= st.number_input(label="**Enter the Value for QUANTITY_TONS (Log Value)**/ Min:-0.3223343801166147, Max:6.924734324081348",format="%0.15f")
        customer_log= st.number_input(label="**Enter the Value for CUSTOMER (Log Value)**/ Min:17.21910565821408, Max:17.230155364880137",format="%0.15f")
    
    with col2:
        thickness_log= st.number_input(label="**Enter the Value for THICKNESS (Log Value)**/ Min:-1.7147984280919266, Max:3.281543137578373",format="%0.15f")
        item_date_day= st.selectbox("**Select the Day for ITEM DATE**",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
        item_date_month= st.selectbox("**Select the Month for ITEM DATE**",("1","2","3","4","5","6","7","8","9","10","11","12"))
        item_date_year= st.selectbox("**Select the Year for ITEM DATE**",("2020","2021"))
        delivery_date_day= st.selectbox("**Select the Day for DELIVERY DATE**",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
        delivery_date_month= st.selectbox("**Select the Month for DELIVERY DATE**",("1","2","3","4","5","6","7","8","9","10","11","12"))
        delivery_date_year= st.selectbox("**Select the Year for DELIVERY DATE**",("2020","2021","2022"))

    button = st.button(":violet[***PREDICT THE SELLING PRICE***]", use_container_width=True)

    if button:
        price = predict_selling_price(country, status, item_type, application, width, product_ref, quantity_tons_log,
                                      customer_log, thickness_log, item_date_day,
                                      item_date_month, item_date_year, delivery_date_day, delivery_date_month,
                                      delivery_date_year)

        st.write("## :green[**The Selling Price is :**]", price)