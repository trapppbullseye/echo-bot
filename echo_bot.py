#!/usr/bin/env python3
"""Discord echo and reverse text bot"""
import argparse
def main():
 p=argparse.ArgumentParser(description="Discord echo and reverse text bot")
 p.add_argument("--version",action="store_true")
 args=p.parse_args()
 if args.version:print("echo-bot v0.1.0");return
 print(f"[12:13] echo-bot ready")
if __name__=="__main__":main()
