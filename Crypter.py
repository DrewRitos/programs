import sys
q = input ("""Do you want to encrypt <1> or decrypt <0> a message?
Or type <off> to exit the program. """)
if q == "off":
        sys.exit(0)
while True:
	if q == "1":
		s = input("Input message to encrypt: ")
		s = s.replace(' ','0000')
		s = s.replace('a','06d3')
		s = s.replace('b','dh83')
		s = s.replace('c','9d80')
		s = s.replace('d','00b8')
		s = s.replace('e','9d86')
		s = s.replace('f','023g')
		s = s.replace('g','324i')
		s = s.replace('h','8ddu')
		s = s.replace('i','32ol')
		s = s.replace('j','0upb')
		s = s.replace('k','l543')
		s = s.replace('l','4lnb')
		s = s.replace('m','8ju4')
		s = s.replace('n','9843')
		s = s.replace('o','0033')
		s = s.replace('p','87bb')
		s = s.replace('q','4456')
		s = s.replace('r','43k0')
		s = s.replace('s','800o')
		s = s.replace('t','877e')
		s = s.replace('u','ee67')
		s = s.replace('v','thuy')
		s = s.replace('w','786u')
		s = s.replace('x','7600')
		s = s.replace('y','432n')
		s = s.replace('z','0808')
		print (s)
		q = input("""Do you want to encrypt <1> or decrypt <0> any more messages?""")
	if q == "0":
		s = input("Input message to decrypt: ")
		for x in range(100):
			s = s.replace('0000',' ')
			s = s.replace('06d3','a')
			s = s.replace('dh83','b')
			s = s.replace('9d80','c')
			s = s.replace('00b8','d')
			s = s.replace('9d86','e')
			s = s.replace('023g','f')
			s = s.replace('324i','g')
			s = s.replace('8ddu','h')
			s = s.replace('32ol','i')
			s = s.replace('0upb','j')
			s = s.replace('l543','k')
			s = s.replace('4lnb','l')
			s = s.replace('8ju4','m')
			s = s.replace('9843','n')
			s = s.replace('0033','o')
			s = s.replace('87bb','p')
			s = s.replace('4456','q')
			s = s.replace('43k0','r')
			s = s.replace('800o','s')
			s = s.replace('877e','t')
			s = s.replace('ee67','u')
			s = s.replace('thuy','v')
			s = s.replace('786u','w')
			s = s.replace('7600','x')
			s = s.replace('432n','y')
			s = s.replace('0808','z')
		print (s)
		q = input("""Do you want to encrypt <1> or decrypt <0> any more messages?""")
