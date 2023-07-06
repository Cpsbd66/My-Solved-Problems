#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define print(x) cout << #x << " = " << x << endl
#define int long long 

vector<int> a;

void run(int n){
    cout << *lower_bound(a.begin(), a.end(), n) << endl;
}

int32_t main()
{

    for( int i=1 ; i<10 ; i++ )
    {
        int sum = 0;
        for(int j=0, ten = 1 ; j<=18 ; j++, ten *= 10){
            sum += ten * i;
            a.push_back(sum);
        }
    }
    
    sort(a.begin(), a.end());
    // for( int i=0 ; i<100 ; i++ )cout << a[i] << endl;
    

    int n;
    cin >> n;
    cout << *lower_bound(a.begin(), a.end(), n) << endl;
    
    return 0;
}
