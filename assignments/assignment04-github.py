from github import Github
import requests
import json
from config import config as cfg

#function to replace text in file content
def replace_text(content, old_text, new_text):
    return content.replace(old_text,new_text)

#authenticate with GitHub API  & path to file
apikey = cfg["githubkey"]
repository_name = "briannemcgrath/WSAA-COURSEWORK"
file_path = "assignments/assignment04-andrew.txt"

#get apikey
g = Github(apikey)
repository = g.get_repo(repository_name)

#print all files in rep to check correct file path 
contents = repository.get_contents("")
for content_file in contents:
    print(content_file.path)

#check inside assignments directory
assignments_contents = repository.get_contents("assignments")
for content_file in assignments_contents:
    print(content_file.path)

#fetch file from repo 
file = repository.get_contents(file_path)

#retrieve file content
file_content = file.decoded_content.decode("utf-8")

#replace "Andrew" with "Bree"
old_text = "Andrew"
new_text = "Bree"
updated_content = replace_text(file_content, old_text, new_text).strip() + "\n"

#commit and update file in repository 
repository.update_file(file.path, f"Replaced {old_text} with {new_text}", updated_content, file.sha)

print("File updated and changes pushed successfully! :)")

