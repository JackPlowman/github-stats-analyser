# GitHub Stats Analyser

## Table of Contents

- [GitHub Stats Analyser](#github-stats-analyser)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Usage](#usage)
    - [GitHub Action Example](#github-action-example)
    - [GitHub Action Inputs](#github-action-inputs)
  - [📄 License](#-license)

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
    REPOSITORY_OWNER: jackplowman # Put your GitHub username here or use ${{ github.repository_owner }}
```

### GitHub Action Inputs

| Name               | Required | Description                                         | Type   | Default               |
| ------------------ | -------- | --------------------------------------------------- | ------ | --------------------- |
| `REPOSITORY_OWNER` | yes      | The GitHub username of the repositories to analyse. | string | N/A                   |
| `GITHUB_TOKEN`     | no       | A GitHub token to authenticate API requests.        | string | `${{ github.token }}` |
| `DEBUG`            | no       | Enable debug logging.                               | string | `false`               |

## 📄 License

This project is licensed under the MIT Licence - see the [LICENCE](LICENCE) file for details.
