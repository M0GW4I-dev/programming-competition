#include <iostream>
using namespace std;

int main(void){
		int N,K;
		cin >> N >> K;
		int a,b=0,count,max=-1,flag=0,ans;
		for(int i=0;i<N;i++){
				cin >> a >> b;
			if(a>max){
					max=a;
			}
			if(flag==0){
			count+=b;
			if(K>=count){
					ans=a;
			}
			flag=1;
			}
		}
		cout << ans << endl;
		return 0;
}

				
