#include <iostream>
#include <fstream>
#include <cstring>
#include <string>
#include <cmath>
#include <stdlib.h>
#include <time.h>  
using namespace std;
ifstream Text;

string h0 = "01100111010001010010001100000001"; //67452301
string h1 = "11101111110011011010101110001001"; //EFCDAB89
string h2 = "10011000101110101101110011111110"; //98BADCFE
string h3 = "00010000001100100101010001110110"; //10325476
string h4 = "11000011110100101110000111110000"; //C3D2E1F0

char words[80][80];
char blocks[50][520];

string b10_to_b2(int x)
{
	string res;	 
	while (x)
	{
		res += char(x % 2 + '0');
		x /= 2;
	}
	int n = res.length();
	while (n < 8)
	{
		res += '0';
		n++;
	}
	for (int i = 0; i < n / 2; i++)
		swap(res[i], res[n - i - 1]);
	return res;
}

long long b2_to_b10(string a)
{
	long long res = 0;
	string ogl = "";
	for (int i = a.length() - 1; i >= 0; i--)
		ogl += a[i];
 
	for (int i = 0; i < a.length(); i++)	 
		if (ogl[i] == '1')
		{
			res = res + pow(2, i);
		}
	return res;	 
}

string b10_to_b16(long long a)
{
	string res = "";
	string temp = "";
	while (a)
	{
		int r = a % 16;
		if (r == 10)
			temp += 'A';
		else if (r == 11)
			temp += 'B';
		else if (r == 12)
			temp += 'C';
		else if (r == 13)
			temp += 'D';
		else if (r == 14)
			temp += 'E';
		else if (r == 15)
			temp += 'F';
		else
			temp += char(a % 16) + '0';
		a /= 16;
	}
	for (int i = temp.length() - 1; i >= 0; i--)
		res += temp[i];
	if (res.length() < 8)
	{
		string zero = "";
		for (int i = 0; i < 8 - res.length(); i++)
			zero += '0';
		res = zero + res;
	}

	return res;
}

string XOR(string a, string b ) {
	string res = "";
	for (int i = 0; i < a.length(); i++)
	{
		if (a[i] == b[i])
			res += "0";
		else
			res += "1";
	}
	return res;
}

string AND(string a, string b) {
	string res = "";
	for (int i = 0; i < a.length(); i++)
	{
		if (a[i] == '1' && b[i] == '1')
			res += "1";
		else 
			res += "0";
	}
	return res;
}

string OR(string a, string b) {
	string res = "";
	for (int i = 0; i < a.length(); i++)
	{
		if (a[i] == '0' && b[i] == '0')
			res += "0";
		else if(a[i] == '1' || b[i] == '1')
			res += "1";
	}
	return res;
}

string NOT(string a)
{
	string res = "";
	for (int i = 0; i < a.length(); i++)
	{
		if (a[i] == '0')
			res += '1';
		else 
			res += '0';
	}
	return res;
}

string left_rotate(string &a)
{
	if (a.length() <= 1)
		return a;
	char first = a[0];
	for (int i = 0; i <= a.length()-2; i++)
	{	  
		a[i] = a[i + 1];
	}
		
	a[a.length() - 1] = first;
	return a;
}

string add(string a, string b) {
	string res = "";
	int temp = 0;
	int size_a = a.size() - 1;
	int size_b = b.size() - 1;
	while (size_a >= 0 || size_b >= 0 || temp == 1) {
		temp += ((size_a >= 0) ? a[size_a] - '0' : 0);
		temp += ((size_b >= 0) ? b[size_b] - '0' : 0);
		res = char(temp % 2 + '0') + res;
		temp /= 2;
		size_a--; size_b--;
	}
	return res;
}

string truncate(string a, int nr) {
	string res = "";
		if (a.length() <= nr)
		return a;
	int s = a.length() - nr;
	
	for (int i = s; i < a.length(); i++)
		res += a[i];
	return res;
}

