#!/usr/bin/env python3
# try:
#     from yaml import CLoader as Loader, CDumper as Dumper
# except ImportError:
#     from yaml import Loader, Dumper
import yaml 
import os,sys



yaml_file = sys.argv[1]
#base orig file name to create new file name
new_yaml_file = "{}.{}".format(yaml_file.split('.')[0]+"_new",yaml_file.split('.')[1])
new_repo = sys.argv[2]

# yaml_file = "kiali.yaml"
# new_repo = "newrepo"
# new_yaml_file = yaml_file+"_new"


# Check if pullsecret name set by arg
if len(sys.argv) >3 :
    pullsecret = sys.argv[3]
else:
    pullsecret = "harbor"

workdir = os.getcwd()
if "/" in sys.argv[1]:
    print("Please run alone with the yaml file you want to change!")
    exit()
with open(workdir+'/'+yaml_file) as f:
#with open(os.path.dirname(os.path.abspath(__file__))+'/'+yaml_file) as f:
    new_datas = []
    datas = yaml.load_all(f, Loader=yaml.FullLoader)
    for data in datas: 
        for k, v in data.items():
            if k in ("spec"): 
                #print(k, "->", v)
                if "template" in v: 
                    for container in v["template"]["spec"]["containers"]:
                        #print(new_repo+'/'+container["image"])
                        container["image"] = new_repo+'/'+container["image"]
                    v["template"]["spec"]["imagePullSecrets"] = [{"name": pullsecret}]    
        new_datas.append(data)                
    f_new = open(workdir+'/'+new_yaml_file, 'w')
    yaml.dump_all(new_datas,f_new)
    f.close()                        
# with open(os.path.dirname(os.path.abspath(__file__))+'/'+new_yaml_file, 'w') as f:
#     yaml.dump_all(datas,f)
#     f.close()
