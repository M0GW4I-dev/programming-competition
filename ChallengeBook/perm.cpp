#include <cstdio>

using namespace std;

int perm[3];
bool used[3];

void permutation(int pos,int n){
		if(pos==n){
				for(int i=0;i<n;i++){
						printf("%d ",perm[i]);
				}
				printf("\n");
				return;
		}
		for(int i=0;i<n;i++){
				if(!used[i]){
						perm[pos]=i;
						used[i]=true;
						permutation(pos+1,n);
						used[i]=false;
				}
		}
		return;
}

int main(){
		permutation(0,3);
}
