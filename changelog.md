
Minecraft Java Edition 26.1

The cutest drop in Minecraft history is here!

Ready or not, here comes the Tiny Takeover drop! New versions of baby mobs have stormed Minecraft, causing cuteness overload across biomes and builds. Listen out for heart-melting sounds, craft name tags for your pets, and keep babies forever young with the golden dandelion. The babies are officially on the loose, so get ready to collect, coo over, and create chaos with these tiny rascals!
New Features

    Added new baby sounds for Wolf, Cat, Pig, Horse, and Chicken
    Added Golden Dandelion
    Added adult sound variants for the following animals:
        Cats have one new sound variant
        Pigs have two new sound variants
        Cows have one new sound variant
        Chickens have one new sound variant
        The original sounds of each animal are used for the variant called classic
        Every one of these animals will have a random sound variant assigned to it from the new variants and the original one
    Added a trumpet instrument for when using a Note Block that is placed on a Copper Block
        The sound is different based on the oxidation level of the Copper Block

Golden Dandelion

    The Golden Dandelion is a new type of flower that can be used to stop baby mobs from aging
        Interacting with a baby mob while holding a Golden Dandelion will stop the mob from aging
            When aging is stopped, green particles moving downwards will be shown
        Interacting with a baby mob that has been stopped from aging while holding a Golden Dandelion will cause it to start aging again
            When aging is started again, green particles moving upwards will be shown
        It cannot be used on undead baby mobs and baby Villagers
    Can be crafted using a Dandelion and Gold Nuggets

A baby Fox stands amongst a field of Golden Dandelions.

 
Changes

    Revamped the visuals of most baby mobs
    Name Tags are now craftable and can be crafted with 1 Paper and 1 of any Metal Nugget
    Removed Name Tags from loot chests in Ancient Cities and Woodland Mansions
    Deepslate can now be directly crafted into its cobbled, polished, brick, and tile variants in the Stonecutter
    Stone can now be directly crafted into cobbled variants in the Stonecutter
    Updated the Main Menu background panorama
    Tweaked default JVM options
    The algorithm that maps block and sky light levels to how bright things appear on screen has been fully rewritten
    Removed baby Herobrine

Baby Mobs

    Updated the models and textures of the following baby mobs:
        Cow
        Mooshroom
        Sheep
        Pig
        Cat
        Ocelot
        Wolf
        Chicken
            Tweaked the bounding box to align with the new model
        Rabbit
            Both adult and baby Rabbits also received new animations
            Tweaked the bounding box to align with the new model
            The programmer art Rabbit textures have been removed following the remodeling of the Rabbit
        Horse
            Increased the bounding box of baby Horses to better fit the new model
        Donkey
        Mule
        Zombie Horse
            Increased the bounding box of baby Zombie Horses to better fit the new model
        Skeleton Horse
            Increased the bounding box of baby Skeleton Horses to better fit the new model
        Camel
        Llama
        Bee
        Fox
        Goat
        Armadillo
        Polar Bear
        Panda
        Snifflet
        Dolphin
        Squid
            Increased the bounding box of baby Squid to better fit the new model
        Glow Squid
            Increased the bounding box of baby Glow Squid to better fit the new model
        Turtle
        Axolotl
            Increased the bounding box of baby Axolotls to better fit the new model
        Strider
        Hoglin
        Zoglin
        Zombie
            Increased the bounding box of baby Zombies to better fit the new model
        Husk
            Increased the bounding box of baby Husks to better fit the new model
        Drowned
            Increased the bounding box of baby Drowned to better fit the new model
        Piglin
            Increased the bounding box of baby Piglins to better fit the new model
        Zombified Piglin
            Increased the bounding box of baby Zombified Piglins to better fit the new model
        Villager
            Increased the bounding box of baby Villagers to better fit the new model
        Zombie Villager
            Increased the bounding box of baby Zombie Villagers to better fit the new model
    Baby Cats are now scaled up to be the same size as baby Ocelots
    Baby Horses are now scaled up slightly
    Baby Polar Bears no longer attack Foxes
    Adult Horses' Blackdot markings were updated to be visually closer to the new baby Horse markings
    Small Armor Stands now display correctly by using the adult armor and scaling it down
    Armor on baby Wolves will no longer render
    Saddles on baby Pigs and baby Camels will no longer render
    Camel Husks no longer have a baby model

 

 
A stack of baby mobs. A warm Chicken on top of a black Cat on top of a woods Wolf on top of a Donkey.

Trades

    The trades that are unlocked by Villager professions are now generated using deterministic random sequences, like loot drops and barter loot
        Re-rolling a Villager's trades still produces a randomized sequence of trades, but that sequence is now determined by the world seed
    Master Librarians no longer offer Name Tags
    Master Librarians now offer Red Candles and Yellow Candles for the price of three Emeralds
    Master Librarians now have three available trades to ensure that an Enchanted Book trade is always offered when using the Rebalance experiment
    The Wandering Trader will now offer Name Tags for the price of one Emerald

 
A Swamp Librarian and an unemployed Swamp Villager are looking at each other in front of a Lectern in a Swamp.

 
Minor Tweaks to Blocks, Items and Entities

    Striders now correctly inherit the warmth of the Strider they are standing on, matching Bedrock
    Zombie Horses no longer panic when hurt
    Updated the dismount speed thresholds for Spears to match Bedrock
    The Tripwire texture is now rendered as alpha cutout instead of transparent

Lightmap Algorithm Changes

    The new algorithm mostly provides the same overall results as before, but:
        It is simpler and more straightforward, and fixes multiple issues of the previous one, as listed in the Fixed Bugs section below
        The Darkness effect and world darkening effect of the Wither fight now work the same way in all dimensions
        The Night Vision effect now simply adds ambient light instead of scaling the resulting colors
            This means that fully dark areas no longer look brighter than areas lit by block or sky light
        More aspects of the algorithm such as block light tint, ambient light color and night vision color are now data-driven through environment attributes, as described in the Data Pack section below

UI

    Along with large changes to the world data format in this release, worlds that need to be upgraded will now show Upgrade and Play instead of Play Selected World, and the Edit World and Re-Create World buttons are disabled until the world has been upgraded
        A new screen has been added to show upgrading progress
    Changes were made to how the chat screen is handled when it's restricted by settings
    Input Method Editor (IME) candidates will now be shown in-game (on supported platforms, currently Windows and macOS) above the currently edited text field
        The game will try to restore the last IME status when any text field is selected
        If no text input is selected, IME input will be canceled and the status will not be updated
    Added a new display option called "Exclusive Fullscreen" which controls if fullscreen mode should take full control of a monitor
        Defaults to false (i.e. non-exclusive mode)
        Any change will be applied only after the game restarts
        Warning: exclusive fullscreen mode might prevent use of input methods (IME)

 

 
Two Rabbits of different types are sitting up in a Cherry Grove.

Debug Screen

    The looking_at_block and looking_at_fluid debug entries no longer show tags
    New debug entries have been added:
        looking_at_block_tags
        looking_at_fluid_tags
        looking_at_entity_tags
        sound_cache
    Renamed debug entries:
        looking_at_block -> looking_at_block_state
        looking_at_fluid -> looking_at_fluid_state
    A day_count debug entry has been split from local_difficulty
    Added a new entry detailed_memory with additional information about used memory
    A new lightmap debug renderer can be enabled using the F3 + 4 keybind

Lightmap Debug Renderer

    A new debug renderer for the lightmap was added, which can be enabled using the F3 + 4 keybind
    It is mutually exclusive with the FPS/TPS and networking charts
    It shows the lightmap texture in real time in the bottom right corner of the screen
    The vertical axis of the texture represents sky light levels (0-15 from bottom to top)
    The horizontal axis of the texture represents block light levels (0-15 from left to right)
    The color of each pixel represents the resulting color that will be applied to blocks and entities lit with the corresponding block and sky light levels

 
An underwater view of a few baby Squid which are swimming in a River.

World Options

    The difficulty button in the pause menu has been replaced with a button leading to a new screen - World Options
    The World Options screen contains the difficulty button as well as a button for changing Game Rules
        The Game Rules screen is available for all operators and otherwise disabled

Game Rules

    A search bar has been added to the top of the Game Rules screen, both in-game and in the world creation menu
        The search bar will select Game Rules based on id, name, category, and description

Chat

    The chat screen can now always be opened, even when chatting is restricted by settings
        When the chat screen is open, specific actions and message types may still be restricted
        Information about the restrictions (if there are any) is displayed on top of the chat box and above the chat input when the chat screen is open
        The same information can also be accessed in the World Settings screen
    Chat entries from client actions like taking screenshots will now be displayed even when messages from Players and servers are restricted
    Changing chat settings will now hide all messages of restricted types and discard any new ones
    The handling of chat messages on a published local server is now more consistent with dedicated servers in regard to chat settings

 
A pen of many baby Chickens and two adult Chickens is shown inside of a Plains Village. There's a Cherry Grove in the background.

Creative Mode

    Using Ctrl + Pick input as an operator on Players and Mannequins will now show the same results as executing the /fetchprofile command for this entity would

