#
# PySNMP MIB module CISCO-NETINT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-NETINT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:08:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ObjectIdentity, iso, MibIdentifier, Counter32, IpAddress, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, Counter64, Gauge32, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "MibIdentifier", "Counter32", "IpAddress", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "Counter64", "Gauge32", "Unsigned32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoNetintMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 490))
ciscoNetintMIB.setRevisions(('2005-09-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoNetintMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoNetintMIB.setLastUpdated('200509260000Z')
if mibBuilder.loadTexts: ciscoNetintMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoNetintMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoNetintMIB.setDescription('This MIB module is for Network Interrupt information on Cisco device.')
ciscoNetintMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 490, 0))
ciscoNetintMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 490, 1))
ciscoNetintMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 490, 2))
cniThrottle = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 490, 1, 1))
cniThrottleTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 490, 1, 1, 1), )
if mibBuilder.loadTexts: cniThrottleTable.setStatus('current')
if mibBuilder.loadTexts: cniThrottleTable.setDescription('This table provides the network interrupt throttle counter information. An entry in this table is populated for each physical entity in the managed system capable of providing this information.')
cniThrottleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 490, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cniThrottleEntry.setStatus('current')
if mibBuilder.loadTexts: cniThrottleEntry.setDescription('An entry containing information about network interrupt throttle counter.')
cniThrottleCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 490, 1, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cniThrottleCount.setStatus('current')
if mibBuilder.loadTexts: cniThrottleCount.setDescription('This object indicates the number of times network interrupt throttle has become active.')
ciscoNetintMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 490, 2, 1))
ciscoNetintMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 490, 2, 2))
ciscoNetintMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 490, 2, 1, 1)).setObjects(("CISCO-NETINT-MIB", "ciscoThrottleGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetintMIBCompliance = ciscoNetintMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoNetintMIBCompliance.setDescription('The compliance statement for entities which implement the Cisco Netint MIB.')
ciscoThrottleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 490, 2, 2, 1)).setObjects(("CISCO-NETINT-MIB", "cniThrottleCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoThrottleGroup = ciscoThrottleGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoThrottleGroup.setDescription('A collection of object providing network interrupt throttle count.')
mibBuilder.exportSymbols("CISCO-NETINT-MIB", ciscoNetintMIBCompliance=ciscoNetintMIBCompliance, ciscoNetintMIBCompliances=ciscoNetintMIBCompliances, cniThrottleEntry=cniThrottleEntry, ciscoNetintMIB=ciscoNetintMIB, ciscoNetintMIBConformance=ciscoNetintMIBConformance, ciscoNetintMIBGroups=ciscoNetintMIBGroups, ciscoThrottleGroup=ciscoThrottleGroup, ciscoNetintMIBNotifs=ciscoNetintMIBNotifs, PYSNMP_MODULE_ID=ciscoNetintMIB, ciscoNetintMIBObjects=ciscoNetintMIBObjects, cniThrottleTable=cniThrottleTable, cniThrottleCount=cniThrottleCount, cniThrottle=cniThrottle)
