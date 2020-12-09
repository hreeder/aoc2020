defmodule AOC.Day1 do
  def parse_data(data) do
    data
    |> String.split("\n", trim: true)
    |> Enum.map(&String.to_integer/1)
  end

  def part1(data) do
    nums = parse_data(data)

    try do
      for a <- nums,
          b <- nums,
          a + b == 2020,
          do: throw({:break, [a, b]})
    catch
      {:break, result} -> result
      |> Enum.reduce(fn x, acc -> x * acc end)
    end
  end

  def part2(data) do
    nums = parse_data(data)

    try do
      for a <- nums,
          b <- nums,
          c <- nums,
          a + b + c == 2020,
          do: throw({:break, [a, b, c]})
    catch
      {:break, result} -> result
      |> Enum.reduce(fn x, acc -> x * acc end)
    end
  end
end
