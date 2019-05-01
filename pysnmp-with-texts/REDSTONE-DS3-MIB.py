#
# PySNMP MIB module REDSTONE-DS3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/REDSTONE-DS3-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:55:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
rsMgmt, = mibBuilder.importSymbols("REDSTONE-SMI", "rsMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
NotificationType, ModuleIdentity, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, IpAddress, iso, Unsigned32, Bits, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "IpAddress", "iso", "Unsigned32", "Bits", "MibIdentifier", "Counter32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rsDs3MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2773, 2, 4))
rsDs3MIB.setRevisions(('1999-07-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rsDs3MIB.setRevisionsDescriptions(('Revised version of this MIB module.',))
if mibBuilder.loadTexts: rsDs3MIB.setLastUpdated('9907270000Z')
if mibBuilder.loadTexts: rsDs3MIB.setOrganization('Redstone Communications, Inc.')
if mibBuilder.loadTexts: rsDs3MIB.setContactInfo(' Redstone Communications, Inc. 5 Carlisle Road Westford MA 01886 USA Tel: +1-978-692-1999 Email: mib@redstonecom.com ')
if mibBuilder.loadTexts: rsDs3MIB.setDescription('The DS3 MIB for the Redstone Communications Inc. enterprise.')
rsDs3Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 4, 1))
rsDsx3ConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2773, 2, 4, 1, 1), )
if mibBuilder.loadTexts: rsDsx3ConfigTable.setStatus('current')
if mibBuilder.loadTexts: rsDsx3ConfigTable.setDescription('This table contains entries for DS3/E3 interfaces present in the system.')
rsDsx3ConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2773, 2, 4, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rsDsx3ConfigEntry.setStatus('current')
if mibBuilder.loadTexts: rsDsx3ConfigEntry.setDescription('Each entry describes the characteristics of an DS3/E3 interface.')
rsDsx3LineLength = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 4, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64000))).setUnits('meters').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsDsx3LineLength.setStatus('current')
if mibBuilder.loadTexts: rsDsx3LineLength.setDescription('The length of the DS3/E3 line in meters. This objects provides information for line build out circuitry. This object is only useful if the interface has configurable line build out circuitry.')
rsDsx3LineType = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 4, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 18, 20))).clone(namedValues=NamedValues(("rsDsx3other", 1), ("rsDsx3M23", 2), ("rsDsx3SYNTRAN", 3), ("rsDsx3CbitParity", 4), ("rsDsx3ClearChannel", 5), ("rsE3G832", 6), ("rsE3Framed", 7), ("rsE3Plcp", 8), ("rsDsx3M23Plcp", 18), ("rsDsx3CbitParityPlcp", 20)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsDsx3LineType.setStatus('current')
if mibBuilder.loadTexts: rsDsx3LineType.setDescription('This variable indicates the variety of DS3 C-bit or E3 application implementing this interface. The type of interface affects the interpretation of the usage and error statistics. The rate of DS3 is 44.736 Mbps and E3 is 34.368 Mbps. The dsx3ClearChannel value means that the C-bits are not used except for sending/receiving AIS. Note that this object represents the actual line type when the corresponding value of dsx3LineType is dsx3other(1). The values, in sequence, describe: TITLE: SPECIFICATION: dsx3M23 ANSI T1.107-1988 dsx3SYNTRAN ANSI T1.107-1988 dsx3CbitParity ANSI T1.107a-1989 dsx3ClearChannel ANSI T1.102-1987 e3G832 ITU-T G.832 e3Framed ITU-T G.751 e3Plcp ETSI T/NA(91)18. dsx3M23Plcp ATM Forum af-phy-0054.000 dsx3CbitParityPlcp ATM Forum af-phy-0054.000')
rsDsx3CellScramblerConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 4, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("scramblerOn", 1), ("scramblerOff", 2), ("notSupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsDsx3CellScramblerConfig.setStatus('current')
if mibBuilder.loadTexts: rsDsx3CellScramblerConfig.setDescription('This variable indicates the state of the ATM cell scrambler for interfaces which support ATM over DS3 or E3. For interfaces which do not support ATM, this object returns the value notSupported(3).')
rsDs3Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 4, 4))
rsDs3Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 4, 4, 1))
rsDs3Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 4, 4, 2))
rsDs3Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2773, 2, 4, 4, 1, 1)).setObjects(("REDSTONE-DS3-MIB", "rsDs3Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsDs3Compliance = rsDs3Compliance.setStatus('current')
if mibBuilder.loadTexts: rsDs3Compliance.setDescription('The compliance statement for entities which implement the Redstone DS3/E3 MIB.')
rsDs3Group = ObjectGroup((1, 3, 6, 1, 4, 1, 2773, 2, 4, 4, 2, 1)).setObjects(("REDSTONE-DS3-MIB", "rsDsx3LineLength"), ("REDSTONE-DS3-MIB", "rsDsx3LineType"), ("REDSTONE-DS3-MIB", "rsDsx3CellScramblerConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsDs3Group = rsDs3Group.setStatus('current')
if mibBuilder.loadTexts: rsDs3Group.setDescription('A collection of objects providing management of DS3/E3 interfaces in a Redstone product.')
mibBuilder.exportSymbols("REDSTONE-DS3-MIB", rsDsx3CellScramblerConfig=rsDsx3CellScramblerConfig, rsDs3Group=rsDs3Group, rsDs3Compliance=rsDs3Compliance, PYSNMP_MODULE_ID=rsDs3MIB, rsDsx3LineLength=rsDsx3LineLength, rsDsx3LineType=rsDsx3LineType, rsDs3Compliances=rsDs3Compliances, rsDs3Objects=rsDs3Objects, rsDs3MIB=rsDs3MIB, rsDsx3ConfigTable=rsDsx3ConfigTable, rsDs3Groups=rsDs3Groups, rsDsx3ConfigEntry=rsDsx3ConfigEntry, rsDs3Conformance=rsDs3Conformance)
