#include <iostream>
#include <vector>

using namespace std;

typedef struct Node {
    char data;
    struct Node *next;
    struct Node *prev;
} Node;

int main(void) {
    int M;  // 입력할 명령어의 갯수
    string text;
    vector<char>::iterator it;

    cin >> text;
    cin >> M;

    int length = text.size();
    Node* head = new Node();    // empty node
    Node* tail = head;
    for (int i=0; i<length; i++) {
        Node* newNode = new Node();
        newNode->data = text[i];

        tail->next = newNode;
        newNode->prev = tail;
        
        tail = newNode;
    }

    Node* cursor = tail;

    for (int i=0; i<M; i++) {
        string command;
        string newchar;
        cin >> command;

        if (command == "P") {
            cin >> newchar;
            Node* newNode = new Node();
            newNode->data = newchar[0];

            newNode->next = cursor->next;
            newNode->prev = cursor;
            if (newNode->next != NULL) {
                newNode->next->prev = newNode;
            }
            if (newNode->prev != NULL) {
                newNode->prev->next = newNode;
            }
            cursor = newNode;
            length += 1;
        } else if (command == "L") {
            if (cursor->prev != NULL) {
                cursor = cursor->prev;
            }
        } else if (command == "D") {
            if (cursor->next != NULL) {
                cursor = cursor->next;
            }
        } else if (command == "B") {
            if (cursor->prev != NULL) {
                cursor->prev->next = cursor->next;
                if (cursor->next != NULL) {
                    cursor->next->prev = cursor->prev;
                }
                cursor = cursor->prev;
                length -= 1;
            }
        }
        
        // cout << command;
        // cout << cursor->data << endl;
    }

    Node* currentNode = head->next;
    while (currentNode != NULL) {
        cout << currentNode->data;
        currentNode = currentNode->next;
    }

    return 0;
}