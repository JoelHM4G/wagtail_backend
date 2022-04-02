from wagtail.core import hooks
from wagtail.admin.action_menu import ActionMenuItem
from .admin import SubscriberAdmin
from wagtail.admin.widgets import PageListingButton

@hooks.register('register_page_listing_buttons')
def add_author_edit_buttons(page, page_perms, is_parent=False, next_url=None):
    """
    For pages that have an author, add an additional button to the page listing,
    linking to the 'edit' page for that author.
    """
    author_id = getattr(page, 'author_id', None)
    if author_id:
        # the url helper will return something like: /admin/my-app/author/edit/2/
        author_edit_url = SubscriberAdmin.url_helper.get_action_url('edit', author_id)
        yield PageListingButton('Edit Author',  author_edit_url, priority=10)