import streamlit as st
import requests
from amzqr import amzqr


# Configuración de la página
st.set_page_config(
    page_title="Generador de QR con Amazing-QR",
    page_icon=":frame_with_picture:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.linkedin.com/in/estebansantillansuarez'
    }
)


# Pie de página
st.sidebar.image("foto/mi_foto.png", caption = "Esteban Santillan")

st.sidebar.markdown("---")

# Título en la barra lateral
st.sidebar.title('Mis cuentas')

# Desplegable con el título "Mis cuentas"
with st.sidebar.expander("Ver cuentas"):
    # Agregar enlaces a tu cuenta de Git y LinkedIn
    st.markdown("[Github](https://github.com/Esteban-S-S)")
    st.markdown("[Linkedin](https://www.linkedin.com/in/estebansantillansuarez/)")

st.sidebar.write(
    """He realizado el presente trabajo con el fin de aprender a usar streamlit 
        ya que lo considero una herramienta muy buena para realizar informes y 
        algunas aplicaciones."""
)

st.sidebar.write("""El presente generador de códigos QR fue realizado
                    con la librería [amzqr](https://github.com/x-hw/amazing-qr/tree/master) 
                    la cual se encuentra habilitada para uso libre.
                 """
)


# Título y descrpción de la página
st.header("Generador de código QR", divider='rainbow')
st.markdown("""¡Bienvenido al generador de códigos QR! Puedes generar tu código QR 
            con la imagen o gif que quieras, puede ser de una empresa, una foto tuya, 
            la de tu mascota, ¡una foto tuya con tu mascota! y mucho mas.""")
#Ejemplos
st.write("<h1 style='font-size: 24px;'>¡Mira estos ejemplos!</h1>", unsafe_allow_html=True)
columna1, columna2, columna3, columna4, columna5 = st.columns(5)
with columna1:
    st.image("ejemplos/ave_color.gif", caption="Ejemplo1")
with columna2:
    st.image("ejemplos/CódigoQR_perro_blancoynegro.png", caption="Ejemplo2")
with columna3:
    st.image("ejemplos/codigo_qr_basico.png", caption="Ejemplo3")
with columna4:
    st.image("ejemplos/ave_blancoynegro.gif", caption="Ejemplo4")
with columna5:
    st.image("ejemplos/perro_color.png", caption="Ejemplo5")



st.header("Genera tu código QR", divider='orange')

st.markdown("Generar tu propio codigo QR es muy fácil:")

st.markdown(":large_orange_circle: Sólo completando el espacio del enlace \
            al que te quieres dirigir generas un QR simple")

st.markdown(':large_yellow_circle: Para tener una imagen o gif de fondo puedes arrastrar el \
            archivo hacia el sector marcado por este punto o seleccionas donde dice "Browse files" \
            para buscar la imagen o gif que deseas agregar a tu codigo QR')

st.markdown(":large_purple_circle: También puedes escribir la direción web de la imagen \
             o gif que quieres tener de fondo")

st.markdown("Nota: Si pones una imagen o o gif sin completar el espacio de la dirección \
            web a la que quieres que el usuario se dirija al escanear el codigo QR, \
            al escanearlo obtendras un mensaje en blanco.")



"""___"""



intro1, intro2 = st.columns(2)

with intro1:
    words = st.text_input(":large_orange_circle: Introduce el enlace al que te quieres ditigir",
                          value = None,
                          placeholder = "https://www.direccion-qr.com",
                          help = """puedes escrib un enlace o simplemente un mensaje. 
                          Te muestro algunos ejemplos: 
                          www.google.com
                          www.duckduckgo.com""")

    
                                
    archivo_cargado = st.file_uploader(":large_yellow_circle: Cargar imagen", type=["jpg", "png", "jpeg", "gif"],
                                       help = """Puedes arrastrar tu imagen o gif aquí o agregarlo dando clic en Browse files""")
    

with intro2:
    
    
    url = st.text_input(":large_purple_circle: introduce el enlace a la :red[imagen] o :red[gif] que quieres \
                        tener de fondo",
                          value = None,
                          placeholder = "https://www.example.com/imagen.jpg",
                          help = """Si no encuentra la imagen o no está entre sus opciones no hace nada,
                            te muestro algunos ejemplos: 
                            #IMAGEN: https://i.pinimg.com/originals/1e/99/e2/1e99e24268d9c473fbdbc241b34ae809.gif
                            #GIF: https://media.istockphoto.com/id/1333497883/es/vector/vector-simple-isolated-dog-icon.jpg?s=612x612&w=0&k=20&c=5Q14i_qVFy6mxZT0-txNjsXrr4LdrNoUYecrxD7XZBs=
                            """)
