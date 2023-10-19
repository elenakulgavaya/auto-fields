import decimal
import uuid

from fild.sdk import (
    Bool, DateTime, Decimal, Enum, Float, Int, Raw, String, StringDecimal,
    Uuid
)


def test_generate_bool():
    value = Bool().value
    assert isinstance(value, bool)


def test_generate_int():
    value = Int().value
    assert isinstance(value, int)


def test_generate_float():
    value = Float().value
    assert isinstance(value, float)


def test_generate_decimal():
    value = Decimal().value
    assert isinstance(value, decimal.Decimal)


def test_decimal_from_str_value():
    value = Decimal.from_value('2.02').value
    assert isinstance(value, decimal.Decimal)


def test_decimal_from_float_value():
    value = Decimal.from_value(1.9).value
    assert isinstance(value, decimal.Decimal)


def test_generate_string_decimal():
    value = StringDecimal().value
    assert isinstance(value, str)


def test_generate_string_decimal_value():
    value = StringDecimal().value
    assert isinstance(decimal.Decimal(value), decimal.Decimal)


def test_string_decimal_no_value():
    value = StringDecimal().with_values('').value
    assert value == ''


def test_generate_string():
    value = String().value
    assert isinstance(value, str)


def test_generate_enum():
    class EnumVals(Enum):
        Example = 'example'

    assert EnumVals().value == 'example'


def test_enum_to_list():
    class EnumVals(Enum):
        Value1 = 'val_1'
        Value2 = 'val_2'
        Value3 = 'val_3'

    assert EnumVals.to_list() == ['val_1', 'val_2', 'val_3']


def test_enum_to_list_exclude_value():
    class EnumVals(Enum):
        Value1 = 'val_1'
        Value2 = 'val_2'
        Value3 = 'val_3'

    assert EnumVals.to_list(exclude=EnumVals.Value2) == ['val_1', 'val_3']


def test_enum_to_list_exclude_multiple_values():
    class EnumVals(Enum):
        Value1 = 'val_1'
        Value2 = 'val_2'
        Value3 = 'val_3'

    assert EnumVals.to_list(
        exclude=(EnumVals.Value2, EnumVals.Value3)
    ) == ['val_1']


def test_generate_raw():
    value = Raw().value
    assert isinstance(value, dict)


def test_raw_with_values():
    value = Raw().with_values({'test': 123}).value
    assert value == {'test': 123}


def test_raw_with_values_override():
    value = Raw().with_values({
        'first': 'val1',
        'second': 'val2',
        'third': 'val3'
    }).with_values({'second': 'val_two'}).value
    assert value == {
        'first': 'val1',
        'second': 'val_two',
        'third': 'val3'
    }


def test_generate_datetime_type():
    value = DateTime().value
    assert isinstance(value, str)


def test_generate_uuid_type():
    value = Uuid().value
    assert isinstance(value, str)


def test_generate_uuid_value():
    value = Uuid().value
    assert isinstance(uuid.UUID(value, version=4), uuid.UUID)
