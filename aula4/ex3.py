#!/usr/bin/python3

from ex2 import Conta as CC
from ex2 import Poupanca as CP

def main():

	joao_cc = CC('joao','123', 30000)
	maria_cc = CC('maria','222', 2000)
	joao_pp = CP('joao','111', 100)

	joao_cc.transferir(3000,maria_cc)
	joao_cc.descrever()
	maria_cc.descrever()

	joao_cc.transferir(5000,joao_pp)
	joao_cc.descrever()
	joao_pp.descrever()

	joao_pp.render()
	joao_pp.descrever()

if __name__ == '__main__':
	main()