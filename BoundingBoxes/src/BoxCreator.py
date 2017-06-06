'''
Created on 31.05.2017

@author: Martin Gerstmaier
'''
from lxml import etree
from PIL import Image
import glob


folder = "images"
annotationsFolder = "annotations"
counter=0

def createBoundingBox(imageName, w, h):
    annotation = etree.Element("annotation")
    etree.SubElement(annotation, "folder").text = folder
    etree.SubElement(annotation, "filename").text = imageName[len(folder)+1:]
    source = etree.SubElement(annotation, "source")

    etree.SubElement(source, "database").text = "flickr"
    etree.SubElement(source, "annotation").text = "MG"
    etree.SubElement(source, "image").text = "flickr"
    
    size = etree.SubElement(annotation, "size")
    
    etree.SubElement(size, "width").text = w
    etree.SubElement(size, "height").text = h
    etree.SubElement(size, "depth").text = "3"
    
    etree.SubElement(annotation, "segmented").text = "1"
    object = etree.SubElement(annotation, "object")
    
    etree.SubElement(object, "name").text = "noObject"
    etree.SubElement(object, "pose").text = "Unspecified"
    etree.SubElement(object, "truncated").text = "0"
    etree.SubElement(object, "difficult").text = "0"
    
    bndbox = etree.SubElement(object, "bndbox")
    
    etree.SubElement(bndbox, "xmin").text = "0"
    etree.SubElement(bndbox, "ymin").text = "0"
    etree.SubElement(bndbox, "xmax").text = w
    etree.SubElement(bndbox, "ymax").text = h
    
    tree = etree.ElementTree(annotation)
    tree.write(annotationsFolder + "/" + imageName[len(folder)+1:len(imageName)-4] + ".xml", pretty_print = True)
    #print(counter)


for imageName in glob.glob(folder + '/*.jpg'):
    try:
        img = Image.open(imageName)
        width, height = img.size
        w = str(width)
        h = str(height)
        createBoundingBox(imageName, w, h)
        counter +=1
    except:
        print("Error")
    
