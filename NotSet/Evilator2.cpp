#include <iostream>
using namespace std;

int main(){
		string row;
		cin >> row ;
		int count = row.size();
		int ans=0;
		for(int i=0;i<count;i++){
				if(i==0){
						ans+=(count-1);
				}else if(i==count-1){
						ans+=(count-1);
				}else{
					if(row[i]=='U'){
							ans+=count-1-i;
							ans+=(i*2);
					}else{
							ans+=i;
							ans+=((count-1-i)*2);
					}
				}
		}
		if(ans<=0) ans=0;
		cout << ans << endl;
		return 0;
}
