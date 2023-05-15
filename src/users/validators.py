from django.core.exceptions import ValidationError


def validate_card_number(value):
    """
    Validate the card number using the Luhn algorithm.
    Raises a ValidationError if the card number is invalid.
    :param str value: the card number to validate
    :raises ValidationError: if the card number is invalid
    """

    def luhn_checksum(card_number):
        """
        Calculate the Luhn checksum for the given card number.
        :param str card_number: the card number
        :return: the Luhn checksum
        :rtype: int
        """

        def digits_of(n):
            return [int(d) for d in str(n)]

        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = 0
        checksum += sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d * 2))
        return checksum

    if luhn_checksum(value) % 10 != 0:
        raise ValidationError("Invalid card number.")
