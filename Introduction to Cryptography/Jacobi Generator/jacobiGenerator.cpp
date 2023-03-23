#include <iostream>
#include <NTL/ZZ.h>
#include <assert.h>
 

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



int jacobiSymbol(ZZ n, ZZ a) {
	int s = 1;

	assert(a > n > 0 && a % 2 == 1);
	n %= a;
	while (n != 0) {
		while (n % 2 == 0) {
			n = n / 2;
			int r = a % 8;
			if (r == 3 || r == 5)
				s = -s;
		}
		swap(n, a);
		if (n % 4 == 3 && a % 4 == 3)
			s = -s;
		n = n % a;
	}
	if (a == 1)
		return s;
	else
		return 0;
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

	ZZ random;
	random = RandomBnd(n);
	cout << "random seed= " << random<< endl << endl;

	ZZ jacobi, bit;
	bit = 0;
	int nr0 = 0, nr1 = 0;
	for (int i = 0; i < 100; i++) {
		jacobi = jacobiSymbol(random + i, n);
		bit = (jacobi + 1) / 2;

		if (bit == 1)
			nr1++;
		else
			nr0++;

		cout << bit;
	}
	cout << endl;
	cout << "nr0= " << nr0 << endl;
	cout << "nr1= " << nr1 << endl;

	
	//p = 1236; q = 20003;
	//cout << jacobiSymbol(p, q);

	return 0;
}