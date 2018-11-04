#include <iostream>
using namespace std;

string row;
int main(){
		cin >> row;
		int count=row.size();
		int ans=0;
		for(int i=0;i<count;i++){
				for(int c=0;c<count;c++){
						if(c==i) continue;
		if(row[i]=='U'){
				if(i<c){
						ans+=1;
				}else{
						ans+=2;
				}
		}else{
				if(i>c){
						ans+=1;
				}else{
						ans+=2;
				}
		}
				}
		}
		cout << ans << endl;
}


				


