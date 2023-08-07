import pytube as pt
import youtubesearchpython as ys
import os
NEW_FAIL = []
NEW_PASS = []

def finalize_list():
    global NEW_PASS
    global NEW_FAIL
    with open('music/songlist.txt', 'r') as f:
        lines = f.readlines()
    
    if len(lines) == 0:
        lines.append('----Downloaded-Songs:----\n')
        for passed in NEW_PASS:
            lines.append(passed)
        lines.append('----Failed-Songs:----\n')
        for failed in NEW_FAIL:
            lines.append(failed)
    else:
        found_pass = False
        found_fail = False
        for line in lines:
            if line == '----Downloaded-Songs:----\n' or line == '----Downloaded-Songs:----':
                found_pass = True
                pass_ind = lines.index(line) 
            elif line == '----Failed-Songs:----\n' or line == '----Failed-Songs:----':
                found_fail = True 
                fail_ind = lines.index(line)
        
        NEW_LINES = [line.strip() for line in lines] 
        
        if found_pass:
            for success in NEW_PASS:
                if success not in NEW_LINES:
                    lines.insert(pass_ind+1, success)
        else:
            lines.insert(0,'----Downloaded-Songs:----')
            
        if found_fail:
            fail_ind = lines.index(line)
            for failure in NEW_FAIL:
                if failure not in NEW_LINES:
                    lines.insert(fail_ind+1, failure)
        else:
            lines.insert(-1,'----Failed-Songs:----')
        
    with open('music/songlist.txt', 'w') as f:
        for i, line in enumerate(lines):
            f.write(line.strip())
            if i != len(lines) - 1:
                f.write("\n")
        

def make_music_folder():
    dirname = os.path.dirname(__file__)
    dirname = dirname + "\Music"
    if not os.path.exists(dirname):
        os.makedirs(dirname)
        
    return dirname


def get_passed_songs():
    dirname = os.path.dirname(__file__)
    dirname = dirname + "\Music"
    if not os.path.exists(dirname + "/songlist.txt"):
        print("This is the first time downloading")
        with open('music/songlist.txt', 'w') as f:
            pass
        return []
    else:
        has_passes = False        
        with open('D:\songs\Youtube grab\music\songlist.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line == '----Downloaded-Songs:----\n' or line == '----Downloaded-Songs:----':
                    split_at = lines.index(line)
                    has_passes = True
                    break
                
            passed = []
            try:
                ending = lines.index('----Failed-Songs:----\n') 
            except:
                try:
                    ending = lines.index('----Failed-Songs:----')
                except:
                    pass
            finally:
                ending = len(lines)
            if has_passes:    
                for i in range(split_at, ending):
                    passed.append(lines[i].strip())
            return passed


def get_video_link(name):

    try:
        videosSearch = ys.VideosSearch(name,limit=1)
        link = videosSearch.result()["result"][0]["link"]
        return link
    except:
        global NEW_FAIL
        NEW_FAIL.append(name)
        return ""
        


def call_download(name, link, path, passed_songlist):
    global NEW_FAIL
    global NEW_PASS
    if name in passed_songlist or name in NEW_FAIL:
        return
    else:
        NEW_PASS.append(name)

        
    def progress_func(stream, chunk, bytes_remaining):
        print(f"{name} has been downloaded")
            
    yt = pt.YouTube(
            link,
            on_progress_callback=progress_func,
        )

    try:
        stream = yt.streams.filter(only_audio=True)[0]
        out_file = stream.download(output_path=path)
        base, _ = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
    except:
        os.remove(out_file)


def read_input_file():
    with open('D:\songs\Youtube grab\input.txt', 'r') as f:
        names = f.readlines()
        names = [name.strip() for name in names]

        return names



if __name__ == '__main__':
    list_of_names = read_input_file()
    path = make_music_folder()
    PassedSongs = get_passed_songs()
    
    for name in list_of_names:
        link = get_video_link(name)
        call_download(name=name, link=link, path=path, passed_songlist=PassedSongs)
    finalize_list()
    print("\nProgram has ended")
    
    '''
    How to run:
    open your terminal and run the following command.
      pip install -r requirements.txt
    -throw all your music in the songlist.txt file separated by a space.
    -run the program and wait for the download.
    -enjoy your music!
    
    OR
    
    simply run the following in your terminal
      source env/bin/activate
    run the app, and enjoy
    '''