USE [lab1]
GO
/****** Object:  StoredProcedure [dbo].[sp_v3_upgrade]    Script Date: 11/14/2017 2:53:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER procedure [dbo].[sp_v3_upgrade]
as
BEGIN
create table Filler
(
id int not null 
primary key(id)
)
END
