import csv
import os

def write_project(project_name,path,category):
    with open('project.csv',mode='a') as project_file:
        project_writer = csv.writer(project_file, delimiter = ',', quotechar ='"', quoting = csv.QUOTE_MINIMAL)
        project_writer.writerow([project_name, path, category])

def find_project(project_name): #return path
    with open("project.csv") as project_file:
        cvs_reader = csv.reader(project_file, delimiter= ',')
        for row in cvs_reader:
            if not row:
                continue
            else :
                if project_name == row[0]:
                  return row[1]
           
        return "" #project not found

#write_project("course", "C:\\Users\\Admin\\Documents\\course","course")
#write_project("project", "C:\\Users\\Admin\\Documents\\project","project")
#write_project("test", "C:\\Users\\Admin\\Documents\\project","test")

project_path = find_project("test")
if len(project_path) >0:
    os.system('code '+project_path)

#print(find_project("test"))