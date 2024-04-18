if status is-interactive
    # starship
    starship init fish | source
    # path
    export PATH="$PATH:$USER/.local/bin"
    # default programs
    export TERMINAL=alacritty
    export TerminalEmulator=alacritty
    # pfetch
    export PF_SEP="    "
    export EDITOR="nvim"
    export PF_INFO="ascii os host kernel pkgs shell wm editor"
    # aliases
    alias activate="source venv/bin/activate.fish"
    alias tt="tt -theme ocean-dark -n 200 -showwpm -noskip -oneshot -json"
    alias t="tmux"
    alias xi="sudo xbps-install -S"
    alias xu="sudo xbps-install -Suy"
    alias gc="git clone"
end
