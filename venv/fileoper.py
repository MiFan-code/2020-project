# -*- coding: utf-8 -*-
def writein(filename,string,encoding='utf-8'):
    with open(filename,'w+',encoding=encoding)as file:
        file.write(string);
        file.close();
def readout(filename,encoding='utf-8'):
    with open(filename,'r',encoding=encoding) as file:
        filedata=file.read();
        file.close();
        return filedata;