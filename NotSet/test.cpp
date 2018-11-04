#include <iostream>
using namespace std;

int main(void){
		int ar[200];
		for(int i=0;i<200;i++){
				ar[i]=i%100;
		}
		sort(ar,ar+200);
		for(int i=0;i<200;i++){
				cout << ar[i] << endl;
		}
}


