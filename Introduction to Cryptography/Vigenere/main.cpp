#include <iostream>
#include <fstream>
#include <cstring>
#include <string>
using namespace std;
ifstream Text;

int frequency[26];

int main()
{

	ifstream input;
	ofstream output;
	input.open("TEXT.txt");
	output.open("PLAINTEXT.txt");
	//CREARE PLAINTEXT: ADAUGAM DOAR toupper(litera) si spatiile ' '
	char c;
	while (input.get(c))
	{
		if (c >= 'a' && c <= 'z')
			c = toupper(c);
		if (c >= 'A' && c <= 'Z')
			output << c;
	}
	//CHEIE
	char key[21] = "ABABAB";
	input.close();
	output.close();
	input.open("PLAINTEXT.txt");
	output.open("ENCRYPTED_NUMBERS.txt");
	//CREARE ENCRYPTED TEXT CU NUMERE: formula c_i=(p_i+k_(i mod 26))mod 26
	int index = 0;
	int n;
	while (input.get(c))
	{
		n = (c - 'A' + (key[index % 26] - 'A')) % 26;
		index++;
		if (index == strlen(key))
			index = 0;
		output << n;
		output << ' ';
	}
	input.close();
	output.close();
	input.open("ENCRYPTED_NUMBERS.txt");
	output.open("ENCRYPTED_TEXT.txt");
	//ENCRYPTED TEXT
	string encrypted_text;
	while (input.get(c))
	{
		int index;
		if (c != ' ')
		{
			index = c - '0';
			input.get(c);
			if (c != ' ')
			{
				n = c - '0';
				index = index * 10 + n;
			}
			output << char(index + 'A');
			encrypted_text.push_back(char(index + 'A'));
		}
	}
	input.close();
	output.close();
	//determinarea frecventei in textul criptat
//	input.open("ENCRYPTED_TEXT.txt");
//	while (input.get(c))
//	{
//		frequency[c - 'A']++;
//	}
//	input.close();
	//determinarea indexului de coincidente IC
	double m = 2; //presupunem ca lungimiea initiala a cheii este 2
	double IC;
	double length;

	while (m <= 30)     //lungimea maxima a cheii este 30
	{

		double sum = 0;
		for (int j = 0; j < m; j++)
		{
			IC = 0;
			length = 0;
			for (int i = 0; i < 26; i++)
				frequency[i] = 0;
			for (int i = j; i < encrypted_text.length(); i += m)
			{
				length++;
				frequency[encrypted_text[i] - 'A']++;
			}

			for (int i = 0; i < 26; i++)
				IC = IC + ((double)frequency[i] * ((double)frequency[i] - 1)) / (length * (length - 1));
			sum += IC;
		}


		sum /= m;
		if (abs(0.065 - sum) < 0.01)
		{
			//cout << endl << "DA" << ' ' << m << ' ' << sum << ' ' << endl;
			length = m;
			m = 30;
		}
		//cout << m << ' ' << sum << endl;
		m++;
	}

	m--;
	cout << "length=" << length;
	//determinarea cheii
	double MIC;
	int count, s;
	double eng_letters[26] = { 8.55 ,1.60,3.16,3.87,12.10,2.18,2.09,4.96,7.33,0.22,0.81,4.21,2.53,7.17,7.47,2.07,0.10,6.33,6.73,8.94,2.68,1.06,1.83,0.19,1.72,0.11 };
	//frecventa literelor in lb engleza
	int kj;
	char KEY[30];
	for (int i = 0; i < length; i++)
	{
		s = -1;
		MIC = 0;
		while (abs(0.065 - MIC) > 0.01)
		{
			count = 0;
			for (int j = 0; j < 26; j++)
				frequency[j] = 0;
			s++;
			for (int j = i; j < encrypted_text.length(); j += length)
			{
				count++;
				frequency[(encrypted_text[j] - 'A' + s) % 26]++;

			}
			MIC = 0;
			for (int j = 0; j < 26; j++)
			{
				MIC = MIC + (double)(eng_letters[j] / 100 * (double)frequency[j] / count);
			}
		}
		kj = (26 - s) % 26;
		KEY[i] = (char)(kj + 'A');

	}
	KEY[(int)length] = NULL;
	cout << endl << KEY;

	return 0;
}