Default JVM Options

    The game now allocates 4 GB of RAM by default (up from 2 GB)
    Garbage collection has been changed from G1GC to ZGC for compatible devices

    Developer's Note: The default memory allocation has been bumped from 2GB to 4GB to make the game run smoother and reduce stutters. Furthermore, with generational ZGC, you should see a more stable framerate – especially when operating memory heavy tasks. If you're running Minecraft on a machine with less than 4GB of RAM – please refer to this help article. If you want to change the garbage collector – please refer to this help article. Third-party launchers may not support these changes.

 
A Dolphin is jumping out of the water in front of a sunset.

 
Technical Changes

    The Data Pack version is now 101.1
    The Resource Pack version is now 84
    Game executables are no longer obfuscated - see this Minecraft.net article for more details
    If a server's disk space is low, a toast will now be shown to server operators
    The game now requires Java 25
    The included Java distribution is now the Microsoft build of OpenJDK 25
    The report generator for item components has been renamed to "Default Components" and now outputs one file for each element that has default components
    The file structure of how worlds and their data are stored have been changed
    The internals of how chunk geometry data is stored in GPU memory and how they are rendered has been changed
    The game will now save all data once after the world has finished loading/the server has started up

    Developer's Note: If you experience any visual bugs, performance degradation or crashes, please report it to us on our bug tracker.

World Storage

    All default dimensions are now stored in the dimensions subfolder
        Data for the Overworld has been moved from the root folder to dimensions/minecraft/overworld
            This includes the region, entities, and poi folders, as well as related files out of data
        Data for the Nether has been moved from DIM-1 to dimensions/minecraft/the_nether
        Data for the End has been moved from DIM1 to dimensions/minecraft/the_end
        The top level data folder is now only for data shared across dimensions instead of also for the Overworld
    Player storage has been moved to the players subdirectory
        advancements -> players/advancements
        playerdata -> players/data
        stats -> players/stats
    The world resource pack (resources.zip) has been moved to the resourcepacks subdirectory
    Data saved in the data folder is now namespaced
        This means that all that data will now be stored in a namespace subfolder in the corresponding data folder
            All existing vanilla data files have been moved accordingly
            Example: data/scoreboard.dat -> data/minecraft/scoreboard.dat
        Command storage is now stored in namespace subfolders instead of having a namespace suffix
            Example: data/command_storage_foo.dat -> data/foo/command_storage.dat
        chunks.dat has been renamed to chunk_tickets.dat
        Data for maps is now stored in the data/minecraft/maps subfolder
            Map index files have been renamed to only the number
                Example: map_1.dat -> 1.dat
            idcounts.dat has been renamed to last_id.dat
        There is no more raids_end.dat special case
            The End now uses raids.dat as well
    Structures saved by Structure Blocks have been moved from generated/namespace/structures to generated/namespace/structure

Changes to level.dat

    The Player tag has been replaced with a singleplayer_uuid tag, referencing the player data file to use
    Difficulty-related settings have been moved into a difficulty_settings tag
        Difficulty is renamed to difficulty and is now a string instead of an integer
            Allowed values:
                peaceful
                easy
                normal
                hard
        DifficultyLocked is renamed to locked
    Data for the Ender Dragon fight has been moved out to the data folder
        It can now be found at dimensions/minecraft/the_end/data/minecraft/ender_dragon_fight.dat
        The Ender Dragon fight can be activated in other dimensions, see the Dimension Types section below
        Data changes:
            NeedsStateScanning has been renamed to needs_state_scanning
            DragonKilled has been renamed to dragon_killed
            PreviouslyKilled has been renamed to previously_killed
            IsRespawning has been replaced by respawn_stage
                Allowed values:
                    start
                    preparing_to_summon_pillars
                    summoning_pillars
                    summoning_dragon
                    end
            Dragon has been renamed to dragon_uuid
            ExitPortalLocation has been renamed to exit_portal_location
            Gateways has been renamed to gateways
            Added respawn_time - the time in ticks that has elapsed since the current stage of the respawn sequence started
            Added respawn_crystals - a list of UUIDs for the End Crystals used to trigger the respawn sequence
    Wandering Trader data has been moved out to the data folder
        It can now be found at data/minecraft/wandering_trader.dat
        Data changes:
            WanderingTraderId has been removed
            WanderingTraderSpawnChance has been renamed to spawn_chance
            WanderingTraderSpawnDelay has been renamed to spawn_delay
    CustomBossEvents has been moved to the data folder
        It can now be found at data/minecraft/custom_boss_events.dat
    Weather-related data has been moved to the data folder
        It can now be found at data/minecraft/weather.dat
        Data changes:
            clearWeatherTime has been renamed to clear_weather_time
            rainTime has been renamed to rain_time
            thunderTime has been renamed to thunder_time
    ScheduledEvents has been moved out to the data folder
        It can now be found at data/minecraft/scheduled_events.dat
        Data changes:
            Name has been renamed to id
            TriggerTime has been renamed to trigger_time
            Callback has been renamed to callback
                Type has been renamed to type
                Name has been renamed to id
    game_rules has been moved out to the data folder
        It can now be found at data/minecraft/game_rules.dat
    WorldGenSettings has been moved out to the data folder
        It can now be found at data/minecraft/world_gen_settings.dat
        Data changes:
            generate_features has been renamed to generate_structures
    world_clocks has been moved out to the data folder
        It can now be found at data/minecraft/world_clocks.dat

 

 
A Camel is laying in a Desert Village. There's a Villager next to it.

 
Data Pack Versions 95 through 101.1

    Added data-driven World Clocks
    Added data-driven registry for Villager trades
    Added data-driven registry for sound variants for Pig, Cat, Cow, and Chicken
    Changed the syntax of some custom recipe fields
    Added new block, fluid, item, entity, enchantment, potion, and configured feature tags

World Clocks

World Clocks contain an internal time that increases every tick. They can be defined in data packs under the world_clock registry (found under data/<namespace>/world_clock/<id>.json)

    World Clocks can be paused or resumed, and the time of the clock can be changed or queried from the time command
    Format: object with no fields

Timelines

    Added a clock field: a World Clock ID, specifies which World Clock the timeline is tied to
        This field is required, but to match previous behavior the minecraft:overworld clock can be used
    Added an optional time_markers field, an optional map between namespaced Time Marker IDs and either an integer or a Time Marker object,
        Format:
            Non-negative integer, the tick that the time marker marks
            Or object with fields:
                ticks - Integer between 0 and period_ticks, the tick that the Time Marker marks
                show_in_commands - optional boolean, specifies whether the Time Marker will show up in command suggestions
                    Default: false

Time Markers

Time Markers assign a particular name to a specific (optionally repeating) point in time for a specific World Clock. Time Markers replace the previously predetermined names that could be used by /time set, for example day or night.

Time Markers will exist within the context of a specific World Clock. This means that even though the different Time Markers are defined by different Timelines, only one Time Marker can exist with a particular id for a particular World Clock. It also means that two World Clocks can have a Time Marker with the same name.
Built-in uses of Time Markers

Some Time Markers are used to drive Vanilla game behavior. Usually, they are configured to not show up in /time commands.

    minecraft:wake_up_from_sleep - the time to advance the dimension's default clock to when Players in that dimension wake up after sleeping
    minecraft:roll_village_siege - the time of the dimension's default clock at which the random chance for a Zombie Village siege to occur should be evaluated

Environment Attributes
Added minecraft:visual/block_light_tint

Tint of the block light. Block light color starts as dark gray at low light levels, becomes tinted by this attribute at medium levels, and turns white at high levels. By default, it provides the yellowish tint of torches. Bright colors work best for this attribute, with at least one color component being fully bright. The tint applies globally to all light sources visible on the screen. Individual lights cannot be tinted differently.

    Value type: RGB color
    Default value: #FFD88C
    Modifiers: RGB Color Modifiers
    Interpolated: yes
    Resolved at the camera's position

Added minecraft:visual/ambient_light_color

Defines both the ambient light tint and brightness. This light is applied to the world at 0 light level. Block and sky light are added on top of it.

    Value type: RGB color
    Default values: #0A0A0A for the Overworld, #302821 for the Nether, #3f473f for the End
    Modifiers: RGB Color Modifiers
    Interpolated: yes
    Resolved at the camera's position

Added minecraft:visual/night_vision_color

This color is used similarly to ambient light color. When the Night Vision effect is active, the per-component maximum of minecraft:visual/night_vision_color and minecraft:visual/ambient_light_color is used as the ambient color. Night Vision is not tinted by default.

    Value type: RGB color
    Default value: #999999
    Modifiers: RGB Color Modifiers
    Interpolated: yes
    Resolved at the camera's position

Changed minecraft:gameplay/turtle_egg_hatch_chance

    Now has a default value of 0.002

Data-driven Villager Trades

