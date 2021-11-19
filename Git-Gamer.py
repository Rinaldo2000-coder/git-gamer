import os
from os import path
from datetime import datetime

# Checking the default location
# add remote location

home = (path.expanduser("~"))
git_gamer_location = path.join(home, "GitGamer")
current_cwd = os.getcwd()
if not (path.isdir(git_gamer_location)):
	os.mkdir(git_gamer_location)
	os.chdir(git_gamer_location)
	os.system('git init -b "main"')
	os.chdir(current_cwd)
	with open("git-repo-url.txt", 'r') as url_file:
		remote_url = url_file.readline()
		os.chdir(git_gamer_location)
		os.system(f"git remote add origin {remote_url}")
		os.chdir(current_cwd)
		url_file.close()
else:
	pass
# read location file
def remove_lines(list_path):
	output_list = []
	for line in list_path:
		if "\n" in line:
			line = line.replace('\n', '')
		output_list.append(line)
	return output_list

save_location_file = open("save-location.txt", 'r')

game_name_file = open("game-name.txt", 'r')

save_location_list = save_location_file.readlines()

game_name_list = game_name_file.readlines()

save_location_list = remove_lines(save_location_list)

game_name_list = remove_lines(game_name_list)

for num1 in range(len(save_location_list)):
	temp_loc = save_location_list[num1]
	temp_name = game_name_list[num1]
	temp_path = path.join(git_gamer_location, temp_name)
	if not (path.isdir(temp_path)):
		os.mkdir(temp_path)
	temp_loc = temp_loc + "\\*.*"
	# print(f'copy "{temp_loc}" "{temp_path}"')
	os.system(f'echo  | del /Q /S /F "{temp_path}"')
	os.system(f'xcopy /S /Q /F /Y "{temp_loc}" "{temp_path}"')

os.chdir(git_gamer_location)
os.system("git add .")

date_time = datetime.now().strftime("%D%M%Y%H%M%S")

os.system(f"git commit -m '{date_time}'")
os.system("git push -u origin main")