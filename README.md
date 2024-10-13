# GitHub Stats Analyser

## Table of Contents

- [GitHub Stats Analyser](#github-stats-analyser)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Usage](#usage)
    - [GitHub Action Example](#github-action-example)
    - [GitHub Action Inputs](#github-action-inputs)
  - [License](#license)

## Introduction

This project is a tool to analyse the statistics of a user's GitHub repositories.

It is designed to be used as a GitHub Action.

The tool is written in Python and uses the GitHub API to some of the statistics. As well it clones the repositories to be analysed and analyses the files in the repositories.

## Usage

### GitHub Action Example

The GitHub Action is designed to be used in a workflow.

```yaml
- name: Analyse GitHub repositories
  uses: jackplowman/github-stats-analyser@latest
  with:
    REPOSITORY_OWNER: jackplowman # Put your GitHub username here or use ${{ github.REPOSITORY_OWNER }}
```

### GitHub Action Inputs

| Name                     | Required | Description                                                                                                                                                                                                         | Type   | Default               |
| ------------------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | --------------------- |
| `REPOSITORY_OWNER`       | yes      | The GitHub username of the repositories to analyse.                                                                                                                                                                 | string | N/A                   |
| `GITHUB_TOKEN`           | no       | A GitHub token to authenticate API requests.                                                                                                                                                                        | string | `${{ github.token }}` |
| `REPOSITORY_SEARCH_TYPE` | no       | The type of search to perform. Options are `all` or `named`. All finds all repositories owned by the user. Named finds repositories with the specified names. Names must be set using the `REPOSITORY_NAMES` input. | string | `all`                 |
| `REPOSITORY_NAMES`       | no       | A comma-separated list of repository names to analyse.                                                                                                                                                              | string | N/A                   |

## License

[MIT](https://github.com/jackplowman/github-stats-analyser/blob/master/LICENSE)
