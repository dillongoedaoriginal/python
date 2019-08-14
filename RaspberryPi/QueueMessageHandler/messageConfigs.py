import messageHandlers

supportedMessages = {
    'video': lambda: messageHandlers.handle_video_capture(),
    'image': lambda: messageHandlers.handle_image_capture(),
    'reboot': lambda: messageHandlers.handle_reboot(),
    'shutdown': lambda: messageHandlers.handle_shutdown(),
    'ip': lambda: messageHandlers.handle_send_ip()
}
