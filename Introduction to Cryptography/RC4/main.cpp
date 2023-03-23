#include<iostream>
#include <fstream>
#include <cstring>
#include <string>
#include <time.h> 
using namespace std;
ifstream Text;

int S[256], key[256], M[256];
int N = 256, L = 16;
int lenghtPlainText=0;


void KSA()
{
	for (int i = 0; i <= N-1; i++)
		S[i] = i;
	int j = 0;
	for (int i = 0; i <= N-1; i++)
	{
		j = (j + S[i] + key[i % L]) % N;
		swap(S[i], S[j]);
	}
}

void PRGA()
{
	int j = 0;
	int i = 0;
	for(i = i + 1; i <= lenghtPlainText; i++)
	{
		i = i % N;
		j = (j + S[i]) % N;
		swap(S[i], S[j]);
		M[i] = S[(S[i] + S[j]) % N];
	} 
}



int main()
{
	ifstream input;
	ofstream output;
	input.open("TEXT.txt");
	output.open("PLAINTEXT.txt");
	//CREARE PLAINTEXT: ADAUGAM DOAR toupper(litera)
	char c;
	while (input.get(c))
	{
		if (c >= 'a' && c <= 'z')
		{
			c = toupper(c);
			lenghtPlainText++;
		}
		if (c >= 'A' && c <= 'Z')
		{
			output << c;
			lenghtPlainText++;
		}
	}
	//CHEIE

	srand(time(NULL));
	for (int i = 0; i < L; i++)
		key[i] = rand() % 255;
	cout << "key = ";
	for (int i = 0; i < L; i++)
		cout << key[i] << ' ';
	cout << endl;

	
	KSA();
	cout << endl << "S = ";
	for (int i = 0; i < N; i++)
		cout << S[i] << ' ';
	cout << endl;
 
	PRGA();
	cout << endl << "Length of plainText is: " << lenghtPlainText << endl;
	cout << "KeyStream is: ";
	for (int i = 1; i <= lenghtPlainText; i++)
		cout << M[i] << ' ';


	//generam textul criptat cu numere facand xor intre KeyStream (M) si PlainText
	input.close();
	output.close();
	input.open("PLAINTEXT.txt");
	output.open("ENCRYPTED_NUMBERS.txt");
	int poz = 0;
	while (input.get(c))
	{
		output << (c - 'A' + M[poz]) % (N - 1);
		output << ' ';
	}
	input.close();
	output.close();

	//Verificare bias-uri
	double bit2 = 0;
	for (int k = 0; k < 100000; k++) 
	{
		for (int i = 0; i < L; i++)
			key[i] = rand() % 255;
 
		KSA();
		PRGA();

		if (M[2] == 0)
			bit2++;
	}

	cout << endl << endl << "Probability for second bit to be 0: " << bit2 / 100000.0;

	// 1/128 = 0.0078125
 
	return 0;
}