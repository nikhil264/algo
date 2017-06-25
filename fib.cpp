#include <iostream>

using namespace std;

long memo[10000] = {0};

long fib(int n){
	if (memo[n]) return memo[n];
	if(n<3 ) return 1;
	memo[n] = fib(n-1)+fib(n-2);
	return memo[n];

}

int main(int argc, char const *argv[])
{	int n;
	cin>>n;
	for (int i = 1; i <= n; ++i)
		cout<<fib(i)<<endl;
	
	return 0;
}