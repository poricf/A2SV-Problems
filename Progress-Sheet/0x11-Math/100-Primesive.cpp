#include <bits/stdc++.h>
using namespace std;

#define all(x) x.begin(), x.end()
#define ll long long

void primeSieve(vector<ll>& v, ll n) {
    v[0] = 0;
    v[1] = 0;

    for (ll i = 2; i < n; i++) {
        if (v[i] == 1) {
            for (ll j = i*i; j < n; j += i) {
                v[j] = 0;
            }
        }
    }
}

ll countPrimes(ll n) {
    if (n < 2) return 0;

    vector<ll> prime(n, 1);
    primeSieve(prime, n);
    ll res = count(all(prime), 1);
    return res;
}

int main() {
    ll n;
    cin >> n;
    cout << countPrimes(n) << endl;
    return 0;
}