from talkgenerator.slide.slides import Slide


class SlideDeck():
    """ Represents a deck of Slide objects    """

    def __init__(self, size):
        self._size = size
        self._slides = [None] * size

    def add_slide(self, slide_index: int, slide):
        self._slides[slide_index] = slide

    def is_complete(self):
        return len(self._slides) >= self._size and (None not in self._slides)

    def to_powerpoint(self, prs_template):
        """ Should generate a slide in the powerpoint """
        if not self.is_complete():
            print("ERROR: SOME SLIDES WERE NOT GENERATED:", self._slides)
            self._slides = [slide for slide in self._slides if slide is not None]
        return list(map(lambda x: x.create_powerpoint_slide(prs_template), self._slides))