#
# PySNMP MIB module RADLAN-CDB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-CDB-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:37:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, MibIdentifier, IpAddress, Bits, ModuleIdentity, Integer32, Gauge32, ObjectIdentity, Counter32, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "MibIdentifier", "IpAddress", "Bits", "ModuleIdentity", "Integer32", "Gauge32", "ObjectIdentity", "Counter32", "TimeTicks", "Unsigned32", "iso")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
rlCDB = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 94))
rlCDB.setRevisions(('2007-01-02 00:00',))
if mibBuilder.loadTexts: rlCDB.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlCDB.setOrganization('Radlan - a MARVELL company. Marvell Semiconductor, Inc.')
rlStartupCDBChanged = MibScalar((1, 3, 6, 1, 4, 1, 89, 94, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStartupCDBChanged.setStatus('current')
rlManualReboot = MibScalar((1, 3, 6, 1, 4, 1, 89, 94, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlManualReboot.setStatus('current')
rlStartupCDBEmpty = MibScalar((1, 3, 6, 1, 4, 1, 89, 94, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStartupCDBEmpty.setStatus('current')
mibBuilder.exportSymbols("RADLAN-CDB-MIB", rlStartupCDBEmpty=rlStartupCDBEmpty, rlCDB=rlCDB, rlStartupCDBChanged=rlStartupCDBChanged, PYSNMP_MODULE_ID=rlCDB, rlManualReboot=rlManualReboot)
