import streamlit as st
import pickle
import pandas as pd


new_df = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))



def recommend(movie):
    movie=movie.lower()
    index = new_df[new_df['title'].str.lower() == movie].index[0]

    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies=[]
    for i in movies_list:
        recommend_movies.append(new_df.iloc[i[0]].title)
    return recommend_movies
    
st.title('Movie Recommendation System')

Select_Movie_Name=st.selectbox(
    'Choose a Movie',new_df['title'].values)


if st.button('Recommend'):
   recommendations=recommend(Select_Movie_Name)
   for i in recommendations:
       st.write(i)
                          
                        
                    
                          
                         
