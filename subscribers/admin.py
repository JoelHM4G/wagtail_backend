from django.contrib import admin
from wagtail.contrib.modeladmin.helpers import ButtonHelper

from wagtail.contrib.modeladmin.options import(
    ModelAdmin,
    modeladmin_register
)
from .models import Subscribers

class SubscriberButtonHelper(ButtonHelper):

    # Define classes for our button, here we can set an icon for example
    view_button_classnames = ["button","button-small", "icon", "icon-site"]

    def publish_button(self, obj, classnames_add=None, classnames_exclude=None):
        
        text = "Publicar"
        return {
            "url":"publicar/"+str(obj.id),  # decide where the button links to
            "label": text,
            "classname": self.finalise_classname(self.view_button_classnames),
            "title": text,
        }
    def unpublish_button(self, obj):
        # Define a label for our button
        text = "Despublicar"
        return {
            "url": "despublicar/"+str(obj.id),  # decide where the button links to
            "label": text,
            "classname": self.finalise_classname(self.view_button_classnames),
            "title": text,
        }
  
    def get_buttons_for_obj(
        self, obj, exclude=None, classnames_add=None, classnames_exclude=None
    ):
        """
        This function is used to gather all available buttons.
        We append our custom button to the btns list.
        """
        btns = super().get_buttons_for_obj(
            obj, exclude, classnames_add, classnames_exclude
        )
        if "view" not in (exclude or []):
            btns.append(self.publish_button(obj))
            btns.append(self.unpublish_button(obj))
        return btns
class SubscriberAdmin(ModelAdmin):
    model=Subscribers
    menu_label="Subscribers"
    menu_icon="placeholder"
    menu_order=290
    add_to_settings_menu=False
    exclude_from_explorer=False
    list_display=("email","full_name")
    search_fields=("email","full_name")
    button_helper_class = SubscriberButtonHelper
modeladmin_register(SubscriberAdmin)
