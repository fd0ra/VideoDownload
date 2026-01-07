import yt_dlp
import os

def downloader():
    print("--- YouTube Downloader CLI ---")
    
    # 1. Get the URL
    url = input("Enter the link (Video or Playlist): ").strip()
    if not url:
        print("❌ Error: No URL provided.")
        return

    # 2. Check for Premium/Members-Only content
    print("\nIs this a 'Members Only' or 'Premium' video?")
    is_member = input("Answer (y/n): ").lower().strip()
    
    use_cookies = False
    if is_member == 'y':
        if os.path.exists('cookies.txt'):
            use_cookies = True
            print(">> ✅ 'cookies.txt' found. Using authentication.")
        else:
            print("⚠️  WARNING: 'cookies.txt' not found in the current directory!")
            print("   Proceeding without cookies (download might fail for locked content).")
    else:
        print(">> Proceeding anonymously (No cookies used).")

    # 3. Select Format
    print("\nSelect Format:")
    print("1. Video (Best Quality + Audio merged into MP4)")
    print("2. Audio Only (MP3)")
    choice = input("Choice (1 or 2): ").strip()

    # 4. Configure yt-dlp options
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s', # Output filename pattern
        'ignoreerrors': True,            # Continue playlist even if one video fails
        'no_warnings': True,
        'quiet': False,
    }

    # Add cookie file if requested
    if use_cookies:
        ydl_opts['cookiefile'] = 'cookies.txt'

    # Set specific format options
    if choice == '2':
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
        print("\n⬇️  Downloading as MP3...")
    else:
        ydl_opts.update({
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4', # Requires ffmpeg
        })
        print("\n⬇️  Downloading as Video...")

    # 5. Start Download
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n✅ Operation completed successfully!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        if use_cookies:
            print("   (Tip: Ensure your 'cookies.txt' is valid and up-to-date.)")

if __name__ == "__main__":
    downloader()
