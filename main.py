# titulo
# input do chat
# o que fazer a cada mensagem:
    # mostrar a mensagem que o usuario enviar
    # pegar a pergunta e enviar para uma IA responder
    # exibir a respota da IA na tela

# Vamos usar:
    # Streamlit
    # IA da OpenAI
    # Para instalar usar o comando 'pip install streamlit openai'dentro do terminal

import streamlit as st
from openai import OpenAI


modelo_ia = OpenAI(api_key=st.secrets['api_key'])


# Usar # para criar titulo
st.write('# Projeto Chatbot')

#Lista de mensagens
if not 'lista_mensagens' in st.session_state:

    st.session_state['lista_mensagens'] = []


#Campo para enviar a mensagem
texto_usuario = st.chat_input('Digite sua mensagem') 

for mensagem in st.session_state['lista_mensagens']:
    role = mensagem['role']
    content = mensagem['content']
    st.chat_message(role).write(content)

if texto_usuario:
    st.chat_message('user').write(texto_usuario)
    mensagem_usuario = {'role':'user', 'content':texto_usuario}
    st.session_state['lista_mensagens'].append(mensagem_usuario)

    #Resposta da IA
    resposta_ia = modelo_ia.chat.completions.create(
        messages= st.session_state['lista_mensagens'],
        model= 'gpt-4o'
    )
    
    texto_resposta_ia = resposta_ia.choices[0].message.content

    st.chat_message('assistant').write(texto_resposta_ia)
    mensagem_ia = {'role':'assistant', 'content':texto_resposta_ia}
    st.session_state['lista_mensagens'].append(mensagem_ia)



 
