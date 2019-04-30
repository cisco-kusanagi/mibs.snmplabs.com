#
# PySNMP MIB module CISCO-GPRS-ISGSN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-GPRS-ISGSN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:42:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter32, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, iso, Bits, Integer32, NotificationType, ModuleIdentity, IpAddress, Unsigned32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "iso", "Bits", "Integer32", "NotificationType", "ModuleIdentity", "IpAddress", "Unsigned32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoGprsIsgsnMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 9992))
if mibBuilder.loadTexts: ciscoGprsIsgsnMIB.setLastUpdated('9810150000Z')
if mibBuilder.loadTexts: ciscoGprsIsgsnMIB.setOrganization('Cisco Systems, Inc.')
ciscoGprsIsgsnMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9992, 1))
ciscoGprsIsgsnStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9992, 1, 1))
cgprsIsgsnRxPacketCountFromTnode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9992, 1, 1, 1), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgprsIsgsnRxPacketCountFromTnode.setStatus('current')
cgprsIsgsnTxPacketCountToTnode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9992, 1, 1, 2), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgprsIsgsnTxPacketCountToTnode.setStatus('current')
cgprsIsgsnRxOctetCountFromTnode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9992, 1, 1, 3), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgprsIsgsnRxOctetCountFromTnode.setStatus('current')
cgprsIsgsnTxOctetCountToTnode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9992, 1, 1, 4), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgprsIsgsnTxOctetCountToTnode.setStatus('current')
cgprsIsgsnErrorCountRxFromTnode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9992, 1, 1, 5), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgprsIsgsnErrorCountRxFromTnode.setStatus('current')
cgprsIsgsnErrorCountRxToTnode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9992, 1, 1, 6), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgprsIsgsnErrorCountRxToTnode.setStatus('current')
ciscoGprsIsgsnConformances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9992, 3))
cgprsIsgsnGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9992, 3, 1))
cgprsIsgsnCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9992, 3, 2))
cgprsIsgsnCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 9992, 3, 2, 1)).setObjects(("CISCO-GPRS-ISGSN-MIB", "cgprsIsgsnStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsIsgsnCompliance1 = cgprsIsgsnCompliance1.setStatus('current')
cgprsIsgsnStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9992, 3, 1, 1)).setObjects(("CISCO-GPRS-ISGSN-MIB", "cgprsIsgsnRxPacketCountFromTnode"), ("CISCO-GPRS-ISGSN-MIB", "cgprsIsgsnTxPacketCountToTnode"), ("CISCO-GPRS-ISGSN-MIB", "cgprsIsgsnRxOctetCountFromTnode"), ("CISCO-GPRS-ISGSN-MIB", "cgprsIsgsnTxOctetCountToTnode"), ("CISCO-GPRS-ISGSN-MIB", "cgprsIsgsnErrorCountRxFromTnode"), ("CISCO-GPRS-ISGSN-MIB", "cgprsIsgsnErrorCountRxToTnode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsIsgsnStatsGroup = cgprsIsgsnStatsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-GPRS-ISGSN-MIB", cgprsIsgsnTxPacketCountToTnode=cgprsIsgsnTxPacketCountToTnode, cgprsIsgsnTxOctetCountToTnode=cgprsIsgsnTxOctetCountToTnode, ciscoGprsIsgsnMIBObjects=ciscoGprsIsgsnMIBObjects, cgprsIsgsnCompliances=cgprsIsgsnCompliances, ciscoGprsIsgsnConformances=ciscoGprsIsgsnConformances, cgprsIsgsnStatsGroup=cgprsIsgsnStatsGroup, ciscoGprsIsgsnStats=ciscoGprsIsgsnStats, cgprsIsgsnGroups=cgprsIsgsnGroups, cgprsIsgsnRxPacketCountFromTnode=cgprsIsgsnRxPacketCountFromTnode, cgprsIsgsnRxOctetCountFromTnode=cgprsIsgsnRxOctetCountFromTnode, cgprsIsgsnErrorCountRxToTnode=cgprsIsgsnErrorCountRxToTnode, PYSNMP_MODULE_ID=ciscoGprsIsgsnMIB, cgprsIsgsnErrorCountRxFromTnode=cgprsIsgsnErrorCountRxFromTnode, cgprsIsgsnCompliance1=cgprsIsgsnCompliance1, ciscoGprsIsgsnMIB=ciscoGprsIsgsnMIB)
