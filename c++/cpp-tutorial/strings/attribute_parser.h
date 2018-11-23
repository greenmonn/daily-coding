#ifndef CPP_TUTORIAL_ATTRIBUTE_PARSER_H
#define CPP_TUTORIAL_ATTRIBUTE_PARSER_H

#endif

#include <string>

using namespace std;

typedef pair<string, string> Attribute;

class Tag {
public:
    string tagName;
    vector<Attribute> attributes;
    vector<Tag *> childTags;
};

string parse_tag_name(string line);

vector<Attribute> parse_attributes(string line);

vector<Tag *> parseLines(int lineLength, string *lines);

string getQueryResult(string query, vector<Tag *> tags);

string trim(const string &word);

bool isOpeningTag(string line);
