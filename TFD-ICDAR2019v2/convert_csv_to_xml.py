from xml.etree.ElementTree import Element, indent
from lxml import etree
import csv


def write_csv_to_xml(fileName:str, bbox):
    print(fileName)
    print(bbox)
    ################################## ROOT ############################
    root: Element = etree.Element('annotation')
    folder = etree.SubElement(root, 'folder')

    ################################ NAME ##############################
    folder.text = 'images'

    filename = etree.SubElement(root, 'filename')
    ### Change filename
    filename.text= (fileName + '.png')

    ############################# SIZE ##################################
    # Change file size
    size = etree.SubElement(root,'size')
    width=etree.SubElement(size,'width')
    width.text='5100'

    height = etree.SubElement(size,'height')
    height.text='6601'

    depth = etree.SubElement(size, 'depth')
    depth.text='3'

    ############################# SEGMENTED ############################

    segmented=etree.SubElement(root,'segmented')
    segmented.text='0'

    ############################ OBJECT ###############################

    for box in bbox:
        object = etree.Element('object')
        name=etree.SubElement(object,'name')
        name.text='expr'
        pose=etree.SubElement(object,'pose')
        pose.text='Unspecified'
        trunc=etree.SubElement(object,'truncated')
        trunc.text='0'
        occluded=etree.SubElement(object,'occluded')
        occluded.text='0'
        difficult=etree.SubElement(object,'difficult')
        difficult.text='0'
        bndbox =etree.SubElement(object,'bndbox')

        # CHange object elements
        xmin=etree.SubElement(bndbox,'xmin')
        xmin.text= box[0]
        ymin=etree.SubElement(bndbox,'ymin')
        ymin.text= box[1]
        xmax=etree.SubElement(bndbox,'xmax')
        xmax.text= box[2]
        ymax=etree.SubElement(bndbox,'ymax')
        ymax.text= box[3]

        
        root.append(object)




    indent(root)
    result=etree.tostring(root)


    # Change xml filename
    xmlFile=open('Train/train_xml/' + fileName + '.xml','wb')

    xmlFile.write(result)

csv_file='Train/math_gt/Arkiv_1971_141_163.csv'
xml_file='Train/train_xml/'

with open(csv_file,'r') as my_input_file:
    num_pages=0
    for i in csv.reader(my_input_file):
        num_pages = max(int(i[0]),num_pages)
    num_pages+=1
        
    my_input_file.seek(0)

    for i in range(0, num_pages):
        with open (xml_file + str(i+1) + '.xml', 'wb') as my_output_file:
            line = list()
            for elements in csv.reader(my_input_file):
                if elements[0] == str(i):
                    line.append(elements[1:])
            write_csv_to_xml(str(i+1), line)
            line=list()
            my_input_file.seek(0)
        my_output_file.close()

my_input_file.close()







