package launcher

const (
	dbNameRoot    = "postgres"
	dbNameMojave  = "mojave"
	dbNameVentura = "ventura"
)

const (
	defaultUser          = "postgres"
	defaultPass          = "password"
	defaultFolderName    = "data/postgres"
	defaultPort          = "5432"
	defaultListenAddress = "*"
	defaultDateLayout    = "20060102150405"
	localhost            = "localhost"
)

const (
	filePWD    = "pwfile"
	fileLog    = "postgres.log"
	fileConfig = "postgresql.conf"
)

const (
	migrationTable = "schema_migrations"
	backupMetaFile = ".meta"
)
