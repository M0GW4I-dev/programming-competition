#include <iostream>
using namespace std;

int main(){
		long int n,a,b;
		cin >> n >> a >> b;
		long int ans=(b-a+1)+(n-3)*b-(n-3)*a; 
		if(ans<=0){
				cout << 0 << endl;
		}else{
				cout << ans << endl;
		}
		return 0;
}