Trades offered by Villagers and Wandering Traders are now data-driven and can be customized by data pack developers
Villager Trades

    Present in the villager_trade folder, represents a blueprint for trades which is used by Villagers and Wandering Traders to generate actual trades
    Entry Format:
        wants - Object, represents an item type and number of them needed to trade
            id - String, the id of the item
            count - optional number provider, how many of the item is needed for the trade
                Defaults to a constant 1
            components - optional component map, the expected data components on the item
                Defaults to an empty map
        additional_wants - optional object, an additional item required by the merchant, has the same format as wants
        gives - Item Stack, the resulting item given by the merchant when trading
            Uses the existing format for Item Stacks
        given_item_modifiers - optional list of Item Modifiers, modifiers to apply to the item in gives such as enchantments or potions, used to add dynamism to the trade rather than hardcoding certain values
            Uses the existing format for Item Modifiers (also known as loot modifiers, item functions, loot functions...)
            If any of these returns an empty item the entire trade will be discarded
            Item Modifier references are not yet supported
            If the final item has a stored_enchantment component containing an enchantment in the #double_trade_price tag, then the count of wants is doubled
        max_uses - optional number provider, the maximum number of times a trade may be used
            Is set to 1 if the number provider returns a lower value
            Defaults to a constant 4
        reputation_discount - number provider, how much factors such as demand, discounts, or penalties affect the cost represented by wants
            Is set to 0.0 if the number provider returns a lower value
            Defaults to a constant 0.0
        xp - optional number provider, the amount of xp a merchant gets when the trade is done
            Is set to 0 if the number provider returns a lower value
            Defaults to a constant 1
        merchant_predicate - Predicate, conditions on the merchant that need to be met for the trade to be offered
            Uses the existing format for Predicates (also known as loot conditions)
            Predicate references are not yet supported
        double_trade_price_enchantments - optional enchantment id, list of namespaced enchantment IDs, or hash-prefixed enchantment tag representing enchantments that will double the additional cost from minecraft:enchant_randomly and minecraft:enchant_with_levels if they have include_additional_cost_component set to true and if the item has one of the provided values in its minecraft:stored_enchantments component

An example trade of an Emerald and a Book for an Enchanted Book offered only by Desert Villagers

{
  "additional_wants": {
    "id": "minecraft:book"
  },
  "double_trade_price_enchantments": "#minecraft:double_trade_price",
  "given_item_modifiers": [
    {
      "function": "minecraft:enchant_randomly",
      "include_additional_cost_component": true,
      "only_compatible": false,
      "options": "#minecraft:trades/desert_common"
    },
    {
      "function": "minecraft:filtered",
      "item_filter": {
        "items": "minecraft:enchanted_book",
        "predicates": {
          "minecraft:stored_enchantments": [
            {}
          ]
        }
      },
      "on_fail": {
        "function": "minecraft:discard"
      }
    }
  ],
  "gives": {
    "count": 1,
    "id": "minecraft:enchanted_book"
  },
  "max_uses": 12.0,
  "merchant_predicate": {
    "condition": "minecraft:entity_properties",
    "entity": "this",
    "predicate": {
      "predicates": {
        "minecraft:villager/variant": "minecraft:desert"
      }
    }
  },
  "reputation_discount": 0.2,
  "wants": {
    "id": "minecraft:emerald"
  }
}




Trade Sets

    Present in the trade_set folder, they're groupings of trades offered by Villagers and Wandering Traders
    We currently only have hardcoded ones available in <profession>/level_<level> for Villagers, as well as wandering_trader/buying, wandering_trader/special, wandering_trader/common for Wandering Traders
    Entry Format:
        trades - Villager trade id, list of namespaced Villager trade IDs, or hash-prefixed Villager trade tag representing the trades that are part of this trade set
        amount - Number provider, the amount of trades to be generated from this set when used
            If the generated number is greater than the number of available trades then it will only generate until all trades have been used once, unless allow_duplicates is set to true
        allow_duplicates - Boolean, representing if the trade set can use the same Villager Trade multiple times to generate trades
            Defaults to false
        random_sequence - optional named random sequence, determines which trades are generated
            Defaults to a non-deterministic random sequence

An example trade set offering 2 trades from the #minecraft:armorer/level_1 tag, allowing duplicates

{
  "amount": 2.0,
  "trades": "#minecraft:armorer/level_1",
  "random_sequence": "minecraft:trade_set/armorer/level_1",
  "allow_duplicates": true
}




Mob Variants
Cat Sound Variants

    Cat sound variants can be data-driven by adding entries to data/<namespace>/cat_sound_variant/<id>.json
    The file contains two sound sets defining adult_sounds and baby_sounds
    Each sound set contains the following fields which correspond to sound events used for the specific behavior:
        ambient_sound
        stray_ambient_sound
        hiss_sound
        hurt_sound
        death_sound
        eat_sound
        beg_for_food_sound
        purr_sound
        purreow_sound

Pig Sound Variants

    Pig sound variants can be data-driven by adding entries to data/<namespace>/pig_sound_variant/<id>.json
    The file contains two sound sets defining adult_sounds and baby_sounds
    Each sound set contains the following fields which correspond to sound events used for the specific behavior:
        ambient_sound
        hurt_sound
        death_sound
        step_sound
        eat_sound

Cow Sound Variants

    Cow sound variants can be data-driven by adding entries to data/<namespace>/cow_sound_variant/<id>.json
    Each sound variant contains the following fields which correspond to sound events used for the specific behavior:
        ambient_sound
        hurt_sound
        death_sound
        step_sound

Chicken Sound Variants

    Chicken sound variants can be data-driven by adding entries to data/<namespace>/chicken_sound_variant/<id>.json
    The file contains two sound sets defining adult_sounds and baby_sounds
    Each sound set contains the following fields which correspond to sound events used for the specific behavior:
        ambient_sound
        hurt_sound
        death_sound
        step_sound

Wolf Sound Variants

    All sound event fields have been moved into a new object in the field adult_sounds
        Added a new baby_sounds field with the same fields

Commands

    Villager and Piglin inventory slots can now only be accessed using mob.inventory.*
        villager.* and piglin.* have been removed

Added swing

    New command that enables swinging of entities' arms
    Not all entities support the swing animation - swing will still succeed for those entities, but clients will only display it when possible
    For example, this makes it possible to swing Mannequins' arms
    Returns the amount of entities for which a swing was sent

Syntax: /swing [<target>] [<hand>]

Arguments:

    target - Entity selector, the entity to swing
        If not present, defaults to @s
    hand - String, which hand to swing, one of mainhand, offhand
        If not present, defaults to mainhand

Changes to time

    The time command is now based on World Clocks
        A clock can be optionally specified as an input for the time command with time of <clock> ...
        If the clock is not specified (/time ... as before), the default clock for the dimension is used
    The return value (e.g. from /execute store) from the set and add subcommands is now the total elapsed ticks of the clock instead of the current time of day
    A new rate subcommand has additionally been added that can modify the speed at which a World Clock advances

Syntax:

    time [of <clock>] set <time> - sets the total elapsed ticks of the clock
    time [of <clock>] set <timemarker> - advances the clock forward to the next occurrence of the Time Marker
        For the minecraft:overworld clock, the available Time Markers are: day, noon, night, and midnight
    time [of <clock>] add <time> - adds ticks to the clock, can be a negative or a positive number
    time [of <clock>] pause - pauses the clock
    time [of <clock>] resume - resumes the clock
    time [of <clock>] rate <rate> - sets the rate multiplier at which the clock should advance
        Note: this only changes the rate at which the World Clock and any Timelines dependent on it advance their internal timers
            For example, in the case of the minecraft:overworld clock, the day/night cycle will pass quicker with a larger value, but actual game simulation will not speed up (as would happen with /tick rate)
        A rate of 1 corresponds to normal speed
        rate is a float between 0 (exclusive) and 1000 (inclusive)
    time [of <clock>] query <timeline> - displays and returns the current number of ticks within the Timeline's period
    time [of <clock>] query <timeline> repetitions - displays and returns the number of times the Timeline's period has repeated
    time [of <clock>] query time - displays and returns the total elapsed ticks of the clock
    time query gametime - as before, the total elapsed ticks within the world (unaffected by changes made to clocks using /time)

Changes to /fetchprofile

    Added a new entity subcommand that will print profile information from an entity in the world
        Syntax: /fetchprofile entity <single entity selector>
        If the targeted entity does not have a profile (currently only Players and Mannequins do), this command will fail
        Note that the profile is shown as is - no additional resolving is done

Game Test Environments
Added timeline_attributes definition

    Allows setting any number of Timelines on the Environment

Format:

    timelines - a list of timelines to set

Replaced time_of_day with clock_time

    Added a new required field clock - World Clock ID, the clock within which to set time (from the existing time field)

Data Components
Added minecraft:additional_trade_cost

    Transient component used to modify the count needed of the gives item in a Villager trade
    Is removed after a trade has been generated
    Format: integer

Added minecraft:dye

    Represents a color of dye
    Used in various places that previously required the exact dye item, including mob and block interactions
        Note: the presence of this component itself does not enable functionality. The item has to be explicitly allowed for the given functionality, for example by adding it to tags or changing recipe ingredients
    Format: one of white, orange, magenta, light_blue, yellow, lime, pink, gray, light_gray, cyan, purple, blue, brown, green, red, black

Changed minecraft:provides_banner_patterns

    The component now also accepts an ID or a list of IDs in addition to a tag

Changed minecraft:blocks_attacks

    The field bypassed_by now also accepts an ID or a list of IDs in addition to a tag

Changed minecraft:damage_resistant

    The field types now also accepts an ID or a list of IDs in addition to a tag

Entity Data

    The current_explosion_impact_pos and current_impulse_context_reset_grace_time fields from Players have been added to all mobs and the Armor Stand
    The ignore_fall_damage_from_current_explosion field on Players has been removed

Block States

    Therotation property in the default block state of Banners and Signs has been changed from 0 to 8

    Developer's Note: The default block state is used in very few contexts, most notably /setblock without any properties. This change was done to align the default orientation of those blocks with other ones (like Skulls or Dispensers)

