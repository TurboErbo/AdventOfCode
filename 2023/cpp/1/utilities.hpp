#include <string>

class Utility
{
public:
    static int parse_line(const std::string &s)
    {
        int firstdigit{-1}, lastdigit;
        for (const auto ch : s)
        {
            if (std::isdigit(ch))
            {
                if (-1 == firstdigit)
                {
                    firstdigit = ch - '0';
                }
                lastdigit = ch - '0';
            }
        }
        return firstdigit * 10 + lastdigit;
    }
};