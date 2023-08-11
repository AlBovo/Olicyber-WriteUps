#!/usr/bin/env python3
import socket   
import dns.resolver

vis = []
res = dns.resolver.Resolver()
res.timeout = 100
res.port = 10500
res.nameservers = [socket.gethostbyname("pisani.challs.olicyber.it")]

def dfs(pos):
    if pos in vis:
        return
    vis.append(pos)
    risp = res.resolve(pos, "txt").response.answer[0][0].to_text().split(" ")[0]
    if not "flag" in risp:
        print("No risp in " + pos)
    else:
        print(risp)
        exit(0)
    l = [f"down.{pos}", f"up.{pos}", f"left.{pos}", f"right.{pos}"]
    for i in l:
        try:
            risp = res.resolve(i, "cname").response.answer[0][0].to_text().split(" ")[0][:-1]
        except Exception as e:
            continue
        dfs(risp)
dfs("00000000-0000-4000-0000-000000000000.maze.localhost")
