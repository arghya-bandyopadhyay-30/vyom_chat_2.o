import argparse
import asyncio

from pipeline.config.pipeline_config_service import PipelineConfigService


async def run(config_file_path: str = "config.yml"):
    config = PipelineConfigService(config_path=config_file_path).get_config()
    await run_task(config)

async def run_task(config):
    for stage in config.pipeline.stages:
        stage.run()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pipeline Configuration Runner")
    parser.add_argument("config_path", type=str, help="Path to the pipeline config YAML file")
    args = parser.parse_args()

    asyncio.run(run(args.config_path))