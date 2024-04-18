return {
  {
    "iamcco/markdown-preview.nvim",
    cmd = { "MarkdownPreviewToggle", "MarkdownPreview", "MarkdownPreviewStop" },
    build = "cd app && yarn install",
    init = function()
      vim.g.mkdp_filetypes = { "markdown" }
    end,
    ft = { "markdown" },
  },
  { "mistricky/codesnap.nvim",
    build = "make",
    config = function()
      require("codesnap").setup({
        save_path = "~/Pictures/codesnap",
        bg_theme = "bamboo",
        watermark = "",
        mac_window_bar = true,
        code_font_family = "JetBrainsMono Nerd Font",
      })
    end,
  },
  {
    "nvimdev/dashboard-nvim",
    event = "VimEnter",
    config = function()
      require("dashboard").setup({
        theme = "doom",
        config = {
          header = {"",
"",
"██╗          ",
"╚██╗         ",
" ╚██╗        ",
" ██╔╝        ",
"██╔╝ ███████╗",
"╚═╝  ╚══════╝",
"",
"",},
          center = {
            {
              icon = "󰈞  ",
              icon_hl = "Title",
              desc = "Find File  ",
              desc_hl = "String",
              key = "f",
              keymap = "SPC f f",
              key_hl = "Number",
              key_format = " %s",
              action = "Telescope find_files",
            },
            {
              icon = "󱋡  ",
              icon_hl = "Title",
              desc = "Recently Used Files",
              desc_hl = "String",
              key = "r",
              keymap = "SPC f o",
              key_hl = "Number",
              key_format = " %s",
              action = "Telescope oldfiles",
            },
            {
              icon = "  ",
              icon_hl = "Title",
              desc = "Find Word",
              desc_hl = "String",
              key = "w",
              keymap = "SPC f w",
              key_hl = "Number",
              key_format = " %s",
              action = "Telescope live_grep",
            },
            {
              icon = "  ",
              icon_hl = "Title",
              desc = "Open Bookmarks",
              desc_hl = "String",
              key = "b",
              keymap = "None",
              key_hl = "Number",
              key_format = " %s",
              action = "Telescope marks",
            },
            {
              icon = "󰏘  ",
              icon_hl = "Title",
              desc = "Change Theme",
              desc_hl = "String",
              key = "t",
              keymap = "SPC t h",
              key_hl = "Number",
              key_format = " %s",
              action = "Telescope themes",
            },
            {
              icon = "󰘳  ",
              icon_hl = "Title",
              desc = "Open Cheatsheet",
              desc_hl = "String",
              key = "c",
              keymap = "SPC c h",
              key_hl = "Number",
              key_format = " %s",
              action = "NvCheatsheet",
            },
          }
        },
        hide = {
          statusline
        },
      })
    end,
    dependencies = { {"nvim-tree/nvim-web-devicons"}}
  },

  {
    "neovim/nvim-lspconfig",
    config = function()
      require("nvchad.configs.lspconfig").defaults()
      require "configs.lspconfig"
    end,
  },

  {
    'Exafunction/codeium.vim',
    event = 'BufEnter',
  },

  {
    'AlphaTechnolog/pywal.nvim',
    as = 'pywal',
  },

  {
    "elkowar/yuck.vim",
  },

  {
    "stevearc/conform.nvim",
    config = function()
      require "configs.conform"
    end,
  },

  {
    "nvim-tree/nvim-tree.lua",
    opts = {
      git = { enable = true },
    },
  },
}
