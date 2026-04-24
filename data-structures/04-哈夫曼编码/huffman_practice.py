"""
哈夫曼编码练习文件

本文件用于练习哈夫曼编码的相关知识点，包括构建哈夫曼树、生成哈夫曼编码等。
"""

class HuffmanNode:
    """
    哈夫曼树的节点类
    """
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char  # 字符
        self.freq = freq  # 频率
        self.left = left  # 左子节点
        self.right = right  # 右子节点

    def __lt__(self, other):
        """
        用于比较两个节点的频率
        """
        return self.freq < other.freq


def build_huffman_tree(freq_dict):
    """
    根据字符频率字典构建哈夫曼树
    :param freq_dict: 字符及其频率的字典
    :return: 哈夫曼树的根节点
    """
    from heapq import heappush, heappop, heapify

    # 创建优先队列（最小堆）
    heap = []
    for char, freq in freq_dict.items():
        heappush(heap, HuffmanNode(char, freq))

    # 构建哈夫曼树
    while len(heap) > 1:
        left = heappop(heap)
        right = heappop(heap)
        merged = HuffmanNode(freq=left.freq + right.freq, left=left, right=right)
        heappush(heap, merged)

    return heappop(heap)


def generate_huffman_codes(root, current_code="", codes=None):
    """
    生成哈夫曼编码
    :param root: 哈夫曼树的根节点
    :param current_code: 当前编码
    :param codes: 存储编码的字典
    :return: 字符及其哈夫曼编码的字典
    """
    if codes is None:
        codes = {}

    if root is None:
        return

    if root.char is not None:
        codes[root.char] = current_code
        return

    generate_huffman_codes(root.left, current_code + "0", codes)
    generate_huffman_codes(root.right, current_code + "1", codes)

    return codes


def huffman_encoding(text):
    """
    哈夫曼编码
    :param text: 输入文本
    :return: 编码后的文本和哈夫曼编码字典
    """
    if not text:
        return "", {}

    # 统计字符频率
    freq_dict = {}
    for char in text:
        freq_dict[char] = freq_dict.get(char, 0) + 1

    # 构建哈夫曼树
    root = build_huffman_tree(freq_dict)

    # 生成哈夫曼编码
    huffman_codes = generate_huffman_codes(root)

    # 编码文本
    encoded_text = "".join([huffman_codes[char] for char in text])

    return encoded_text, huffman_codes


def huffman_decoding(encoded_text, huffman_codes):
    """
    哈夫曼解码
    :param encoded_text: 编码后的文本
    :param huffman_codes: 哈夫曼编码字典
    :return: 解码后的文本
    """
    if not encoded_text or not huffman_codes:
        return ""

    # 反转编码字典
    reverse_codes = {v: k for k, v in huffman_codes.items()}

    current_code = ""
    decoded_text = ""

    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded_text += reverse_codes[current_code]
            current_code = ""

    return decoded_text


# 示例用法
if __name__ == "__main__":
    text = "hello world"
    print(f"原始文本: {text}")

    encoded_text, huffman_codes = huffman_encoding(text)
    print(f"编码后的文本: {encoded_text}")
    print(f"哈夫曼编码字典: {huffman_codes}")

    decoded_text = huffman_decoding(encoded_text, huffman_codes)
    print(f"解码后的文本: {decoded_text}")