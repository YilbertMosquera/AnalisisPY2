def crearTaba(dataFrame,nombreTabla):
    archivoHTML = dataFrame.to_html()
    archivo = open(f"./table/{nombreTabla}.html","w")
    archivo.write('''
            <html>
                <head>
                    <titles>tabla aire></title>
                </head>
                <body>
                 ''')
    archivo.write(archivoHTML)   
    archivo.write(
                        '''
                </body>
            </html>
        ''')