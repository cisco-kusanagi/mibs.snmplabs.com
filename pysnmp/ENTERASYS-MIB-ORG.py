#
# PySNMP MIB module ENTERASYS-MIB-ORG (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-MIB-ORG
# Produced by pysmi-0.3.4 at Mon Apr 29 18:49:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Bits, Integer32, TimeTicks, Counter32, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, iso, ObjectIdentity, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "Integer32", "TimeTicks", "Counter32", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "iso", "ObjectIdentity", "MibIdentifier", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
etsysMibOrg = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 3))
etsysMibOrg.setRevisions(('2010-08-17 12:15', '2010-06-02 11:30', '2010-03-25 20:29', '2009-12-07 14:41', '2009-08-10 18:56', '2009-08-04 13:43', '2009-07-02 13:34', '2009-02-20 16:20', '2009-02-12 15:04', '2009-01-07 21:18', '2008-07-23 14:11', '2008-04-10 14:51', '2007-02-27 18:16', '2006-03-06 13:53', '2005-11-14 16:48', '2005-01-26 22:18', '2005-01-25 15:41', '2005-01-12 21:00', '2004-08-24 13:29', '2004-08-19 21:20', '2004-08-17 17:03', '2004-08-13 16:57', '2004-08-05 20:25', '2004-07-29 18:59', '2004-07-28 16:24', '2004-06-02 13:40', '2004-04-02 22:53', '2004-02-13 20:00', '2004-02-03 15:33', '2003-11-14 16:01', '2003-11-06 15:15', '2003-10-21 15:39', '2003-10-16 12:16', '2003-08-19 20:53', '2003-06-13 18:09', '2003-05-16 20:07', '2002-12-20 15:19', '2002-12-13 20:54', '2002-11-01 21:20', '2002-10-08 20:27', '2002-09-25 20:03', '2002-09-13 19:30', '2002-08-07 18:51', '2002-07-18 15:31', '2002-06-24 21:34', '2002-05-07 17:55', '2002-04-05 15:01', '2002-03-14 20:54', '2002-02-20 20:02', '2002-01-24 18:23', '2001-08-16 13:00', '2001-08-14 19:30', '2001-05-22 13:00', '2001-04-02 21:00', '2001-01-24 17:00', '2000-11-28 14:00', '2000-10-03 18:44',))
if mibBuilder.loadTexts: etsysMibOrg.setLastUpdated('201008171215Z')
if mibBuilder.loadTexts: etsysMibOrg.setOrganization('Enterasys Networks, Inc.')
mibBuilder.exportSymbols("ENTERASYS-MIB-ORG", etsysMibOrg=etsysMibOrg, PYSNMP_MODULE_ID=etsysMibOrg)
