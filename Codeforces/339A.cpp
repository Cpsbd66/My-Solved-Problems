#include <iostream>
#include <string>

using namespace std;

int main() {
    string s;
    cin >> s;
    int n1 = 0, n2 = 0, n3 = 0;
    for (int i = 0; i < s.length(); i += 2) {
        if (s[i] == '1') {
            n1++;
        } else if (s[i] == '2') {
            n2++;
        } else {
            n3++;
        }
    }
    string ss = "";
    for (int i = 0; i < n1; i++) {
        ss += "1+";
    }
    for (int i = 0; i < n2; i++) {
        ss += "2+";
    }
    for (int i = 0; i < n3; i++) {
        ss += "3+";
    }
    cout << ss.substr(0, ss.length() - 1) << endl;
    return 0;
}
