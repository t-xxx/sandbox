# Queueの実装（リスト）

class Queue:
    """
    Queueをリストを使って操作する。

    Attributes
    ----------
    size : int
        Queueの長さ。
    """
    size: int = 1000

    def __init__(self, size) -> None:
        """
        Parameters
        ----------
        size : int
            Queueの長さ。
        """
        self.queue_array = [None] * size
        self.capacity = size
        self.flont = 0  # 開始の要素
        self.rear = -1  # 最後の要素
        self.count = 0  # Queueのサイズ

    def dequeue(self):
        """
        Queueの先頭から要素取り出して、ポインタを右に一つ移動する。

        Returns
        -------
        flont_value :
            Queueの始めの値。
        """

        # Queueのアンダーフローのチェック
        if self.isEmpty():
            print('Queue Underflow!! Terminating process.')
            exit(-1)

        # 要素の取り出しとポインタの移動
        flont_value = self.queue_array[self.flont]
        self.flont = (self.flont + 1) % self.capacity
        self.count = self.count - 1
        return flont_value

    def enqueue(self, value):
        """
        Queueの後ろに要素を挿入する、ポインタを右に一つ移動する。

        Parameters
        ----------
        value :
            Queueに挿入する要素。
        """

        # Queueのオーバーフローのチェック
        if self.isFull():
            print('Overflow!! Terminating process.')
            exit(-1)

        # 要素の挿入とポインタの移動
        self.rear = (self.rear + 1) % self.capacity
        self.queue_array[self.rear] = value
        self.count += 1

    def peek(self):
        """
        Queueの先頭の要素を取り出す。

        Returns
        -------
        self.queue_array[self.flont] :
            Queueの始めの値。
        """
        # アンダーフローのチェック
        if self.isEmpty():
            print('Queue Underflow!! Terminating process.')
            exit(-1)
        return self.queue_array[self.flont]

    def size(self) -> int:
        """
        Queueのサイズを返す。

        Returns
        -------
        count : int
            Queueのサイズ。
        """
        return self.count

    def isEmpty(self) -> bool:
        """
        Queueが空かどうかを返す。

        Returns
        -------
        self.size() : int
            Queueの空かどうかの真偽値。
        """
        return self.size() == 0

    def isFull(self) -> bool:
        """
        Queueが限界かどうかを返す。

        Returns
        -------
        self.size() == self.capacity :
            Queueが限界かどうかの真偽値。
        """
        return self.size() == self.capacity


if __name__ == '__main__':

    # は容量5のQueueを作成
    q = Queue(5)

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print('The queue size is', q.size())
    print('The front element is', q.peek())
    q.dequeue()
    print('The front element is', q.peek())

    q.dequeue()
    q.dequeue()

    if q.isEmpty():
        print('The queue is empty')
    else:
        print('The queue is not empty')
