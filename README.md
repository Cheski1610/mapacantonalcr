# MapaCantonal

![Mapa Cantonal Costa Rica](https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Mapa_de_Costa_Rica_%28cantones_y_distritos%29.svg/666px-Mapa_de_Costa_Rica_%28cantones_y_distritos%29.svg.png)

La segmentación de la información geográficamente puede beneficiar a las organizaciones para:
 - Obtener un mayor entendimiento del mercado. 
 - Segmentar los clientes para el establecimiento de estrategias focalizadas.
 - Optimizar la Cadena de Suministros al entender la ubicación de los proveedores, la distribución de los centros de fabricación y la demanda de productos en diferentes regiones.
 - Administrar los riesgos al poder gestionar y mitigar por zonas de manera proactiva posibles amenazas a sus operaciones. 

En la actualidad, existen muchas opciones en el mercado, tanto de pago como de código libre, para graficar mapas y visualizaciones geográficas, lo que facilita la interpretación de la información. Una de estas opciones es [Pydeck](https://deckgl.readthedocs.io/en/latest/index.html#), librería de Python que permite de forma sencilla ilustrar la información geográficamente. En este notebook de Google Colab se puede interactuar un poco y entender como funciona esta librería: [Uso_Pydeck_&_Geopy](https://colab.research.google.com/drive/1bAZ2rdfPUX3WJNDH4Q1FRh6hTr_yJORa?usp=sharing)

Costa Rica cuenta con un total de 84 cantones (2023). Visualizar la información económica de cada uno es relevante para determinar políticas de desarrollo y gestionar la distribución de recursos.

En este repositorio se pone a disposición lo necesario para la generación de una app en [Azure](https://azure.microsoft.com/es-es/free/search/) que muestra algunos indicadores económicos y geográficos de los cantones de Costa Rica.

### Fuentes información cantonal:
- [https://app.powerbi.com/view?r=eyJrIjoiZDNlZmE0OWMtMTBjOS00MWYyLWFjMjgtYTFjZjBkYWI5MmEyIiwidCI6ImU3OTg0Y2FjLTI1NDMtNGY4OC04Zjk3LTk1MjQzMzVlNmJjNCIsImMiOjR9](https://app.powerbi.com/view?r=eyJrIjoiZDNlZmE0OWMtMTBjOS00MWYyLWFjMjgtYTFjZjBkYWI5MmEyIiwidCI6ImU3OTg0Y2FjLTI1NDMtNGY4OC04Zjk3LTk1MjQzMzVlNmJjNCIsImMiOjR9)
- [https://inec.cr/mapas-cartografia/densidad-poblacion-canton?variable=705&year=2021](https://inec.cr/mapas-cartografia/densidad-poblacion-canton?variable=705&year=2021)
- [https://app.powerbi.com/view?r=eyJrIjoiMDU2ZDNiMjgtNGQ1YS00NjBhLWJlODktY2E4NTkyMjAyZTg0IiwidCI6IjYxOGQwYTQ1LTI1YTYtNDYxOC05ZjgwLThmNzBhNDM1ZWU1MiJ9](https://app.powerbi.com/view?r=eyJrIjoiMDU2ZDNiMjgtNGQ1YS00NjBhLWJlODktY2E4NTkyMjAyZTg0IiwidCI6IjYxOGQwYTQ1LTI1YTYtNDYxOC05ZjgwLThmNzBhNDM1ZWU1MiJ9)