#
# PySNMP MIB module CISCO-ATM-ADDR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ATM-ADDR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:50:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, NotificationType, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, TimeTicks, ObjectIdentity, ModuleIdentity, Counter64, Gauge32, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "Counter64", "Gauge32", "Unsigned32", "Bits")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
ciscoAtmAddrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 12))
ciscoAtmAddrMIB.setRevisions(('1996-05-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAtmAddrMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoAtmAddrMIB.setLastUpdated('9605060000Z')
if mibBuilder.loadTexts: ciscoAtmAddrMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAtmAddrMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-atm@cisco.com')
if mibBuilder.loadTexts: ciscoAtmAddrMIB.setDescription('ATM address MIB')
class AtmAddr(TextualConvention, OctetString):
    description = 'The ATM address used by the network entity. The address types are: no address (0 octets), E.164 (8 octets), network prefix (13 octets), and NSAP (20 octets). Note: The E.164 address is encoded in BCD format.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(8, 8), ValueSizeConstraint(13, 13), ValueSizeConstraint(20, 20), )
ciscoAtmAddrMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 12, 1))
ciscoAtmIfAdminAddrTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 12, 1, 1), )
if mibBuilder.loadTexts: ciscoAtmIfAdminAddrTable.setStatus('current')
if mibBuilder.loadTexts: ciscoAtmIfAdminAddrTable.setDescription('This table contains an address list on a per interface basis. This table only applies to switches or networks and only for interfaces that have more than one address assigned.')
ciscoAtmIfAdminAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 12, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-ATM-ADDR-MIB", "ciscoAtmIfAdminAddrAddress"))
if mibBuilder.loadTexts: ciscoAtmIfAdminAddrEntry.setStatus('current')
if mibBuilder.loadTexts: ciscoAtmIfAdminAddrEntry.setDescription('An entry in the CiscoAtmIfAdminAddrTable.')
ciscoAtmIfAdminAddrAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 12, 1, 1, 1, 1), AtmAddr())
if mibBuilder.loadTexts: ciscoAtmIfAdminAddrAddress.setStatus('current')
if mibBuilder.loadTexts: ciscoAtmIfAdminAddrAddress.setDescription('A valid address for a given switch or network interface.')
ciscoAtmIfAdminAddrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 12, 1, 1, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoAtmIfAdminAddrRowStatus.setStatus('current')
if mibBuilder.loadTexts: ciscoAtmIfAdminAddrRowStatus.setDescription('This object is used to create and delete rows in the atmIfAdminAddrTable.')
ciscoAtmIfAdminAddrMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 12, 3))
ciscoAtmIfAdminAddrMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 12, 3, 1))
ciscoAtmIfAdminAddrMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 12, 3, 2))
ciscoAtmIfAdminAddrMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 12, 3, 1, 1)).setObjects(("CISCO-ATM-ADDR-MIB", "ciscoAtmIfAdminAddrMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmIfAdminAddrMIBCompliance = ciscoAtmIfAdminAddrMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoAtmIfAdminAddrMIBCompliance.setDescription('The compliance statement for the Cisco ATM address group.')
ciscoAtmIfAdminAddrMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 12, 3, 2, 1)).setObjects(("CISCO-ATM-ADDR-MIB", "ciscoAtmIfAdminAddrRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmIfAdminAddrMIBGroup = ciscoAtmIfAdminAddrMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoAtmIfAdminAddrMIBGroup.setDescription('This object is used to create and delete rows in the atmIfAdminAddrTable.')
mibBuilder.exportSymbols("CISCO-ATM-ADDR-MIB", ciscoAtmIfAdminAddrEntry=ciscoAtmIfAdminAddrEntry, ciscoAtmIfAdminAddrRowStatus=ciscoAtmIfAdminAddrRowStatus, PYSNMP_MODULE_ID=ciscoAtmAddrMIB, ciscoAtmIfAdminAddrMIBCompliances=ciscoAtmIfAdminAddrMIBCompliances, ciscoAtmIfAdminAddrMIBCompliance=ciscoAtmIfAdminAddrMIBCompliance, ciscoAtmIfAdminAddrMIBGroup=ciscoAtmIfAdminAddrMIBGroup, ciscoAtmAddrMIBObjects=ciscoAtmAddrMIBObjects, AtmAddr=AtmAddr, ciscoAtmIfAdminAddrAddress=ciscoAtmIfAdminAddrAddress, ciscoAtmIfAdminAddrMIBConformance=ciscoAtmIfAdminAddrMIBConformance, ciscoAtmIfAdminAddrMIBGroups=ciscoAtmIfAdminAddrMIBGroups, ciscoAtmIfAdminAddrTable=ciscoAtmIfAdminAddrTable, ciscoAtmAddrMIB=ciscoAtmAddrMIB)
