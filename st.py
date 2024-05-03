import streamlit as st    

st.title('iris predictions')

st.write('iris data predictions')

sl=st.number_input('enter the sepal lemgth value')
sw=st.number_input('enter the sepal width value')
pl=st.number_input('enter the petal length value')
pw=st.number_input('enter the petal width value')

if st.button('predict'):

    with open('iris_model.pkl','rb')as model:
        main_model=pickle.load(model)

        datas=[[sl,sw,pl,pw]]

        preds=main_model.predict(datas)

        st.wrtie(f'the predicted value is {preds}')