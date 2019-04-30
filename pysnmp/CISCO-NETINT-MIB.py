#
# PySNMP MIB module CISCO-NETINT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-NETINT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:51:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, Unsigned32, IpAddress, Counter32, MibIdentifier, Bits, NotificationType, Gauge32, iso, TimeTicks, ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "IpAddress", "Counter32", "MibIdentifier", "Bits", "NotificationType", "Gauge32", "iso", "TimeTicks", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoNetintMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 490))
ciscoNetintMIB.setRevisions(('2005-09-26 00:00',))
if mibBuilder.loadTexts: ciscoNetintMIB.setLastUpdated('200509260000Z')
if mibBuilder.loadTexts: ciscoNetintMIB.setOrganization('Cisco Systems, Inc.')
ciscoNetintMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 490, 0))
ciscoNetintMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 490, 1))
ciscoNetintMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 490, 2))
cniThrottle = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 490, 1, 1))
cniThrottleTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 490, 1, 1, 1), )
if mibBuilder.loadTexts: cniThrottleTable.setStatus('current')
cniThrottleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 490, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cniThrottleEntry.setStatus('current')
cniThrottleCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 490, 1, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cniThrottleCount.setStatus('current')
ciscoNetintMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 490, 2, 1))
ciscoNetintMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 490, 2, 2))
ciscoNetintMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 490, 2, 1, 1)).setObjects(("CISCO-NETINT-MIB", "ciscoThrottleGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetintMIBCompliance = ciscoNetintMIBCompliance.setStatus('current')
ciscoThrottleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 490, 2, 2, 1)).setObjects(("CISCO-NETINT-MIB", "cniThrottleCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoThrottleGroup = ciscoThrottleGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-NETINT-MIB", ciscoNetintMIBCompliance=ciscoNetintMIBCompliance, cniThrottle=cniThrottle, ciscoNetintMIBCompliances=ciscoNetintMIBCompliances, cniThrottleTable=cniThrottleTable, PYSNMP_MODULE_ID=ciscoNetintMIB, ciscoNetintMIB=ciscoNetintMIB, cniThrottleEntry=cniThrottleEntry, ciscoNetintMIBNotifs=ciscoNetintMIBNotifs, cniThrottleCount=cniThrottleCount, ciscoNetintMIBGroups=ciscoNetintMIBGroups, ciscoThrottleGroup=ciscoThrottleGroup, ciscoNetintMIBObjects=ciscoNetintMIBObjects, ciscoNetintMIBConformance=ciscoNetintMIBConformance)
