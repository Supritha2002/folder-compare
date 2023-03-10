import os
import json
standardfile = "standardfile.json"
folderpath = "folder_missing_files"


def load_contents_of_standardfile(standardfilename):
    fileObject = open(standardfilename, "r")
    jsoncontent = fileObject.read()
    standardfilelist = json.loads(jsoncontent)
    fileObject.close()
    return standardfilelist


def missingfileslist(standardfilelist, compared_files):
    missing_files = []
    [missing_files.append(file) for file in standardfilelist if file not in compared_files]
    return missing_files


def compared_n_additionalfiles(allfiles, standardfilelist):
    compared_files = []
    additional_files = []
    for filename in allfiles:
        if filename in standardfilelist:
            compared_files.append(filename)
        else:
            additional_files.append(filename)
    print("c",compared_files)
    print("a",additional_files)
    return compared_files, additional_files


def compare_folder_contents(directory_path, standard_file):
    standardfilelist = load_contents_of_standardfile(standard_file)
    allfiles = []
    for root, dirnames, filenames in os.walk(directory_path):
        for filename in filenames:
            fullpath = os.path.join(root, filename)
            _, subpath = fullpath.split("/", 1)
            allfiles.append(subpath)
    print("all",allfiles)
    compared_files, additional_files = compared_n_additionalfiles(allfiles, standardfilelist)
    missing_files = missingfileslist(standardfilelist, compared_files)
    print(missing_files)
    return missing_files, additional_files

if __name__=="__main__":
    compare_folder_contents(folderpath,standardfile)
