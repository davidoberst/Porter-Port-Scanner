import socket
import pyfiglet
import argparse
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(1)

#Add parameters
parser = argparse.ArgumentParser()
parser.add_argument("target",help="Type the target IP adress")
parser.add_argument("port",help="Target Port")
args = parser.parse_args() #read user arguments 



def logo():
 print(pyfiglet.figlet_format("Porter", font="small"))
 print("by: davidoberst")
 print("")

 
logo()