string SHA1(char text[500])
{
	string hash = "";

	//cream un vector de caractere ascii
	int ascii[500];
	int len = strlen(text);
	for (int i = 0; i < len; i++)
		ascii[i] = int(text[i]);

	/*cout << "ASCII: ";
	for (int i = 0; i < len; i++)
		cout << ascii[i] << ' ';
	cout << endl;
	*/

	//convertim vectorul ascii in numere binare
	string binary[500];
	for (int i = 0; i < len; i++)
		binary[i] = b10_to_b2(ascii[i]);
	/*
	cout << "Binary: ";
	for (int i = 0; i < len; i++)
		cout << binary[i] << ' ';
	cout << endl;
	*/

	//concatenam numerele binare si adaugam '1' la final
	string stringNumber;
	for (int i = 0; i < len; i++)
		stringNumber += binary[i];
	stringNumber += '1';
	//cout << "stringNumber: " << stringNumber << endl;

	//adaugam '0' la finalul lui stringNumber pana cand lungimea este 448 mod 512

	while (stringNumber.length() % 512 != 448)
		stringNumber += '0';
	//cout << "stringNumber: " << stringNumber << endl;

	//luam lungimea vectorului binar si adaugam '0' pana lungimea este 64
	string l = b10_to_b2(len * 8);
	string zeros;
	for (int i = 0; i < 55; i++)
		zeros += '0';
	l = zeros + l;
	//cout << endl << "Binary array length: " << l << endl << endl;

	//concatenam lungimea la stringNumber

	stringNumber += l;
	//cout << "stringNumber: " << stringNumber << endl;

	//impartim sirul in blocuri de 512 caractere

	int nrOfBlocks = -1;
	for (int i = 0; i < stringNumber.length(); i++)
	{
		if (i % 512 == 0)
			nrOfBlocks++;
		char c = stringNumber[i];
		if (i != stringNumber.length())
			blocks[nrOfBlocks][i % 512] = c;
	}
	/*
	for (int i = 0; i < nrOfBlocks + 1; i++)
		cout << endl << "block " << i << ": " << blocks[i] << endl << endl << endl;
	*/
	//impartim fiecare block in 80 grupuri de 32 biti  


	for (int k = 0; k < nrOfBlocks + 1; k++)
	{
		int index = -1;
		for (int i = 0; i < 512; i++)
		{
			if (i % 32 == 0)
				index++;
			words[index][i % 32] = blocks[k][i];
		}
		/*
		cout << endl << "words from block " << k << ": ";
		for (int i = 0; i < 16; i++)
		{
			for (int j = 0; j < 32; j++)
				if (words[i][j])cout << words[i][j];
			cout << ' ';
		}
		cout << endl;
		*/
		index = 15;
		for (int i = 16; i <= 79; i++)
		{
			string A = words[i - 3];
			string B = words[i - 8];
			string C = words[i - 14];
			string D = words[i - 16];


			string xorA = XOR(A, B);
			string xorB = XOR(xorA, C);
			string xorC = XOR(xorB, D);

			string newWord = left_rotate(xorC);
			index++;
			for (int i = 0; i < 32; i++)
				words[index][i] = newWord[i];
		}

		/*
		cout << endl << "words from block " << k << ": ";
		for (int i = 0; i < 80; i++)
		{
			for (int j = 0; j < 32; j++)
				cout << words[i][j];
			cout << ' ';
		}
		cout << endl;
		*/

		string A = h0;
		string B = h1;
		string C = h2;
		string D = h3;
		string E = h4;

		string F;
		string G;

		for (int j = 0; j <= 79; j++)
		{
			if (j < 20)
			{
				string BandC = AND(B, C);
				string notB = AND(NOT(B), D);
				F = OR(BandC, notB);
				G = "01011010100000100111100110011001"; //5A827999
			}
			else if (j < 40)
			{
				string BxorC = XOR(B, C);
				F = XOR(BxorC, D);
				G = "01101110110110011110101110100001"; //6ED9EBA1
			}
			else if (j < 60)
			{
				string BandC = AND(B, C);
				string BandD = AND(B, D);
				string CandD = AND(C, D);
				string BandCorBandD = OR(BandC, BandD);
				F = OR(BandCorBandD, CandD);
				G = "10001111000110111011110011011100"; //8F1BBCDC
			}
			else
			{
				string BxorC = XOR(B, C);
				F = XOR(BxorC, D);
				G = "11001010011000101100000111010110"; //CA62C1D6
			}

			string word = words[j];
			string rotateA = A;
			for (int h = 0; h < 5; h++)
				left_rotate(rotateA);

			string tempA = add(rotateA, F);
			string tempB = add(tempA, E);
			string tempC = add(tempB, G);
			string temp = add(tempC, word);;

			temp = truncate(temp, 32);
			E = D;
			D = C;

			string rotateB = B;
			for (int h = 0; h < 30; h++)
				left_rotate(rotateB);

			C = rotateB;
			B = A;
			A = temp;

			//cout << j << ": " << b10_to_b16(b2_to_b10(A)) << ' ' << b10_to_b16(b2_to_b10(B)) << ' ' << b10_to_b16(b2_to_b10(C)) << ' ' << b10_to_b16(b2_to_b10(D)) << ' ' << b10_to_b16(b2_to_b10(E)) << endl;
		}

		h0 = truncate(add(h0, A), 32);
		h1 = truncate(add(h1, B), 32);
		h2 = truncate(add(h2, C), 32);
		h3 = truncate(add(h3, D), 32);
		h4 = truncate(add(h4, E), 32);

		hash += b10_to_b16(b2_to_b10(h0));
		hash += b10_to_b16(b2_to_b10(h1));
		hash += b10_to_b16(b2_to_b10(h2));
		hash += b10_to_b16(b2_to_b10(h3));
		hash += b10_to_b16(b2_to_b10(h4));

		//cout << endl << "hash from block " << k << ": ";
		//cout << b10_to_b16(b2_to_b10(h0)) << ' ' << b10_to_b16(b2_to_b10(h1)) << ' ' << b10_to_b16(b2_to_b10(h2)) << ' ' << b10_to_b16(b2_to_b10(h3)) << ' ' << b10_to_b16(b2_to_b10(h4)) << endl << endl;

	}
	return hash;
}

