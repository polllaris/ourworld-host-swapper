import os
import json
from traceback import print_exc


BANNER_TEXT = (
	"+=========================================+\n"
	"|         ourWorld Host Swapper           |\n"
	"+-----------------------------------------|\n"
	"| A proxyless server hopper for ourWorld. |\n"
	"|-----------------------------------------|\n"
	"|       Created By: Jessica Winters       |\n"
	"+=========================================+\n"
	"|  THIS VERSION IS NOT FULLY FUNCTIONAL   |\n"
	"+=========================================+\n"
)
SERVERS = [
	"35.247.43.97",
	"34.83.142.207",
	"35.233.241.189",
	"34.82.115.163",
	"35.247.19.106",
	"34.105.109.230"
]

HOSTNAMES = [
	"game2.ourworld.com",
	"game3.ourworld.com",
	"game4.ourworld.com",
	"game5.ourworld.com",
	"game52.ourworld.com",
	"game53.ourworld.com"
]
class Configurator:
	def __init__(self, hostspath="/etc/hosts", hostnames=[]):
		self.hostspath = hostspath
		self.hostnames = hostnames
	def load_hosts(self):
		try:
			with open(self.hostspath, "r") as f:
				return f.read()
		except:
			print_exc()
			return False
	def save_hosts(self, content):
		try:
			with open(self.hostspath, "w") as f:
				f.write(content)

			return True
		except:
			print_exc()
			return False
	def rem_host_overrides(self):
		newhosts = ""
		oldhosts = self.load_hosts()
		if not oldhosts: return

		for line in oldhosts.split("\n"):
			if len(line) <= 1: continue
			badline = False
			for host in self.hostnames:
				if host in line: badline = True

			if badline: continue

			newhosts += line + "\n"

		return self.save_hosts(newhosts)
	def add_host_overrides(self, addr):
		# remove any host overrides if there
		self.rem_host_overrides()

		newhosts = self.load_hosts()

		for host in self.hostnames:
			newhosts += addr + " " + host + "\n"


		return self.save_hosts(newhosts)

class Interface:
	def __init__(self, configurator, servers):
		self.configurator = configurator
		self.servers = servers
	def clearscreen(self):
		if os.name == "nt":
			os.system("cls")
		else:
			os.system("clear")
	def banner(self):
		self.clearscreen()
		print(BANNER_TEXT)

	def main(self):

		options = (
			"[R] RESET TO NORMAL\n\n"
			"1) game2.ourworld.com\n"
			"2) game3.ourworld.com\n"
			"3) game4.ourworld.com\n"
			"4) game52.ourworld.com\n"
			"5) game53.ourworld.com\n"
		)

		while True:
			self.banner()
			print(options)

			choice = input("#? ")

			if choice == "1":
				addr = self.servers[0]
			elif choice == "2":
				addr = self.servers[1]
			elif choice == "3":
				addr = self.servers[2]
			elif choice == "4":
				addr = self.servers[3]
			elif choice == "5":
				addr = self.servers[4]
			elif choice == "5":
				addr = self.servers[5]
			elif choice == "6":
				addr = self.servers[6]
			elif choice in ["r", "R"]:
				self.configurator.rem_host_overrides()
				continue
			else:
				continue

			self.configurator.add_host_overrides(addr)

def main():
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument("-s", "--servers")
	parser.add_argument("--hostspath")
	parser.add_argument("--hostnames")

	arguments = parser.parse_args()

	if arguments.servers:
		servers = arguments.servers.split(",")
	else:
		servers = SERVERS
	if arguments.hostspath:
		hostspath = arguments.hosts
	else:
		hostspath = None
	if arguments.hostnames:
		hostnames = arguments.hostnames.split(",")
	else:
		hostnames = HOSTNAMES
	if arguments.hostspath:
		hostspath = arguments.hosts
	else:
		if os.name == "nt":
			hostspath = "C:\\Windows\\System32\\Drivers\\etc\\hosts"
		else:
			hostspath = "/etc/hosts"


	configurator = Configurator(hostspath, hostnames)

	interface = Interface(configurator, servers)
	interface.banner()
	interface.main()
if __name__ == "__main__":
	main()
