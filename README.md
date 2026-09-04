# EnvCheck

> Catch configuration mistakes without exposing the secrets being checked.

EnvCheck is a local configuration-hygiene checker for `.env` files and environment-driven application settings.

## Highlights

- Detect missing values
- Flag duplicate entries
- Identify weak placeholder values
- Catch common formatting mistakes
- Avoid printing secret values in diagnostics
- Useful before deployment or commits

## Usage

```bash
envcheck .env
envcheck .env --json
```

## Workflow

```text
.env / configuration
        ↓
   parse + inspect
        ↓
     findings
        ↓
  fix before shipping
```

## Use Cases

- Local configuration review
- Pre-deployment checks
- CI hygiene checks
- Debugging environment configuration
- Security-conscious development workflows

## Security

Never commit real credentials simply to test a scanner. EnvCheck is designed for local inspection and avoids printing secret values as part of its normal diagnostics.

## Development

```bash
python -m unittest discover -s tests -v
```

## License

MIT

Built by **Meduuv**.

[More projects](https://github.com/meduuv?tab=repositories) · [guns.lol/meduu](https://guns.lol/meduu)
