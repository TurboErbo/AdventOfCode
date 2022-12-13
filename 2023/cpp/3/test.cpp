#include <gtest/gtest.h>
#include "utilities.hpp"

TEST(AocTest, TestParse)
{
    auto expected = std::vector<Utilities::Number>{Utilities::Number{0, 1, 42}};
    EXPECT_EQ(Utilities::parse_numbers_in_line("42"), expected);
}