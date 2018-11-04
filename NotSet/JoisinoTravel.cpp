#include <cstdio>
#include <algorithm>
using namespace std;
#define MAX_V 200
#define INF 1000000
int d[MAX_V][MAX_V];
int r[MAX_V];
int V,R;

void solve(){
		int N,M;
		scanf("%d %d %d",&V,&M,&R);
		for(int i=0;i<R;i++){
				scanf("%d",&r[i]);
		}
		int a,b,c;
		for(int i=0;i<M;i++){
				scanf("%d %d %d",&a,&b,&c);
				for(int i=0;i<R;i++){
						if(r[i]==a || r[i]==b){
								d[a][b]=min(d[a][b],c);
								d[b][a]=min(d[b][a],c);
						}
				}
		}
		int ans;
		for (int k=0;k<V;k++){
				for(int i=0;i<V;i++){
						for(int j=0;j<V;j++){
								d[i][j]=min(d[i][j],d[i][k]+d[k][j]);
								ans=d[i][j];
						}
				}
		}
		printf("%d\n",ans);
}

int main(){
		for(int i=0;i<MAX_V;i++){
				for(int j=0;j<MAX_V;j++){
						d[i][j]=INF;
				}
		}
		solve();
		return 0;
}
