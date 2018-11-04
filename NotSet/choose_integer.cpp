#include <iostream>
#include <stdlib.h>
using namespace std;

int main(void){
		int a,b,c;
		cin >> a >> b >> c;
		int f=0;
		for(int sum=1;sum<1000000;sum++){
				if(sum%b==c && sum%a==0){
						f=1;
						break;
				}
		}
		if(f==0){
				cout << "NO" << endl;
		}else{
				cout << "YES" << endl;
		}
		exit(0);
}
