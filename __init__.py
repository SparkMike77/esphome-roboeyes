import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import display
from esphome.const import CONF_ID

CODEOWNERS = ["@SparkMike77"]
DEPENDENCIES = ["display"]

roboeyes_ns = cg.esphome_ns.namespace("roboeyes")
RoboEyes = roboeyes_ns.class_("RoboEyes", cg.Component)

CONF_DISPLAY_ID = "display_id"

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(RoboEyes),
        cv.Required(CONF_DISPLAY_ID): cv.use_id(display.DisplayBuffer),
    }
).extend(cv.COMPONENT_SCHEMA)


async def to_code(config):
    disp = await cg.get_variable(config[CONF_DISPLAY_ID])
    var = cg.new_Pvariable(config[cv.GenerateID()], disp)
    await cg.register_component(var, config)
