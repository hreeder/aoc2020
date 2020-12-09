defmodule AOC.Day1Test do
  use ExUnit.Case, async: true

  test "gets part 1 correct" do
    data = File.read!("test/fixtures/day1.txt")
    assert AOC.Day1.part1(data) == 514579
  end

  test "gets part 2 correct" do
    data = File.read!("test/fixtures/day1.txt")
    assert AOC.Day1.part2(data) == 241861950
  end
end
