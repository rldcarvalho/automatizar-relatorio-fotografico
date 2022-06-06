from pdf_annotate import PdfAnnotator, Location, Appearance
from pdf_annotate.config.constants import TEXT_BASELINE_MIDDLE

a = PdfAnnotator('relatorio.pdf')

desvio_quadrado_x = 50
desvio_quadrado_y = 400
desvio_texto_x = 10
desvio_texto_y = 4

x_1 = 0 + desvio_quadrado_x
y_1 = 0 + desvio_quadrado_y
x_2 = 50 + desvio_quadrado_x
y_2 = 18 + desvio_quadrado_y

a.add_annotation(
    'square',
    Location(x1=x_1, y1=y_1, x2=x_2, y2=y_2, page=0),
    Appearance(stroke_color=(1, 0, 0), stroke_width=1.5),
)
a.add_annotation(
    'text',
    Location(x1=x_1 - desvio_texto_x, y1=y_1 - desvio_texto_y, x2=x_2 - desvio_texto_x, y2=y_2 - desvio_texto_y, page=0),
    Appearance(
        fill=[0, 0, 0],
        stroke_width=1,
        font_size=5,
        content="Coord. Inicial  \n99999:999999",
        text_baseline='top',
        text_align='right',
    ),
)
a.write('relatorio2.pdf')  # or use overwrite=True if you feel lucky


#********************************************************************************



########################################################

# from pdf_annotate import Appearance
# from pdf_annotate import Location
# from pdf_annotate import PdfAnnotator
# from pdf_annotate.config.constants import TEXT_BASELINE_BOTTOM
#
#
# path = 'relatorio.pdf'
#
# pdf_file = PdfAnnotator(path)
#
# # These are pixel coordinates with (0, 0) as bottom left.
# # Note PDF coordinates define (0, 0) as the top left, so you may have to perform a
# # transform depending on how you're getting these coordinates.
# x1_pixel, y1_pixel, x2_pixel, y2_pixel = 50, 50, 100, 100
#
# # This is the 0-indexed page index, not the 1-indexed page number
# page_idx = 0
#
# text_string = 'Coord: 999999:999999'
#
# pdf_file.add_annotation(
#             'text',
#             Location(x1=x1_pixel, y1=y2_pixel, x2=x2_pixel, y2=y2_pixel, page=page_idx),
#             Appearance(
#                 fill=(0, 0, 0),  # solid fill
#                 font_size=40,
#                 content=text_string,
#                 text_baseline=TEXT_BASELINE_BOTTOM,
#             ),
#         )
#
# out_path = 'relatorio2.pdf'
# pdf_file.write(out_path)

#################################################################