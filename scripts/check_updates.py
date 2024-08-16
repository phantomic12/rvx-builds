import json
import os
import sys
from datetime import datetime

import requests
from loguru import logger


@logger.catch
def get_env(branch):
    # Get env file contents
    url = f"https://raw.githubusercontent.com/{repository}/{branch}/.env"
    try:
        response = requests.get(url)
        content = response.text
        if response.status_code != 200:
            print(f"Failed to fetch the .env file. Status code: {response.status_code}", flush=True)
            print("Assuming the .env file doesn't exist, using an empty one...", flush=True)
            content = "# Empty .env file"
    except:
        print("The .env file doesn't exist. Using an empty one...", flush=True)
        content = "# Empty .env file"
    finally:
        return content


@logger.catch
def get_monitored_patches(branch, file):
    # Get monitored-patches.json file contents
    url = f"https://raw.githubusercontent.com/{repository}/{branch}/{file}"
    try:
        response = requests.get(url)
        data = response.json()
    except:
        print("The monitored-patches.json file doesn't exist. It'd be created in the following run.", flush=True)
        data = []
    finally:
        return data


@logger.catch
def get_patches_dls(dict):
    dls = set()
    for key, value in dict.items():
        if key.endswith("_JSON_DL"):
            value = manage_dls(value)
            dls.add(value)
    dls = set(filter(lambda value: value is not None, dls))
    if default_patch_dl not in dls:
        dls.add(manage_dls(default_patch_dl))
    return list(dls)


@logger.catch
def get_patch_data(dl_list):
    api_dls = []
    tags = []
    tag_data = []
    releases = []
    for url in dl_list:
        api_url = github_api_url(url)
        api_dls.append(api_url)
        response = requests.get(api_url)
        release_json = response.json()
        tag = release_json["tag_name"]
        tags.append(tag)
        tag_data.append({"patches_json_dl": url, "tag_name": tag})
        releases.append({"patches_json_dl": url, "response": release_json})
    print("Different Patch DLs:\n\n", "\n ".join(dl_list), "\n", flush=True)
    return tag_data, releases


@logger.catch
def compare_tags(old_json, new_json):
    data1 = old_json
    data2 = new_json
    compare_tags.data = new_json

    print("Current JSON of Patch DLs: \n\n", json.dumps(data1, indent=4), "\n", flush=True)
    print("Latest JSON of Patch DLs: \n\n", json.dumps(data2, indent=4), "\n", flush=True)

    for entry2 in data2:
        patch_dl = entry2["patches_json_dl"]
        tag = entry2["tag_name"]
        if entry2 in data1:
            # The iterated object is already present
            continue
        else:
            # The iterated object isn't present

            # Now, checking if the patch Dl is present
            patch_obj = next((item for item in data1 if item["patches_json_dl"] == patch_dl), None)

            if not patch_obj or len(data1) < len(data2):
                # Patch Dl wasn't present or the newer patch dls are more
                # Therefore would only update the 'monitored.json' & no build.
                print(f"Oh, I notice some changes. Either a Patch DL was modified to: \n\n'{patch_dl}'\n", flush=True)
                print("or some Patch DLs were added!!", flush=True)
                print("So, I assume that the user would have already run the build manually.", flush=True)
                print("Thus, the building would be done in the upcoming runs of the script.", flush=True)
                return "write_json"

            # Patch DL was already present
            if patch_obj:
                # Trying to match tag
                old_tag = patch_obj["tag_name"]
                if old_tag != tag:
                    print(
                        f"Update found!!\nThe following Patch Dl was updated with tag '{tag}': \n{patch_dl}\n",
                        flush=True,
                    )
                    return "build"

    print("The patches are already up-to-date!!", flush=True)
    return "write_json"


@logger.catch
def format_changelog(response):
    source_name = "/".join(response["html_url"].split("/")[3:5])
    date_obj = datetime.strptime(response["published_at"], "%Y-%m-%dT%H:%M:%SZ")
    release_date = date_obj.strftime("%B %d, %Y, %H:%M:%S UTC")

    content = (
        f"# {source_name}\n\n"
        f"***Release Version: [{response['tag_name']}]({response['html_url']})***  \n"
        f"***Release Date: {release_date}***  \n"
        f"<details>\n<summary><b><i>Changelog:</i></b></summary>\n\n{response['body']}</details>\n\n"
    )
    return f"{content}"


