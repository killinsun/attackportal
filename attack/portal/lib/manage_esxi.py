import sys
import re
import os
#from paramiko import SSHClient, AutoAddPolicy
import pexpect
import configparser as ConfigPerser

inifile = ConfigPerser.SafeConfigParser()
inifile.read(os.path.dirname(os.path.abspath(__file__)) + "/conf.ini")

def detect_tmp_os(os_type):
    os_type = int(os_type)

    if os_type == 1:
        tmp_os_name = inifile.get('template_list', 'centos_7')
    elif os_type == 2:
        tmp_os_name = inifile.get('template_list', 'centos_6')
    elif os_type == 3:
        tmp_os_name = inifile.get('template_list', 'ubuntu_17')
    elif os_type == 4:
        tmp_os_name = inifile.get('template_list', 'winsrv_12')
    elif os_type == 5:
        tmp_os_name = inifile.get('template_list', 'winsrv_08')
    elif os_type == 6:
        tmp_os_name = inifile.get('template_list', 'winsrv_03')

    return tmp_os_name


def duplicate_vmdk(vm_name,os_type):
    
    esxi_name               = inifile.get('server_conf', 'esxi_name')
    template_datastore      = inifile.get('server_conf', 'template_datastore')
    deploy_target_datastore = inifile.get('server_conf', 'deploy_target_datastore')
    Password                = inifile.get('server_conf', 'Password')
    template_vm             = detect_tmp_os(os_type)

    child = pexpect.spawn("/usr/bin/ssh root@" + esxi_name)
    child.expect("Password:")
    child.sendline(Password)
    child.expect("~ #")
    child.sendline("mkdir /vmfs/volumes/" + deploy_target_datastore + "/" + vm_name + "/")
    child.expect("~ #")
    child.sendline("vmkfstools -i /vmfs/volumes/" + template_datastore + "/" + template_vm + "/" + template_vm + ".vmdk /vmfs/volumes/" + deploy_target_datastore + "/" + vm_name +"/" + vm_name +".vmdk -d thin")
    index = child.expect([r"Clone: [0-9][0-9]% done",r"~ #"])
    while True:
      if index == 0:
        child.sendline("")
        index = child.expect([r"Clone: [0-9][0-9]% done",r"~ #"])
        print(child.after.decode('utf-8'))
        time.sleep(10)
      elif index == 1:
        child.sendline("")
        index = child.expect([r"Clone: [0-9][0-9]% done",r"~ #"])
        print("Completed!")
        time.sleep(0.1)
        child.close()
        print(child.after.decode('utf-8'))
        print(child.before.decode('utf-8'))
        break
  
 
def create_vm_from_tmp(vm_name,os_type):
    

    esxi_name               = inifile.get('server_conf', 'esxi_name')
    template_datastore      = inifile.get('server_conf', 'template_datastore')
    deploy_target_datastore = inifile.get('server_conf', 'deploy_target_datastore')
    Password                = inifile.get('server_conf', 'Password')
    old_text                 = detect_tmp_os(os_type)
    new_text                = vm_name
    this_file_path          = os.path.dirname(os.path.abspath(__file__))


    #Create vmx file from template vmx file..
    dir_path = this_file_path +  "/../resources/"
    f_old = open(dir_path + old_text +".vmx",'r')
    f_new = open(dir_path + new_text +".vmx",'w')
    print(dir_path)

    for line in f_old:
      new_line = re.sub(old_text, new_text, line.strip())
      f_new.write(new_line + "\n")

    f_old.close()
    f_new.close()


    #Upload vmx file.

   # ssh = SSHClient()
   # ssh.set_missing_host_key_policy(AutoAddPolicy())
   # ssh.connect(esxi_name, 22, "root", Password)
   # sftp = ssh.open_sftp()

    local_file = dir_path + new_text + ".vmx"
    remote_file = "/vmfs/volumes/" + deploy_target_datastore + "/" + vm_name + "/" + vm_name + ".vmx"
   # sftp.put(local_file, remote_file)
   # 
   # sftp.close()
   # ssh.close()
   # 
    child = pexpect.spawn("scp " + local_file + " root@" + esxi_name + ":" + remote_file)
    child.expect("Password:")
    child.sendline(Password)
    print(child.after.decode('utf-8'))
    print(child.before.decode('utf-8'))
    child.close()
    print("section1 complete")
    print("scp " + local_file + " root@" + esxi_name + ":" + remote_file)


    #Delete be created local vmx file.
    vmx_path = remote_file

    child = pexpect.spawn("/usr/bin/ssh root@" + esxi_name)
    child.expect("Password:")
    child.sendline(Password)
    child.expect("~ #")
    child.sendline("vim-cmd solo/registervm " + vmx_path + " " + vm_name)
    print(child.after.decode('utf-8'))
    print(child.before.decode('utf-8'))
    child.expect("~ #")
    print(child.after.decode('utf-8'))
    print(child.before.decode('utf-8'))
    time.sleep(0.1)
    child.close()


def connect_test(vm_name,os_type):

    esxi_name               = inifile.get('server_conf', 'esxi_name')
    template_datastore      = inifile.get('server_conf', 'template_datastore')
    deploy_target_datastore = inifile.get('server_conf', 'deploy_target_datastore')
    Password                = inifile.get('server_conf', 'Password')
    old_text                = detect_tmp_os(os_type)

    print(esxi_name)
    print(old_text)
