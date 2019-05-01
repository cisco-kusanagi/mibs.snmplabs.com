#
# PySNMP MIB module CISCO-ATM-SWITCH-ADDR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ATM-SWITCH-ADDR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:50:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
IpAddress, Unsigned32, NotificationType, Bits, Integer32, iso, Gauge32, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Unsigned32", "NotificationType", "Bits", "Integer32", "iso", "Gauge32", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
ciscoAtmSwAddrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 51))
ciscoAtmSwAddrMIB.setRevisions(('1996-01-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAtmSwAddrMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoAtmSwAddrMIB.setLastUpdated('9601100000Z')
if mibBuilder.loadTexts: ciscoAtmSwAddrMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAtmSwAddrMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoAtmSwAddrMIB.setDescription('ATM Switch address MIB')
ciscoAtmSwAddrMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 51, 1))
class AtmAddr(TextualConvention, OctetString):
    description = 'The ATM address used by the network entity. The address types are: network prefix (13 octets), and NSAP (20 octets).'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(13, 13), ValueSizeConstraint(20, 20), )
ciscoAtmSwAddrTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 51, 1, 1), )
if mibBuilder.loadTexts: ciscoAtmSwAddrTable.setStatus('current')
if mibBuilder.loadTexts: ciscoAtmSwAddrTable.setDescription('This table contains an address list on a per switch basis.')
ciscoAtmSwAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 51, 1, 1, 1), ).setIndexNames((0, "CISCO-ATM-SWITCH-ADDR-MIB", "ciscoAtmSwAddrIndex"))
if mibBuilder.loadTexts: ciscoAtmSwAddrEntry.setStatus('current')
if mibBuilder.loadTexts: ciscoAtmSwAddrEntry.setDescription('An entry in the ciscoAtmSwAddrTable.')
ciscoAtmSwAddrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 51, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: ciscoAtmSwAddrIndex.setStatus('current')
if mibBuilder.loadTexts: ciscoAtmSwAddrIndex.setDescription('A sequence number when address gets created. 1 is the primary address. This is dense table and this index will be re-sequenced when a entry get deleted and it can only create new entry when append in the end of table.')
ciscoAtmSwAddrAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 51, 1, 1, 1, 2), AtmAddr()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoAtmSwAddrAddress.setStatus('current')
if mibBuilder.loadTexts: ciscoAtmSwAddrAddress.setDescription('A valid address for a given switch.')
ciscoAtmSwAddrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 51, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoAtmSwAddrRowStatus.setStatus('current')
if mibBuilder.loadTexts: ciscoAtmSwAddrRowStatus.setDescription('This object is used to create and delete rows in the ciscoAtmSwAddrTable.')
ciscoAtmSwAddrMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 51, 3))
ciscoAtmSwAddrMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 51, 3, 1))
ciscoAtmSwAddrMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 51, 3, 2))
ciscoAtmSwAddrMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 51, 3, 1, 1)).setObjects()

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmSwAddrMIBCompliance = ciscoAtmSwAddrMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoAtmSwAddrMIBCompliance.setDescription('The compliance statement for the Cisco ATM switch address group.')
ciscoAtmSwAddrMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 51, 3, 2, 1)).setObjects(("CISCO-ATM-SWITCH-ADDR-MIB", "ciscoAtmSwAddrAddress"), ("CISCO-ATM-SWITCH-ADDR-MIB", "ciscoAtmSwAddrRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmSwAddrMIBGroup = ciscoAtmSwAddrMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoAtmSwAddrMIBGroup.setDescription('')
mibBuilder.exportSymbols("CISCO-ATM-SWITCH-ADDR-MIB", ciscoAtmSwAddrMIBGroup=ciscoAtmSwAddrMIBGroup, ciscoAtmSwAddrAddress=ciscoAtmSwAddrAddress, ciscoAtmSwAddrMIBObjects=ciscoAtmSwAddrMIBObjects, ciscoAtmSwAddrRowStatus=ciscoAtmSwAddrRowStatus, ciscoAtmSwAddrMIBConformance=ciscoAtmSwAddrMIBConformance, ciscoAtmSwAddrMIBGroups=ciscoAtmSwAddrMIBGroups, PYSNMP_MODULE_ID=ciscoAtmSwAddrMIB, AtmAddr=AtmAddr, ciscoAtmSwAddrEntry=ciscoAtmSwAddrEntry, ciscoAtmSwAddrIndex=ciscoAtmSwAddrIndex, ciscoAtmSwAddrMIBCompliances=ciscoAtmSwAddrMIBCompliances, ciscoAtmSwAddrMIBCompliance=ciscoAtmSwAddrMIBCompliance, ciscoAtmSwAddrTable=ciscoAtmSwAddrTable, ciscoAtmSwAddrMIB=ciscoAtmSwAddrMIB)
