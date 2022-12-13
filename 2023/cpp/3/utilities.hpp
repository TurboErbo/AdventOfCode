#include <vector>
#include <string>
#include <regex>
#include <set>

class Utilities
{
public:
    struct Number
    {
        std::size_t start;
        std::size_t end;
        int value;
        bool operator==(const Number &other) const = default;
    };

    struct Symbol
    {
        int row;
        int col;
        char value;
    };

    static std::pair<std::vector<std::vector<Number>>, std::vector<Symbol>> parse_input(const std::vector<std::string> &input)
    {
        std::vector<std::vector<Number>> numbers;
        std::vector<Symbol> symbols;

        for (int row = 0; row < static_cast<int>(input.size()); row++)
        {
            const std::string &line = input[row];
            numbers.emplace_back(parse_numbers_in_line(line));
            auto symbols_in_line = parse_symbols_in_line(line, row);
            symbols.insert(symbols.end(), symbols_in_line.begin(), symbols_in_line.end());
        }

        return {std::move(numbers), std::move(symbols)};
    }

    static std::vector<Number> parse_numbers_in_line(const std::string &line)
    {
        std::vector<Number> numbers;
        std::regex r("\\d+");
        std::sregex_iterator rend;
        for (std::sregex_iterator it(line.begin(), line.end(), r);
             it != rend;
             it++)
        {
            numbers.push_back(
                Number{static_cast<std::size_t>(it->position()),
                       it->position() + static_cast<std::size_t>(it->length()) - 1,
                       std::stoi(it->str())});
        }

        return numbers;
    }

    static std::vector<Symbol> parse_symbols_in_line(const std::string &line, int row)
    {
        std::vector<Symbol> symbols;
        std::regex r("[^\\d.]");
        std::sregex_iterator rend;
        for (std::sregex_iterator it(line.begin(), line.end(), r);
             it != rend;
             it++)
        {
            symbols.push_back(Symbol{row, static_cast<int>(it->position()), line[it->position()]});
        }

        return symbols;
    }

    static bool has_overlap(std::pair<int, int> span1, std::pair<int, int> span2)
    {
        return !(span1.first > span2.second || span1.second < span2.first);
    }

    static std::vector<int> extract_part_numbers(const std::vector<std::vector<Number>> &numbers, const std::vector<Symbol> symbols)
    {
        std::set<const Number *> part_numbers;
        for (const auto &symbol : symbols)
        {
            for (int row = symbol.row - 1; row <= std::min(symbol.row + 1, static_cast<int>(numbers.size())); row++)
            {
                for (const auto &n : numbers[row])
                {
                    if (has_overlap({n.start, n.end}, {symbol.col - 1, symbol.col + 1}))
                    {
                        part_numbers.insert(&n);
                    }
                }
            }
        }
        std::vector<int> result;
        std::transform(part_numbers.begin(), part_numbers.end(), std::back_inserter(result),
                       [](const Number *n)
                       { return n->value; });
        return result;
    }
};