import csv

def write_project(project_name,path,category):
    with open('project.csv',mode='a') as project_file:
        project_writer = csv.writer(project_file, delimiter = ',', quotechar ='"', quoting = csv.QUOTE_MINIMAL)
        project_writer.writerow([project_name, path, category])


write_project("course", "C:\\Users\\Admin\\Documents\\course","course")
write_project("project", "C:\\Users\\Admin\\Documents\\project","project")
write_project("test", "C:\\Users\\Admin\\Documents\\project","test")