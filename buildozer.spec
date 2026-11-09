[app]
title = YT Downloader
package.name = ytdownloader
package.domain = org.yourname

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3,kivy,yt-dlp,certifi,urllib3,idna,charset-normalizer

orientation = portrait
fullscreen = 0

# Android specific configurations
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b

# Target architectures requested: v7a (32-bit) and v8a (64-bit)
android.archs = armeabi-v7a, arm64-v8a

# Request Storage Write permissions to save the downloaded videos
android.permissions = android.permission.WRITE_EXTERNAL_STORAGE, android.permission.READ_EXTERNAL_STORAGE, android.permission.INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
