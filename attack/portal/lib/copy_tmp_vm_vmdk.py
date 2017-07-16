# -*- coding: utf-8 -*-
import pexpect
import sys
import time
import ConfigParser
 
def main(vm_name,os_type):
    
    inifile = ConfigPerser.SafeConfigParser()
    inifile.read(os.path.dirname(os.path.abspath(__file__)) + "config.ini")

    esxi_name               = inifile.get('server_conf', 'esxi_name')
    template_datastore      = inifile.get('server_conf', 'template_datastore')
    deploy_target_datastore = inifile.get('server_conf', 'deploy_target_datastore')
    Password                = inifile.get('server_conf', 'Password')

    if os_type == 1:
        template_vm = inifile.get('template_list', 'centos_7')
    elif os_type == 2:
        template_vm = inifile.get('template_list', 'centos_6')
    elif os_type == 3:
        template_vm = inifile.get('template_list', 'ubuntu_17')
    elif os_type == 4:
        template_vm = inifile.get('template_list', 'winsrv_12')
    elif os_type == 5:
        template_vm = inifile.get('template_list', 'winsrv_08')
    elif os_type == 6:
        template_vm = inifile.get('template_list', 'winsrv_03')

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
  
 
if __name__ == "__main__": 
        main()
