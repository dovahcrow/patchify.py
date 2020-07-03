black:
  poetry run black patchify
  
ci: format ci-black typeck test lint

ci-black:
  poetry run black --check --quiet patchify

format:
  poetry run black patchify

typeck: ci-mypy

test:
  poetry run pytest patchify

testf +ARGS="patchify":
  poetry run pytest {{ARGS}}

lint:
  poetry run pylint patchify

ci-mypy:
  poetry run mypy patchify