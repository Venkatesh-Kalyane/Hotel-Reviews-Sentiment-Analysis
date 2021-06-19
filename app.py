import pickle
import streamlit as st

# loading the trained model
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

def predict_hotel_review(description):
    description= [description]
    prediction= classifier.predict(description)
    return prediction

def main():

    html_temp = """ 
    <div style ="background-color:tomato;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Hotel Review Sentiment Analysis ML App</h1> 
    </div> 
    """

    st.markdown(html_temp, unsafe_allow_html=True)

    description= st.text_area("description", "Enter Review")
    result=""

    if st.button("Predict"):
        result= predict_hotel_review(description)

    st.success('The output is {}'.format(result))

    if st.button("About"):
        st.text("Lets Learn....")
        st.text("App Built By Venkatesh Kalyane")

if __name__ == '__main__':
    main()


