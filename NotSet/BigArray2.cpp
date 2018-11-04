#include <iostream>
#include <utility>
using namespace std;

int main(void){
		int N,K,ai,bi;
		cin >> N >> K;
		vector<pair<int,int> > p(N);

		for(int i=0;i<N;i++){
				cin >> p[i].first >> p[i].second;
		}

		sort(p.begin(),p.end(),[](const pair& x, const pair& y) { return x.first < y.first;});

		for(int i=0;i<N;i++){
				cout << p[i].first << p[i].second << endl;

		}
		return 0;
}




