#include <iostream>
using namespace std;

int main(void){
	int N,M;
	cin >> N >> M;
	int road[N];
	int c;
	for(int i=0;i<N;i++){
		road[i]=0;
	}
	for(int i=0;i<M*2;i++){
		cin >> c;
		road[c-1]++;
	}
	for(int i=0;i<N;i++){
			cout << road[i] << endl;
	}
	return 0;
}
