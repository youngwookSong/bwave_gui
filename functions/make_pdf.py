from PIL import Image, ImageFont, ImageDraw
from fpdf import FPDF
import os
import personal_data.resources as personal_res
from pdf_data import *

font_size = 15
font = ImageFont.load_default()


def png_save(seletedData):
    data_root = os.path.join(personal_res.root, "{}".format(seletedData))  # 절대 경로

    ###### main page ########

    ###### mdd detail page ########
    mdd_detail = Image.open('./pdf_base_file/mdd_detail_base.png')

    psd_detail_0 = Image.open(os.path.join(data_root, 'psd_detail_0.png'))
    psd_detail_0 = psd_detail_0.resize((180,180))
    psd_detail_1 = Image.open(os.path.join(data_root, 'psd_detail_1.png'))
    psd_detail_1 = psd_detail_1.resize((180, 180))
    psd_detail_2 = Image.open(os.path.join(data_root, 'psd_detail_2.png'))
    psd_detail_2 = psd_detail_2.resize((180, 180))
    plv_detail_0 = Image.open(os.path.join(data_root, 'plv_detail_0.png'))
    plv_detail_0 = plv_detail_0.resize((180, 180))
    plv_detail_1 = Image.open(os.path.join(data_root, 'plv_detail_1.png'))
    plv_detail_1 = plv_detail_1.resize((180, 180))
    plv_detail_2 = Image.open(os.path.join(data_root, 'plv_detail_2.png'))
    plv_detail_2 = plv_detail_2.resize((180, 180))
    ni_detail_0 = Image.open(os.path.join(data_root, 'ni_detail_0.png'))
    ni_detail_0 = ni_detail_0.resize((180, 180))
    ni_detail_1 = Image.open(os.path.join(data_root, 'ni_detail_1.png'))
    ni_detail_1 = ni_detail_1.resize((180, 180))
    ni_detail_2 = Image.open(os.path.join(data_root, 'ni_detail_2.png'))
    ni_detail_2 = ni_detail_2.resize((180, 180))

    mdd_detail.paste(psd_detail_0, (95, 280))
    mdd_detail.paste(psd_detail_1, (290, 280))
    mdd_detail.paste(psd_detail_2, (485, 280))
    mdd_detail.paste(plv_detail_0, (95, 515))
    mdd_detail.paste(plv_detail_1, (290, 515))
    mdd_detail.paste(plv_detail_2, (485, 515))
    mdd_detail.paste(ni_detail_0, (95, 775))
    mdd_detail.paste(ni_detail_1, (290, 775))
    mdd_detail.paste(ni_detail_2, (485, 775))
    mdd_detail.save(os.path.join(data_root, 'mdd_detail.png'))

    ###### sensor detail page ########

    ###### frequency page ########
    frequency_1 = Image.open('./pdf_base_file/base.png')
    frequency_1.paste(Image.open(os.path.join(data_root, 'frequency/frequency_abs_1.png')), (-30, 178))
    frequency_1.save(os.path.join(data_root, 'frequency_1.png'))

    frequency_2 = Image.open('./pdf_base_file/base.png')
    frequency_2.paste(Image.open(os.path.join(data_root, 'frequency/frequency_abs_2.png')), (-30, 178))
    frequency_2.save(os.path.join(data_root, 'frequency_2.png'))

    frequency_3 = Image.open('./pdf_base_file/base.png')
    frequency_3.paste(Image.open(os.path.join(data_root, 'frequency/frequency_rel_1.png')), (-30, 178))
    frequency_3.save(os.path.join(data_root, 'frequency_3.png'))

    frequency_4 = Image.open('./pdf_base_file/base.png')
    frequency_4.paste(Image.open(os.path.join(data_root, 'frequency/frequency_rel_2.png')), (-30, 178))
    frequency_4.save(os.path.join(data_root, 'frequency_4.png'))

    pdf_save(seletedData)

def pdf_save(seletedData):
    data_root = os.path.join(personal_res.root, "{}".format(seletedData))  # 절대 경로
    print("\nMake PDF")
    '''
    PDF Setting
    '''
    # Global Variables
    WIDTH = 210
    HEIGHT = 297

    # Create PDF
    pdf = FPDF()  # A4 (210 by 297 mm)
    pdf.set_y(-15)
    pdf.set_font('Arial', 'I', 8)
    pdf.set_text_color(128)

    '''
    1
    '''
    pdf.add_page()  # Add Page
    pdf.image(os.path.join(data_root, 'mdd_detail.png'), 0, 0, WIDTH)  # Add Table
    '''
    2
    '''
    pdf.add_page()  # Add Page
    pdf.image(os.path.join(data_root, 'frequency_1.png'), 0, 0, WIDTH)  # Add Table
    '''
    3
    '''
    pdf.add_page()
    pdf.image(os.path.join(data_root, 'frequency_2.png'), 0, 0, WIDTH)
    '''
    4
    '''
    pdf.add_page()
    pdf.image(os.path.join(data_root, 'frequency_3.png'), 0, 0, WIDTH)
    '''
    5
    '''
    pdf.add_page()
    pdf.image(os.path.join(data_root, 'frequency_4.png'), 0, 0, WIDTH)

    pdf.output("./pdf_data/{}.pdf".format(seletedData), 'F')