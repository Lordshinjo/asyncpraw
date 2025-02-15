import pytest

from asyncpraw.models import Emoji, Subreddit
from asyncpraw.models.reddit.emoji import SubredditEmoji

from ... import UnitTest


class TestEmoji(UnitTest):
    def test_equality(self):
        emoji1 = Emoji(self.reddit, subreddit=Subreddit(self.reddit, "a"), name="x")
        emoji2 = Emoji(self.reddit, subreddit=Subreddit(self.reddit, "a"), name="2")
        emoji3 = Emoji(self.reddit, subreddit=Subreddit(self.reddit, "b"), name="1")
        emoji4 = Emoji(self.reddit, subreddit=Subreddit(self.reddit, "A"), name="x")
        emoji5 = Emoji(self.reddit, subreddit=Subreddit(self.reddit, "a"), name="X")
        emoji6 = Emoji(self.reddit, subreddit=Subreddit(self.reddit, "b"), name="x")
        assert emoji1 == emoji1
        assert emoji1 == "x"
        assert emoji2 == emoji2
        assert emoji3 == emoji3
        assert emoji1 != emoji2
        assert emoji1 != emoji3
        assert emoji1 == emoji4
        assert emoji1 != emoji5
        assert emoji1 != emoji6
        assert emoji1 != 5

    async def test__get(self):
        subreddit = Subreddit(self.reddit, display_name="a")
        emoji = await subreddit.emoji.get_emoji("a", lazy=True)
        assert isinstance(emoji, Emoji)

    def test_hash(self):
        emoji1 = Emoji(self.reddit, subreddit=Subreddit(self.reddit, "a"), name="x")
        emoji2 = Emoji(self.reddit, subreddit=Subreddit(self.reddit, "a"), name="2")
        emoji3 = Emoji(self.reddit, subreddit=Subreddit(self.reddit, "b"), name="1")
        emoji4 = Emoji(self.reddit, subreddit=Subreddit(self.reddit, "A"), name="x")
        emoji5 = Emoji(self.reddit, subreddit=Subreddit(self.reddit, "a"), name="X")
        emoji6 = Emoji(self.reddit, subreddit=Subreddit(self.reddit, "b"), name="x")
        assert hash(emoji1) == hash(emoji1)
        assert hash(emoji2) == hash(emoji2)
        assert hash(emoji3) == hash(emoji3)
        assert hash(emoji1) != hash(emoji2)
        assert hash(emoji1) != hash(emoji3)
        assert hash(emoji1) == hash(emoji4)
        assert hash(emoji1) != hash(emoji5)
        assert hash(emoji1) != hash(emoji6)

    def test_repr(self):
        emoji = Emoji(self.reddit, subreddit=Subreddit(self.reddit, "a"), name="x")
        assert repr(emoji) == "Emoji(name='x')"

    def test_str(self):
        emoji = Emoji(self.reddit, subreddit=Subreddit(self.reddit, "a"), name="x")
        assert str(emoji) == "x"

    async def test_update(self):
        emoji = Emoji(self.reddit, subreddit=Subreddit(self.reddit, "a"), name="x")
        with pytest.raises(TypeError) as excinfo:
            await emoji.update()
        assert str(excinfo.value) == "At least one attribute must be provided"


class TestSubredditEmoji(UnitTest):
    def test_repr(self):
        se = SubredditEmoji(subreddit=Subreddit(self.reddit, "a"))
        assert repr(se)  # assert it has some repr
