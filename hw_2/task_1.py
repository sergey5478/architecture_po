from random import choice
from abc import ABC, abstractmethod


class ItemFabric(ABC):
    @abstractmethod
    def create_item(self):
        pass

    def open_reward(self):
        self.game_item = self.create_item()
        self.game_item.open()


class IGameItem(ABC):
    @abstractmethod
    def open(self):
        pass


class GoldReward(IGameItem):
    def open(self):
        print('Gold')


class GoldGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return GoldReward()


class GemReward(IGameItem):
    def open(self):
        print('Gem')


class GemGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return GemReward()


class NewReward(IGameItem):
    def open(self):
        print('New Reward')


class NewRewardGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag2')
        return NewReward()


if __name__ == '__main__':
    lst = [GoldGenerator(), GemGenerator(), NewRewardGenerator()]
    for i in range(20):
        choice(lst).open_reward()