Loot Functions

    Added minecraft:villager_trade loot table type which takes the following parameters:
        this - the entity offering the trade
        origin - the block position of the entity at its feet

Changed minecraft:furnace_smelt

    Added boolean field use_input_count (default: true)
        If set to true, the output of the smelting recipe will be multiplied by the number of input items

Added minecraft:set_random_dyes

    Additively adds dyes to an item's minecraft:dyed_color data component

Format: object with fields:

    conditions - list of conditions, conditions for the function to apply
    number_of_dyes - Number provider, the number of random dyes out of sixteen to apply to the item
        The same dye might be selected repeatedly

Added minecraft:set_random_potion

    Randomly sets the minecraft:potion_contents data component on an item

Format: object with fields:

    conditions - list of conditions, conditions for the function to apply
    options - optional potion id, list of namespaced potion IDs, or hash-prefixed potion tag, the possible potions to select from
        Defaults to any potion in the potions registry

Changed minecraft:enchant_with_levels

Now also takes the following field:

    include_additional_cost_component - optional boolean, representing if an minecraft:additional_cost_component should be added to the item based on the cost of the enchantment
        Defaults to false
        The value is determined by the levels number provider and is the same that is used to determine what enchantment level is used for enchanting

Changed minecraft:enchant_randomly

Now also takes the following field:

    include_additional_cost_component - optional boolean, representing if an minecraft:additional_cost_component should be added to the item based on the cost of the enchantment
        Defaults to false
        The value is determined by the value selected by levels or its default value using the following formula: 2 + random(0, 5 + level * 10) + 3 * level

Changed minecraft:set_instrument

    The options field now also accepts an ID and a list of IDs in addition to a tag

Predicates
Loot Predicates
Added minecraft:environment_attribute_check

Exactly matches the value of an Environment Attribute at a given position. Note: this predicate requires a context with an origin position set as long as the Environment Attribute can vary positionally.

Format: object with fields:

    attribute - Environment Attribute ID to test
    value - Exact value of the Environment Attribute to match
    e.g. {condition: 'environment_attribute_check', attribute: 'gameplay/piglins_zombify', value: true}

Changed minecraft:time_check

    Added clock field: a World Clock ID, specifies which World Clock the time check should be done for

Entity Predicates
player Sub-Predicate

    New optional field: food - A Food predicate
    Format: object with fields:
        level - optional integer, min/max range specifying the required food level
        saturation - optional float, min/max range specifying the required saturation level

Number Providers
Added minecraft:sum

    Returns the sum of a list of number providers Format:
    summands - a list of number providers

Added minecraft:environment_attribute

Fetches and provides the value of an Environment Attribute (that can be represented as a number). Note: this provider requires a context with an origin position set as long as the Environment Attribute can vary positionally.

Format: object with fields:

    attribute - Environment Attribute ID to fetch
    e.g. {type: 'environment_attribute', attribute: 'gameplay/sky_light_level'}

Recipes

    result field should now be more consistent across all recipe types that contain it
        It will now accept a short form (e.g. "minecraft:foo", which is equivalent to {"id":"minecraft:foo", "count": 1})
        For the recipe types smelting, blasting, smoking, and campfire_cooking this field now also accepts a count field
    minecraft:crafting_special_mapcloning recipe type has been removed, the functionality has been absorbed by minecraft:crafting_transmute
    New show_notification fields with the same functionality as the existing one in minecraft:crafting_shaped have been added to the following existing recipe types:
        minecraft:crafting_shapeless
        minecraft:crafting_shaped
        minecraft:crafting_transmute
        minecraft:smelting
        minecraft:blasting
        minecraft:smoking
        minecraft:campfire_cooking
        minecraft:stonecutting
        minecraft:smithing_transform
        minecraft:smithing_trim
    Removed the unused group field from recipes without a recipe book:
        minecraft:stonecutting
        minecraft:smithing_transform
        minecraft:smithing_trim
    Renamed the following stonecutter recipes, along with the relevant advancement:
        minecraft:chiseled_stone_bricks_stone_from_stonecutting is renamed to minecraft:chiseled_stone_bricks_from_stone_stonecutting
        minecraft:end_stone_brick_slab_from_end_stone_brick_stonecutting is renamed to minecraft:end_stone_brick_slab_from_end_stone_bricks_stonecutting
        minecraft:end_stone_brick_stairs_from_end_stone_brick_stonecutting is renamed to minecraft:end_stone_brick_stairs_from_end_stone_bricks_stonecutting
        minecraft:end_stone_brick_wall_from_end_stone_brick_stonecutting is renamed to minecraft:end_stone_brick_wall_from_end_stone_bricks_stonecutting
        minecraft:mossy_stone_brick_slab_from_mossy_stone_brick_stonecutting is renamed to minecraft:mossy_stone_brick_slab_from_mossy_stone_bricks_stonecutting
        minecraft:mossy_stone_brick_stairs_from_mossy_stone_brick_stonecutting is renamed to minecraft:mossy_stone_brick_stairs_from_mossy_stone_bricks_stonecutting
        minecraft:mossy_stone_brick_wall_from_mossy_stone_brick_stonecutting is renamed to minecraft:mossy_stone_brick_wall_from_mossy_stone_bricks_stonecutting
        minecraft:prismarine_brick_slab_from_prismarine_stonecutting is renamed to minecraft:prismarine_brick_slab_from_prismarine_bricks_stonecutting
        minecraft:prismarine_brick_stairs_from_prismarine_stonecutting is renamed to minecraft:prismarine_brick_stairs_from_prismarine_bricks_stonecutting
        minecraft:quartz_slab_from_stonecutting is renamed to minecraft:quartz_slab_from_quartz_block_stonecutting
        minecraft:stone_brick_walls_from_stone_stonecutting is renamed to minecraft:stone_brick_wall_from_stone_stonecutting

Note: several of the recipes below use the term "transmuting" when describing crafting output. This procedure is the same as the one currently used by minecraft:crafting_transmute, i.e:

    First, a new item stack is created with the item type and count taken from the result field of the described recipe
    Then, components from a source stack (the actual ingredient depends on the described recipe) are applied to the new stack
    Lastly, components from the result field are applied to the new stack

Changed minecraft:crafting_transmute

    Recipes with this type can now accept multiple items matched by the material ingredient

Added fields:

    material_count - Integer range, the amount of items matched by the material ingredient
        Must be a subrange of [2,8]
        Default: [1,1] (i.e. exactly one item)
    add_material_count_to_result - Boolean
        Default: false
        When true, the amount of slots containing items matched by the material ingredient will be added to the final count of the result

Added minecraft:crafting_dye

    Replaces minecraft:crafting_special_armordye
    Output:
        This recipe will mix the current value of the minecraft:dyed_color component from the item matched by the target ingredient with the minecraft:dye component values from the items matched by the dye ingredients
        The result will be built by transmuting the item matched by the target ingredient into the result item stack and then applying the new value of the minecraft:dyed_color component

