#!/usr/bind/env python
#_*_ coding: utf8 _*_

import os

#COLORS
RED = '\033[1;31m'
BLUE = '\033[1;34m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
MAGENTA = '\033[1;35m'
WHITE = '\033[1;37m'
CYAN = '\033[1;36m'
END = '\033[0m'
RED_NORMAL = '\033[0;31m'
GREEN_NORMAL = '\033[0;32m'

autor = '\033[1;41;37m.:R3LI4NT:.\033[0m'
tool = '\033[1;44;37m.:.:FAKE DATA GENERATOR:.:.\033[0m'

def banner():
	print(f"""
	
{RED}██████╗  █████╗ ████████╗ █████╗ {WHITE}███████╗ █████╗ ██╗  ██╗███████╗██████╗ {END}
{RED}██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗{WHITE}██╔════╝██╔══██╗██║ ██╔╝██╔════╝██╔══██╗{END}
{RED}██║  ██║███████║   ██║   ███████║{WHITE}█████╗  ███████║█████╔╝ █████╗  ██████╔╝{END}
{RED}██║  ██║██╔══██║   ██║   ██╔══██║{WHITE}██╔══╝  ██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗{END}
{RED}██████╔╝██║  ██║   ██║   ██║  ██║{WHITE}██║     ██║  ██║██║  ██╗███████╗██║  ██║{END}
{RED}╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝{WHITE}╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝v1.0{END}

\t\t     {tool}
\t\t\t{WHITE}Github: {autor}{END}
""")
	