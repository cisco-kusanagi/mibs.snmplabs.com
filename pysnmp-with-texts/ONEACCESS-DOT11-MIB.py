#
# PySNMP MIB module ONEACCESS-DOT11-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ONEACCESS-DOT11-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:34:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
oacRequirements, oacMIBModules, oacExpIMDot11 = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacRequirements", "oacMIBModules", "oacExpIMDot11")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
TimeTicks, MibIdentifier, Bits, Counter32, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity, ObjectIdentity, Gauge32, Unsigned32, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "Bits", "Counter32", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity", "ObjectIdentity", "Gauge32", "Unsigned32", "iso", "Integer32")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
oacDot11MIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 1, 100, 900))
oacDot11MIBModule.setRevisions(('2011-10-27 00:00', '2010-07-08 00:01',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: oacDot11MIBModule.setRevisionsDescriptions(('Fixed Minor correction added last revision.', 'This MIB module describes DOT11 objects.',))
if mibBuilder.loadTexts: oacDot11MIBModule.setLastUpdated('201110270000Z')
if mibBuilder.loadTexts: oacDot11MIBModule.setOrganization(' OneAccess ')
if mibBuilder.loadTexts: oacDot11MIBModule.setContactInfo('Pascal KESTELOOT Postal: ONE ACCESS 381 Avenue du Gnral de Gaulle 92140 Clamart, France FRANCE Tel: (+33) 01 41 87 70 00 Fax: (+33) 01 41 87 74 00 E-mail: pascal.kesteloot@oneaccess-net.com')
if mibBuilder.loadTexts: oacDot11MIBModule.setDescription('Contact updated')
class InterfaceType(TextualConvention, Integer32):
    description = 'The interface type'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("mainInterface", 1), ("subInterface", 2))

oacExpIMDot11Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 8, 1))
oacExpIMDot11InterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 8, 1, 1), )
if mibBuilder.loadTexts: oacExpIMDot11InterfaceTable.setStatus('current')
if mibBuilder.loadTexts: oacExpIMDot11InterfaceTable.setDescription(' Table to collect status information counters on an dot11 interface basis, either logical or physical (i.e. radio) For these interfaces, IANAifType is ieee80211(71) This table is an extension to MIBII ifTable where standard status and counters are collected')
oacExpIMDot11InterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 8, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: oacExpIMDot11InterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: oacExpIMDot11InterfaceEntry.setDescription(' index is MIBII standard index ')
oacExpIMDot11EntryType = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 8, 1, 1, 1, 1), InterfaceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacExpIMDot11EntryType.setStatus('current')
if mibBuilder.loadTexts: oacExpIMDot11EntryType.setDescription('This attribute shall specify the type of entry mainInterface i.e. radio interface is physical radio interface subInterface i.e. vap is logical dot11 interface aka Virtual Access Point')
oacExpIMDot11MACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 8, 1, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacExpIMDot11MACAddress.setStatus('current')
if mibBuilder.loadTexts: oacExpIMDot11MACAddress.setDescription('Unique MAC Address assigned to the VAP available for VAP entries')
oacExpIMDot11SSID = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 8, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacExpIMDot11SSID.setStatus('current')
if mibBuilder.loadTexts: oacExpIMDot11SSID.setDescription('This attribute reflects the Service Set ID used available for VAP entries')
oacExpIMDot11AssociatedStations = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 8, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacExpIMDot11AssociatedStations.setStatus('current')
if mibBuilder.loadTexts: oacExpIMDot11AssociatedStations.setDescription('This counter is the number of currently associated stations, for vap entries, the stations associated on the SSID of this vap, for radio entry the total of all associated stations')
oacExpIMDot11Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 5, 900))
oacExpIMDot11Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 5, 900, 1))
oacExpIMDot11Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 5, 900, 2))
oacExpIMDot11Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 13191, 5, 900, 2, 1)).setObjects(("ONEACCESS-DOT11-MIB", "oacExpIMDot11GeneralGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oacExpIMDot11Compliance = oacExpIMDot11Compliance.setStatus('current')
if mibBuilder.loadTexts: oacExpIMDot11Compliance.setDescription('The compliance statement for agents that support the ONEACCESS-DOT11-MIB.')
oacExpIMDot11GeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13191, 5, 900, 1, 1)).setObjects(("ONEACCESS-DOT11-MIB", "oacExpIMDot11EntryType"), ("ONEACCESS-DOT11-MIB", "oacExpIMDot11MACAddress"), ("ONEACCESS-DOT11-MIB", "oacExpIMDot11SSID"), ("ONEACCESS-DOT11-MIB", "oacExpIMDot11AssociatedStations"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oacExpIMDot11GeneralGroup = oacExpIMDot11GeneralGroup.setStatus('current')
if mibBuilder.loadTexts: oacExpIMDot11GeneralGroup.setDescription('This group is mandatory for DOT11 entity.')
mibBuilder.exportSymbols("ONEACCESS-DOT11-MIB", oacExpIMDot11EntryType=oacExpIMDot11EntryType, oacExpIMDot11SSID=oacExpIMDot11SSID, oacExpIMDot11InterfaceTable=oacExpIMDot11InterfaceTable, oacDot11MIBModule=oacDot11MIBModule, oacExpIMDot11InterfaceEntry=oacExpIMDot11InterfaceEntry, InterfaceType=InterfaceType, oacExpIMDot11MACAddress=oacExpIMDot11MACAddress, PYSNMP_MODULE_ID=oacDot11MIBModule, oacExpIMDot11Compliances=oacExpIMDot11Compliances, oacExpIMDot11GeneralGroup=oacExpIMDot11GeneralGroup, oacExpIMDot11AssociatedStations=oacExpIMDot11AssociatedStations, oacExpIMDot11Compliance=oacExpIMDot11Compliance, oacExpIMDot11Groups=oacExpIMDot11Groups, oacExpIMDot11Objects=oacExpIMDot11Objects, oacExpIMDot11Conformance=oacExpIMDot11Conformance)
