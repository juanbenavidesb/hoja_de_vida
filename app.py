import dash
from dash import html, dcc
import os
app = dash.Dash(__name__, assets_folder='assets')

app.layout = html.Div([
    html.Div([
        html.Div([
            html.Img(src='/assets/profile.jpg', className="profile-image"),
            html.H2("PERFIL PROFESIONAL", className="section-title"),
            html.P("Soy estudiante de VI semestre de ciencia de datos, con conocimientos en: Programación, análisis de datos, minería de datos y Machine Learning. Destaco mi pasión por el aprendizaje continuo, el análisis y la interpretación de datos para identificar y resolver problemas"),
            html.H2("CONTACTO", className="section-title"),
            html.Ul([
                html.Li([
                    html.I(className="fas fa-envelope"),
                    html.Span("juanbenavidesb@hotmail.com", className="contact-text")
                ]),
                html.Li([
                    html.I(className="fas fa-phone"),
                    html.Span(" (+57) 312- 4239977", className="contact-text")
                ]),

                html.Li([
                    html.I(className="fas fa-map-marker-alt"),
                    html.Span(" cra 79 #19-20 ", className="contact-text")
                ]),
            ], className="contact-list"),
            html.H2("HABILIDADES", className="section-title"),
            html.Ul([
                html.Li("manejo de python"),
                html.Li("manejo de R"),
                html.Li("Machine Learning"),
                html.Li("Habilidades analíticas"),
                html.Li("Visualización de datos"),
                html.Li("Mineria de datos"),
            ], className="skills-list"),
        ], className="left-column"),
        html.Div([
            html.H1("Juan Andrés Benavides Beltrán", className="name"),
            html.H2("Científico de datos", className="job-title"),
            html.Div([
                html.H2("EXPERIENCIA LABORAL", className="section-title"),
                html.Div([
                    html.H3("Universidad Externado de Colombia"),
                    html.P("Enero 2023 - Nomviembre 2023"),
                    html.P("Monitor Matemáticas discretas", className="job-position"),
                    html.Ul([
                        html.Li("Como monitor, oriente a los estudiantes de ciencia de datos, de semestres anteriores en los distintos temas de la materia de matemáticas discretas."),
                    ]),
                ], className="job-entry"),
            ]),
            html.Div([
                html.H2("Estudios académicos", className="section-title"),
                html.Div([
                    html.P("2011-2021"),
                    html.H3("Bachiller"),
                    html.P("Colegio Santa Ana de Fontibón"),
                ], className="education-entry"),
                html.Div([
                    html.P("2022-2026 (Actualmente)"),
                    html.H3("Pregrado en Ciencia de datos"),
                    html.P("Universidad Externado de Colombia"),
                ], className="education-entry"),
                html.Div([
                    html.P("2022"),
                    html.H3(" Curso de programación avanzada en python"),
                    html.P("Platzi"),
                ], className="education-entry"),
                html.Div([
                    html.P("2022"),
                    html.H3(" Curso programación orientada a objetos en python"),
                    html.P("Platzi"),
                ], className="education-entry"),
            ]),
            html.Div([
                html.H2("TRABAJOS", className="section-title"),
                html.Div([
                    html.P("Puedes ver uno de mis trabajos publicados en el siguiente enlace:"),
                    html.A("Trabajo Publicado", href="https://app.powerbi.com/view?r=eyJrIjoiNDQyNWM1YmQtN2JhMS00MTk0LWFmNzAtMTQ5NjM4ODVjODA3IiwidCI6IjNiOTQ0ZDlhLTEwNTEtNDY4NS1iMDlkLTlhOTVlZTJkYmQ5OSIsImMiOjR9", className="work-link"),
                ], className="work-entry"),
            ]),
        ], className="right-column"),
    ], className="resume-container"),
], className="page-container")

if __name__ == '__main__':
    app.run_server(debug=True)


