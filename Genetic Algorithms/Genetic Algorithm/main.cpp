#include <iostream>
#include <ctime>
#include <iomanip>
#include <chrono>
#include <algorithm>
#include <random>
#include <iomanip>
using namespace std;

#define PI 3.14159

//double a = -500, b = 500;   //schwefel
//double a=-5.12, b = 5.12;  //de jong, rastring
int D = 30;
double a = 0, b = PI;   //michalewicz

 
double de_jong(double x[])  //De Jong1
{
	double s = 0;
	for (int i = 0; i < D; i++)
		s += (x[i] * x[i]);
	return s;
}

double rastring(double x[])  //Rastring's
{
	double s = 0;
	for (int i = 0; i < D; i++)
	{
		double n = x[i] * 2 * PI;
		s += (x[i] * x[i] - 10 * cos(n));
	}
	s += 10 * D;
	return  s;
}

double schwefel(double x[])   //Schwefel's  a=-500, b=500
{
	double s = 0;
	for (int i = 0; i < D; i++)
		s -= x[i] * sin(sqrt(abs(x[i])));
	return s;
}

double michalewicz(double x[])  //Michalewicz's  a= 0,  b=PI
{

	double s = 0;
	for (int i = 0; i < D; i++)
		s -= (sin(x[i]) * pow(sin(((i + 1) * x[i] * x[i]) / PI), 20));
	return s;
}


void bitstring(int vc[], int L)
{
	for (int i = 0; i < L; i++)
		vc[i] = rand() % 2;
}


void evaluate(int v[], int l, double sol[])
{
	double s = 0;

	for (int i = 0; i < l * D; i++)
	{
		s *= 2;
		s += v[i];
		if ((i + 1) % l == 0)
		{
			s = s / (pow(2, l) - 1);
			s *= (b - a);
			s += a;

			sol[int(i / l)] = s;
			s = 0;
		}
	}
}



int** population_generator(int population_size, double L)
{
	int** pop = 0;
	pop = new int* [population_size];
	for (int i = 0; i < population_size; i++)
	{
		pop[i] = new int[L];
		int v[1001];
		bitstring(v, L);  //generam random o linie din matrice
		for (int j = 0; j < L; j++)
			pop[i][j] = v[j];
	}
	return pop;

}


double fitness(double value)
{
	double res;
	//res = value - 999999;
	res = 1 / (999999999+value);
	return res;
}

 

int** evaluate_population(int population_size, int** pop, int l, int elitism, double &global_minima)
{
	double fitness_sum = 0;
	float min_value = 999999999;
	float max_value = -999999999;
	double** data = 0;
	data = new double* [population_size];
	for (int i = 0; i < population_size; i++)
	{
		data[i] = new double[4];
		data[i][0] = i;  //indicele
		double decimal[1001];
		evaluate(pop[i], l, decimal);
		data[i][1] = michalewicz(decimal);  //valoarea functiei
		if (data[i][1] < min_value)
			min_value = data[i][1];    //min value from pop
		 

		data[i][2] = fitness(data[i][1]);  //fitness-ul valorii
		fitness_sum += data[i][2];         //total fitness
	}
  
	for (int i = 0; i < population_size; i++)
		data[i][2] /= fitness_sum;     //probabilitatea de selectie individuala
	
	//sortam matricea crescator dupa valoarea functiei, data[0][1] cea mai mica valoare

	int ok;
	do {
		ok = 0;
		for (int i = 0; i < population_size - 1; i++)
			if (data[i][1] > data[i + 1][1])
			{
				swap(data[i][0], data[i + 1][0]);
				swap(data[i][1], data[i + 1][1]);
				swap(data[i][2], data[i + 1][2]);
				swap(data[i][3], data[i + 1][3]);
				ok = 1;
			}
	} while (ok == 1);

	//salvam solutiile elitism intr-o populatie noua
	int** pop2 = population_generator(population_size, l * D);     //new population
	for (int i = 0; i < elitism; i++)
		for (int j = 0; j < l * D; j++)
			pop2[i][j] = pop[(int)data[i][0]][j];


	//sortam matricea crescator dupa valoarea fitness-ului, data[0][2] cea mai mica valoare

	do {
		ok = 0;
		for (int i = 0; i < population_size - 1; i++)
			if (data[i][2] > data[i + 1][2])
			{
				swap(data[i][0], data[i + 1][0]);
				swap(data[i][1], data[i + 1][1]);
				swap(data[i][2], data[i + 1][2]);
				swap(data[i][3], data[i + 1][3]);
				ok = 1;
			}
	} while (ok == 1);





	data[0][3] = data[0][2];
	for (int i = 0; i < population_size - 1; i++)
		data[i + 1][3] = data[i][3] + data[i][2];        //probabilitatea cumulativa
	data[population_size - 1][3] = 1;

	
	/*
	for (int i = 0; i < population_size; i++)
	{
		for (int j = 0; j < 4; j++)
			cout << fixed << setprecision(5)<<data[i][j] << ' ';
		cout << endl;
	}
	cout << endl;
	*/
	
	

	//selectam restul cromozomilor pentru populatia noua
	for (int i = elitism; i < population_size; i++)
	{
		float probability = (float)rand() / (float)RAND_MAX;  //generate random probability
		for (int j = 0; j < population_size; j++)
			if (probability < data[i][3])
			{
				int index = data[i][0];
				for (int k = 0; k < l * D; k++)
					pop2[i][k] = pop[index][k];
				break;
			}			
	}

 
	//update global minima
	if (min_value < global_minima)
		global_minima = min_value;

	return pop2;
}


