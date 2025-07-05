# 🔥 Alpha Dev Proxy Checker v1.2

<div align="center">
  
![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Version](https://img.shields.io/badge/version-1.2-orange.svg)
![Status](https://img.shields.io/badge/status-Active-brightgreen.svg)

[![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/5YsStsgmXA)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ALLAY-XD-20/PROXY-CHEAK)
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)

</div>

## 📋 Table of Contents

- [🌟 Features](#-features)
- [⚡ Quick Start](#-quick-start)
- [🛠️ Installation](#️-installation)
- [📖 Usage](#-usage)
- [📁 Directory Structure](#-directory-structure)
- [🎯 Proxy Types](#-proxy-types)
- [📊 Results](#-results)
- [🔧 Configuration](#-configuration)
- [🤝 Contributing](#-contributing)
- [📞 Support](#-support)
- [📄 License](#-license)

## 🌟 Features

### 🎨 **Beautiful Interface**
- **ASCII Art Banner** with Alpha Dev branding
- **Color-coded Console Output** (Green for good, Red for bad)
- **Real-time Progress Tracking** with `(current/total)` format
- **Professional Menu System** with blue-themed interface

### 🚀 **High Performance**
- **Multi-threaded Checking** (50 concurrent connections)
- **Asynchronous Processing** for optimal speed
- **Thread-safe Operations** with proper locking
- **Real-time Statistics** and progress updates

### 🔍 **Multiple Proxy Support**
- **HTTP/HTTPS Proxies** - Full web proxy support
- **SOCKS4 Proxies** - Socket secure protocol v4
- **SOCKS5 Proxies** - Socket secure protocol v5
- **Auto-detection** of proxy formats

### 💾 **Smart Results Management**
- **Automatic Directory Creation** for organization
- **Timestamped Results** for easy tracking
- **Separate Good/Bad Lists** for efficiency
- **Detailed Summary Reports** with statistics

### 🔄 **GitHub Integration**
- **Auto-update Feature** from GitHub repository
- **Remote Proxy Lists** downloading capability
- **Version Control** integration

## ⚡ Quick Start

```bash
# Clone the repository
git clone https://github.com/ALLAY-XD-20/PROXY-CHEAK.git

# Navigate to directory
cd PROXY-CHEAK

# Install dependencies
pip install -r requirements.txt

# Run the tool
python proxy_checker.py
```

## 🛠️ Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager
- Internet connection

### Step-by-Step Installation

1. **Clone Repository**
   ```bash
   git clone https://github.com/ALLAY-XD-20/PROXY-CHEAK.git
   cd PROXY-CHEAK
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify Installation**
   ```bash
   python main.py
   ```

### Required Packages
- `requests` - HTTP library for proxy testing
- `aiohttp` - Async HTTP client/server framework
- `colorama` - Cross-platform colored terminal text
- `asyncio` - Asynchronous I/O support

## 📖 Usage

### 🎯 **Main Menu Options**

```
1. HTTP PROXIES CHECK    - Test HTTP/HTTPS proxies
2. SOCKS4 PROXIES CHECK  - Test SOCKS4 proxies
3. SOCKS5 PROXIES CHECK  - Test SOCKS5 proxies
4. UPDATE (GitHub)       - Update from repository
5. EXIT                  - Close application
```

### 📝 **Proxy File Format**
Place your proxy lists in `.txt` files with the format:
```
IP:PORT
192.168.1.1:8080
10.0.0.1:3128
proxy.example.com:8080
```

### 🎨 **Console Output Example**
```
GOOD: 192.168.1.1:8080 (1/1000)
BAD: 192.168.1.2:8080 (2/1000)
GOOD: 192.168.1.3:8080 (3/1000)
BAD: 192.168.1.4:8080 (4/1000)
```

## 📁 Directory Structure

```
PROXY-CHEAK/
├── proxy_checker.py      # Main application
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── http/                # HTTP proxy lists
│   ├── list1.txt
│   ├── list2.txt
│   └── ...
├── socks4/              # SOCKS4 proxy lists
│   ├── list1.txt
│   ├── list2.txt
│   └── ...
├── socks5/              # SOCKS5 proxy lists
│   ├── list1.txt
│   ├── list2.txt
│   └── ...
└── results/             # Results storage
    ├── http/
    │   ├── good_proxies_20240101_120000.txt
    │   ├── bad_proxies_20240101_120000.txt
    │   └── summary_20240101_120000.txt
    ├── socks4/
    └── socks5/
```

## 🎯 Proxy Types

### 🌐 **HTTP Proxies**
- **Protocol**: HTTP/HTTPS
- **Use Case**: Web browsing, API requests
- **Testing Method**: HTTP request to test endpoint
- **Timeout**: 10 seconds

### 🔌 **SOCKS4 Proxies**
- **Protocol**: SOCKS version 4
- **Use Case**: General TCP connections
- **Testing Method**: Socket connection test
- **Timeout**: 10 seconds

### 🔐 **SOCKS5 Proxies**
- **Protocol**: SOCKS version 5
- **Use Case**: TCP/UDP connections with authentication
- **Testing Method**: Socket connection test
- **Timeout**: 10 seconds

## 📊 Results

### 📈 **Statistics Provided**
- **Total Proxies Checked**
- **Good Proxies Count**
- **Bad Proxies Count**
- **Success Rate Percentage**
- **Time Taken**

### 📄 **Output Files**
- `good_proxies_TIMESTAMP.txt` - Working proxies
- `bad_proxies_TIMESTAMP.txt` - Non-working proxies
- `summary_TIMESTAMP.txt` - Detailed statistics

### 📅 **Timestamp Format**
```
YYYYMMDD_HHMMSS
Example: 20240101_120000
```

## 🔧 Configuration

### ⚙️ **Customizable Settings**
- **Thread Count**: Modify `max_workers=50` in the code
- **Timeout**: Adjust `timeout=10` for proxy testing
- **Test URL**: Change test endpoint in HTTP checker
- **Output Format**: Modify result file formats

### 🎨 **Color Customization**
- **Good Proxies**: Green (`Fore.GREEN`)
- **Bad Proxies**: Red (`Fore.RED`)
- **Menu**: Blue (`Fore.BLUE`)
- **Info**: Yellow (`Fore.YELLOW`)

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### 🐛 **Bug Reports**
- Use GitHub Issues to report bugs
- Include detailed steps to reproduce
- Provide system information

### 💡 **Feature Requests**
- Suggest new features via GitHub Issues
- Explain the use case and benefits
- Provide implementation ideas if possible

### 🔄 **Pull Requests**
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### 📋 **Development Setup**
```bash
git clone https://github.com/ALLAY-XD-20/PROXY-CHEAK.git
cd PROXY-CHEAK
pip install -r requirements.txt
# Make your changes
python proxy_checker.py  # Test
```

## 📞 Support

### 💬 **Discord Community**
Join our Discord server for:
- **Real-time Support** from developers and community
- **Feature Discussions** and feedback
- **Updates and Announcements**
- **Community Proxy Lists** sharing

[![Join Discord](https://img.shields.io/badge/Join%20Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/5YsStsgmXA)

### 🐛 **GitHub Issues**
For bug reports and feature requests:
- [Create an Issue](https://github.com/ALLAY-XD-20/PROXY-CHEAK/issues)
- [View Documentation](https://github.com/ALLAY-XD-20/PROXY-CHEAK/wiki)

### 📧 **Contact Information**
- **GitHub**: [@ALLAY-XD-20](https://github.com/ALLAY-XD-20)
- **Discord**: [Alpha Dev Community](https://discord.gg/5YsStsgmXA)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Alpha Dev Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

<div align="center">

**Made with ❤️ by Alpha Dev Team**

[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ALLAY-XD-20/PROXY-CHEAK)
[![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/5YsStsgmXA)
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)

⭐ **Star this repository if you find it helpful!** ⭐

</div>
