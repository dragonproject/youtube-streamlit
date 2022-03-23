# イントロ
# Streamlitの準備
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
# Streamlitの基本的な使い方
# タイトルの追加
st.title('Streamlit 超入門')

"""
#### Dataframe
"""
st.write('データフレーム')


df = pd.DataFrame({
    '1column': [1, 2, 3, 4],
    '2column': [10, 20, 30, 40]
}
)

# データフレーム（表） の使い方
st.dataframe(df.style.highlight_max(axis=0))

st.table(df.style.highlight_max(axis=0))

# マジックコマンドを使用
"""
# 1章
## 1節
### 1項


```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

df2 = pd.DataFrame(
    np.random.randn(100, 2)/[200, 200] + [35.69, 139.70],
    columns=['lat', 'lon']
)
# チャートを描く
# st.write(df)
# st.dataframe(df.style.highlight_max(axis=0), width=200, height=200)
st.write(df2)
# st.line_chart(df2)
# st.area_chart(df2)
# st.bar_chart(df2)

# マップをプロット
"""
#### Image Mapping
"""
st.map(df2)


# 画像を表示
st.write('Display Image')


# インタラクティブなウィジェット
"""
#### Display Image
"""
# チェックボックスによるメディアの表示可否
if st.checkbox('Show Image'):
    img = Image.open('./mqdefault.jpg')
    st.image(img, caption='Kohei Imanishi', use_column_width=True)

"""
#### Interactive Widgets
"""
# セレクトボックスによる値の動的変更
option = st.selectbox(
    'あなたが好きな数字を教えてください。',
    list(range(1, 11))
)

'あなたの好きな数字は', option, 'です。'
# st.write('あなたの好きな数字は', option, 'です。')


# レイアウトを整える
# サイドバーを追加
st.sidebar.write('Interactive Widgets')
# スライダーによる値の動的変更
"""
###### ライダーによる値の動的変更
"""
# テキスト入力による値の動的変更
"""
###### テキスト入力による値の動的変更
"""
text = st.sidebar.text_input('あなたの趣味を教えてください。')
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
'あなたの趣味：', text
'コンディション：', condition

# 2カラムレイアウトにする
left_column, right_column = st.columns(2)

button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

# プログレスバーの表示
st.write('プログレスバーの表示')
'Start!!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i +1)
    time.sleep(0.1)

"Done!"

# expanderの追加
expander = st.expander('問い合わせ')
expander.write('お問合せ内容を書く')


# Webアプリの公開
