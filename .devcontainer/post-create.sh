#!/bin/bash

echo "Installing Spaceship Prompt"
mkdir -p $HOME/.config
touch $HOME/.config/spaceship.zsh

# Set config for spaceship prompt
# Display time
echo "SPACESHIP_TIME_SHOW=true" >> $HOME/.config/spaceship.zsh
# Display username always
echo "SPACESHIP_USER_SHOW=always" >> $HOME/.config/spaceship.zsh
# Prompt new line
echo "SPACESHIP_PROMPT_ADD_NEWLINE=false" >> $HOME/.config/spaceship.zsh


mkdir -p $HOME/.zsh
git clone --depth=1 https://github.com/spaceship-prompt/spaceship-prompt.git $HOME/.zsh/spaceship

# Append the following lines to your ~/.zshrc file:
echo "source $HOME/.zsh/spaceship/spaceship.zsh" >> $HOME/.zshrc

exit 0
