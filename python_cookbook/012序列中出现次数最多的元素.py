from collections import Counter

foods = [
    'banana', 'banana', 'apple', 'pear', 'beef', 'beef', 'pork', 'chicken', 'pizza',
]


from collections import defaultdict


def get_counter(array):
    foods_count = defaultdict(int)
    for a in array:
        if a in foods_count:
            foods_count[a] += 1
            continue
        foods_count[a] = 1
    return foods_count
print(sorted(get_counter(foods).items(), key=lambda x: x[1], reverse=True))

word_counts = Counter(foods)
print(type(word_counts), word_counts)

# 出现次数最多的3个
top_three = word_counts.most_common(3)
print(top_three)

# beef 出现的次数
word_beef_count = word_counts['beef']
print(word_beef_count)
# 等效
print(foods.count('beef'))

print(f'element: {word_counts.elements()}')
print(f'list(element): {list(word_counts.elements())}')

more_foods = ['apple', 'banana', 'sandwich', 'orange']
# 把另一个列表里面的元素，添加到Counter
for word in more_foods:
    word_counts[word] += 1
print(type(word_counts), word_counts)
# or
word_counts.update(more_foods)
print(type(word_counts), word_counts)

# 运算
a = Counter(foods)
b = Counter(more_foods)
print(f'a: {a}\nb: {b}\n')

c = a + b
print(f'c: {c}')

d = a - b
print(f'd: {d}')

e = b - a
print(f'e: {e}')


# 字符串
text = 'abcdeabcdabcaba'
w = Counter(text)
print(w)

# 下面两个方法每想到有使用的场景
element = w.elements()
print(f'element: {element}')
print(f'list(element): {list(element)}')

value = w.values()
print(f'value: {value}')