@logger.catch
def trigger_workflow(access_token, repository, branch, workflow_name):
    url = f"https://api.github.com/repos/{repository}/actions/workflows/{workflow_name}/dispatches"

    headers = {"Authorization": f"Bearer {access_token}", "Accept": "application/vnd.github.v3+json"}

    payload = {
        "ref": branch,  # The branch to trigger the workflow on
        # You can add any inputs required by your workflow here
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 204:
            print("Workflow triggered successfully!", flush=True)
        else:
            print(f"Failed to trigger workflow. Status code: {response.status_code}", flush=True)
    except Exception as e:
        print("Error:", e, flush=True)
    finally:
        if response.status_code != 204:
            print("Couldn't update the monitored-patches.json file!! Exiting...")
            sys.exit(1)


@logger.catch
def manage_tasks(action):
    if action == "build":
        print("Running the workflow: Build & Release", flush=True)
        trigger_workflow(access_token, repository, branch, workflow_name)
        action = "write_json"

    if action == "write_json":
        print("Updating the 'monitored-patches.json' file.", flush=True)
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(compare_tags.data, f, indent=4)
        action = "write_changelog"

    if action == "write_changelog":
        print("Updating the 'changelog.md' file.", flush=True)
        doc = ""
        for release in parse_env.releases:
            doc += format_changelog(response=release["response"])
        os.remove(changelog_file) if os.path.exists(changelog_file) else None
        with open(changelog_file, "w", encoding="utf-8") as f:
            f.write(doc)


@logger.catch
def manage_dls(url):
    new_url = None
    if url.startswith("https://github.com"):
        url_arr = url.split("/")
        arrL = len(url_arr)
        prefix = "https://github.com"
        owner = url_arr[3].lower()
        repo = url_arr[4].lower()
        suffix = f"{owner}/{repo}"
        if arrL > 5:
            suffix = suffix + "/" + "/".join(url_arr[5:])
        if arrL == 5:
            suffix = suffix + "/releases/latest"
        if arrL == 6:
            suffix = suffix + "/latest"
        new_url = f"{prefix}/{suffix}"
    return new_url


@logger.catch
def github_api_url(url):
    api_url = None
    if url.startswith("https://github.com"):
        url_arr = url.split("/")
        prefix = "https://api.github.com/repos"
        suffix = "/".join(url_arr[3:])
        if "/tag/" in url:
            suffix = suffix.replace("/tag/", "/tags/")
        elif not url.endswith("latest"):
            suffix = suffix + "/releases/latest"
        api_url = f"{prefix}/{suffix}"
    # print(api_url, flush=True)
    return api_url


# Parse json_data from env_content
@logger.catch
def parse_env():
    env_content = get_env(branch)
    old_patches_data = get_monitored_patches(monitored_branch, output_file)
    old_patches_dl_values = [item["patches_json_dl"] for item in old_patches_data]

    env_dict = {}
    lines = env_content.strip().split("\n")
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#") or line.isspace():
            continue
        if "#" in line:
            line = line.split("#")[0].strip()
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        env_dict[key] = value

    dl_list = get_patches_dls(env_dict)
    latest_patches_data, releases_data = get_patch_data(dl_list)
    sorting_key = lambda x: (
        x["patches_json_dl"] in old_patches_dl_values,
        x["patches_json_dl"],
    )
    latest_patches_data = sorted(latest_patches_data, key=sorting_key)
    releases_data = sorted(releases_data, key=sorting_key)
    parse_env.releases = releases_data
    action = compare_tags(old_patches_data, latest_patches_data)
    manage_tasks(action)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python <script.py> <USER/REPO>", flush=True)
    else:
        repository = sys.argv[1]
        access_token = os.environ.get("GH_TOKEN")
        workflow_name = "build-apk.yml"

        branch = "main"  # Branch to get the env
        monitored_branch = "check-updates"  # Branch to get the monitored-patches.json
        output_file = "scripts/monitored-patches.json"
        changelog_file = "changelog.md"

        default_patch_dl = "https://github.com/revanced/revanced-patches/releases/latest"
        parse_env()
