FROM mcr.microsoft.com/vscode/devcontainers/universal:1-linux

USER root

RUN wget https://packages.erlang-solutions.com/erlang-solutions_2.0_all.deb \
    && dpkg -i erlang-solutions_2.0_all.deb \
    && apt-get update \
    && apt-get install esl-erlang elixir

USER codespace