agregado = "                                                                        "
if words == None:
    words = agregado #es para que de no ser completado el espacio dé un QR grande, al menos por un tiempo hasta que estudie mas y pueda editar esto en la librería
                    #no he dejado el valor de la variable value por defecto porque no muestra lo que han en la variable placeholder

"___"
# Espacio de edición QR
esp1, esp2 = st.columns(2)
colorized = True
with esp2:
     st.header(" Espacio de edición QR", divider = 'orange')
     edit_1, edit_2 = st.columns(2)
     with edit_1:
          contrast = st.slider("Contraste", 0.0, 2.0, 1.0, 0.1)
          brightness = st.slider("Brillo", 0.0, 2.0, 1.0, 0.1)
          if st.button("Color"):
                colorized = True
          if st.button("Blanco y Negro"):
                colorized = False

with esp1:
    st.header(":arrow_down_small: QR generado", divider = 'orange')
    try:
        try:
            response = requests.get(url)
            value_response = response.status_code

        except:
            value_response = None
        

        if archivo_cargado != None: 
            if (".jpg" in archivo_cargado.name) or \
                (".png" in archivo_cargado.name) or \
                (".jpeg" in archivo_cargado.name): #.bmp
                archivo_gif_img = "imagen_cargada_streamlit.png"
                descarga_img_gif = "CódigoQR.png"

                with open(archivo_gif_img, "wb") as archivo:
                    archivo.write(archivo_cargado.getvalue())
                
                result = "codigo_qr_personalizado.png"


            elif ".gif" in archivo_cargado.name:
                print("esgif")
                archivo_gif_img = "gif_cargado_streamlit.gif"
                descarga_img_gif = "CódigoQR.gif"

                with open(archivo_gif_img, "wb") as archivo:
                    archivo.write(archivo_cargado.getvalue())

                result = "codigo_qr_personalizado.gif"
                
            version, level, qr_name = amzqr.run(
                    words,
                    version=1,
                    level='H',
                    picture=archivo_gif_img,
                    colorized = colorized,
                    contrast=contrast,
                    brightness=brightness,
                    save_name=result,
                )
                    
            st.image(result, caption="Código QR generado", use_column_width = True)
            # Botón de descarga
            with st.spinner("Generando código QR..."):
                st.download_button("Descargar código QR",
                                    open(result, 'rb').read(),
                                          descarga_img_gif)
            

        elif value_response == 200:

            if (".jpg" in url) or (".png" in url) or (".jpeg" in url): #.bmp
                img_or_gif = "nueva_imagen.png"
                descarga_img_gif = "CódigoQR.png"
                with open(img_or_gif, 'wb') as archivo:
                    archivo.write(response.content)
                result = "codigo_qr_personalizado.png"
                print("imagen descargada exitosamente como", img_or_gif)


            elif ".gif" in url:
                img_or_gif = "nuevo_gif.gif"
                descarga_img_gif = "CódigoQR.gif"
                with open(img_or_gif, 'wb') as archivo:
                    archivo.write(response.content)
                result = "codigo_qr_personalizado.gif"
                print("GIF descargado exitosamente como", img_or_gif)
            
            version, level, qr_name = amzqr.run(
                    words,
                    version=1,
                    level='H',
                    picture=img_or_gif,
                    colorized = colorized,
                    contrast=contrast,
                    brightness=brightness,
                    save_name=result,
                )
            
            st.image(result, caption="Código QR generado", use_column_width = True)
            # Botón de descarga
            with st.spinner("Generando código QR..."):
                st.download_button("Descargar código QR",
                                    open(result, 'rb').read(),
                                          descarga_img_gif)
        
        elif words != agregado:
                     
            result = "codigo_qr_personalizado.png"

            version, level, qr_name = amzqr.run(
                    words,
                    version=1,
                    level='H',
                    picture=None,
                    colorized = colorized,
                    contrast=contrast,
                    brightness=brightness,
                    save_name=result,
                )
            st.image(result, caption="Código QR generado", use_column_width = True)
            # Botón de descarga
            with st.spinner("Generando código QR..."):
                st.download_button("Descargar código QR", 
                                   open(result, 'rb').read(), 
                                    "CódigoQR.png")
        
    except Exception as e:
        print(e)



 