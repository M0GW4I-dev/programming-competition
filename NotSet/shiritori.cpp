#include <iostream>
#include <stdlib.h>
using namespace std;

int main(void){
		string a[3];
		int f=0;
		cin >> a[0] >> a[1] >> a[2];
		for(int i=0;i<2;i++){
				int len = a[i].size();
				if(a[i][len-1]!=a[i+1][0]){
						f=1;
						break;
			}
		}
		if(f==0){
				cout << "YES" << endl;
		}else{
				cout << "NO" << endl;
		}
		exit(0);
}