void crossover(int population_size, int** pop, int l, int elitism, float pc)
{
	//SELECT PARENTS FOR CROSSOVER
	int parents[2001];        //vector in care memoram indecsii parintilor cu care facem cross
	int index = 0;
	for (int i = elitism; i < population_size; i++)
	{
		float probability = (float)rand() / (float)RAND_MAX;  //generate random probability between 0 and 1
		if (probability < pc)
		{
			parents[index] = i;    //index from population
			index += 1;
		}
	}
	//CROSS OPERATION
	int nr_parents = index;
	int seed = rand() % 1000;

	shuffle(parents, parents + nr_parents, default_random_engine(seed));
	/*
	for (int i = 0; i < nr_parents; i++)
		cout << parents[i] << ' ';
	cout << endl;
	*/

	int index_first_parent, index_second_parent;
	for (int k = 0; k < 2; k++)
	{
		for (int i = 0; i < nr_parents - 1; i += 2)
		{
			index_first_parent = parents[i];
			index_second_parent = parents[i + 1];
			int pos = rand() % (l * D - 2) + 1;  //position for cut
			//cout << index_first_parent << ' ' << index_second_parent << ' ' << pos << endl;

			for (int j = pos; j < l * D; j++)
			{
				int aux = pop[index_first_parent][j];
				pop[index_first_parent][j] = pop[index_second_parent][j];
				pop[index_second_parent][j] = aux;
			}
		}

	}
	
}


void mutate(int population_size, int** pop, int l, int elitism, float p_mut)
{
	for (int i = elitism; i < population_size; i++)
	{
		//int nr = 0;
		for (int j = 0; j < l * D; j++)
		{
		
			float probability = (float)rand() / (float)RAND_MAX;
			if (probability < p_mut)
			{
				//nr++;
				if (pop[i][j] == 1)
					pop[i][j] = 0;
				else pop[i][j] = 1;
			}

		}
		//if (nr != 0)cout << nr << endl;
	}
	
}


int main()
{
	srand(time(0));
	double l, L, t = 0, best;
	bool local = false;
	best = 999999;
	l = floor(log2((b - a) * pow(10, 5))) + 1;
	L = D * l;                      //dimensiunea vc
	int population_size = 200;  //200
	int elitism = 35;		  //15  //25  //35
	double global_minima = 999999999;
	float pc = 0.9;          //the probability for crossover
	float p_mut = 0.001;      //the probability for mutation  

	//####################### Generam populatia random ########################

	int **pop = population_generator(population_size, L);   //initial population
	
 
	cout << "CROSS-RATE = " << pc << endl;
	cout << "MUTATION RATE = " << p_mut << endl;
	auto start = std::chrono::steady_clock::now();

	global_minima = 999999999;
	for (int i = 0; i < 2000; i++)
	{
		pop = evaluate_population(population_size, pop, l, elitism, global_minima);
		cout << i << ' ' << fixed << setprecision(5) << global_minima << endl;
		crossover(population_size, pop, l, elitism, pc);
		mutate(population_size, pop, l, elitism, p_mut);
	}

	//cout << "GLOBAL MINIMA: " << fixed << setprecision(5) << global_minima;
	cout << fixed << setprecision(5) << global_minima<<endl;
			
	auto end = std::chrono::steady_clock::now();
	double time = double(std::chrono::duration_cast<std::chrono::nanoseconds> (end - start).count());
	cout << "time: " << time / 1e9<<endl;

	

	
	

	return 0;
}