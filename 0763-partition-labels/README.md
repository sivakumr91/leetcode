# 763. Partition Labels

| Detail | Value |
| --- | --- |
| Difficulty | Medium |
| Language | python |
| Runtime | 0 ms |
| Memory | 12.4 MB |

## Description

You are given a string `s`. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string `"ababcc"` can be partitioned into `["abab", "cc"]`, but partitions such as `["aba", "bcc"]` or `["ab", "ab", "cc"]` are invalid.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be `s`.

Return *a list of integers representing the size of these parts*.

Example 1:

```

**Input:** s = "ababcbacadefegdehijhklij"
**Output:** [9,7,8]
**Explanation:**
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

```

Example 2:

```

**Input:** s = "eccbbbbdec"
**Output:** [10]

```

**Constraints:**

- `1 <= s.length <= 500`

- `s` consists of lowercase English letters.

## Topics

`Hash Table` `Two Pointers` `String` `Greedy`

## Solution

See the accompanying solution file for the submitted implementation.

## Links

- [LeetCode problem](https://leetcode.com/problems/partition-labels/submissions/2158814202/)
- [GitHub source](https://github.com/sivakumr91/leetcode/blob/main/0763-partition-labels/solution.py)
