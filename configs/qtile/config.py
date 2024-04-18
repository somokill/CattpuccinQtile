from os import path
from libqtile import hook, bar, widget, qtile
from libqtile.layout.floating import Floating
from libqtile.layout.spiral import Spiral
from libqtile.layout.bsp import Bsp
from libqtile.layout.columns import Columns
from libqtile.layout.matrix import Matrix
from libqtile.layout.ratiotile import RatioTile
from libqtile.layout.stack import Stack
from libqtile.layout.tile import Tile
from libqtile.layout.verticaltile import VerticalTile
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras import widget
from libqtile.config import Group, Key, Match, Screen, Drag, Click
from libqtile.lazy import lazy

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Any
    from libqtile.core.manager import Qtile

menu = "rofi -show drun"
power_menu = "rofi -show power-menu -modi power-menu:~/.local/bin/rofi-power-menu -config ~/.config/rofi/config.rasi"
terminal = "alacritty"
sstool = "flameshot gui"
file_manager = "thunar"

mod = "mod4"
home = path.expanduser("~")
qconf = f"{home}/.config/qtile/"

# Floating dialogs
@hook.subscribe.client_new
def floating_dialogs(window):
    dialog = window.window.get_wm_type() == 'dialog'
    transient = window.window.get_wm_transient_for()
    if dialog or transient:
        window.floating = True

# Keybinds
keys = [
    # Switch between groups
    Key([mod], "Tab", lazy.screen.toggle_group()),
    # Move focus
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Up", lazy.layout.up()),
    # Move windows
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    # Launch
    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod], "print", lazy.spawn(sstool)),
    Key([mod], "space", lazy.spawn(menu)),
    Key([mod], "n", lazy.spawn(file_manager)),
    # Setting window
    Key([mod], "w", lazy.window.kill()),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "t", lazy.window.toggle_floating()),
    # Qtile
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    # Keyboard
    Key(["shift"], "Alt_L", lazy.widget["keyboardlayout"].next_keyboard()),
    # Volume
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer sset 'Master' 2%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer sset 'Master' 2%-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer sset 'Master' toggle")),
    Key([mod], "XF86AudioRaiseVolume", lazy.spawn("cmus-remote --next")),
    Key([mod], "XF86AudioLowerVolume", lazy.spawn("cmus-remote --prev")),
    Key([mod], "XF86AudioMute", lazy.spawn("cmus-remote --pause")),
]

for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )

# Groups
groups = [
    Group("1", label="󱓻"),
    Group("2", label="󱓻"),
    Group("3", label="󱓻"),
    Group("4", label="󱓻"),
    Group("5", label="󱓻"),
    Group("6", label="󱓻"),
    Group("7", label="󱓻"),
]

for i in groups:
    keys.extend([Key([mod], i.name, lazy.group[i.name].toscreen()), Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True))])

# Layouts
layouts = [
    # Spiral(
    #     border_width=0,
    #     border_on_single=False,
    #     margin = 10,
    #     main_pane = "left",
    #     clockwise = True,
    #     new_client_position = "after_current",
    #     ratio = 0.5,
    # ),
    Bsp(
        border_width=0,
        border_on_single=False,
        margin = 10,
    ),
]

widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    foreground="#babbf1",
    background="#414559",
    fontsize=13,
    padding=6,
)
extension_defaults = widget_defaults.copy()

# Bar decorations
clock = {
    "decorations": [
        RectDecoration(colour="#babbf1", radius=14, filled=True, padding_y=5, padding_x=3, group=False)
    ],
    "padding": 14,
}

rect = {
    "decorations": [
        RectDecoration(colour="#626880", radius=14, filled=True, padding_y=5, padding_x=3, group=False)
    ],
    "padding": 14,
}

archmenu = {
    "decorations": [
        RectDecoration(extrawidth=14, colour="#babbf1", radius=14, filled=True, padding_y=5, padding_x=0, group=False)
    ],
    "padding": 10,
}

github = {
    "decorations": [
        RectDecoration(extrawidth=4, colour="#babbf1", radius=14, filled=True, padding_y=5, padding_x=0, group=False)
    ],
    "padding": 10,
}

powermenu = {
    "decorations": [
        RectDecoration(extrawidth=0, colour="#babbf1", radius=14, filled=True, padding_y=5, padding_x=0, group=False)
    ],
    "padding": 10,
}

rect_g = {
    "decorations": [
        RectDecoration(extrawidth=12, colour="#babbf1", radius=14, filled=True, padding_y=5, padding_x=0, group=True)
    ],
    "padding": 5,
}

rect_systray = {
    "decorations": [
        RectDecoration(extrawidth=12, colour="#babbf1", radius=14, filled=True, padding_y=5, padding_x=0, group=True)
    ],
    "padding": 5,
}

rect_groupbox = {
    "decorations": [
        RectDecoration(colour="#626880", radius=14, filled=True, padding_y=5, padding_x=3, group=False)
    ],
}

# Bar
screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.Spacer(length=6),
                widget.TextBox(" ", fontsize=15, foreground="#414559", mouse_callbacks={"Button1":lazy.spawn(menu)}, **archmenu),
                widget.Spacer(length=6),
                widget.TextBox("󰤄", fontsize=15, foreground="#414559", mouse_callbacks={"Button1":lazy.spawn(power_menu)}, **powermenu),
                widget.Spacer(length=3),
                widget.CheckUpdates(distro="Void", display_format="  {updates} ups", no_update_string="  0 ups", colour_have_updates="#babbf1", colour_no_updates="#babbf1", update_interval=300, **rect),
                widget.Cmus(play_icon="", noplay_color="#babbf1", play_color="#babbf1", fmt='  {}', **rect),
                widget.Spacer(),
                widget.OpenWeather(location="Magnitogorsk", api_key="aa5002a95c1e9f3e666d54f7ea42313e", metric=True, format="  {temp:.0f}°{units_temperature}", **rect),
                widget.Clock(foreground="#414559", format="󱑓  %H:%M, %b (%d)", **clock),
                widget.GroupBox(active="#737994", this_current_screen_border="#babbf1", borderwidth=0, margin_x=10, fontshadow=None, disable_drag=True, fontsize=11, highlight_method="text", padding_x=5, padding_y=2, hide_unused=True, **rect_groupbox),
                widget.Spacer(),
                widget.KeyboardLayout(configured_keyboards=["us", "ru"], fmt='  {}', display_map={"us": "us", "ru": "ru"}, **rect),
                widget.Volume(step=5, fmt='  {}', **rect),
                widget.Spacer(length=3),
                widget.WidgetBox(foreground="#414559", widgets=[widget.Systray(foreground="#414559", icon_size=13, **rect_systray)], close_button_location='left', fontsize=24 ,text_closed=' 󰍟', text_open='󰍞', **rect_g),
                widget.Spacer(length=6),
                widget.TextBox("", fontsize=15, foreground="#414559", mouse_callbacks={"Button1":lazy.spawn("github-desktop")}, **github),
                widget.Spacer(length=6),
            ],
            40, # Bar height
            border_width=[0,0,0,0], # Border width
            margin=[0,200,10,200] # Margin
        ),
    ),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# Misc
dgroups_key_binder = None
dgroups_app_rules = [] # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = Floating(
    border_width=0,
    float_rules=[
        *Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
        Match(wm_class="Telegram"),
        Match(wm_class="gnome-calculator"),
        # Match(wm_class="Alacritty"),
        Match(wm_class="Flet"),
        Match(wm_class="notion.so"),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "Qtile"
