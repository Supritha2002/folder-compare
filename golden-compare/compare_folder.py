import os
import json
import sys


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
    return compared_files, additional_files


def allfileslist(directory_path):
    allfiles = []
    for root, dirnames, filenames in os.walk(directory_path):
        for filename in filenames:
            fullpath = os.path.join(root, filename)
            _, subpath = fullpath.split("/", 1)
            allfiles.append(subpath)
    return allfiles


def compare_folder_contents(directory_path, standard_file):
    standardfilelist = load_contents_of_standardfile(standard_file)
    isExisting = os.path.exists(directory_path)
    if(isExisting is False ):
        sys.exit()
    allfiles = allfileslist(directory_path)
    compared_files, additional_files = compared_n_additionalfiles(allfiles, standardfilelist)
    missing_files = missingfileslist(standardfilelist, compared_files)
    return missing_files, additional_files
