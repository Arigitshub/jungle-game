import unreal


MAP_PATH = "/Game/Maps/Jungle_Prototype"


def ensure_directories():
    for path in (
        "/Game/Maps",
        "/Game/Blueprints",
        "/Game/Environment",
        "/Game/Audio",
    ):
        unreal.EditorAssetLibrary.make_directory(path)


def ensure_map():
    if unreal.EditorAssetLibrary.does_asset_exist(MAP_PATH):
        unreal.log(f"Map already exists: {MAP_PATH}")
        unreal.EditorLevelLibrary.load_level(MAP_PATH)
        return

    created = unreal.EditorLevelLibrary.new_level(MAP_PATH)
    if not created:
        raise RuntimeError(f"Failed to create map at {MAP_PATH}")

    unreal.log(f"Created map: {MAP_PATH}")


ensure_directories()
ensure_map()
