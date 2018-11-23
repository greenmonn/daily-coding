#include <gtest/gtest.h>
#include "attribute_parser.h"

using namespace std;

GTEST_TEST(ParserTest, tag) {
    string line = "<tag1 value = \"HelloWorld\">";
    EXPECT_EQ("tag1", parse_tag_name(line));
}

GTEST_TEST(ParserTest, attributes) {
    string line = "<b value = \"BadVal\" size = \"10\">";

    vector<Attribute> attributes = parse_attributes(line);

    string name = attributes[0].first;
    string value = attributes[0].second;

    EXPECT_EQ("value", name);
    EXPECT_EQ("BadVal", value);
}

GTEST_TEST(ParserTest, isOpeningTag) {
    EXPECT_EQ(true, isOpeningTag("<tag1 value = 1>"));
    EXPECT_EQ(false, isOpeningTag("</tag2>"));
}

GTEST_TEST(ParserTest, lines) {
    string lines[10] = {
            "<a>",
            "<b name = \"tag_one\">",
            "<c name = \"tag_two\" value = \"val_907\">",
            "</c>",
            "</b>",
            "</a>"
    };

    vector<Tag *> tags = parseLines(6, lines);

    Tag &a = *tags[0];

    Tag &b = *a.childTags[0];

    Tag &c = *b.childTags[0];

    EXPECT_EQ(1, tags.size());
    EXPECT_EQ("a", a.tagName);

    EXPECT_EQ("name", b.attributes[0].first);
    EXPECT_EQ("tag_one", b.attributes[0].second);

    EXPECT_EQ("value", c.attributes[1].first);
    EXPECT_EQ("val_907", c.attributes[1].second);
}

GTEST_TEST(ParserTest, query) {
    Attribute item;

    Tag tag1 = Tag();
    tag1.tagName = "tag1";

    item = make_pair("value", "test");
    tag1.attributes.push_back(item);

    Tag tag2 = Tag();
    tag2.tagName = "tag2";

    item = make_pair("name", "test");
    tag2.attributes.push_back(item);

    tag1.childTags.push_back(&tag2);

    vector<Tag *> tags = {&tag1};

    EXPECT_EQ("test", getQueryResult("tag1~value", tags));
    EXPECT_EQ("Not Found!", getQueryResult("tag1~name", tags));
    EXPECT_EQ("test", getQueryResult("tag1.tag2~name", tags));
}

int main(int argc, char **argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}