# Usage:
# BB_black.py https://*/CXP9029710_27-f3f7c0d.cxp - Will unpack the .bin file
# BB_black.py 10.64.175.61 - Will send the black to node and reboot it

import subprocess,sys
link = sys.argv[1]
print("Your CXP:\n" + link)
cxp_name = link[-25:-4]
print("CXP name:\n" + cxp_name)

if sys.argv[1][-4:] == ".cxp":
    def term(command):
        subprocess.call(command, shell=True)
    term('wget '+ link)
    term('mv '+ cxp_name + '.cxp ' + cxp_name + '.gz')
    term('gunzip ' + cxp_name + '.gz')
    term('tar -xvf ' + cxp_name)
    term('ar x sw.ar')
    term('/app/rbs/wrtools/tools-sdk-20130220/usr/sbin/unsquashfs -v sqfs.img')
    term('mv ./squashfs-root/bbmContLteRdbfBlm4TrinityLm/bin/bbmContLteRdbfBlm4TrinityLmC.bin ./bbmContLteRdbfBlm4TrinityLmC.bin')
    #term('scp ./bbmContLteRdbfBlm4TrinityLmC.bin l:')
else:
HOST="root@"+sys.argv[1]
ssh = subprocess.Popen(["ssh", "%s" % HOST],
    shell=False,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    universal_newlines=True,
    bufsize=0)
ssh.stdin.write("ln -s /rcs/bbmContLteRdbfBlm4TrinityLmC.bin /home/sirpa/dev_patches/bbmContLteRdbfBlm4TrinityLmC.bin \n")
ssh.stdin.write("chmod 777  /home/sirpa/dev_patches/bbmContLteRdbfBlm4TrinityLmC.bin \n")
ssh.stdin.write("chmod 777  /rcs/bbmContLteRdbfBlm4TrinityLmC.bin \n")
ssh.stdin.write("reboot \n")
stdout, stderr = ssh.communicate()
print(stdout)
ssh.stdin.close()

