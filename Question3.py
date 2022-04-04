import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(layout = 'wide')

st.title("Question 3")
variable = ['Credit_Card_Exceed_Months',	'Loan_Amount'	,'Loan_Tenure_Year','Credit_Card_More_Than_Months',	'Number_of_Dependents',	'Years_to_Financial_Freedom',	'Number_of_Credit_Card_Facility',	'Number_of_Properties'	,'Number_of_Bank_Products'	,'Number_of_Loan_to_Approve'	,'Years_for_Property_to_Completion'	,'Number_of_Side_Income',	'Monthly_Salary',	'Total_Sum_of_Loan',	'Total_Income_for_Join_Application'	,'Score']
mean = [4.723404,448350.120851,17.053191,2.12766,3.12766,13.382979,3.744681,2.382979,2.106383,1.991915,10.659574,2.020426,7972.040000,9.435756e+05,13767.859574,7.496596]
min = [1,100194,10	,1,	2,	5	,2	,2	,1,	1,	10,	1,	3583,	4.202390e+05,	7523,	6]
max = [7,799628,24,	5,	6,	19,	6,	5,	5	,3,	13,	3,	12562,	1.449960e+06,	19995,	9]
finalResult = ['best of three model']
ClusteringScore = [0.8702705486262635,0.90860047518049,0.931204640481955]
NBScore = [0.7416413373860182,0.7574468085106383]
DecisionScore = [0.7673758865248227,0.6312056737588653,0.624113475177305]
st.header('Mean')
for i in range(len(variable)):
    st.write("Mean of ", variable[i] , ": " , mean[i])

st.header('Min')
for i in range(len(variable)):
    st.write("Max of ", variable[i] , ": " , min[i])

st.header('Max')
for i in range(len(variable)):
    st.write("Max of ", variable[i] , ": " , max[i])

st.header('Relationship between Variable')
st.image('Relationship.png', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
st.image('Relationship2.png', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.title("KMeans")
states = st.selectbox("Select K number:", [2, 3,4])

button = st.button("Click Here to Generate Result")
if(button):
    st.write("Silhouette Score = ", ClusteringScore[int(states)-2])# calculate the score
    st.image(str(states)+'Cluster'+'.png', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.image('Silhouette'+str(states)+'.png', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.header('Elbow Method')
st.image('Elbow.png', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.title("Decision Tree")
states2 = st.selectbox("Select Max Depth number:", [2, 20,'Default'])

button2 = st.button("Click Here")
if(button2):
    if (str(states2) == '2'):
        st.write("Score = ", DecisionScore[0])
        st.image('DecisionTree2.png', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

    elif (str(states2) == '20'):
        st.write("Score = ", DecisionScore[1])
        st.image('DecisionTree20.png', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

    else:
        st.write("Score = ", DecisionScore[2])
        st.image('DecisionTreeNotSpecify.png', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")


st.title("GaussianNB")
st.write("Result for training dataset: ",0.7416413373860182)
st.write("Result for testing dataset: ",0.7574468085106383)
st.write('Gap between training and testing is: ',0.0158054711246201)

st.title('Recommendation and Conclusion')
st.write("From my opinion, KMeans model is suitable for this questions as:")
st.write("- It can cluster a large or growing system rapidly ")
st.write("- It get the highest result compare to other model ")
st.write("- Easily adapts to new examples ")
st.write("- Although the number of cluster is quite random, but it can be determine by using elbow method")
