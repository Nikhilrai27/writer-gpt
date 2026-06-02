from src.memory.canon import CanonManager

canon = CanonManager("data/projects/demo_story")

canon.add_entity(
    entity_type="character",
    name="John Carter",
    attributes={
        "occupation": "Soldier",
        "eye_color": "Brown"
    }
)

print(canon.list_entities())

canon.update_entity(
    "John Carter",
    {
        "rank": "Captain",
        "alive": True
    }
)

print(canon.get_entity("John Carter"))