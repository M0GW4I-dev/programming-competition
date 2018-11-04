#include <iostream>
#include <stdlib.h>

using namespace std;

int main(void){
		int N,T;
		cin >> N >> T;
		int t[N];
		for(int i=0;i<N;i++){
				cin >> t[i];
		}
		int length=0;
		int sum=0;
		for(int i=1;i<N;i++){
				if(T>t[i]){
						length+=t[i];
				}else{
						length+=T;
				}
				sum+=t[i];
		}
		length+=t[N-1];

		cout << length << endl;
		exit(0);
}
				

		

