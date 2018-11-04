#include <cstdio>
#include <algorithm>
using namespace std;
#define MAX_V 100
#define INF 1000000
int d[MAX_V+1][MAX_V+1];
int V;
void solve(){
		int M,R;
		scanf("%d %d %d",&V,&M,&R);
		int r[R];
		for(int i=0;i<R;i++){
				scanf("%d",&r[i]);
		}
		int a,b,c;
		for(int i=0;i<M;i++){
				scanf("%d %d %d",&a,&b,&c);
				d[a][b]=min(d[a][b],c);
				d[b][a]=min(d[b][a],c);
		}
		for(int i=0;i<R;i++){
				for(int i=0;i<V;i++){
						for(int j=0;j<V;j++){
								d[i][j]=min(d[i][j],d[i][r[i]]+d[r[i]][j]);
								printf("%d\n",d[i][j]);
						}
				}
		}
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
		
