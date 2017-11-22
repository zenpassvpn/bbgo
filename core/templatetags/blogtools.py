from blogs.models import Blog

from django import template
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404

register = template.Library()


@register.filter(name='bloginfo')
def _bloginfo(id):
    post = get_object_or_404(Blog, pk=id)
    title = post.title
    count = post.comment_count
    posturl = reverse_lazy('blogs:show_post', args=[post.id])

    return "<a href='%s'>%s</a><span class='bloginfo'>%d</span>" % (posturl, title, count)
