#include <iostream>
#include <iomanip>
#include <cmath>
#include <ctime>
#include <chrono>

using namespace std;
#define MAX 10000
#define pi 3.14159

float a = -5.12, b = 5.12;
int D = 30;


double eval(double x[])
{
    double s = 0;
                        //de jong 1
     for(int i=0;i<D;i++)
          s+=(x[i]*x[i]);
  

 //Schwefel's function 7
    /*
  for(int i=0;i<D;i++)
      s+=( -1*x[i]*sin(sqrt(abs(x[i]))));
      */
                      //Rastrigin's function 6
  /*
      for(int i=0;i<D;i++)
           s+=(x[i]*x[i] - 10*cos(2*pi*x[i]));
      s+=10*D;
  */
  //Michalewicz's
    /*
    int m = 10;
    for (int i = 0; i < D; i++)
        s += (sin(x[i]) * pow(sin((i + 1) * x[i] * x[i] / pi), 2 * m));
    s *= -1;
    */
    return s;

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
void bitstring(int vc[], int L)
{
    for (int i = 0; i < L; i++)
        vc[i] = rand() % 2;
}
void select_vn(int vn[], int vc[], int L, int poz)
{
    for (int i = 0; i < L; i++)
        vn[i] = vc[i];
    poz = poz % L;
    if (vn[poz] == 1)
        vn[poz] = 0;
    else vn[poz] = 1;
}
void vc_vn(int vc[], int vn[], int L, int poz)   //vc <- vn, schimbam bitul de pe pozitia poz
{
    poz = poz % L;
    if (vc[poz] == 1)
        vc[poz] = 0;
    else vc[poz] = 1;
}
double results[31];
double executions_time[31];

int main()
{
    cout << "D= " << D << endl;
    cout << "Simulated Annealing" << endl;

    srand(time(0));
    double l, L, T = 500;
    int t = 0;
    l = floor(log2((b - a) * pow(10, 5))) + 1;
    L = D * l;                      //dimensiunea vc
    int vc[1001], vn[1001];
    bitstring(vc, L);
    double decimal_vn[1001], decimal_vc[1001];
    evaluate(vc, l, decimal_vc);

    int poz;
     
    
    for (int k = 1; k <= 30; k++) {
        auto start = std::chrono::steady_clock::now();

        T = 500;
        t = 0;
        do {
            int nr = 0;
           

            do {
                nr++;
                select_vn(vn, vc, L, nr);
                evaluate(vn, l, decimal_vn);
                evaluate(vc, l, decimal_vc);

                if (eval(decimal_vn) < eval(decimal_vc))    //vn better than vc
                    vc_vn(vc, vn, L, nr);   //vc <- vn
                else if (float(rand() % 99999) / 100000 < exp(-1 * abs(eval(decimal_vn) - eval(decimal_vc)) / T))
                    vc_vn(vc, vn, L, nr);

            } while (nr != L * 10);
            T = T * 0.95;
            t++;
            evaluate(vc, l, decimal_vc);
            //cout<<"Solutia "<<int(t)<<" = "<<fixed<<setprecision(10)<<eval(decimal_vc)<<endl;
        } while (t != MAX && T >= 0.00001);


        //evaluate(vc,l,decimal_vc);
        //cout<<fixed<<setprecision(10)<<eval(decimal_vc)<<endl;
        results[k] = eval(decimal_vc);
        auto end = std::chrono::steady_clock::now();
        double time = double(std::chrono::duration_cast<std::chrono::nanoseconds> (end - start).count());
        executions_time[k] = time / 1e9;
    }

    cout << "RESULTS:" << endl;
    for (int k = 1; k <= 30; k++)
        cout << fixed << setprecision(5) << results[k] << endl;
    cout <<endl<< "TIME:" << endl;
    for (int k = 1; k <= 30; k++)
        cout << fixed << setprecision(5) << executions_time[k] << endl;

    return 0;
}
