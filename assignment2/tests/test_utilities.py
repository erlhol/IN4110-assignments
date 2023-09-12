""" Test script executing all the necessary unit tests for the functions in analytic_tools/utilities.py module
    which is a part of the analytic_tools package
"""

# TODO:

# Include the necessary packages here
from pathlib import Path

import pytest

# This should work if analytic_tools has been installed properly in your environment
from analytic_tools.utilities import (
    get_dest_dir_from_csv_file,
    get_diagnostics,
    is_gas_csv,
    merge_parent_and_basename,
)


@pytest.mark.task12
def test_get_diagnostics(example_config):
    """Test functionality of get_diagnostics in utilities module

    Parameters:
        example_config (pytest fixture): a preconfigured temporary directory containing the example configuration
                                     from Figure 1 in assignment2.md

    Returns:
    None
    """
    res = get_diagnostics(example_config)
    assert res["files"] == 10
    assert res["subdirectories"] == 5
    assert res[".csv files"] == 8
    assert res[".txt files"] == 0
    assert res[".npy files"] == 2
    assert res[".md files"] == 0
    assert res["other files"] == 0


@pytest.mark.task12
@pytest.mark.parametrize(
    "exception, dir",
    [
        (NotADirectoryError, "Not_a_real_directory"),
        (NotADirectoryError,"pollution_data/not_a_directory"),
        (TypeError,5),
        (TypeError,False)
    ],
)
def test_get_diagnostics_exceptions(exception, dir):
    """Test the error handling of get_diagnostics function

    Parameters:
        exception (concrete exception): The exception to raise
        dir (str or pathlib.Path): The parameter to pass as 'dir' to the function

    Returns:
        None
    """
    with pytest.raises(exception):
        get_diagnostics(dir)

@pytest.mark.task22
def test_is_gas_csv():
    """Test functionality of is_gas_csv from utilities module

    Parameters:
        None

    Returns:
        None
    """

    """
    You should pretend that you do not know the implementation 
    of this function and pass several paths with different syntax, 
    combinations of lowercase/uppercase and even non-alphanumerical characters

    Then you should do sanity checks on the return values (are they of correct type?)
    """
    false_tests = ["path/my_path/C02.csv","path/my_path/name.csv","CO2_WSn.csv",
                   "N2O_hIU.csv","CH2.csv","aDiReCtOrYwItHuPpErAnDlOwErCaSe/GiBBerish.csv"]
    for test in false_tests:
        res = is_gas_csv(test)
        assert isinstance(res,bool)
        assert res == False
    
    true_tests = ["aDiReCtOrYwItHuPpErAnDlOwErCaSe/CO2.csv", "&:@~/CH4.csv", "my_path/CO2.csv",
                  "CH4.csv", "SF6.csv", "my_path/CH4.csv", "my_path/CO2.csv", "my_path/N2O.csv",
                  "my_path/SF6.csv", "my_path/H2.csv"]
    for test in true_tests:
        res = is_gas_csv(test)
        assert isinstance(res,bool)
        assert res == True


@pytest.mark.task22
@pytest.mark.parametrize(
    "exception, path",
    [
        (ValueError, Path(__file__).parent.absolute()),
        (TypeError, 5),
        (ValueError, Path("my_path/SF6.npy")),
        (TypeError, False)

        # add more combinations of (exception, path) here
    ],
)
def test_is_gas_csv_exceptions(exception, path):
    """Test the error handling of is_gas_csv function

    Parameters:
        exception (concrete exception): The exception to raise
        path (str or pathlib.Path): The parameter to pass as 'path' to function

    Returns:
        None
    """
    # Check this once more!!
    # Will have to extend the check of this test. What does sanitixe mean?
    with pytest.raises(exception):
        is_gas_csv(path)


@pytest.mark.task24
def test_get_dest_dir_from_csv_file(example_config):
    """Test functionality of get_dest_dir_from_csv_file in utilities module.

    Parameters:
        example_config (pytest fixture): a preconfigured temporary directory containing the example configuration
            from Figure 1 in assignment2.md

    Returns:
        None
    """

    parent_dir = Path(__file__).parents[1].absolute()
    restructured_path = parent_dir / Path("pollution_data_restructured/by_gas")

    # H2:
    h2 = Path(example_config) / Path("pollution_data/by_src/src_agriculture/H2.csv")
    co2 = Path(example_config) / Path("pollution_data/by_src/src_airtraffic/CO2.csv")
    co2_2 = Path(example_config) / Path("pollution_data/by_src/src_oil_and_gass/CO2.csv")
    ch4 = Path(example_config) / Path("pollution_data/by_src/src_oil_and_gass/CH4.csv")

    dest_path1 = get_dest_dir_from_csv_file(restructured_path, h2)
    dest_path2 = get_dest_dir_from_csv_file(restructured_path, co2)
    dest_path3 = get_dest_dir_from_csv_file(restructured_path, co2_2)
    dest_path4 = get_dest_dir_from_csv_file(restructured_path, ch4)

    assert dest_path1 == (parent_dir / Path('pollution_data_restructured/by_gas/gas_H2')) and dest_path1.is_dir()
    assert dest_path2 == (parent_dir / Path('pollution_data_restructured/by_gas/gas_CO2')) and dest_path2.is_dir()
    assert dest_path3 == (parent_dir / Path('pollution_data_restructured/by_gas/gas_CO2')) and dest_path3.is_dir()
    assert dest_path4 == (parent_dir / Path('pollution_data_restructured/by_gas/gas_CH4')) and dest_path4.is_dir()


@pytest.mark.task24
@pytest.mark.parametrize(
    "exception, dest_parent, file_path",
    [
        (ValueError, Path(__file__).parent.absolute(), "foo.txt"),
        # add more combinations of (exception, dest_parent, file_path) here
    ],
)
def test_get_dest_dir_from_csv_file_exceptions(exception, dest_parent, file_path):
    """Test the error handling of get_dest_dir_from_csv_file function

    Parameters:
        exception (concrete exception): The exception to raise
        dest_parent (str or pathlib.Path): The parameter to pass as 'dest_parent' to the function
        file_path (str or pathlib.Path): The parameter to pass as 'file_path' to the function

    Returns:
        None
    """
    # Remove if you implement this task
    raise NotImplementedError("Remove me if you implement this mandatory task")
    ...


@pytest.mark.task26
def test_merge_parent_and_basename():
    """Test functionality of merge_parent_and_basename from utilities module

    Parameters:
        None

    Returns:
        None
    """
    assert Path('src_agriculture_CO2.csv') == merge_parent_and_basename('/User/.../assignment2/pollution_data/by_src/src_agriculture/CO2.csv')
    assert Path('some_dir_some_sub_dir') == merge_parent_and_basename('some_dir/some_sub_dir')
    assert Path('some_dir_some_file.txt') == merge_parent_and_basename('some_dir/some_file.txt')


@pytest.mark.task26
@pytest.mark.parametrize(
    "exception, path",
    [
        (TypeError, 33),
        (ValueError, "some_file.txt"),
        (ValueError, "parentdir/")
        # add more combinations of (exception, path) here
    ],
)
def test_merge_parent_and_basename_exceptions(exception, path):
    """Test the error handling of merge_parent_and_basename function

    Parameters:
        exception (concrete exception): The exception to raise
        path (str or pathlib.Path): The parameter to pass as 'pass' to the function

    Returns:
        None
    """
    with pytest.raises(exception):
        merge_parent_and_basename(path)
