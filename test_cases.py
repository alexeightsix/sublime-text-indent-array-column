import pytest
import parser
import textwrap
import inspect


def test_case_1():
    string_input = textwrap.dedent("""\
    "1"     => "string",
    '2'         => "string",
    "3"             => 0,
    "4" => true,
    "5" => false,
    "6"             => new Object(),
    "7"         => function_name(),
    "8"     => Static::FUNCTION,
    """)

    string_formatted = parser.parse(string_input).indent()

    res = textwrap.dedent("""\
    "1" => "string",
    '2' => "string",
    "3" => 0,
    "4" => true,
    "5" => false,
    "6" => new Object(),
    "7" => function_name(),
    "8" => Static::FUNCTION,
    """)

    assert res == string_formatted


def test_case_2():
    string_input = textwrap.dedent("""\
    $1 = 1;
    $2      = "true";
    $3              = false;
    $4 = "";
    """)

    string_formatted = parser.parse(string_input).indent()

    res = textwrap.dedent("""\
    $1 = 1;
    $2 = "true";
    $3 = false;
    $4 = "";
    """)

    assert res == string_formatted


def test_case_3():
    string_input = textwrap.dedent("""\
    $1->asdasd = 1;
    $2->asda = "true";
    $3->asdasdasd = false;
    $4->asdasdadasdasd = "";
    """)

    string_formatted = parser.parse(string_input).indent()

    res = textwrap.dedent("""\
    $1->asdasd         = 1;
    $2->asda           = "true";
    $3->asdasdasd      = false;
    $4->asdasdadasdasd = "";
    """)

    assert res == string_formatted

# FIX ME: this case is somewhat broken


def test_case_4():
    string_input = textwrap.dedent("""\
    $1["asdasdasdasdasdasdasdasdasd"] = 1;
    $2["asdasdasdadasdasdasd"] = "true";
    """)

    string_formatted = parser.parse(string_input).indent()

    res = textwrap.dedent("""\
    $1["asdasdasdasdasdasdasdasdasd"] = 1;
    $2["asdasdasdadasdasdasd"]        = "true";
    """)

    assert res == string_formatted