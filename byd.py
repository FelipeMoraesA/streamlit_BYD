import streamlit as st
import json
import urllib
import base64

st.set_page_config(
    page_title = 'Descubra a BYD',
    page_icon = 'https://www.byd.com.br/wp-content/uploads/2020/08/cropped-logo-BYD-new-2022-small-90x57.png',
    layout = 'wide'
)

def embed(link: str, h: str) -> str:
    return f'''
    <iframe 
        width="100%" height="{h}" src="https://www.youtube-nocookie.com/embed/{link}" 
        frameborder="0" allow="autoplay; 
        clipboard-write; encrypted-media; picture-in-picture; web-share" allowfullscreen>
    </iframe>
    '''

#function to display the PDF of a given file 
def displayPDF(file):
    # Opening file from file path. this is used to open the file from a website rather than local
    with urllib.request.urlopen(file) as f:
        base64_pdf = base64.b64encode(f.read()) # 

    # Embedding PDF in HTML
    return f'''
    <embed
        src="data:application/pdf;base64,{base64_pdf.decode('utf-8')}"
        width="100%" height="600", type="application/pdf">
    '''

css = '''
<style>
section.main > div:has(~ footer ) {
    padding-bottom: 0px;
}
</style>
'''
st.markdown(css, unsafe_allow_html=True)

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
            st.write(f'''Faz de 0 a 100 km/h em **{i['acceleration_0_100']}** segundos;''')
            st.write(f'''Autonomia de **{str(i['autonomy_km'])}km**;''')
            st.write(f'Possui **{i["colors"]}** cores disponíveis;')
            price = i['price']
            price_f = '{:,.2f}'.format(price).replace(',','*').replace('.', ',').replace('*', '.')
            st.write(f'Preço: **R$ {price_f}**.')
            url_img = i['url_img']
            url_pdf = i['pdf']
            url_video = i['video']

    pv_min = float(price * 0.2)
    
    pv = st.number_input('Entrada', 1, 10000, 50)
    n = st.slider('Nº de Parcelas', 1, 36, 12, 1)
    i = st.slider('Taxa de Juros', 0.1, 50.0, 1.0, 0.1, format = '%:.2f')
           
with c2:
    tab1, tab2, tab3 = st.tabs(['Imagem', 'Vídeo', 'Ficha Técnica'])

    with tab1:
        st.image(
            url_img, use_column_width = 'always',
            caption = 'Imagem meramente ilustrativa',
            width = 800
        )
    with tab2:
        st.markdown(
            embed(url_video, "600"), unsafe_allow_html = True
        )

    with tab3:
         st.link_button('Acesse o PDF', url_pdf)

st.write('---')
st.markdown(f'''
    <center>
        <a href="https://www.scielo.br/j/rbme/a/Z8PKY9Vrmf98Lhj8PhmMdcS/?lang=pt">
            Saiba os benefícios da spirulina
        </a>
    </center>''',
    unsafe_allow_html = True
)
