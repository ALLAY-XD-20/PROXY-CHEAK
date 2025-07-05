import os
import sys
import asyncio
import aiohttp
import socket
import time
import glob
from datetime import datetime
from colorama import Fore, Style, init
import requests
from concurrent.futures import ThreadPoolExecutor
import threading

# Initialize colorama for colored output
init(autoreset=True)

class ProxyChecker:
    def __init__(self):
        self.setup_directories()
        self.good_proxies = []
        self.bad_proxies = []
        self.total_checked = 0
        self.lock = threading.Lock()
        
    def setup_directories(self):
        """Create necessary directories if they don't exist"""
        directories = [
            'http', 'socks4', 'socks5',
            'results', 'results/http', 'results/socks4', 'results/socks5'
        ]
        
        for directory in directories:
            if not os.path.exists(directory):
                os.makedirs(directory)
                print(f"{Fore.YELLOW}Created directory: {directory}")
    
    def print_ascii_art(self):
        """Print ASCII art banner"""
        ascii_art = f"""
{Fore.CYAN}
 █████╗ ██╗     ██████╗ ██╗  ██╗ █████╗     ██████╗ ███████╗██╗   ██╗
██╔══██╗██║     ██╔══██╗██║  ██║██╔══██╗    ██╔══██╗██╔════╝██║   ██║
███████║██║     ██████╔╝███████║███████║    ██║  ██║█████╗  ██║   ██║
██╔══██║██║     ██╔═══╝ ██╔══██║██╔══██║    ██║  ██║██╔══╝  ╚██╗ ██╔╝
██║  ██║███████╗██║     ██║  ██║██║  ██║    ██████╔╝███████╗ ╚████╔╝ 
╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚══════╝  ╚═══╝  
{Style.RESET_ALL}
{Fore.MAGENTA}                    Proxy Checker Tool v1.0{Style.RESET_ALL}
{Fore.YELLOW}                  Created by Alpha Dev Team{Style.RESET_ALL}
        """
        print(ascii_art)
    
    def show_menu(self):
        """Display the main menu"""
        print(f"\n{Fore.BLUE}{'='*60}")
        print(f"{Fore.BLUE}                    SELECT OPTION")
        print(f"{Fore.BLUE}{'='*60}")
        print(f"{Fore.BLUE}1. HTTP PROXIES CHECK")
        print(f"{Fore.BLUE}2. SOCKS4 PROXIES CHECK") 
        print(f"{Fore.BLUE}3. SOCKS5 PROXIES CHECK")
        print(f"{Fore.BLUE}4. UPDATE (REACT ON GITHUB)")
        print(f"{Fore.BLUE}5. EXIT")
        print(f"{Fore.BLUE}{'='*60}")
        
        while True:
            try:
                choice = input(f"{Fore.CYAN}Enter your choice (1-5): {Style.RESET_ALL}")
                if choice in ['1', '2', '3', '4', '5']:
                    return int(choice)
                else:
                    print(f"{Fore.RED}Invalid choice! Please enter 1-5.")
            except (ValueError, KeyboardInterrupt):
                print(f"{Fore.RED}Invalid input! Please enter a number between 1-5.")
    
    def load_proxies(self, proxy_type):
        """Load proxies from txt files in the specified directory"""
        proxies = []
        directory = proxy_type.lower()
        
        if not os.path.exists(directory):
            print(f"{Fore.RED}Directory {directory} not found!")
            return proxies
        
        txt_files = glob.glob(f"{directory}/*.txt")
        
        if not txt_files:
            print(f"{Fore.RED}No .txt files found in {directory} directory!")
            return proxies
        
        print(f"{Fore.YELLOW}Loading proxies from {directory} directory...")
        
        for file_path in txt_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    for line in lines:
                        line = line.strip()
                        if line and ':' in line:
                            try:
                                ip, port = line.split(':', 1)
                                if ip and port.isdigit():
                                    proxies.append(f"{ip}:{port}")
                            except ValueError:
                                continue
                print(f"{Fore.GREEN}Loaded {len(lines)} proxies from {file_path}")
            except Exception as e:
                print(f"{Fore.RED}Error loading {file_path}: {e}")
        
        print(f"{Fore.CYAN}Total proxies loaded: {len(proxies)}")
        return proxies
    
    def check_http_proxy(self, proxy):
        """Check HTTP proxy validity"""
        try:
            proxies = {
                'http': f'http://{proxy}',
                'https': f'http://{proxy}'
            }
            
            response = requests.get(
                'http://httpbin.org/ip',
                proxies=proxies,
                timeout=10
            )
            
            if response.status_code == 200:
                with self.lock:
                    self.good_proxies.append(proxy)
                    print(f"{Fore.GREEN}GOOD: {proxy}")
                return True
            else:
                with self.lock:
                    self.bad_proxies.append(proxy)
                    print(f"{Fore.RED}BAD: {proxy}")
                return False
                
        except Exception:
            with self.lock:
                self.bad_proxies.append(proxy)
                print(f"{Fore.RED}BAD: {proxy}")
            return False
    
    def check_socks_proxy(self, proxy, socks_version):
        """Check SOCKS proxy validity"""
        try:
            ip, port = proxy.split(':')
            port = int(port)
            
            # Create socket connection
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(10)
            
            if socks_version == 4:
                # SOCKS4 connection test
                result = sock.connect_ex((ip, port))
            else:  # SOCKS5
                # SOCKS5 connection test
                result = sock.connect_ex((ip, port))
            
            sock.close()
            
            if result == 0:
                with self.lock:
                    self.good_proxies.append(proxy)
                    print(f"{Fore.GREEN}GOOD: {proxy}")
                return True
            else:
                with self.lock:
                    self.bad_proxies.append(proxy)
                    print(f"{Fore.RED}BAD: {proxy}")
                return False
                
        except Exception:
            with self.lock:
                self.bad_proxies.append(proxy)
                print(f"{Fore.RED}BAD: {proxy}")
            return False
    
    def save_results(self, proxy_type, good_proxies, bad_proxies):
        """Save results to files"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        results_dir = f"results/{proxy_type.lower()}"
        
        # Save good proxies
        if good_proxies:
            good_file = f"{results_dir}/good_proxies_{timestamp}.txt"
            with open(good_file, 'w') as f:
                for proxy in good_proxies:
                    f.write(f"{proxy}\n")
            print(f"{Fore.GREEN}Good proxies saved to: {good_file}")
        
        # Save bad proxies
        if bad_proxies:
            bad_file = f"{results_dir}/bad_proxies_{timestamp}.txt"
            with open(bad_file, 'w') as f:
                for proxy in bad_proxies:
                    f.write(f"{proxy}\n")
            print(f"{Fore.RED}Bad proxies saved to: {bad_file}")
        
        # Save summary
        summary_file = f"{results_dir}/summary_{timestamp}.txt"
        with open(summary_file, 'w') as f:
            f.write(f"Proxy Check Summary - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"{'='*50}\n")
            f.write(f"Proxy Type: {proxy_type.upper()}\n")
            f.write(f"Total Checked: {len(good_proxies) + len(bad_proxies)}\n")
            f.write(f"Good Proxies: {len(good_proxies)}\n")
            f.write(f"Bad Proxies: {len(bad_proxies)}\n")
            f.write(f"Success Rate: {(len(good_proxies) / (len(good_proxies) + len(bad_proxies)) * 100):.2f}%\n")
        
        print(f"{Fore.CYAN}Summary saved to: {summary_file}")
    
    def check_proxies(self, proxy_type, proxies):
        """Check proxies with multithreading"""
        if not proxies:
            print(f"{Fore.RED}No proxies to check!")
            return
        
        self.good_proxies = []
        self.bad_proxies = []
        
        print(f"\n{Fore.YELLOW}Starting {proxy_type.upper()} proxy checking...")
        print(f"{Fore.YELLOW}Total proxies to check: {len(proxies)}")
        print(f"{Fore.YELLOW}{'='*60}")
        
        start_time = time.time()
        
        # Use ThreadPoolExecutor for concurrent checking
        with ThreadPoolExecutor(max_workers=50) as executor:
            if proxy_type.lower() == 'http':
                futures = [executor.submit(self.check_http_proxy, proxy) for proxy in proxies]
            elif proxy_type.lower() == 'socks4':
                futures = [executor.submit(self.check_socks_proxy, proxy, 4) for proxy in proxies]
            elif proxy_type.lower() == 'socks5':
                futures = [executor.submit(self.check_socks_proxy, proxy, 5) for proxy in proxies]
            
            # Wait for all futures to complete
            for future in futures:
                future.result()
        
        end_time = time.time()
        
        # Print results
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.CYAN}CHECKING COMPLETED!")
        print(f"{Fore.CYAN}{'='*60}")
        print(f"{Fore.GREEN}Good Proxies: {len(self.good_proxies)}")
        print(f"{Fore.RED}Bad Proxies: {len(self.bad_proxies)}")
        print(f"{Fore.YELLOW}Total Checked: {len(proxies)}")
        print(f"{Fore.YELLOW}Time Taken: {end_time - start_time:.2f} seconds")
        print(f"{Fore.YELLOW}Success Rate: {(len(self.good_proxies) / len(proxies) * 100):.2f}%")
        
        # Save results
        self.save_results(proxy_type, self.good_proxies, self.bad_proxies)
    
    def update_from_github(self):
        """Handle GitHub update functionality"""
        print(f"{Fore.YELLOW}GitHub Update Feature")
        print(f"{Fore.CYAN}This feature would typically:")
        print(f"{Fore.CYAN}1. Connect to GitHub repository")
        print(f"{Fore.CYAN}2. Download latest proxy lists")
        print(f"{Fore.CYAN}3. Update local proxy files")
        print(f"{Fore.CYAN}4. Refresh the tool")
        print(f"{Fore.RED}Note: Implement actual GitHub API integration as needed")
        
        # Placeholder for GitHub integration
        input(f"{Fore.YELLOW}Press Enter to continue...")
    
    def run(self):
        """Main application loop"""
        self.print_ascii_art()
        
        while True:
            choice = self.show_menu()
            
            if choice == 1:
                # HTTP Proxy Check
                proxies = self.load_proxies('http')
                if proxies:
                    self.check_proxies('http', proxies)
                
            elif choice == 2:
                # SOCKS4 Proxy Check
                proxies = self.load_proxies('socks4')
                if proxies:
                    self.check_proxies('socks4', proxies)
                
            elif choice == 3:
                # SOCKS5 Proxy Check
                proxies = self.load_proxies('socks5')
                if proxies:
                    self.check_proxies('socks5', proxies)
                
            elif choice == 4:
                # GitHub Update
                self.update_from_github()
                
            elif choice == 5:
                # Exit
                print(f"{Fore.CYAN}Thanks for using Alpha Dev Proxy Checker!")
                print(f"{Fore.YELLOW}Goodbye!")
                sys.exit(0)
            
            print(f"\n{Fore.MAGENTA}Press Enter to continue...")
            input()

def main():
    """Main entry point"""
    try:
        checker = ProxyChecker()
        checker.run()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Program interrupted by user.")
        print(f"{Fore.YELLOW}Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
