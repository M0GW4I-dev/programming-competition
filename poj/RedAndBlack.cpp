#include <cstdio>
#define MAX_H 100
#define MAX_W 100

char maze[MAX_H][MAX_W];
int dx[4] = { 0,1,0,-1},dy[4] = {-1,0,1,0},ans,w,h;
void rec(int ny,int nx){
		maze[ny][nx]='#';
		ans++;
		for(int i=0;i<4;i++){
				if( 0 <= ny+dy[i] && ny+dy[i] < h && 0<=nx+dx[i] && nx+dx[i]<w && maze[ny+dy[i]][nx+dx[i]]=='.'){
						rec(ny+dy[i],nx+dx[i]);
				}
		}
}

int main(){
		for(int k=0;k<5;k++){
				int startx,starty;
				ans = 0;
				scanf("%d %d",&w,&h);
				for (int i=0;i<h;i++){
						scanf("%s",maze[i]);
						for(int j=0;j<w;j++){
								if (maze[i][j]=='@'){
										startx=j;
										starty=i;
								}
						}
				}
				rec(starty,startx);
				printf("%d\n",ans);
		}
}

