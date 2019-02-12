class StackStorage:
    storage = 0

    def putBytes(self, data):
        """
        Put bytes to storage.
        You can read storaged data from
        file and put it to this stack.
        ~Or you can do anything else with
        this method.

        Args:
            data (bytes): Nothing to say.
        """
        if isinstance(data, bytes):
            for val in data:
                self.storage = self.storage*256 + val
        else:
            raise TypeError('Argument data must have <bytes> type')

    def put(self, value, scope):
        """
        Put value (limited on scope) to stack.

        Args:
            value (int): put it to storage.
            scope (int): limit of value.
        """
        if value < scope and value >= 0:
            self.storage = self.storage*scope + value
        else:
            raise ValueError('0 =< value < scope')

    def pull(self, scope):
        """
        Pull value from stack limited on scope.

        Args:
            scope (int): limit of value.

        Returns:
            int: storaged value.

        Example:
            storage = StackStorage()

            storage.put(3, 15)
            storage.put(14, 20)
            storage.put(5, 22)
            storage.put(18, 20)

            storage.pull(20) # return 18
            storage.pull(22) # return 5
            storage.pull(20) # return 14
            storage.pull(15) # return 3
        """
        val = self.storage % scope
        self.storage = self.storage // scope
        return val

    def getDataBytes(self):
        """
        Return storaged data in bytes.
        ~Then you can write to a file or do something another.
        """
        data = []
        stor = self.storage
        while stor > 0:
            data.append(stor % 256)
            stor = stor // 256

        return bytes(reversed(data))

    def pullDataBytes(self):
        """
        Pull all data from storage and return it in bytes.
        ~Then you can write to a file or do something another.
        """
        data = []
        while self.storage > 0:
            data.append(self.storage % 256)
            self.storage = self.storage // 256

        return bytes(reversed(data))
