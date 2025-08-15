#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    ll n;
    cin >> n;
    ll res = 0;
    vector<ll>v(n, 0);

    for (ll i = 0; i < n; i++) {
        cin >> v[i];
    }

    for (ll i = 0; i < n; i++) {
        ll sum = 0;
        for (ll j = i; j < n; j++) {
            sum += v[j];

            if (sum == 0) {
                res += 1;
            }
        }
    }

    cout << res;
}