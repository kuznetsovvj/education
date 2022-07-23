#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;


vector<int64_t> items;

int main() {
    int64_t t;
    cin >> t;

    for (size_t c = 0; c < t; c++) {
        items.clear();
        int64_t n, l, r;
        cin >> n >> l >> r;
        items.resize(n);
        int64_t value;
        for (size_t z = 0; z < n; z++) {
            cin >> value;
            items[z] = value;
        }

        sort(items.begin(), items.end());
        int64_t res = 0;
        int64_t down = n - 1;
        int64_t up = n - 1;
        bool upflag, downflag;
        int64_t k = 0;
        bool alreadyPrinted = false;
        while (k < n - 1) {
            alreadyPrinted = false;
            upflag = false;
            downflag = false;
            while (items[k] + items[up] > r && up > k + 1) {
                up--;
            }
            if (items[k] + items[up] <= r) {
                upflag = true;
            }
            int64_t down_j = k + 1;
            while (items[k] + items[down_j] < l && down_j < down) {
                down_j++;
            }
            if (items[k] + items[down_j] >= l) {
                downflag = true;
            }
            k++;
            if (!downflag) {
                continue;
            }
            if (!upflag) {
                cout << res << endl;
                alreadyPrinted = true;
                break;
            }
            res = res + up - down_j + 1;
            if (down_j + 1 < n - 1) {
                down = down_j + 1;
            }
            else {
                down = n;
            }
        }
        if (!alreadyPrinted) {
            cout << res << endl;
        }
    }
}