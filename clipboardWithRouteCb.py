from gevent import monkey
monkey.patch_all()

import os
from flask import Flask, Response, send_file
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='gevent')

DB_FILE = "cb.txt"
if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f: f.write("暂无数据")

@app.route("/", methods=["GET", "POST"])
def index():
    return Response(
        '''<!DOCTYPE html><html lang="zh-cn"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><link rel="icon" type="image/svg+xml"  href="data:image/svg+xml,%3C?xml version=%221.0%22 encoding=%22UTF-8%22?%3E%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%22144%22 height=%22144%22 viewBox=%220 0 144 144%22%3E%3Cdefs%3E%3Cstyle%3E:root {--stroke-color: %23000;}@media (prefers-color-scheme: dark) {:root {--stroke-color: %23fff;}}.st0,.st1 {fill: none;stroke: var(--stroke-color);stroke-linecap: round;stroke-miterlimit: 10;}.st0,.st2 {stroke-width: 5px;}.st1 {stroke-width: 5px;}.st2 {stroke: var(--stroke-color);fill: var(--stroke-color);}%3C/style%3E%3C/defs%3E%3Cg%3E%3Cpath class=%22st0%22 d=%22M56.96,30.24c-2.3,0-4.16-1.86-4.16-4.16s1.86-4.16,4.16-4.16%22/%3E%3Cpath class=%22st0%22 d=%22M87.04,21.92c2.3,0,4.16,1.86,4.16,4.16s-1.86,4.16-4.16,4.16%22/%3E%3Cline class=%22st0%22 x1=%2256.96%22 y1=%2221.92%22 x2=%2287.04%22 y2=%2221.92%22/%3E%3Cline class=%22st0%22 x1=%2256.96%22 y1=%2230.24%22 x2=%2287.04%22 y2=%2230.24%22/%3E%3C/g%3E%3Cline class=%22st0%22 x1=%2252.8%22 y1=%2226.08%22 x2=%2238.39%22 y2=%2225.97%22/%3E%3Cline class=%22st0%22 x1=%2234.39%22 y1=%22117.08%22 x2=%2234.39%22 y2=%2229.97%22/%3E%3Cline class=%22st0%22 x1=%2291.2%22 y1=%2226.08%22 x2=%22105.72%22 y2=%2225.97%22/%3E%3Cline class=%22st0%22 x1=%22109.72%22 y1=%22117.08%22 x2=%22109.72%22 y2=%2229.97%22/%3E%3Cline class=%22st0%22 x1=%2238.39%22 y1=%22121.08%22 x2=%22105.72%22 y2=%22121.08%22/%3E%3Cline class=%22st1%22 x1=%2247.42%22 y1=%2261.08%22 x2=%2282.25%22 y2=%2261.08%22/%3E%3Cline class=%22st1%22 x1=%2247.42%22 y1=%2279.08%22 x2=%2282.25%22 y2=%2279.08%22/%3E%3Cline class=%22st1%22 x1=%2247.81%22 y1=%2297.08%22 x2=%2282.64%22 y2=%2297.08%22/%3E%3Ccircle class=%22st2%22 cx=%2296.03%22 cy=%2261.08%22 r=%223.5%22/%3E%3Ccircle class=%22st2%22 cx=%2296.03%22 cy=%2279.08%22 r=%223.5%22/%3E%3Ccircle class=%22st2%22 cx=%2296.03%22 cy=%2297.08%22 r=%223.5%22/%3E%3Cpath class=%22st0%22 d=%22M105.72,25.97c2.21,0,4,1.79,4,4%22/%3E%3Cpath class=%22st0%22 d=%22M34.39,29.97c0-2.21,1.79-4,4-4%22/%3E%3Cpath class=%22st0%22 d=%22M38.39,121.08c-2.21,0-4-1.79-4-4%22/%3E%3Cpath class=%22st0%22 d=%22M109.72,117.08c0,2.21-1.79,4-4,4%22/%3E%3C/svg%3E"><title>网络剪贴板</title><style>html::before {content: "";width: 100%;height: 100%;position: fixed;z-index: -1;background-image: linear-gradient(120deg, #f0fffc 0%, #f6ffea 100%);}textarea {font-family: inherit;font-size: 16px;background-color: inherit;}button {font-size: 16px;}.btn {background-color: #6464644C;border: none;border-radius: 8px;transition: transform 0.3s, background-color 0.5s;}.btn:hover {transform: translateY(-1.5px) scaleX(1.03);background-color: #9696964C;}#in {border-radius: 8px;background-color: #E6E6E64C;transition: transform 0.3s, background-color 0.3s;}#in:hover {transform: translateY(-1.5px) scaleX(1.003);background-color: #FFFFFF4C;}</style>
        <script src="socket.io.min.js"></script>
        </head><span style="font-size: 50px;margin: 10px;">网络剪贴板</span><button onclick="location.reload();" class="btn" style="margin-top: 10px">刷新</button>&emsp;<button onclick="copyText('0')" class="btn">复制</button><form id="form"><div style="display: flex;"><textarea name="txt" rows="1" oninput="resizeTextarea(this)"  style="flex: 1; resize: none" id="in"></textarea><button type="submit" style="align-self: stretch;height: auto;margin-left: 4px;" class="btn">提交</button></div></form><br><textarea readonly style="width: 100%;resize: none;border: none; outline: none;" id="0">加载中...</textarea><script>function resizeTextarea(textarea) {textarea.style.height = "auto";textarea.style.height = textarea.scrollHeight + "px";}function copyText(id) {const copyText = document.getElementById(id);copyText.select();copyText.setSelectionRange(0, 99999);document.execCommand("copy");}resizeTextarea(document.getElementById("0"));resizeTextarea(document.getElementById("in"));
        
        const socket = io({
    path: '/cb/socket.io',
    transports: ['websocket'] 
});

        socket.on("message", (data) => {
            document.getElementById("0").value = data;
            resizeTextarea(document.getElementById("0"));
        });

        const form = document.getElementById("form");
        form.addEventListener("submit", (e) => {
            e.preventDefault();
            const txtInput = form.querySelector('textarea[name="txt"]');
            const txt = txtInput.value;
            if (socket.connected) {
                socket.send(txt);
                txtInput.value = "";
                resizeTextarea(document.getElementById("in"));
            } else {
                alert("未连接，请检查网络");
            }
        });</script>''',
        content_type="text/html"
    )

@app.route("/source", methods=["GET", "POST"])
def source():
    try:
        txt = open(DB_FILE, mode='r').read()
    except:
        txt = "暂无数据"
    return Response(txt, content_type="text/plain")

@app.route("/socket.io.min.js")
def js_file():
    return send_file('socket.io.min.js')

@socketio.on('connect')
def handle_connect():
    try:
        with open(DB_FILE, mode='r') as f:
            content = f.read()
    except:
        content = ""
    send(content)

@socketio.on('message')
def handle_message(msg):
    with open(DB_FILE, mode='w') as f:
        f.write(msg)
    send(msg, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=11451)