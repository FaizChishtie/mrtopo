from mrtopo.structures.network import Network


class MutantNetwork():
    def __init__(self, network: Network, _id: int, description: str, operation):
        self.network = network
        self._id = _id
        self.description = description
        self.operation = operation
        self.modified_item = None

    def __repr__(self):
        return "<MutantNetwork (" + str(self.network) + ", " + str(self._id) + ", " + str(
            self.description) + ", " + str(self.operation) + ", Modified - " + str(self.modified_item) + ")>"

    def get_id(self):
        return self._id

    def get_network(self):
        return self.network

    def get_description(self):
        return self.description

    def get_operation(self):
        return self.operation

    def get_modified_item(self):
        return self.modified_item

    def add_modified_item(self, mi):
        self.modified_item = mi
