
import streamlit as st
import json

st.set_page_config(
    page_title = 'Descubra a BYD',
    page_icon = 'https://www.byd.com.br/wp-content/uploads/2020/08/cropped-logo-BYD-new-2022-small-90x57.png',
    layout = 'wide'
)

st.title('Do you love BYD?')
st.write('Conheca as características de cada veículo')

c1, c2 = st.columns([1, 2])

with c1:
    model = st.selectbox(
        label = 'Escolha um Modelo:',
        options = ['BYD SEAL', 'BYD DOLPHIN', 'BYD YUAN PLUS', 'BYD SONG PLUS', 'BYD TAN', 'BYD HAN']
    )

    with open('byd.json', 'r') as arquivo_json:
        dados = json.load(arquivo_json)

    for i in dados:
        if i['car'] == model.lower():
            st.write(f'Modelo da linha "**{i["line"]}**", sua propulsão e **{i["prop"]}**;')
            st.write(f'Faz de 0 a 100 km/h em **{i["acceleration_0_100"]}** segundos;')
            st.write(f'Possui **{i["colors"]}** cores disponíveis;')
            price = i['price']
            price = '{:,.2f}'.format(price).replace(',','*').replace('.', ',').replace('*', '.')
            st.write(f'Preço: **R$ {price}**.')
            url_img = i['url_img']
            url_pdf = i['pdf']
    
    # st.write(f'Veja a ficha completa em [pdf]({url_pdf}).')

    st.link_button('Veja a ficha completa', url_pdf)
    
with c2:
    tab1, tab2, tab3 = st.tabs(['Imagem', 'Vídeo', 'Ficha Técnica'])

    with tab1:
        st.image(
            url_img, 
            caption = 'Imagem meramente ilustrativa',
            width = 800
        )
    

st.write('---')
st.markdown(f''''<center>{'{:-^100}'.format('Saiba os benefícios da spirulina clicando [AQUI](https://www.scielo.br/j/rbme/a/Z8PKY9Vrmf98Lhj8PhmMdcS/?lang=pt)')}</center>''', unsafe_allow_html = True)