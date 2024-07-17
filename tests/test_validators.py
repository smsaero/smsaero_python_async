import unittest

from smsaero import SmsAero


class TestSmsAeroValidators(unittest.TestCase):
    def setUp(self):
        self.smsaero = SmsAero("admin@smsaero.ru", "test_api_key_lX8APMlgliHvkHk04i7")

    def test_send_sms_validate(self):
        with self.assertRaises(TypeError):
            self.smsaero.send_sms_validate("invalid_number", "test text")
        with self.assertRaises(TypeError):
            self.smsaero.send_sms_validate(70000000000, 123)
        with self.assertRaises(TypeError):
            self.smsaero.send_sms_validate(70000000000, "test text", 123)
        with self.assertRaises(TypeError):
            self.smsaero.send_sms_validate(70000000000, "test text", date_to_send="invalid_date")
        with self.assertRaises(TypeError):
            self.smsaero.send_sms_validate(70000000000, "test text", callback_url=123)
        with self.assertRaises(ValueError):
            self.smsaero.send_sms_validate(1, "test text")
        with self.assertRaises(ValueError):
            self.smsaero.send_sms_validate(70000000000, "t")
        with self.assertRaises(ValueError):
            self.smsaero.send_sms_validate(70000000000, "test text", callback_url="invalid_url")

    def test_sms_list_validate(self):
        with self.assertRaises(TypeError):
            self.smsaero.sms_list_validate(number="invalid_number")
        with self.assertRaises(TypeError):
            self.smsaero.sms_list_validate(text=123)
        with self.assertRaises(TypeError):
            self.smsaero.sms_list_validate(page="invalid_page")
        with self.assertRaises(ValueError):
            self.smsaero.sms_list_validate(page=0)
        with self.assertRaises(ValueError):
            self.smsaero.sms_list_validate(number=[79038805678, "invalid_number"])

    def test_viber_send_validate(self):
        with self.assertRaises(TypeError):
            self.smsaero.viber_send_validate(123, "channel", "text")

        with self.assertRaises(TypeError):
            self.smsaero.viber_send_validate("sign", 123, "text")

        with self.assertRaises(TypeError):
            self.smsaero.viber_send_validate("sign", "channel", 123)

        with self.assertRaises(TypeError):
            self.smsaero.viber_send_validate(
                "sign",
                "channel",
                "text",
                "invalid_number",
            )

        with self.assertRaises(TypeError):
            self.smsaero.viber_send_validate(
                "sign",
                "channel",
                "text",
                1234567890,
                "invalid_group_id",
            )

        with self.assertRaises(TypeError):
            self.smsaero.viber_send_validate(
                "sign",
                "channel",
                "text",
                1234567890,
                123,
                123,
            )

        with self.assertRaises(TypeError):
            self.smsaero.viber_send_validate(
                "sign",
                "channel",
                "text",
                1234567890,
                123,
                "image_source",
                123,
            )

        with self.assertRaises(TypeError):
            self.smsaero.viber_send_validate(
                "sign",
                "channel",
                "text",
                1234567890,
                123,
                "image_source",
                "text_button",
                123,
            )

        with self.assertRaises(TypeError):
            self.smsaero.viber_send_validate(
                "sign",
                "channel",
                "text",
                1234567890,
                123,
                "image_source",
                "text_button",
                "link_button",
                123,
            )

        with self.assertRaises(TypeError):
            self.smsaero.viber_send_validate(
                "sign",
                "channel",
                "text",
                1234567890,
                123,
                "image_source",
                "text_button",
                "link_button",
                "date_send",
                123,
            )

        with self.assertRaises(TypeError):
            self.smsaero.viber_send_validate(
                "sign",
                "channel",
                "text",
                1234567890,
                123,
                "image_source",
                "text_button",
                "link_button",
                "date_send",
                "sign_sms",
                123,
            )

        with self.assertRaises(TypeError):
            self.smsaero.viber_send_validate(
                "sign",
                "channel",
                "text",
                1234567890,
                123,
                "image_source",
                "text_button",
                "link_button",
                "date_send",
                "sign_sms",
                "channel_sms",
                123,
            )

        with self.assertRaises(TypeError):
            self.smsaero.viber_send_validate(
                "sign",
                "channel",
                "text",
                1234567890,
                123,
                "image_source",
                "text_button",
                "link_button",
                "date_send",
                "sign_sms",
                "channel_sms",
                "text_sms",
                "invalid_price_sms",
            )

        with self.assertRaises(ValueError):
            self.smsaero.viber_send_validate(
                "sign",
                "channel",
                "text",
                number=112345678901234567890,
            )

        with self.assertRaises(ValueError):
            self.smsaero.viber_send_validate(
                "sign",
                "channel",
                "text",
                number=[112345678901234567890, 12345678901234567890],
            )

        with self.assertRaises(ValueError):
            self.smsaero.viber_send_validate(
                "sign",
                "channel",
                "text",
                number=123,
            )

        with self.assertRaises(ValueError):
            self.smsaero.viber_send_validate(
                "sign",
                "channel",
                "text",
                number=[1234567890, 123],
            )

        with self.assertRaises(ValueError):
            self.smsaero.viber_send_validate(
                sign="TestSign",
                channel="TestChannel",
                text="T" * 641,
            )

        with self.assertRaises(ValueError):
            self.smsaero.viber_send_validate(
                sign="TestSign",
                channel="TestChannel",
                text="",
            )

        with self.assertRaises(ValueError):
            self.smsaero.viber_send_validate(
                sign="T" * 65,
                channel="TestChannel",
                text="TestText",
            )

        with self.assertRaises(ValueError):
            self.smsaero.viber_send_validate(
                sign="T",
                channel="TestChannel",
                text="TestText",
            )

    def test_contact_add_validate(self):
        with self.assertRaises(TypeError):
            self.smsaero.contact_add_validate(number="invalid_number")

        with self.assertRaises(TypeError):
            self.smsaero.contact_add_validate(number=79038805678, group_id="invalid_group_id")

        with self.assertRaises(TypeError):
            self.smsaero.contact_add_validate(number=79038805678, group_id=123, birthday=123)

        with self.assertRaises(TypeError):
            self.smsaero.contact_add_validate(number=79038805678, group_id=123, birthday="01-01-2000", sex=123)

        with self.assertRaises(TypeError):
            self.smsaero.contact_add_validate(
                number=79038805678, group_id=123, birthday="01-01-2000", sex="male", last_name=123
            )

        with self.assertRaises(TypeError):
            self.smsaero.contact_add_validate(
                number=79038805678, group_id=123, birthday="01-01-2000", sex="male", last_name="Doe", first_name=123
            )

        with self.assertRaises(TypeError):
            self.smsaero.contact_add_validate(
                number=79038805678,
                group_id=123,
                birthday="01-01-2000",
                sex="male",
                last_name="Doe",
                first_name="John",
                surname=123,
            )

        with self.assertRaises(TypeError):
            self.smsaero.contact_add_validate(
                number=79038805678,
                group_id=123,
                birthday="01-01-2000",
                sex="male",
                last_name="Doe",
                first_name="John",
                surname="Smith",
                param1=123,
            )

        with self.assertRaises(TypeError):
            self.smsaero.contact_add_validate(
                number=79038805678,
                group_id=123,
                birthday="01-01-2000",
                sex="male",
                last_name="Doe",
                first_name="John",
                surname="Smith",
                param1="param1",
                param2=123,
            )

        with self.assertRaises(TypeError):
            self.smsaero.contact_add_validate(
                number=79038805678,
                group_id=123,
                birthday="01-01-2000",
                sex="male",
                last_name="Doe",
                first_name="John",
                surname="Smith",
                param1="param1",
                param2="param2",
                param3=123,
            )

        with self.assertRaises(ValueError):
            self.smsaero.contact_add_validate(number=[123, "invalid_number"])

        with self.assertRaises(ValueError):
            self.smsaero.contact_add_validate(number=[123, 1234567890123456])

        with self.assertRaises(ValueError):
            self.smsaero.contact_add_validate(number=1234567890123456)

    def test_contact_list_validate(self):
        with self.assertRaises(TypeError):
            self.smsaero.contact_list_validate(number="invalid_number")
        with self.assertRaises(TypeError):
            self.smsaero.contact_list_validate(group_id="invalid_group_id")
        with self.assertRaises(TypeError):
            self.smsaero.contact_list_validate(birthday=123)
        with self.assertRaises(TypeError):
            self.smsaero.contact_list_validate(sex=123)
        with self.assertRaises(TypeError):
            self.smsaero.contact_list_validate(operator=123)
        with self.assertRaises(TypeError):
            self.smsaero.contact_list_validate(last_name=123)
        with self.assertRaises(TypeError):
            self.smsaero.contact_list_validate(first_name=123)
        with self.assertRaises(TypeError):
            self.smsaero.contact_list_validate(surname=123)
        with self.assertRaises(TypeError):
            self.smsaero.contact_list_validate(page="invalid_page")
        with self.assertRaises(ValueError):
            self.smsaero.contact_list_validate(number=[79038805678, "invalid_number"])
