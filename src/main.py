from .constants import *

# Read az commands list 
az_commands_list = open(AZ_COMMAND_FILENAME,"r").read().split("\n")

print(az_commands_list)