Format: object with fields:

    category - String, crafting book category, one of building, redstone, equipment, misc, default: misc
    group - String, used for grouping recipes in the crafting book, default: empty string
    show_notification - optional boolean, describing if a popup should be shown when this recipe is unlocked, default: true
    target - Ingredient (was hardcoded to #dyeable tag)
    dye - Ingredient (was hardcoded to Dye items)
        The minecraft:dye component is required on matching items for the whole recipe to match
    result - resulting item stack (was always a copy of the item matched by the target ingredient)

Added minecraft:crafting_imbue

    Replaces minecraft:crafting_special_tippedarrow
    Matches a single source ingredient surrounded by eight material ingredients
    Output:
        This recipe will copy the minecraft:potion_contents component value from the item matched by the source ingredient to the resulting stack

Format: object with fields:

    category - String, crafting book category, one of building, redstone, equipment, misc, default: misc
    group - String, used for grouping recipes in the crafting book, default: empty string
    show_notification - Optional boolean, describing if a popup should be shown when this recipe is unlocked, default: true
    source - Ingredient (was hardcoded to minecraft:lingering_potion)
    material - Ingredient (was hardcoded to minecraft:arrow)
    result - resulting item stack (was hardcoded to eight minecraft:tipped_arrows)

Changed minecraft:crafting_special_bannerduplicate

    Ingredients can now be restrained
    The output can now be configured
    The recipe still only works for Banner items
    Removed unused category field
    Added fields:
        banner - Ingredient, to be used for both source and target items (was hardcoded to any Banner item)
        result - resulting item stack (was always a copy of the Banner item with non-empty pattern)
    Output:
        The recipe finds the first Banner item matched by the banner ingredient and treats it as the source Banner
        The result will be built by transmuting the source Banner into the result item stack
        The source Banner will be kept in the crafting grid

Changed minecraft:crafting_special_bookcloning

    Ingredients and output can now be configured
    Removed unused category field
    Added fields:
        source - Ingredient, to be used as a source book
            The minecraft:written_book_contents component is required on the matching item for the whole recipe to match
        material - Ingredient, to target the item to be cloned (was hardcoded to #book_cloning_target tag)
        allowed_generations - Integer range, allowed values of the generation field of minecraft:written_book_contents component on the item matched by the material ingredient
            Must be a subrange of [0,2]
            Default: [0,1] (i.e. accepting the original and first copies, but not copies of a copy)
        result - resulting item stack (was always a copy of the item matched by the source ingredient)
    Output:
        The recipe will first take the value of the minecraft:written_book_contents component in the item matched by the source ingredient
        The field generation in minecraft:written_book_contents will be incremented by one
            The recipe will not yield a result if the value of generation is 2 or more
        The result will be built by transmuting the item matched by the source ingredient to the result item stack and then applying the new value of the minecraft:written_book_contents component
        The number of items matched by the material ingredient beyond the first one will be added to the resulting stack size
        The original item matched by the source ingredient will be kept in the crafting grid

Changed minecraft:crafting_decorated_pot

    Ingredients and result can now be configured
    Removed unused category field
    Added fields:
        back, left, right, front - Ingredient (was hardcoded to #decorated_pot_ingredients)
        result - resulting item stack (was hardcoded to a single minecraft:decorated_pot)
    Other functionality remains unchanged, i.e. items matched by the ingredients will be added to the matching fields in the minecraft:pot_decorations component of the resulting stack

Changed minecraft:crafting_special_firework_rocket

    Ingredients and result can now be configured
    Removed unused category field
    Added fields:
        shell - Ingredient (was hardcoded to minecraft:paper)
        fuel - Ingredient (was hardcoded to minecraft:gunpowder)
        star - Ingredient (was hardcoded to minecraft:firework_star)
        result - resulting item stack (was hardcoded to three minecraft:firework_rockets)
    Output:
        Exactly one stack matching the shell ingredient must be present
        The number of stacks matching the fuel ingredient will control the flight_duration field
        The explosions field will be copied from the minecraft:firework_explosion component of the star ingredient (if any)

Changed minecraft:crafting_special_firework_star_fade

    Ingredients can now be configured
    Removed unused category field
    The recipe will now use the minecraft:dye component instead of a hardcoded mapping of Dye items to colors
    Added fields:
        target - Ingredient (was hardcoded to minecraft:firework_star)
        dye - Ingredient (was hardcoded to Dye items)
            The minecraft:dye component is required on matching items for the whole recipe to match
        result - resulting item stack (was always a copy of the item matched by the target ingredient)
    Output:
        This recipe will find the current value of the minecraft:firework_explosion component from the item matched by the target ingredient
        The fade_colors field of the minecraft:dye component will be set to the values from the items matched by the dye ingredients
        The result will be built by transmuting the item matched by the target ingredient into the result item stack and then applying the new value of minecraft:firework_explosion component

Changed minecraft:crafting_special_firework_star

    Ingredients and result can now be configured
    Removed unused category field
    Added fields:
        trail - Ingredient (was hardcoded to minecraft:diamond)
        twinkle - Ingredient (was hardcoded to minecraft:glowstone_dust)
        fuel - Ingredient (was hardcoded to minecraft:gunpowder)
        dye - Ingredient (was hardcoded to Dye items)
            The minecraft:dye component is required on matching items for the whole recipe to match
        shapes - a map of shapes to ingredients
            Allowed keys are the same as the ones for the shape field in the minecraft:firework_explosion component (i.e. small_ball, large_ball, star, creeper, burst)
            Was hardcoded to: minecraft:fire_charge (now large_ball), minecraft:feather (now burst), minecraft:gold_nugget (now star), any Skull or Head (now creeper)
        result - resulting item stack (was hardcoded to three minecraft:firework_stars)
    The recipe will now use the minecraft:dye component instead of a hardcoded mapping of Dye items to colors
    Output:
        Exactly one stack matching the fuel ingredient must be present
        The result will be based on the result field, with the contents of the minecraft:firework_explosion component built with the following values:
            The values of the minecraft:dye component of all items matched by the dye ingredient will be added to the colors field
            If an item matched by the trail ingredient is present, the has_trail field will be set to true
            If an item matched by the twinkle ingredient is present, the has_twinkle field will be set to true
            The shape field will be set based on the item matched by any of the ingredients in the shape field (or small_ball if none is found)

Changed minecraft:crafting_special_mapextending

    Ingredients and output can now be configured
    Removed unused category field
    Added fields:
        map - Ingredient (was hardcoded to minecraft:filled_map with a minecraft:map_id component)
            The minecraft:map_id component is required on the matching map item for the whole recipe to match
        material - Ingredient (was hardcoded to minecraft:paper)
        result - resulting item stack (was always a copy of the item matched by the map ingredient)
    Output:
        The recipe finds the item matched by the map ingredient with the minecraft:map_id component set
        The result will be built by transmuting the source item into the result item stack
        The minecraft:map_post_processing component will be set on the result item
        The source item will be kept in the crafting grid

Changed minecraft:crafting_special_shielddecoration

    Ingredients and output can now be configured
    Removed unused category field
    Added fields:
        banner - Ingredient (was hardcoded to any Banner item)
            Will only match if the item is a Banner
        target - Ingredient (was hardcoded to minecraft:shield)
            The minecraft:banner_patterns component must be not set or be empty for the whole recipe to match
        result - resulting item stack (was always a copy of the item matched by the target ingredient)
    Functionality remains unchanged, i.e. this recipe will apply the following changes to the copy of the item matched by the target ingredient:
    Output:
        The result will be built by transmuting the item matched by the target ingredient into the result item stack and then:
            Copying the minecraft:banner_patterns component from the item matched by the banner ingredient
            Setting the minecraft:base_color component based on the type of the Banner matched by the banner ingredient

Enchantments

    The post_piercing_attack component no longer only works for a Player if that Player has a certain food level

World Generation

    Rule-based block state providers (used previously only in the disk feature) have changed
        The fallback field is now optional and can be empty
            In such cases that an empty fallback is invoked, features that use them will not place anything
        Has become a type of block state provider called rule_based_state_provider instead of a separate unique type
            They can now be used in any other feature configurations as a block state provider and are no longer unique to disk
            Format:
                fallback - optional block state provider
                rules - list of rules
                    if_true - Block predicate, checks the block position before providing the block
                    then - Block state provider
    forest_rock feature has been renamed to block_blob
    block_blob feature configuration has changed to support the following parameters:
        state - Block state, the block the blob is made out of
        can_place_on - Block predicate, defines which blocks the blob can be placed on
    ice_spike feature has been renamed to spike
    spike feature configuration now supports the following parameters:
        state - Block state, the block the spike is made out of
        can_place_on - Block predicate, defines which blocks the spike can be placed on
        can_replace - Block predicate, defines which blocks the spike can replace
    huge_red_mushroom and huge_brown_mushroom feature configurations have a new parameter:
        can_place_on - Block predicate, defines which blocks the huge mushroom can be placed on
    alter_ground tree decorator configuration has changed so that provider is now a rule-based block state provider
    tree feature configuration has replaced the force_dirt and dirt_provider parameters with a single below_trunk_provider block state provider
        Default value:

        "below_trunk_provider": {
            "type": "minecraft:rule_based_state_provider",
            "rules": [
                {
                    "if_true": {
                        "type": "minecraft:not",
                        "predicate": {
                            "type": "minecraft:matching_block_tag",
                            "tag": "minecraft:cannot_replace_below_tree_trunk"
                        }
                    },
                    "then": {
                        "type": "minecraft:simple_state_provider",
                        "state": {
                            "Name": "minecraft:dirt"
                        }
                    }
                }
            ]
        }




        Any trees that previously used force_dirt have a below_trunk_provider that always provides a dirt block instead

Flower Features

    Features spawned from Bone Meal are no longer restricted to the flower feature type, and instead controlled by the #can_spawn_from_bone_meal Configured Feature Tag
    The flower, flower_no_bonemeal, and random_patch feature types have been removed
        Instead, patches can be expressed as a sequence of count and random_offset placement modifiers

Placement Modifiers
count Placement Modifier

    The count field is now limited to a range of 0 to 4096 instead of the previous 256

Dimension Types

    Added fields:
        default_clock - optional World Clock ID
            Specifies the default clock that will be used for the time command.
                If not specified, the time command will require an explicit clock argument
            Also specifies the clock to which the minecraft:wake_up_from_sleep and minecraft:roll_village_siege Time Markers apply
                If not specified, those Time Markers will never apply in that dimension
        has_ender_dragon_fight - Boolean
            Controls whether it is possible for an Ender Dragon fight to exist in the dimension

Int Providers
Added trapezoid

Selects a random value with a trapezoid distribution, similar to the trapezoid Float Provider.

Format: object with fields:

    min - Integer, the minimum value to generate
    max - Integer, the maximum value to generate
    plateau - Integer, the width of the "plateau" of the distribution in which all values are equally likely to occur
        A value of 0 is equivalent to a triangle distribution
        A value of max-min is equivalent to a uniform distribution

Tags

    Added several tags representing groups of Villager trades from which Villagers and Wandering Traders derive their trading pools
        Villagers have the following tags representing each profession and level of trade in the format: #<profession>/level_<level>, up to level 5
            Smiths have the #common_smith/level_<level> tags representing common trades among armorers, weaponsmiths and toolsmiths, up to level 5
        Wandering Traders have the following tags: #wandering_trader/buying, #wandering_trader/special, #wandering_trader/common

Block Tags

    Added the following tags which determine which blocks a category of vegetation can be placed on and survive
        #supports_vegetation which provides support to the following blocks:
            Bush
            Short Grass
            Tall Grass
            Fern
            Large Fern
            Pitcher Plant
            Sunflower
            Lilac
            Rose Bush
            Peony
            Eyeblossom
            Firefly Bush
            Pink Petals
            Wildflowers
            Dandelion
            Torchflower
            Poppy
            Blue Orchid
            Allium
            Azure Bluet
            Red Tulip
            Orange Tulip
            White Tulip
            Pink Tulip
            Oxeye Daisy
            Cornflower
            Sweet Berry Bush
            Oak Sapling
            Spruce Sapling
            Birch Sapling
            Jungle Sapling
            Acacia Sapling
            Cherry Sapling
            Dark Oak Sapling
            Pale Oak Sapling
        #supports_crops which provides support to the following crops at all growth stages:
            Wheat
            Carrot
            Potato
            Beetroot
            Torchflower Crop
            Pitcher Plant Crop
        #supports_stem_crops
        #supports_stem_fruit
        #supports_pumpkin_stem
        #supports_melon_stem
        #supports_pumpkin_stem_fruit
        #supports_melon_stem_fruit
        #supports_sugar_cane
        #supports_sugar_cane_adjacently
            Which blocks satisfy adjacency support requirements for Sugar Cane
        #supports_cactus
        #supports_chorus_plant
        #supports_chorus_flower
        #supports_nether_sprouts
        #supports_azalea
        #supports_warped_fungus
        #supports_crimson_fungus
        #supports_mangrove_propagule
        #supports_hanging_mangrove_propagule
        #supports_nether_wart
        #supports_warped_roots
        #supports_crimson_roots
        #supports_wither_rose
        #supports_cocoa
        #supports_lily_pad
        #supports_frogspawn
            Empty by default
        #support_override_cactus_flower
            Cactus Flowers can be placed on blocks in this tag even if they do not have a sturdy top face
    Added the following tags which determine which blocks are not able to support specific categories of vegetation
        #cannot_support_seagrass
        #cannot_support_kelp
    Renamed the following tags for consistency:
        #dry_vegetation_may_place_on -> #supports_dry_vegetation
        #bamboo_plantable_on -> #supports_bamboo
        #small_dripleaf_placeable -> #supports_small_dripleaf
        #big_dripleaf_placeable -> #supports_big_dripleaf
        #mushroom_grow_block -> #overrides_mushroom_light_requirement
            Mushrooms cannot survive without a light level below 13 if not in the above tag
        #snow_layer_can_survive_on -> #support_override_snow_layer
            Snow layers can be placed on blocks in this tag even if they do not have a top full face
        #snow_layer_cannot_survive_on -> #cannot_support_snow_layer
    Added #grows_crops which defines which blocks beneath allow the following crops to grow:
        Wheat
        Carrot
        Potato
        Beetroot
        Torchflower Crop
        Pitcher Plant Crop
        Pumpkin Stem
        Melon Stem
    Added the following tags to define which blocks can start particular types of Bubble Columns
        #enables_bubble_column_drag_down
            Magma Block by default
        #enables_bubble_column_push_up
            Soul Sand by default
    Split apart #dirt into multiple block tags
        #dirt now only contains Dirt, Coarse Dirt, and Rooted Dirt
        #mud contains Mud and Muddy Mangrove Roots
        #moss_blocks contains Moss Block and Pale Moss Block
        #grass_blocks contains Grass Block, Mycelium, and Podzol
    Added #substrate_overworld which contains #dirt, #mud, #moss_blocks, and #grass_blocks
        This is used as a collection for world generation conditions
    Added the following tags which define which ground blocks beneath an applicable tree or bamboo can be replaced with podzol:
        #beneath_tree_podzol_replaceable
        #beneath_bamboo_podzol_replaceable
    Added #cannot_replace_below_tree_trunk which contains #dirt, #mud, #moss_blocks, and podzol
    Added the following tags defining which blocks their feature can be placed on
        #forest_rock_can_place_on
        #huge_brown_mushroom_can_place_on
        #huge_red_mushroom_can_place_on
    Added #ice_spike_replaceable defining which blocks an Ice Spike feature can replace
    Added #prevents_nearby_leaf_decay which defines what block types prevent leaf blocks from decaying within a taxicab distance of 6 blocks

Fluid Tags

    Added tags to determine which fluids can support the following blocks:
        #supports_lily_pad
        #supports_frogspawn
    Added #supports_sugar_cane_adjacently
        Which fluids satisfy adjacency support requirements for Sugar Cane
    Added #bubble_columns_can_occupy fluid tag to define which fluids a bubble column can occupy with water as default

Item Tags

    Added #metal_nuggets - Copper, Iron, and Gold Nuggets
    Added #dyes - helper tag containing vanilla dyes
    Added #loom_dyes - items that are allowed in the Loom screen to set pattern colors
        The Loom screen also requires the minecraft:dye component to be present on item stacks
    Added #loom_patterns - items that are allowed in the Loom screen to unlock patterns
        The Loom screen also requires the minecraft:provides_banner_patterns component to be present on item stacks
    Added #cat_collar_dyes - items that can be used to dye a pet Cat's collar
        The color will be taken from the minecraft:dye component of the used item stack
    Added #wolf_collar_dyes - items that can be used to dye a pet Wolf's collar
        The color will be taken from the minecraft:dye component of the used item stack
    Added #cauldron_can_remove_dye - items that can be used on water-filled Cauldron to remove the minecraft:dyed_color component
    Removed #dyeable tag
    Added the following tags which mirror their block tag contents:
        #mud
        #moss_blocks
        #grass_blocks

Entity Type Tags

    Added #cannot_be_age_locked - which baby mobs that age cannot have their aging stopped using a Golden Dandelion

Enchantment Tags

    Removed the following tags:
        trades/desert_special
        trades/jungle_special
        trades/plains_special
        trades/savanna_special
        trades/snow_special
        trades/swamp_special
        trades/taiga_special

Potion Tags

    Added #tradeable - all potion effects that can appear in Villager trades

Configured Feature Tags

    Added #can_spawn_from_bone_meal - features that, when added in a biome, can be spawned when using Bone Meal in that biome

Particles

    Added pause_mob_growth - particles showing on a baby mob which has had its aging stopped using a Golden Dandelion
    Added reset_mob_growth - particles showing on a baby mob which has had its aging reset and started using a Golden Dandelion

Text components
minecraft:selector

    The selector field no longer accepts trailing data after a selector

minecraft:nbt

    Tags resolved with the minecraft:nbt text component when the interpret field is set to false are now pretty-printed instead of being flattened into a single text component
    Contents of the nbt and block fields are no longer silently rejected when parsing fails
    The entity field no longer accepts trailing data after a selector
    A new option called plain has been added to remove styling from pretty-printed text
        The plain and interpret options can't both be enabled at the same time

minecraft:object

    Added a new optional field named fallback that contains a text component to be used when the object component itself can't be displayed (for example when printing messages in server logs or during narration)
    Objects of type player (player heads) can no longer be used in server status messages (MotD)
        All components of that type will be replaced by a fallback text
        Components nested more than 16 times will be discarded and replaced with an ellipsis

Resource Pack Versions 75 through 84

    The Tripwire texture is now rendered as alpha cutout instead of transparent
    The glow particles emitted by Glow Squids, Lightning Rods, blocks being waxed, unwaxed, and scraped are now rendered as opaque, since they never actually used translucency
    Removed demo_background.png in favor of the popup/background.png sprite
    The item model format now supports transformation for individual sub-models

Block State Rendering

    Some changes have been made to the way block states render in places like Enderman-held blocks, Block Display entities, etc. (but not falling blocks or Pistons)
        The Enchanting Table will now show a closed book on the top of the block
        Blocks that use special renderers (like Chests, Banners, Skulls) should now respect block state properties:
            Rendering now respects the rotation and facing properties (where applicable)
            Beds now only render one half of the model, depending on the part property
            Copper Golem Statues will now respect the copper_golem_pose property
            Walls and freestanding Signs, Hanging Signs, Banners, and Skulls/Heads will now have separate models
            Chests now respect part properties (where applicable)
        Note: in general, all block states should look the same when rendered on a Block Display as they look when placed in world, except fluids

Block Model Format

    Any block model can now support cutout or translucent (partially transparent pixels) textures
        Whether a quad is rendered in the cutout or translucent render pass is determined by the contents of its assigned sprite
            Any sprite with translucent (partially transparent) pixels will be assigned to the "translucent" pass
            Any sprite with fully transparent pixels will be assigned to the "cutout" pass
            All other sprites are assigned to the "solid" pass
        Note: the assigned render pass also implies rendering order: all solid geometry is rendered before all cutout geometry, which is rendered before all translucent geometry
    The format of the textures map has been updated:
        Non-string entries will now be rejected, instead of interpreted as strings
        Alongside the previous inline sprite ID form, entries can now be defined as an object with fields:
            sprite - the sprite ID
            force_translucent - optional boolean, true if any geometry with this texture should be forced into the "translucent" pass
                This is useful for example for blocks that don't have any translucent pixels, but use the mean mipmap strategy
                Default: false

Item Models

    The minecraft:model, minecraft:special, minecraft:range_dispatch, minecraft:composite, minecraft:select, minecraft:condition item model types now have a transformation field
        That field has the same format as the transformation field on the minecraft:display entity, i.e. either an array of 16 numbers representing a matrix or a structure with decomposed translation, scale, and rotation info
        For types with children (minecraft:range_dispatch, minecraft:composite, minecraft:select, minecraft:condition), the transformation will be composed with the transformation of the children, except for minecraft:bundle/selected_item
        Model transformations will be applied AFTER item display transformations (i.e. the display section in model files)
    The transformations for some special item models (types referenced by the minecraft:special item model) have been extracted to item models itself
        Affected special model types:
            minecraft:bed
            minecraft:banner
            minecraft:conduit
            minecraft:copper_golem_statue
            minecraft:head
            minecraft:player_head
            minecraft:shulker_box
            minecraft:shield
            minecraft:trident
            minecraft:standing_sign
            minecraft:hanging_sign

minecraft:bell Special Model Type

    New special model type that renders the animated part of a Bell block
    No fields

minecraft:book Special Model Type

    New special model type that renders a book that normally is part of the Enchanting Table and Lectern
    Fields:
        open_angle - Float, angle (in degrees) between book cover and book centerline (0 means closed, 90 means open flat)
        page1, page2 - Float between 0.0 and 1.0, the positions of two pages inside the book
            0.0 means the page is in the leftmost position, 1.0 means the page is in the rightmost position

minecraft:bed Special Model Type

    The model now renders only one half of the Bed
    To render both halves, use a minecraft:composite model
    New field:
        part - String, one of: head, foot

minecraft:banner Special Model Type

    New field:
        attachment - optional String, selects a model to be used, one of wall, ground
            If not present, defaults to ground

minecraft:chest Special Model Type

    New field:
        chest_type - optional String, selects a model to be used, one of single, left, right
            If not present, defaults to single

minecraft:hanging_sign Special Model Type

    New field:
        attachment - optional String, selects a model to be used, one of wall, ceiling, ceiling_middle
            If not present, defaults to ceiling_middle

minecraft:standing_sign Special Model Type

    New field:
        attachment - optional String, selects a model to be used, one of wall, ground
            If not present, defaults to ground

minecraft:shulker_box Special Model Type

    Removed the orientation field

minecraft:end_cube Special Model Type

    New special model type that renders a cube with the same texture effects as the End Portal and the End Gateway blocks
    Format:
        effect - String, texture effect to apply, one of: portal, gateway

Block Sprites

    Added new block textures:
        block/golden_dandelion.png

UI Sprites

    Added new UI sprites:
        gui/sprites/widget/preedit.png for IME preedit overlay background

Entity Textures

    Added new entity textures:
        entity/cat/cat_all_black_baby.png
        entity/cat/cat_black_baby.png
        entity/cat/cat_british_shorthair_baby.png
        entity/cat/cat_calico_baby.png
        entity/cat/cat_collar_baby.png
        entity/cat/cat_jellie_baby.png
        entity/cat/ocelot_baby.png
        entity/cat/cat_persian_baby.png
        entity/cat/cat_ragdoll_baby.png
        entity/cat/cat_red_baby.png
        entity/cat/cat_siamese_baby.png
        entity/cat/cat_tabby_baby.png
        entity/cat/cat_white_baby.png
        entity/chicken/chicken_cold_baby.png
        entity/chicken/chicken_temperate_baby.png
        entity/chicken/chicken_warm_baby.png
        entity/cow/cow_cold_baby.png
        entity/cow/cow_temperate_baby.png
        entity/cow/cow_warm_baby.png
        entity/cow/mooshroom_brown_baby.png
        entity/cow/mooshroom_red_baby.png
        entity/horse/donkey_baby.png
        entity/horse/horse_black_baby.png
        entity/horse/horse_brown_baby.png
        entity/horse/horse_chestnut_baby.png
        entity/horse/horse_creamy_baby.png
        entity/horse/horse_darkbrown_baby.png
        entity/horse/horse_gray_baby.png
        entity/horse/horse_blackdots_baby.png
        entity/horse/horse_markings_white_baby.png
        entity/horse/horse_markings_whitedots_baby.png
        entity/horse/horse_markings_whitefield_baby.png
        entity/horse/horse_skeleton_baby.png
        entity/horse/horse_white_baby.png
        entity/horse/horse_zombie_baby.png
        entity/horse/mule_baby.png
        entity/pig/pig_cold_baby.png
        entity/pig/pig_temperate_baby.png
        entity/pig/pig_warm_baby.png
        entity/rabbit/rabbit_black.png
        entity/rabbit/rabbit_brown.png
        entity/rabbit/rabbit_caerbannog.png
        entity/rabbit/rabbit_gold.png
        entity/rabbit/rabbit_salt.png
        entity/rabbit/rabbit_toast.png
        entity/rabbit/rabbit_white.png
        entity/rabbit/rabbit_white_splotched.png
        entity/sheep/sheep_baby.png
        entity/sheep/sheep_wool_baby.png
        entity/wolf/wolf_angry_baby.png
        entity/wolf/wolf_ashen_angry_baby.png
        entity/wolf/wolf_ashen_baby.png
        entity/wolf/wolf_ashen_tame_baby.png
        entity/wolf/wolf_baby.png
        entity/wolf/wolf_black_angry_baby.png
        entity/wolf/wolf_black_baby.png
        entity/wolf/wolf_black_tame_baby.png
        entity/wolf/wolf_chestnut_angry_baby.png
        entity/wolf/wolf_chestnut_baby.png
        entity/wolf/wolf_chestnut_tame_baby.png
        entity/wolf/wolf_collar_baby.png
        entity/wolf/wolf_rusty_angry_baby.png
        entity/wolf/wolf_rusty_baby.png
        entity/wolf/wolf_rusty_tame_baby.png
        entity/wolf/wolf_snowy_angry_baby.png
        entity/wolf/wolf_snowy_baby.png
        entity/wolf/wolf_snowy_tame_baby.png
        entity/wolf/wolf_spotted_angry_baby.png
        entity/wolf/wolf_spotted_baby.png
        entity/wolf/wolf_spotted_tame_baby.png
        entity/wolf/wolf_striped_angry_baby.png
        entity/wolf/wolf_striped_baby.png
        entity/wolf/wolf_striped_tame_baby.png
        entity/wolf/wolf_tame_baby.png
        entity/wolf/wolf_woods_angry_baby.png
        entity/wolf/wolf_woods_baby.png
        entity/wolf/wolf_woods_tame_baby.png
        entity/bee/bee_baby.png
        entity/bee/bee_angry_baby.png
        entity/bee/bee_nectar_baby.png
        entity/bee/bee_angry_nectar_baby.png
        entity/fox/fox_baby.png
        entity/fox/fox_snow_baby.png
        entity/fox/fox_sleep_baby.png
        entity/fox/fox_snow_sleep_baby.png
        entity/camel/camel_baby.png
        entity/goat/goat_baby.png
        entity/armadillo/armadillo_baby.png
        entity/bear/polarbear_baby.png
        entity/llama/llama_creamy_baby.png
        entity/llama/llama_white_baby.png
        entity/llama/llama_brown_baby.png
        entity/llama/llama_gray_baby.png
        entity/equipment/llama_body/trader_llama_baby.png
        entity/villager/villager_baby.png
        entity/villager/baby/desert.png
        entity/villager/baby/jungle.png
        entity/villager/baby/plains.png
        entity/villager/baby/savanna.png
        entity/villager/baby/snow.png
        entity/villager/baby/swamp.png
        entity/villager/baby/taiga.png
        entity/zombie/drowned_baby.png
        entity/zombie/drowned_outer_layer_baby.png
        entity/zombie/husk_baby.png
        entity/zombie/zombie_baby.png
        entity/zombie_villager/zombie_villager_baby.png
        entity/zombie_villager/baby/desert.png
        entity/zombie_villager/baby/jungle.png
        entity/zombie_villager/baby/plains.png
        entity/zombie_villager/baby/savanna.png
        entity/zombie_villager/baby/snow.png
        entity/zombie_villager/baby/swamp.png
        entity/zombie_villager/baby/taiga.png
        entity/piglin/piglin_baby.png
        entity/piglin/zombiefied_piglin_baby.png
        entity/equipment/humanoid_baby/chainmail.png
        entity/equipment/humanoid_baby/copper.png
        entity/equipment/humanoid_baby/diamond.png
        entity/equipment/humanoid_baby/gold.png
        entity/equipment/humanoid_baby/iron.png
        entity/equipment/humanoid_baby/leather_overlay.png
        entity/equipment/humanoid_baby/leather.png
        entity/equipment/humanoid_baby/netherite.png
        entity/equipment/humanoid_baby/turtle_scute.png
        entity/hoglin/hoglin_baby.png
        entity/hoglin/zoglin_baby.png
        entity/strider/strider_baby.png
        entity/strider/strider_cold_baby.png
        entity/sniffer/snifflet.png
        entity/panda/aggressive_panda_baby.png
        entity/panda/brown_panda_baby.png
        entity/panda/lazy_panda_baby.png
        entity/panda/playful_panda_baby.png
        entity/panda/weak_panda_baby.png
        entity/panda/worried_panda_baby.png
        entity/panda/panda_baby.png

    Renamed the following entity textures:
        entity/armorstand/wood.png -> entity/armorstand/armorstand.png
        entity/cat/all_black.png -> entity/cat/cat_all_black.png
        entity/cat/black.png -> entity/cat/cat_black.png
        entity/cat/british_shorthair.png -> entity/cat/cat_british_shorthair.png
        entity/cat/calico.png -> entity/cat/cat_calico.png
        entity/cat/jellie.png -> entity/cat/cat_jellie.png
        entity/cat/persian.png -> entity/cat/cat_persian.png
        entity/cat/ragdoll.png -> entity/cat/cat_ragdoll.png
        entity/cat/red.png -> entity/cat/cat_red.png
        entity/cat/siamese.png -> entity/cat/cat_siamese.png
        entity/cat/tabby.png -> entity/cat/cat_tabby.png
        entity/cat/white.png -> entity/cat/cat_white.png
        entity/chicken/cold_chicken.png -> entity/chicken/chicken_cold.png
        entity/chicken/temperate_chicken.png -> entity/chicken/chicken_temperate.png
        entity/chicken/warm_chicken.png -> entity/chicken/chicken_warm.png
        entity/copper_golem/exposed_copper_golem.png -> entity/copper_golem/copper_golem_exposed.png
        entity/copper_golem/exposed_copper_golem_eyes.png -> entity/copper_golem/copper_golem_eyes_exposed.png
        entity/copper_golem/oxidized_copper_golem_eyes.png -> entity/copper_golem/copper_golem_eyes_oxidized.png
        entity/copper_golem/weathered_copper_golem_eyes.png -> entity/copper_golem/copper_golem_eyes_weathered.png
        entity/copper_golem/oxidized_copper_golem.png -> entity/copper_golem/copper_golem_oxidized.png
        entity/copper_golem/weathered_copper_golem.png -> entity/copper_golem/copper_golem_weathered.png
        entity/cow/cold_cow.png -> entity/cow/cow_cold.png
        entity/cow/temperate_cow.png -> entity/cow/cow_temperate.png
        entity/cow/warm_cow.png -> entity/cow/cow_warm.png
        entity/cow/brown_mooshroom.png -> entity/cow/mooshroom_brown.png
        entity/cow/red_mooshroom.png -> entity/cow/mooshroom_red.png
        entity/fox/snow_fox.png -> entity/fox/fox_snow.png
        entity/fox/snow_fox_sleep.png -> entity/fox/fox_snow_sleep.png
        entity/frog/cold_frog.png -> entity/frog/frog_cold.png
        entity/frog/temperate_frog.png -> entity/frog/frog_temperate.png
        entity/frog/warm_frog.png -> entity/frog/frog_warm.png
        entity/llama/brown.png -> entity/llama/llama_brown.png
        entity/llama/creamy.png -> entity/llama/llama_creamy.png
        entity/llama/gray.png -> entity/llama/llama_gray.png
        entity/llama/spit.png -> entity/llama/llama_spit.png
        entity/llama/white.png -> entity/llama/llama_white.png
        entity/panda/aggressive_panda.png -> entity/panda/panda_aggressive.png
        entity/panda/brown_panda.png -> entity/panda/panda_brown.png
        entity/panda/lazy_panda.png -> entity/panda/panda_lazy.png
        entity/panda/playful_panda.png -> entity/panda/panda_playful.png
        entity/panda/weak_panda.png -> entity/panda/panda_weak.png
        entity/panda/worried_panda.png -> entity/panda/panda_worried.png
        entity/pig/cold_pig.png -> entity/pig/pig_cold.png
        entity/pig/temperate_pig.png -> entity/pig/pig_temperate.png
        entity/pig/warm_pig.png -> entity/pig/pig_warm.png
        entity/projectiles/spectral.png -> entity/projectiles/arrow_spectral.png
        entity/projectiles/tipped.png -> entity/projectiles/arrow_tipped.png
        entity/turtle/big_sea_turtle.png -> entity/turtle/turtle.png

    Moved the following entity textures:
        entity/armadillo.png -> entity/armadillo/armadillo.png
        entity/banner_base.png -> entity/banner/banner_base.png
        entity/bat.png -> entity/bat/bat.png
        entity/beacon_beam.png -> entity/beacon/beacon_beam.png
        entity/blaze.png -> entity/blaze/blaze.png
        entity/dolphin.png -> entity/dolphin/dolphin.png
        entity/enchanting_table_book.png -> entity/enchantment/enchanting_table_book.png
        entity/end_gateway_beam.png -> entity/end_portal/end_gateway_beam.png
        entity/end_portal.png -> entity/end_portal/end_portal.png
        entity/endermite.png -> entity/endermite/endermite.png
        entity/experience_orb.png -> entity/experience/experience_orb.png
        entity/fishing_hook.png -> entity/fishing/fishing_hook.png
        entity/guardian.png -> entity/guardian/guardian.png
        entity/guardian_beam.png -> entity/guardian/guardian_beam.png
        entity/guardian_elder.png -> entity/guardian/guardian_elder.png
        entity/lead_knot.png -> entity/lead_knot/lead_knot.png
        entity/minecart.png -> entity/minecart/minecart.png
        entity/phantom.png -> entity/phantom/phantom.png
        entity/phantom_eyes.png -> entity/phantom/phantom_eyes.png
        entity/shield_base.png -> entity/shield/shield_base.png
        entity/shield_base_nopattern.png -> entity/shield/shield_base_nopattern.png
        entity/silverfish.png -> entity/silverfish/silverfish.png
        entity/snow_golem.png -> entity/snow_golem/snow_golem.png
        entity/spider_eyes.png -> entity/spider/spider_eyes.png
        entity/trident.png -> entity/trident/trident.png
        entity/trident_riptide.png -> entity/trident/trident_riptide.png
        entity/wandering_trader.png -> entity/wandering_trader/wandering_trader.png
        entity/witch.png -> entity/witch/witch.png

Sounds

    Added new sound events for the Cat:
        entity.baby_cat.ambient
        entity.baby_cat.hiss
        entity.baby_cat.hurt
        entity.baby_cat.death
        entity.baby_cat.eat
        entity.baby_cat.beg_for_food
        entity.baby_cat.purr
        entity.baby_cat.purreow
        entity.baby_cat.stray_ambient
        entity.cat_royal.ambient
        entity.cat_royal.hiss
        entity.cat_royal.hurt
        entity.cat_royal.death
        entity.cat_royal.eat
        entity.cat_royal.beg_for_food
        entity.cat_royal.purr
        entity.cat_royal.purreow
        entity.cat_royal.stray_ambient
    Added new sound events for the Pig:
        entity.baby_pig.ambient
        entity.baby_pig.hurt
        entity.baby_pig.death
        entity.baby_pig.step
        entity.baby_pig.eat
        entity.pig_mini.ambient
        entity.pig_mini.hurt
        entity.pig_mini.death
        entity.pig_mini.eat
        entity.pig_big.ambient
        entity.pig_big.hurt
        entity.pig_big.death
        entity.pig_big.eat
        entity.pig.eat
    Added new sound events for the Wolf:
        entity.baby_wolf.ambient
        entity.baby_wolf.growl
        entity.baby_wolf.death
        entity.baby_wolf.hurt
        entity.baby_wolf.pant
        entity.baby_wolf.whine
        entity.baby_wolf.step
    Added new sound events for the Horse:
        entity.baby_horse.ambient
        entity.baby_horse.hurt
        entity.baby_horse.death
        entity.baby_horse.angry
        entity.baby_horse.eat
        entity.baby_horse.fall
        entity.baby_horse.land
        entity.baby_horse.step
        entity.baby_horse.breathe
    Added new sound events for the Chicken:
        entity.baby_chicken.ambient
        entity.baby_chicken.hurt
        entity.baby_chicken.death
        entity.baby_chicken.step
        entity.chicken_picky.ambient
        entity.chicken_picky.death
        entity.chicken_picky.hurt
        entity.chicken_picky.step
    Added new sound events for the Golden Dandelion:
        item.golden_dandelion.use
        item.golden_dandelion.unuse
    Added new sound events for the Cow:
        entity.cow_moody.ambient
        entity.cow_moody.death
        entity.cow_moody.hurt
        entity.cow_moody.step
    Added new sound events for the trumpet instrument:
        block.note_block.trumpet
        block.note_block.trumpet_exposed
        block.note_block.trumpet_oxidized
        block.note_block.trumpet_weathered

Shaders & Post-process Effects

    Developer's Note: Although it is possible in Resource Packs, overriding Core Shaders is considered as unsupported and not an intended Resource Pack feature. These shaders exist as part of the internal implementation of the game, and as such, may change at any time as the game's internals evolve. We understand that overriding Core Shaders is used for very cool Resource Pack features, many of which lack supported alternatives. We would like to provide better, supported alternatives in the future.

    The core/rendertype_item_entity_translucent_cull shaders have been removed in favor of core/entity
    The core/rendertype_entity_alpha and core/rendertype_entity_decal shaders have been replaced by a DISSOLVE flag implemented by core/entity
    Rendering of items (in UI and in the world) has been split from the core/entity into new core/item shaders
    The block.vsh and terrain.vsh shaders no longer receive the Normal vertex attribute
    The core/rendertype_translucent_moving_block shaders have been removed in favor of core/block

Lightmap Shader

    The lightmap.fsh shader was significantly modified
        The LightmapInfo uniform now has two new fields:
            BlockLightTint
            NightVisionColor
        The AmbientLightFactor field was removed, its value is now premultiplied into AmbientColor
        The DarkenWorldFactor was renamed to BossOverlayWorldDarkeningFactor
    Text and items rendered in UI now use a separate 1x1 white lightmap texture, so the lightmap shader does not always have to keep the 15, 15 pixel purely white