int Hamming(string s1, string s2)
{
	int nr = 0;
	for (int i = 0; i < s1.length(); i++)
		if (s1[i] != s2[i])
			nr++;
	return nr;
}

int main()
{ 
 	char text[500];
	char text2[500];
	int index = -1;
	ifstream input;
	ofstream output;
	input.open("TEXT.txt");

	//luam inputul din fisier intr-un sir de caractere 
	char c;
	while (input.get(c))
	{
		if (c >= 'a' && c <= 'z' || c >= 'A' && c <= 'Z' || c == ' ')
		{
			index++;
			text[index] = c;
			text2[index] = c; //foosim pt distanta Hamming 
		}
	}	
	text[index + 1] = '\0';
	text2[index + 1] = '\0';
	cout << "Text: " << text << endl;

	  
	string s1 = SHA1(text);
	
	//modificam un caracter din text2
	srand(time(NULL));
	int length = strlen(text2);
	int pos = rand() % length;
	cout << endl << "Modificam caracterul de pe pozitia: " << pos << endl;

	if (text2[pos] == 'z')
		text2[pos] = 'a';
	else if (text2[pos] == 'Z')
		text2[pos] = 'A';
	else 
		text2[pos]++;


	string s2 = SHA1(text2);
	cout << endl << "s1: " << s1 << endl;
	cout << "s2: " << s2 << endl << endl;
    
	cout << "Distanta Hamming: " << Hamming(s1, s2) << endl;

	//BIRTHDAY ATTACK

	string outputs[10000];
	int collisions = 0;
	long long p = 64;      //sqrt(2^n) pentru 50% sansa de a gasi o coliziune
	
	for (long long i = 0; i < p; i++)
	{
		//cream un sir de caractere random
		int nr = rand() % 15 + 1;
		char s[20] = {'\0'};
		for (int j = 0; j < nr; j++)
		{
			int c = rand() % 62;
			if (c < 26)            //a-z
				s[j] = (c + 'a');
			else if (c < 52)       //A-Z
				s[j] = (c - 26 + 'A');
			else s[j] = (c -52 + '0');  //0-9 
		}
		//numaram aparitiile
		string s2 = truncate(SHA1(s), 3);
		for (long long j = 0; j < p; j++)
			if (s2 == outputs[j])
				collisions++;
		outputs[i] = s2;
	}
	cout << endl << "Collisions: " << collisions << endl;


	return 0;
}