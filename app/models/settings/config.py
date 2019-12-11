import os, sys
import modules.logging.logging as logging_config
import json
import logging
import platform

# root dir
root_dir = os.path.dirname(os.path.realpath(sys.argv[0]))

# logs dir full path
logs_dir_full_path = ""

# logs dir name
logs_dir_name = "logs"

# configs dir full path
configs_dir_full_path = ""

# configs dir name
configs_dir_name = "configs"

# data dir full path
data_dir_full_path = ""

# data dir name
data_dir_name = "data"

# engine version code
version_code = "0.6"

# build version code
build_version_code = -1

# engine name
engine_name = "Impact AI"

# system name
system_name = "Impact AI"

# show all info when running
show_system_info_on_start = True

# logging config file name
logging_config_file_name = "logging.yaml"

# logging config file full pat
logging_config_file_full_path = ""

# buildcode file name
build_code_file_name = "build_code.json"

# logging config file full pat
build_code_file_full_path = ""

# test file name
test_file_name = ''

# test file full path
test_file_name_full_path = ''

# temp dir full path
temp_dir_full_path = ""

# temp dir name
temp_dir_name = "temp"

# credentials fro DB
db_uri = ''#'postgresql://postgres:12345678@localhost/mhr_onboarding'

#api version code
api_version_code = 1

#api route version
api_route_version = 'v'+str(api_version_code)

# api url
api_url = ''#'http://127.0.0.1:5000/v1/'

#scorm files
scorm_url = ''#'https://app.empiflow.com/empiflow.scorm/'

# uploads dir full path
uploads_dir_full_path = ''#'home/vyadzmak/Projects/Knomary/uploads'

#secret_key
secret_key = '8497bee09bb843acb69272f7ef82ec7e'

#test images dir name
test_images_dir_name = 'test_images'

#test images full path
test_images_full_path =''

#scorm templates dir path
scorm_templates_dir_name = ''#'scorm_templates'

#scorm templates full path
scorm_templates_full_path = ''

#platform_name
platform_name =platform.system()

#scorm export full path
#scorm_export_full_path = '/var/www/empiflow.scorm'
scorm_export_full_path = ''#'/home/vyadzmak/Projects/Knomary/empiflow.scorm'

#os name
os_name = os.name

# all versions
versions_container = [
    ["0.1", "Artemis"],
    ["0.2", "Hestia"],
    ["0.3", "Aphrodite"],
    ["0.4", "Demeter"],
    ["0.5", "Athena"],
    ["0.6", "Hera"],
    ["0.7", "Ares"],
    ["0.8", "Hermes"],
    ["0.9", "Apollo"],
    ["1.0", "Hephaestus"],
    ["1.1", "Poseidon"],
    ["1.2", "Zeus"]

]

#size image for resizing
image_sizes = [
    ['thumb',[256,256]],
    ['micro', [64, 64]],
    ['middle', [512, 512]],
    ['preview', [1024, 1024]],
    ['hq', [2048, 2048]]

]

#target images extension
target_image_extension ='jpg'

# --------------- methods---------------#
# load and increase build version
def load_build_version():
    try:

        with open(build_code_file_full_path) as f:
            data = json.load(f)
            global build_version_code
            build_version_code = int(data["build_version_code"])
            build_version_code += 1
            data["build_version_code"] = build_version_code

        with open(build_code_file_full_path, "w") as jsonFile:
            json.dump(data, jsonFile)

    except Exception as e:
        logging.error(str(e))

# get engine version name
def get_version_name():
    try:
        versions = versions_container
        current_version_code = version_code

        for version in versions:
            if (version[0] == current_version_code):
                return version[1]

    except Exception as e:
        logging.error(str(e))
        return str(e)



# join system paths
def join_path(paths):
    try:
        path = os.path.join(*paths)
        path = os.path.normpath(path)
        return path
    except Exception as e:
        logging.error(str(e))
        return str(e)


# show start info
def show_system_info():
    try:
        print("Start init configuration")
        print("Root dir : " + root_dir)
        print("System name : " + system_name)
        print("Engine name : " + engine_name)
        print("Engine version code: " + version_code)
        print("Engine version name: " + get_version_name())
        print("Build version code: " + str(build_version_code))

        pass
    except Exception as e:
        logging.error(str(e))


# check single dir
def check_single_dir(dir_path):
    try:

        if (platform_name == 'Linux'):
            l = str(dir_path)[:1]

            if (l != '/'):
                dir_path = '/' + dir_path

        dir_exists = os.path.exists(dir_path)


        if (dir_exists == False):
            os.mkdir(dir_path)
            logging.info("Create directory " + dir_path)
    except Exception as e:
        logging.error(str(e))


# check system dirs
def check_dirs():
    try:
        check_single_dir(configs_dir_full_path)
        check_single_dir(logs_dir_full_path)
        check_single_dir(uploads_dir_full_path)
        check_single_dir(test_images_full_path)
        check_single_dir(temp_dir_full_path)
        check_single_dir(scorm_templates_full_path)
    except Exception as e:
        logging.error(str(e))


# config system paths
def config_paths():
    try:
        global configs_dir_full_path
        configs_dir_full_path = join_path([root_dir, configs_dir_name])

        global logging_config_file_full_path
        logging_config_file_full_path = join_path([configs_dir_full_path, logging_config_file_name])

        global build_code_file_full_path
        build_code_file_full_path = join_path([configs_dir_full_path, build_code_file_name])

        global logs_dir_full_path
        logs_dir_full_path = join_path([root_dir, logs_dir_name])

        global data_dir_full_path
        data_dir_full_path = join_path([root_dir, data_dir_name])

        global temp_dir_full_path
        temp_dir_full_path = join_path([data_dir_full_path, temp_dir_name])

        global test_file_name_full_path
        test_file_name_full_path = join_path([data_dir_full_path, test_file_name])

        global test_images_full_path
        test_images_full_path = join_path([data_dir_full_path, test_images_dir_name])

        global scorm_templates_full_path
        scorm_templates_full_path = join_path([data_dir_full_path, scorm_templates_dir_name])

        check_dirs()
    except Exception as e:
        logging.error(str(e))


# init config
def init_config():
    try:
        print('OS system name: '+os_name)
        print('Platform name: '+platform_name)
        config_paths()
        load_build_version()
        logging_config.setup_logging(default_path=logging_config_file_full_path)

        if (show_system_info_on_start == True):
            show_system_info()

        logging.info("Config init successful")

    except Exception as e:
        logging.error(str(e))

