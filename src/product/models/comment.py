from django.db import models, transaction


class Comment(models.Model):
    """
    A comment left by a client on a product variant.
    """

    client = models.ForeignKey(
        "users.Client", on_delete=models.CASCADE, related_name="comments"
    )
    """ A reference to the client who made the comment."""

    variant = models.ForeignKey(
        "product.Variant", on_delete=models.CASCADE, related_name="comments"
    )
    """ A reference to the variant the comment is about."""

    content = models.TextField()
    """ The content of the comment."""

    date_posted = models.DateTimeField(auto_now_add=True)
    """ The date and time when the comment was posted."""

    def __str__(self):
        """Get the comment's client and variant as default instance name"""
        return f"Comment by {self.client} on {self.variant}"
