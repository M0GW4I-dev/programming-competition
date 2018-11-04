#include <cstdio>
#include <algorithm>
using namespace std;
#define MAX_N 100000
int n[MAX_N];
bool table[100000];

int main(){
		int x;
		scanf("%d",&x);
	    for(int i=0;i<x;i++){
		    scanf("%d",&n[i]);
	    }
		sort(n,n+x);
		int temp=n[0],ans=0;
		bool f=true;
		for(int i=1;i<x;i++){
				if(temp!=n[i]){
						if(f){
								ans++;
						}
						temp=n[i];
						f=true;
				}else{
						f=!f;
				}
		}
		printf("%d\n",ans);
		return 0;
}
			   

