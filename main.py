import streamlit as st
import time

st.title('Streamlit 入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!'


left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if  button:
     right_column.write('ここは右カラム')

expander1 = st.beta_expander('問い合わせ')
expander1.write('問い合わせ1')

# text = st.text_input('あなたの趣味を教えてください。')
# condition = st.slider('あなたの今の調子は？',0,100,50)

# 'あなたの趣味：',text
# 'コンディション',condition





