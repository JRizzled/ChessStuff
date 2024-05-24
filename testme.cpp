#include <iostream>
#include <chrono>
#include <iomanip>

using namespace std::chrono;

int main()
{
    int arr[10000];
    for(int i = 0; i < 10000; i++)
    {
        arr[i] = i;
    }
    auto start = high_resolution_clock::now();
    for (int i = 0; i <10000; i++)
    {
        arr[i] = arr[i] *2;
    }
    auto stop= high_resolution_clock::now();
    auto d = duration_cast<nanoseconds>(stop - start);
    double ab = ((double) d.count()) / 1000000000;
    std::cout << "C++ array opperation took   "<< std::fixed << std::setprecision(17) << ab << std::endl;
    
}