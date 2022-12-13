#include <gtest/gtest.h>
#include "utilities.hpp"

// Demonstrate some basic assertions.
TEST(Day1Test, TestParse)
{
    EXPECT_EQ(Utility::parse_line("42"), 42);
    EXPECT_EQ(Utility::parse_line("3"), 33);
    EXPECT_EQ(Utility::parse_line("4abc"), 44);
    EXPECT_EQ(Utility::parse_line("abc6"), 66);
    EXPECT_EQ(Utility::parse_line("5abc6"), 56);
    EXPECT_EQ(Utility::parse_line("abc89def"), 89);
    EXPECT_EQ(Utility::parse_line("abc7234def"), 74);
}