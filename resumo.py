import pandas as pd
import streamlit as st
from datetime import datetime
import plotly.express as px


class Resumo:
    # Construtor da classe ler os dados
    def __init__(self):
        self.df = pd.read_csv('assets\Cursos - Página1.csv')



    # Função para criar um gráfico de barras
    def bar_chart(self):
        self.df = self.df['Nome do Curso'].value_counts()
        st.bar_chart(self.df)

    # Função para criar um gráfico de pizza
    def pie_chart(self):
        self.df = self.df.sort_values(by="Quantidade", ascending=False)
        self.df = self.df.head(10)
        st.write(self.df["Quantidade"].plot.pie(autopct="%1.1f%%"))

    # Função para criar um gráfico de linha

    def line_chart(self):
        self.df = self.df.sort_values(by="Quantidade", ascending=False)
        self.df = self.df.head(10)
        st.line_chart(self.df["Quantidade"])

    def big_number_courses(self):
        quantidade_de_cursos = self.df.shape[0]  # Conta o número de linhas no DataFrame
        titulo = "Cursos"
        
        # Estilização CSS para o card



        card_style = """
                background-color: TRANSPARENT;
                border-radius: 10px;
                border: 1px solid;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
                font-family: 'Arial', sans-serif;
                text-align: center;
                align-items: center;
                justify-content: center;
                display: flex;
                flex-direction: column;
                font-size: 15px;
                height: 120px;
            """
        h1_style = """font-size: 18px;
                    color: #fff;
                    margin: 0;
                    margin-top: 15px;
                    padding: 0;
        """


        # Aplicando o estilo CSS ao card
        st.markdown(f"""<div style="{card_style}">
                        <h1 style="{h1_style}">{titulo}</h1>
                        <h2>{quantidade_de_cursos}</h2>
                </div>""", unsafe_allow_html=True) 
        

    def big_number_work(self):
        data_inicio = "01/08/2017"
        data_presente = datetime.now().strftime("%d/%m/%Y")

        data_inicio = datetime.strptime(data_inicio, "%d/%m/%Y")
        data_presente = datetime.strptime(data_presente, "%d/%m/%Y")

        tempo_carreira = data_presente - data_inicio

        anos_completos = tempo_carreira.days // 365
        meses_restantes = (tempo_carreira.days % 365) // 30

        tempo_carreira = f"{anos_completos} anos"
        

        titulo = "Tempo de Carreira"
        
        # Estilização CSS para o card



        card_style = """
                background-color: TRANSPARENT;
                border-radius: 10px;
                border: 1px solid;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
                font-family: 'Arial', sans-serif;
                text-align: center;
                align-items: center;
                justify-content: center;
                display: flex;
                flex-direction: column;
                font-size: 15px;
                height: 120px;
            """
        h1_style = """font-size: 18px;
                    color: #fff;
                    margin: 0;
                    margin-top: 15px;
                    padding: 0;
        """


        # Aplicando o estilo CSS ao card
        st.markdown(f"""<div style="{card_style}">
                        <h1 style="{h1_style}">{titulo}</h1>
                        <h2>{tempo_carreira}</h2>
                </div>""", unsafe_allow_html=True) 
        
    def big_number_companies(self):
        companies = 2
        
        
        # Estilização CSS para o card

        titulo = "Empresas"

        card_style = """
                background-color: TRANSPARENT;
                border-radius: 10px;
                border: 1px solid;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
                font-family: 'Arial', sans-serif;
                text-align: center;
                align-items: center;
                justify-content: center;
                display: flex;
                flex-direction: column;
                font-size: 15px;
                height: 120px;
            """
        h1_style = """font-size: 18px;
                    color: #fff;
                    margin: 0;
                    margin-top: 15px;
                    padding: 0;
        """


        # Aplicando o estilo CSS ao card
        st.markdown(f"""<div style="{card_style}">
                        <h1 style="{h1_style}">{titulo}</h1>
                        <h2>{companies}</h2>
                </div>""", unsafe_allow_html=True) 
        

    def big_number_institu(self):
        instituicoes = self.df['Instituição'].nunique() + 1
        
        
        # Estilização CSS para o card

        titulo = "Inst. Ensino"

        card_style = """
                background-color: TRANSPARENT;
                border-radius: 10px;
                border: 1px solid;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
                font-family: 'Arial', sans-serif;
                text-align: center;
                align-items: center;
                justify-content: center;
                display: flex;
                flex-direction: column;
                font-size: 15px;
                height: 120px;
            """
        h1_style = """font-size: 18px;
                    color: #fff;
                    margin: 0;
                    margin-top: 15px;
                    padding: 0;
        """


        # Aplicando o estilo CSS ao card
        st.markdown(f"""<div style="{card_style}">
                        <h1 style="{h1_style}">{titulo}</h1>
                        <h2>{instituicoes}</h2>
                </div>""", unsafe_allow_html=True) 
        
    def bar_chart_areacourses(self):
        area_courses = self.df['Área do Curso'].value_counts()
        area_courses = area_courses.sort_values(ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)

        
        st.plotly_chart(px.bar(area_courses, orientation='h', title='Áreas com mais cursos', labels={'value':'','Área do Curso':''}), use_container_width=True,)

    def bar_chart_areatools(self):
        


        area_courses = self.df['Ferramenta'].value_counts()
        area_courses = area_courses.groupby('Ferramenta').sum()

        #ordenar por quantidade de cursos
        area_courses = area_courses.sort_values(ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)





        
        st.plotly_chart(px.bar(area_courses, orientation='h', title='Ferramentas com mais cursos', labels={'value':'', 'Ferramenta':""}), use_container_width=True,)

                    
                
            
        

    

