#include <iostream>
#include <vector>

using namespace std;

class Node {
    private:
        Node* next;
        Node* prev;

    public:
        int id;
        void set_next(Node* next);
        void set_prev(Node* next);
        void delete_next();
        void delete_prev();
        Node* get_next();
        Node* get_prev();

        Node(int _id) {
            id = _id;
        }
};

class CircularLinkedList {
    public:
        Node* head;
        Node* tail;

        CircularLinkedList(int N) {
            head = new Node(1);
            tail = head;

            for (int i=1; i<N; i++) {
                tail->set_next(new Node(i+1));
                tail->get_next()->set_prev(tail);
                tail = tail->get_next();
            }

            tail->set_next(head);
            head->set_prev(tail);
        }
};

void Node::set_next(Node* _next) {
    next = _next;
}

void Node::delete_next() {
    if (next == NULL) {
        // the last node
        return;
    }

    Node* nextNode = next;
    next = nextNode->get_next();
    next->set_prev(this);
    delete nextNode;
}   

void Node::delete_prev() {
    if (prev == NULL) {
        // the first node
        return;
    }

    Node* prevNode = prev;
    prev = prevNode->get_prev();
    prev->set_next(this);
    delete prevNode;
}   

void Node::set_prev(Node* _prev) {
    prev = _prev;
}

Node* Node::get_next() {
    return next;
}

Node* Node::get_prev() {
    return prev;
}

int main(void) {
    int N, K;
    cin >> N;
    cin >> K;

    vector<int> sequence;

    // cout << "N: " << N << ", K: " << K << endl;

    CircularLinkedList l = CircularLinkedList(N);

    Node* currentNode = l.head;

    int iteration = 0;
    while (iteration < N) {
        for (int j=0; j<K; j++) {
            if (iteration == 0 && j == 0) {
                continue;
            }
            currentNode = currentNode->get_next();
            if (j == 0) {
                currentNode->delete_prev();
            }
        }
        sequence.push_back(currentNode->id);
        iteration++;
    }

    // for (int i=0; i<N; i++) {
    //     sequence.push_back(currentNode->id);
    //     currentNode = currentNode->get_next();
    // }

    cout << "<";
    for (int i=0; i<sequence.size() - 1; i++) {
        cout << sequence.at(i) << ", ";
    }
    cout << sequence.at(sequence.size()-1) << ">";


    return 0;
}