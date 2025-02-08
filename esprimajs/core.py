from .minifier import Minifier


def minify(code, source="auto", **kwargs):
	c = Minifier(**kwargs)
	return c.minify(code, source=source)
