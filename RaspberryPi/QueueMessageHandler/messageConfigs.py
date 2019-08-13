import messageHandlers

supportedMessages = {
    'video': lambda: messageHandlers.handle_video_capture()
}
