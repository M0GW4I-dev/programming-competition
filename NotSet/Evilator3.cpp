#include <iostream>
using namespace std;

int main(){
		string row(100000,'\0');
		cin >> row;
		int ans=0;
		int num=row.size();
		for(int i=0;i<num;i++){
				if(row[i]=='U'){
						ans+=num-1-i;
						ans+=2*i;
				}else{
						ans+=i;
						ans+=(num-1-i)*2;
				}
		}
		cout << ans << endl;
		return 0;
}
