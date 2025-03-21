/*
   lunes, 10 de octubre de 202216:02:38
   Usuario: prodmatt
   Servidor: mattilda-prod.database.windows.net
   Base de datos: Mattilda-Prod
   Aplicación: 
*/

/* Para evitar posibles problemas de pérdida de datos, debe revisar este script detalladamente antes de ejecutarlo fuera del contexto del diseñador de base de datos.*/
BEGIN TRANSACTION
SET QUOTED_IDENTIFIER ON
SET ARITHABORT ON
SET NUMERIC_ROUNDABORT OFF
SET CONCAT_NULL_YIELDS_NULL ON
SET ANSI_NULLS ON
SET ANSI_PADDING ON
SET ANSI_WARNINGS ON
COMMIT
BEGIN TRANSACTION
GO
CREATE TABLE dbo.Tmp_t_descuentos
	(
	IDConfig_D int NOT NULL IDENTITY (1, 1),
	IDConcepto nchar(5) NOT NULL,
	IDTipoDesc int NOT NULL,
	Dias_regla int NULL,
	Fecha_Aplicacion date NULL,
	Tipo_monto varchar(30) NOT NULL,
	Porcentaje float(53) NULL,
	Monto float(53) NULL,
	IDConcepto_Aplica nchar(5) NOT NULL,
	IDEstatus nchar(1) NOT NULL,
	IDUsuario int NOT NULL,
	Fecha_actividad datetime NOT NULL
	)  ON [PRIMARY]
GO
ALTER TABLE dbo.Tmp_t_descuentos SET (LOCK_ESCALATION = TABLE)
GO
SET IDENTITY_INSERT dbo.Tmp_t_descuentos ON
GO
IF EXISTS(SELECT * FROM dbo.t_descuentos)
	 EXEC('INSERT INTO dbo.Tmp_t_descuentos (IDConfig_D, IDConcepto, IDTipoDesc, Dias_regla, Fecha_Aplicacion, Tipo_monto, Porcentaje, Monto, IDConcepto_Aplica, IDEstatus, IDUsuario, Fecha_actividad)
		SELECT IDConfig_D, IDConcepto, IDTipoDesc, Dias_regla, Fecha_Aplicacion, Tipo_monto, Porcentaje, Monto, IDConcepto_Aplica, IDEstatus, IDUsuario, Fecha_actividad FROM dbo.t_descuentos WITH (HOLDLOCK TABLOCKX)')
GO
SET IDENTITY_INSERT dbo.Tmp_t_descuentos OFF
GO
DROP TABLE dbo.t_descuentos
GO
EXECUTE sp_rename N'dbo.Tmp_t_descuentos', N't_descuentos', 'OBJECT' 
GO
COMMIT
select Has_Perms_By_Name(N'dbo.t_descuentos', 'Object', 'ALTER') as ALT_Per, Has_Perms_By_Name(N'dbo.t_descuentos', 'Object', 'VIEW DEFINITION') as View_def_Per, Has_Perms_By_Name(N'dbo.t_descuentos', 'Object', 'CONTROL') as Contr_Per 