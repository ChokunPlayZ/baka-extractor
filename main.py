import os
import ffmpeg

silent_ffmpeg = True

def extract_subtitles(file_path, output_path):
    print(f'Extracting subtitles from {file_path}...')
    input_video = ffmpeg.input(file_path)
    output_sub = ffmpeg.output(input_video['2'], output_path, format='ass', copyts=True)
    ffmpeg.run(output_sub, overwrite_output=True, quiet=silent_ffmpeg)
    print(f'Subtitles saved to {output_path}.')

def filter_subtitles(file_path):
    print(f'Filtering subtitles from {file_path}...')
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        subtitles = f.readlines()
    filtered_subs = []
    for sub in subtitles:
        sub_lower = sub.lower()  # Convert subtitle to lowercase
        if 'idiot' in sub_lower or 'dummy' in sub_lower or 'バカ' in sub_lower:
            filtered_subs.append(sub)
    print(f'Filtered {len(filtered_subs)} subtitles.')
    return filtered_subs

def extract_snippets(file_path, subs, output_folder, burn_sub=False):
    for i, sub in enumerate(subs):
        snippet_start = sub.split(',')[1]
        snippet_end = sub.split(',')[2]
        snippet_file_name = f'{os.path.splitext(os.path.basename(file_path))[0]}_{i}.mp4'
        snippet_file_path = os.path.join(output_folder, snippet_file_name)
        input_video = ffmpeg.input(file_path, ss=snippet_start, to=snippet_end)
        if burn_sub:
            input_sub = ffmpeg.input(f'subs/{os.path.splitext(file_path)[0].split("/")[1]}.ass')
            output = ffmpeg.output(input_video, input_sub, snippet_file_path, vcodec='copy', acodec='copy')
        else:
            output = ffmpeg.output(input_video, snippet_file_path, vcodec='copy', acodec='copy', format='mp4')
        ffmpeg.run(output, overwrite_output=True, quiet=silent_ffmpeg)
        print(f'Snippet {i} saved to {snippet_file_path}.')

def main():
    input_folder = 'input'
    subs_folder = 'subs'
    result_folder = 'result'

    burn_sub = input("Do you want to burn subtitles into the final video? (y/n) ").lower() == 'y'

    # Create folders if they don't exist
    for folder in [input_folder, subs_folder, result_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f'Folder "{folder}" not exists creating.')

    for file_name in os.listdir(input_folder):
        if file_name.endswith('.mkv'):
            file_path = os.path.join(input_folder, file_name)
            subtitle_file_name = f'{os.path.splitext(file_name)[0]}.ass'
            subtitle_file_path = os.path.join(subs_folder, subtitle_file_name)
            extract_subtitles(file_path, subtitle_file_path)
            filtered_subs = filter_subtitles(subtitle_file_path)
            if filtered_subs:
                extract_snippets(file_path, filtered_subs, result_folder, burn_sub=burn_sub)
            os.remove(subtitle_file_path)
            print(f'Subtitle file {subtitle_file_path} removed.')

if __name__ == '__main__':
    main()
