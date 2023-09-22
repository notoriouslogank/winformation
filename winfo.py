import emailer as e
import getsysinfo


if __name__ == "__main__":
    SYS_INFO = "SYS_INFO.txt"
    getsysinfo.isPlatformSupported()  # This should probably be renamed, I guess
    e.email.set_content(e.cast_file_to_message(SYS_INFO))
    e.send_mail()
