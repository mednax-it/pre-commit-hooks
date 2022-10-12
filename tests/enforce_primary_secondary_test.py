from __future__ import annotations

import pytest

from pre_commit_hooks.enforce_primary_secondary import main

def test_empty_file_does_not_need_fixing(tmpdir):
    f = tmpdir.join('file.tf')
    f.write_text('', encoding='utf-8')
    assert main((str(f),)) == 0
    
def test_non_tf_files_do_not_need_fixing(tmpdir):
    f = tmpdir.join('file.txt')
    f.write_text('{primary = true}', encoding='utf-8')
    assert main((str(f),)) == 0

def test_tf_files_with_primary_but_no_secondary_will_fail(tmpdir):
    f = tmpdir.join('file.tf')
    f.write_text('{primary = true}', encoding='utf-8')
    assert main((str(f),)) == 1

def test_tf_files_with_primary_and_secondary_will_pass(tmpdir):
    f = tmpdir.join('file.tf')
    f.write_text("""{primary = true}
                {primary = false}
    """, encoding='utf-8')
    assert main((str(f),)) == 0

def test_different_valid_formatting_will_pass(tmpdir):
    f = tmpdir.join('file.tf')
    f.write_text("""{ Primary =             true}
                { primary        =  false}
    """, encoding='utf-8')
    assert main((str(f),)) == 0


