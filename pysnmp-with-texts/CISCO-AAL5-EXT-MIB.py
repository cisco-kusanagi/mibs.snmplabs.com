#
# PySNMP MIB module CISCO-AAL5-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-AAL5-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:49:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
aal5VccEntry, = mibBuilder.importSymbols("ATM-MIB", "aal5VccEntry")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
NotificationType, iso, ModuleIdentity, Bits, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, Counter32, Counter64, Integer32, IpAddress, Unsigned32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "ModuleIdentity", "Bits", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "Counter32", "Counter64", "Integer32", "IpAddress", "Unsigned32", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoAal5ExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 9999))
ciscoAal5ExtMIB.setRevisions(('2001-11-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAal5ExtMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoAal5ExtMIB.setLastUpdated('200111050000Z')
if mibBuilder.loadTexts: ciscoAal5ExtMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAal5ExtMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-atm@cisco.com')
if mibBuilder.loadTexts: ciscoAal5ExtMIB.setDescription('This MIB is the RFC 1695 extension for Cisco product. It provides the additional AAL5 performance statistics of a VCC from RFC 1695.')
ciscoAal5ExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1))
cAal5ExtConnections = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1))
cAal5ExtVccTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1), )
if mibBuilder.loadTexts: cAal5ExtVccTable.setStatus('current')
if mibBuilder.loadTexts: cAal5ExtVccTable.setDescription('This table contains AAL5 VCC performance parameters beyond that provided by aal5VccEntry defined in RFC1695 and AAL5 MIB.')
cAal5ExtVccEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1), )
aal5VccEntry.registerAugmentions(("CISCO-AAL5-EXT-MIB", "cAal5ExtVccEntry"))
cAal5ExtVccEntry.setIndexNames(*aal5VccEntry.getIndexNames())
if mibBuilder.loadTexts: cAal5ExtVccEntry.setStatus('current')
if mibBuilder.loadTexts: cAal5ExtVccEntry.setDescription('This list contains the additional AAL5 VCC performance parameters beyond that provided by aal5VccEntry defined in RFC1695.')
cAal5VccInDroppedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 1), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccInDroppedPkts.setStatus('current')
if mibBuilder.loadTexts: cAal5VccInDroppedPkts.setDescription('The number of AAL5 CPCS PDUs dropped at the receive side of this AAL5 VCC at the interface associated with an AAL5 entity.')
cAal5VccOutDroppedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 2), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccOutDroppedPkts.setStatus('current')
if mibBuilder.loadTexts: cAal5VccOutDroppedPkts.setDescription('The number of AAL5 CPCS PDUs dropped at the transmit side of this AAL5 VCC at the interface associated with an AAL5 entity.')
cAal5VccInDroppedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 3), Counter32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccInDroppedOctets.setStatus('current')
if mibBuilder.loadTexts: cAal5VccInDroppedOctets.setDescription('The number of AAL5 CPCS PDU Octets dropped at the receive side of this AAL5 VCC at the interface associated with an AAL5 entity.')
cAal5VccOutDroppedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 4), Counter32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccOutDroppedOctets.setStatus('current')
if mibBuilder.loadTexts: cAal5VccOutDroppedOctets.setDescription('The number of AAL5 CPCS PDU Octets dropped at the transmit side of this AAL5 VCC at the interface associated with an AAL5 entity.')
cAal5VccInCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 5), Counter32()).setUnits('cells').setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccInCells.setStatus('current')
if mibBuilder.loadTexts: cAal5VccInCells.setDescription('The number of AAL5 SAR cells received on this AAL5 VCC at the interface associated with an AAL5 entity.')
cAal5VccOutCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 6), Counter32()).setUnits('cells').setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccOutCells.setStatus('current')
if mibBuilder.loadTexts: cAal5VccOutCells.setDescription('The number of AAL5 SAR cells transmitted on this AAL5 VCC at the interface associated with an AAL5 entity.')
cAal5VccInDroppedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 7), Counter32()).setUnits('cells').setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccInDroppedCells.setStatus('current')
if mibBuilder.loadTexts: cAal5VccInDroppedCells.setDescription('The number of AAL5 SAR cells dropped at the receive side of this AAL5 VCC at the interface associated with an AAL5 entity.')
cAal5VccOutDroppedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 8), Counter32()).setUnits('cells').setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccOutDroppedCells.setStatus('current')
if mibBuilder.loadTexts: cAal5VccOutDroppedCells.setDescription('The number of AAL5 SAR cells dropped at the transmit side of this AAL5 VCC at the interface associated with an AAL5 entity.')
ciscoAAL5ExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2))
ciscoAAL5ExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 1))
ciscoAAL5ExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2))
ciscoAAL5ExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 1, 1)).setObjects(("CISCO-AAL5-EXT-MIB", "ciscoAal5ExtMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAL5ExtMIBCompliance = ciscoAAL5ExtMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoAAL5ExtMIBCompliance.setDescription('The compliance statement for entities which implement this Cisco AAL5 EXT MIB.')
ciscoAal5ExtMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 1)).setObjects(("CISCO-AAL5-EXT-MIB", "cAal5VccInDroppedPkts"), ("CISCO-AAL5-EXT-MIB", "cAal5VccOutDroppedPkts"), ("CISCO-AAL5-EXT-MIB", "cAal5VccInDroppedOctets"), ("CISCO-AAL5-EXT-MIB", "cAal5VccOutDroppedOctets"), ("CISCO-AAL5-EXT-MIB", "cAal5VccInCells"), ("CISCO-AAL5-EXT-MIB", "cAal5VccOutCells"), ("CISCO-AAL5-EXT-MIB", "cAal5VccInDroppedCells"), ("CISCO-AAL5-EXT-MIB", "cAal5VccOutDroppedCells"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAal5ExtMIBGroup = ciscoAal5ExtMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoAal5ExtMIBGroup.setDescription('A collection of objects providing these extra AAL5 interface related statistics.')
mibBuilder.exportSymbols("CISCO-AAL5-EXT-MIB", ciscoAAL5ExtMIBConformance=ciscoAAL5ExtMIBConformance, ciscoAAL5ExtMIBCompliances=ciscoAAL5ExtMIBCompliances, ciscoAAL5ExtMIBGroups=ciscoAAL5ExtMIBGroups, cAal5VccInDroppedPkts=cAal5VccInDroppedPkts, ciscoAal5ExtMIBObjects=ciscoAal5ExtMIBObjects, ciscoAal5ExtMIBGroup=ciscoAal5ExtMIBGroup, cAal5ExtVccTable=cAal5ExtVccTable, PYSNMP_MODULE_ID=ciscoAal5ExtMIB, cAal5VccOutDroppedPkts=cAal5VccOutDroppedPkts, cAal5ExtVccEntry=cAal5ExtVccEntry, ciscoAal5ExtMIB=ciscoAal5ExtMIB, cAal5VccInDroppedOctets=cAal5VccInDroppedOctets, ciscoAAL5ExtMIBCompliance=ciscoAAL5ExtMIBCompliance, cAal5VccOutCells=cAal5VccOutCells, cAal5ExtConnections=cAal5ExtConnections, cAal5VccOutDroppedCells=cAal5VccOutDroppedCells, cAal5VccInCells=cAal5VccInCells, cAal5VccInDroppedCells=cAal5VccInDroppedCells, cAal5VccOutDroppedOctets=cAal5VccOutDroppedOctets)
