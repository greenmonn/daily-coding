/* TODO: need refactoring */

/* Never use pointer, just reference */

#include <string>
#include <iostream>
#include <vector>
#include <sstream>

#include "attribute_parser.h"

using namespace std;

string parse_tag_name(string line) {
    stringstream buffer(line);

    string token;

    vector<string> tokens;

    while (getline(buffer, token, ' ')) {
        tokens.push_back(trim(token));
    }

    return tokens[0].substr(1);
}

vector<Attribute> parse_attributes(string line) {

    vector<Attribute> attributes;

    stringstream buffer(line);

    string token;
    vector<string> tokens;

    getline(buffer, token, ' ');

    while (getline(buffer, token, '=')) {
        token = trim(token);
        string::size_type pos = token.find_first_of(' ');

        if (pos != string::npos) {
            tokens.push_back(trim(token.substr(0, pos - 1)));
            tokens.push_back(trim(token.substr(pos + 1)));
        } else {
            token = trim(token);
            tokens.push_back(token);
        }
    }

    for (int i = 0; i < tokens.size(); i += 2) {
        Attribute item = make_pair(tokens[i], tokens[i + 1]);

        attributes.push_back(item);
    }

    return attributes;
}

std::string trim_left(const std::string &str) {
    const std::string pattern = " \"\f\n\r\t\v>";
    return str.substr(str.find_first_not_of(pattern));
}

std::string trim_right(const std::string &str) {
    const std::string pattern = " \"\f\n\r\t\v>";
    return str.substr(0, str.find_last_not_of(pattern) + 1);
}

string trim(const string &word) {
    return trim_left(trim_right(word));
}

bool isOpeningTag(string line) {
    return line.compare(0, 2, "</") != 0;
}

vector<Tag *> parseLines(int lineLength, string *lines) {
    vector<Tag *> tags;

    vector<Tag *> taglist;

    for (int i = 0; i < lineLength; i++) {
        if (isOpeningTag(lines[i])) {
            Tag *tag = new Tag();
            tag->tagName = parse_tag_name(lines[i]);

            tag->attributes = parse_attributes(lines[i]);

            if (!tags.empty()) {
                tags.back()->childTags.push_back(tag);

                tags.push_back(tag);
            } else {
                tags.push_back(tag);
            }

        } else {
            Tag *tag = tags.back();

            tags.pop_back();

            if (tags.empty()) {
                taglist.push_back(tag);
            }
        }
    }

    return taglist;
}

Tag *findTag(string tagName, vector<Tag *> tags, bool *found) {
    for (int i = 0; i < tags.size(); i++) {
        if (tagName.compare(0, tagName.size(), tags[i]->tagName) == 0) {
            return tags[i];
        }
    }

    *found = false;
    return nullptr;
}

Attribute findAttribute(string name, Tag *tag, bool *found) {
    for (int i = 0; i < tag->attributes.size(); i++) {
        if (name.compare(0, name.size(), tag->attributes[i].first) == 0) {
            return tag->attributes[i];
        }
    }

    *found = false;
    return make_pair("", "");
}

string getQueryResult(string query, vector<Tag *> tags) {
    string::size_type pos;

    vector<Tag *> parents;

    bool found = true;

    while ((pos = query.find_first_of(".~")) != string::npos) {
        string tagName = query.substr(0, pos);

        if (parents.empty()) {
            parents.push_back(findTag(tagName, tags, &found));
        } else {
            Tag *parent = parents.back();
            parents.pop_back();

            parents.push_back(findTag(tagName, parent->childTags, &found));
        }

        if (!found) {
            return "Not Found!";
        }

        query.erase(0, pos + 1);
    }

    string name = query;

    Tag *parent = parents.back();

    Attribute attribute = findAttribute(name, parent, &found);

    if (!found) {
        return "Not Found!";
    }

    return attribute.second;
}

void Execute() {
    int lineLength, queryCount;

    cin >> lineLength >> queryCount;
    cin.ignore();

    string lines[lineLength];

    for (int i = 0; i < lineLength; i++) {
        getline(cin, lines[i]);
    }

    vector<Tag *> tags = parseLines(lineLength, lines);

    for (int i = 0; i < queryCount; i++) {
        string query;
        getline(cin, query);

        cout << getQueryResult(query, tags) << endl;
    }
}