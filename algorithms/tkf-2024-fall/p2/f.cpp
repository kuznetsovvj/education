#include <iostream>
#include <map>
#include <deque>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);


    int n;
    cin >> n;

    deque<int> deq;
    map<int, int> pos;
    int out = 0;

    int cmd;
    int id;

    for (int i = 0; i < n; i++) {
        cin >> cmd;

        if (cmd == 1) {
            cin >> id;
            pos[id] = deq.size() + out;
            deq.push_back(id);
            continue;
        } 
        if (cmd == 2) {
            deq.pop_front();
            out = out + 1;
            continue;
        } 
        if (cmd == 3) {
            deq.pop_back();
            continue;
        }
        if (cmd == 4) {
            cin >> id;
            cout << pos[id] - out << endl;
            continue;
        }
        if (cmd == 5) {
            cout << deq.front() << endl;
        }
    }
}