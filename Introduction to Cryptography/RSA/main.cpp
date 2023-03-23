#include <iostream>
#include <NTL/ZZ.h>
#include <stdlib.h>  
#include <time.h>        

using namespace std;
using namespace NTL;


ZZ power(ZZ base, ZZ exp, ZZ m) {
	ZZ res;
	res = 1;
	ZZ y = base;
	while (exp > 0) {
		if (exp % 2 == 1)
			res = (res * y) % m;

		exp = exp / 2;
		y = (y * y) % m;
	}
	return res % m;
}
ZZ mulmod(ZZ a, ZZ b, ZZ mod) {
	ZZ x, y;
	x = 0;
	y = a % mod;
	while (b > 0) {
		if (b % 2 == 1) {
			x = (x + y) % mod;
		}
		y = (y * 2) % mod;
		b /= 2;
	}
	return x % mod;
}
bool millerTest(ZZ n, int k) {
	if (n <= 1 || n != 2 && n % 2 == 0) {
		return false;
	}
	ZZ d = n - 1;
	while (d % 2 == 0) {
		d /= 2;
	}
	for (int i = 0; i < k; i++) {
		ZZ a = RandomBnd(n - 2) + 2;
		ZZ mod = power(a, d, n);
		if (mod == 1 || mod == n - 1)
			return true;
		while (d != n - 1 && mod != n - 1 && mod != 1) {
			mod = mulmod(mod, mod, n);
			//mod = (mod * mod) & p;
			d *= 2;

		}
		if (mod != n - 1 && d % 2 == 0) {
			return false;
		}
	}
	return true;
}

ZZ cmmdc(ZZ a, ZZ b) {
	ZZ t;
	while (1) {
		t = a % b;
		if (t == 0)
			return b;
		a = b;
		b = t;
	}
}

ZZ Mod2PrimeExp(ZZ a,ZZ n,ZZ m,ZZ m1,ZZ m2)
{
	ZZ n1, n2, x1, x2, x;
	n1 = n % (m1 - 1);
	n2 = n % (m2 - 1);

	x1 = PowerMod(a % m1, n1, m1);
	x2 = PowerMod(a % m2, n2, m2);
	x = x1 + m1 * PowerMod(x2 - x1, InvMod(m1, m2), m2);

	return x;
}





int main() {
	ZZ p, q, maxLimit, n;
	maxLimit = 1;

	for (int i = 0; i < 512; i++)
		maxLimit = maxLimit * 2;

	do {
		p = RandomBnd(maxLimit + 1);
	} while (millerTest(p, 10) == 0);

	do {
		q = RandomBnd(maxLimit + 1);
	} while (millerTest(q, 10) == 0);
	n = p * q;

	cout << "P= " << p << endl << endl;
	cout << "Q= " << q << endl << endl;
	cout << "P*Q= " << n << endl << endl;

	ZZ phi;
	phi = (p - 1) * (q - 1);
	cout << "PHI= " << phi << endl << endl;

 
	srand(time_t(NULL));
	ZZ e;
	int random = rand() % 100;
	e = random;

	ZZ res;
	while (e < phi) {
		res = cmmdc(e, phi);
		if (res == 1)
			break;
		else
			e++;
	}

	cout << "e= " << e;
	  
	ZZ d;
	d = InvMod(e, phi);
	cout << endl << endl << "d= " << d;
	 
	ZZ message;
	message = RandomBnd(n);
	//message = 5;

	cout << endl << endl << "message= " << message;
	ZZ encryption;
	encryption = PowerMod(message, e, n);

	cout << endl << endl << "encryption= " << encryption;

	ZZ decryption;
	decryption = PowerMod(encryption, d, n);
	cout << endl << endl << "decryption= " << decryption << endl << endl;

	//a^n mod m 
	// a=encryption, n=d, m=n

	//(encryption^d mod n) mod p = (encryption^d mod n)^(d mod q) mod p
	
	 

	//cout << "x= " << Mod2PrimeExp(encryption,d,n,p,q) << endl << endl;
	//cout << InvMod(q, p);



	return 0;
}
