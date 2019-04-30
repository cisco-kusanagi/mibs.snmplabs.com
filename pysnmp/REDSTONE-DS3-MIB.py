#
# PySNMP MIB module REDSTONE-DS3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/REDSTONE-DS3-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:47:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
rsMgmt, = mibBuilder.importSymbols("REDSTONE-SMI", "rsMgmt")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, ObjectIdentity, Counter32, Gauge32, Unsigned32, Counter64, ModuleIdentity, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "Counter32", "Gauge32", "Unsigned32", "Counter64", "ModuleIdentity", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "Integer32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rsDs3MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2773, 2, 4))
rsDs3MIB.setRevisions(('1999-07-27 00:00',))
if mibBuilder.loadTexts: rsDs3MIB.setLastUpdated('9907270000Z')
if mibBuilder.loadTexts: rsDs3MIB.setOrganization('Redstone Communications, Inc.')
rsDs3Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 4, 1))
rsDsx3ConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2773, 2, 4, 1, 1), )
if mibBuilder.loadTexts: rsDsx3ConfigTable.setStatus('current')
rsDsx3ConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2773, 2, 4, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rsDsx3ConfigEntry.setStatus('current')
rsDsx3LineLength = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 4, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64000))).setUnits('meters').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsDsx3LineLength.setStatus('current')
rsDsx3LineType = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 4, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 18, 20))).clone(namedValues=NamedValues(("rsDsx3other", 1), ("rsDsx3M23", 2), ("rsDsx3SYNTRAN", 3), ("rsDsx3CbitParity", 4), ("rsDsx3ClearChannel", 5), ("rsE3G832", 6), ("rsE3Framed", 7), ("rsE3Plcp", 8), ("rsDsx3M23Plcp", 18), ("rsDsx3CbitParityPlcp", 20)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsDsx3LineType.setStatus('current')
rsDsx3CellScramblerConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 4, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("scramblerOn", 1), ("scramblerOff", 2), ("notSupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsDsx3CellScramblerConfig.setStatus('current')
rsDs3Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 4, 4))
rsDs3Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 4, 4, 1))
rsDs3Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 4, 4, 2))
rsDs3Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2773, 2, 4, 4, 1, 1)).setObjects(("REDSTONE-DS3-MIB", "rsDs3Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsDs3Compliance = rsDs3Compliance.setStatus('current')
rsDs3Group = ObjectGroup((1, 3, 6, 1, 4, 1, 2773, 2, 4, 4, 2, 1)).setObjects(("REDSTONE-DS3-MIB", "rsDsx3LineLength"), ("REDSTONE-DS3-MIB", "rsDsx3LineType"), ("REDSTONE-DS3-MIB", "rsDsx3CellScramblerConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsDs3Group = rsDs3Group.setStatus('current')
mibBuilder.exportSymbols("REDSTONE-DS3-MIB", rsDs3Group=rsDs3Group, rsDs3Objects=rsDs3Objects, rsDsx3CellScramblerConfig=rsDsx3CellScramblerConfig, rsDsx3LineType=rsDsx3LineType, rsDs3Compliance=rsDs3Compliance, rsDs3MIB=rsDs3MIB, rsDs3Conformance=rsDs3Conformance, rsDs3Groups=rsDs3Groups, rsDsx3LineLength=rsDsx3LineLength, rsDsx3ConfigTable=rsDsx3ConfigTable, PYSNMP_MODULE_ID=rsDs3MIB, rsDsx3ConfigEntry=rsDsx3ConfigEntry, rsDs3Compliances=rsDs3Compliances)
