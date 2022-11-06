# from xml.etree.ElementTree import Element, indent
# from lxml import etree
import csv
import os
import shutil
import fnmatch

xml_dir='Train/annotations/'


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
    xmlFile=open(xml_dir + fileName + '.xml','wb')

    xmlFile.write(result)

# csv_dir = './Train/math_gt/'
# csv_list = ["./Train/math_gt/Arkiv_1971_141_163.csv","./Train/math_gt/Arkiv_1997_185_199.csv"]

# #csv_file='Train/math_gt/Arkiv_1971_141_163.csv'
# num_xml = 0

# for csv_file in csv_list:
#     with open(csv_file,'r') as my_input_file:
#         num_pages=0
#         for i in csv.reader(my_input_file):
#             num_pages = max(int(i[0]),num_pages)
#         num_pages+=1

#         my_input_file.seek(0)
#         num_xml_per_csv = 0

#         for i in range(0, num_pages):
#             with open (xml_dir + str(num_xml + i + 1) + '.xml', 'wb') as my_output_file:
#                 line = list()
#                 for elements in csv.reader(my_input_file):
#                     if elements[0] == str(i):
#                         line.append(elements[1:])
#                 write_csv_to_xml(str(num_xml + i + 1), line)
#                 line=list()
#                 my_input_file.seek(0)
#             my_output_file.close()
#             num_xml_per_csv += 1
#         num_xml += num_xml_per_csv
        

    


#     my_input_file.close()

# print(num_xml)


directory= './Train/images/'
img_list = []
for folder in os.listdir(directory):
    img_list.append(folder)
# list_dir = ["Arkiv_1971_141_163/","Arkiv_1997_185_199/"]

i = 1
for folder in img_list:
    for filename in os.listdir(directory + folder) :
        shutil.copy2(directory + folder + '/' + filename, './Train/imagesv2/' + str(i) + '.png')
        i += 1
    # shutil.copy(directory + folder , '.\Train\images')

# i = 1
# csv_dir = './Train/math_gt/'
# csv_list = ["Arkiv_1971_141_163.csv","Arkiv_1997_185_199.csv"]

# for csv_file in csv_list:
#     with open (csv_dir + csv_file, 'r') as my_input_file:
#         num_pages = 0
#         for rows in csv.reader(my_input_file):
#             num_pages = max(int(rows[0]), num_pages)

#         num_pages += 1

#         my_input_file.seek(0)

#         for j in range(0, num_pages):
#             with open(xml_dir + '/' + str(j+1) + '.xml', 'wb') as my_output_file:
#                 line = list()
#                 for elements in csv.reader(my_input_file):
#                     if elements[0] == str(j):
#                         line.append(elements[1:])
#                 write_csv_to_xml(str(j+1), line)
#                 line=list()
#             my_output_file.close()

#         i += num_pages
    

#     my_input_file.close()





