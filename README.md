# Project Eden - Multi-Purpose RPG Bot

Welcome to **Project Eden**, a versatile and modular RPG bot designed to enhance your Discord server with a rich, immersive role-playing experience. Built using Python and `discord.py`, Project Eden is perfect for tabletop RPG campaigns, text-based RPGs, or just adding some fun RPG-inspired features to your server.

---

## Features

- **Dice Rolling**: Automatically roll dice with simple commands (e.g., `2d20+5`).
- **Initiative Tracker**: Manage turn-based combat with an easy-to-use initiative system.
- **Multi-Game Support**: Supports various RPG systems (D&D, Pathfinder, custom systems, etc.).
- **Modular Design**: Easily add or remove features to suit your server's needs.
- **Customizable**: Highly configurable to fit your RPG setting and rules.

---

## Work in Progress (WIP)
- **World Building**: Create and manage custom worlds, locations, and NPCs.
- **Character Management**: Create, customize, and manage RPG characters with stats, inventories, and progression systems.
- **Quest System**: Create and track quests for players, complete with objectives, rewards, and storylines.
- **Economy & Shops**: Earn in-game currency, buy items, and trade with other players.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Pedro-Artur-RF/ProjectEdenV2.git
   cd ProjectEdenV2
   ```

2. **Install Dependencies**:
   Make sure you have [Python 3.8 or higher](https://www.python.org/downloads/) installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Configuration**:
   - Rename `config.example.json` to `config.json`.
   - Fill in your Discord bot token and other configuration options.

4. **Run the Bot**:
   ```bash
   python bot.py
   ```

5. **Invite the Bot to Your Server**:
   Use the OAuth2 URL generated in the Discord Developer Portal to invite the bot to your server.

---

## Commands

Here are some of the commands you can use with Project Eden:

### Dice Rolling
- **Single Roll**: Just type the dice format: `xdx` (e.g., `1d20`).
- **Multiple Rolls**: Use the format: `x#xdx` (e.g., `2#2d20` for two rolls of 2d20).

### Initiative Tracker
- **Start Tracker**: Type `!init` to start the initiative tracker.
- **Join Initiative**: Type `<init value> <player name>` to join (e.g., `15 yasho`).

---

## Contributing

We welcome contributions to Project Eden! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Submit a pull request.

Please ensure your code follows our coding standards and includes appropriate documentation.

---

## License

Project Eden is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

## Support

If you encounter any issues or have suggestions for new features, please open an issue on the [GitHub Issues Page](https://github.com/Pedro-Artur-RF/ProjectEdenV2/issues).

Join our [Discord Server](https://discord.gg/wxfcPH7Qey) for community support and updates.

---

## Acknowledgments

- Special thanks to the `discord.py` library for making this bot possible.
- Inspired by various tabletop RPG systems and community-driven projects.

---

**Project Eden** is a labor of love, designed to bring your RPG adventures to life. Enjoy your journey, and may your rolls be ever in your favor! 🎲✨

---

*Project Eden is not affiliated with or endorsed by any specific RPG system or company.*
