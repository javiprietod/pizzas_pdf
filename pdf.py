from xhtml2pdf import pisa

#import PyPDF2, PyMuPDF


def report_block_template(image, height, caption=''):
    graph_block = (''
        f'<a href="{image}" target="_blank">'
            f'<img style="height: {height}px;" src="{image}">'
        '</a>')

    report_block = ('' + graph_block + '{caption}' + '<br>' + '<a href="{image}" style="color: rgb(190,190,190); text-decoration: none; font-weight: 200;" target="_blank">' + '</a>' + '<br>' + '<hr>')
    return report_block.format(image=image, caption=caption)

# Utility function
def convert_html_to_pdf(source_html, output_filename):
    # open output file for writing (truncated binary)
    file = open(output_filename, "wb")

    # convert HTML to PDF
    pisa.CreatePDF(source_html,dest=file)           
    file.close()                 
    return None

if "__main__" == __name__:
    report = """<h1 style="color: #2b2301;font-size: 100px; text-align: center;">MAVEN PIZZAS REPORT</h1>"""


    image = 'pizza.jpeg'
    report += report_block_template(image, 1600,caption='')

    images = ['Genoa Salami.png',
    'Kalamata Olives.png', 
    'Onions.png']
    
    report += '<h1 style="color: #2b2301;font-size: 50px; text-align: center;">Examples of ingredients</h1>'
    for image in images: 
        report += report_block_template(image, 1600,caption='')

    image = 'week_104.png'
    report += report_block_template(image, 1600,caption='')



    weekly_ing = open('weekly_ing.csv', 'r')
    weeks = weekly_ing.readlines()
    ings = weeks[0].replace('\n','').split(',')[1:]
    week104 = weeks[-1].replace('\n','').split(',')[1:]
    lista = {ings:week104 for ings, week104 in zip(ings, week104)}
    lista = sorted(lista.items(), key=lambda x: int(x[1]), reverse=True)
    ings = [i[0] for i in lista]
    week104 = [i[1] for i in lista]
    report += '<h1 style="color: #2b2301;font-size: 60px; text-align: center;">Quantity of ingredients to order</h1>'
    for i in range(len(ings)):
        report += f'<p style="color: #2b2301;font-size: 20px;">{ings[i]}: {week104[i]}</p>'

    
    convert_html_to_pdf(report, 'report.pdf')

