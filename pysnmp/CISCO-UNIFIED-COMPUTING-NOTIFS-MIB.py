#
# PySNMP MIB module CISCO-UNIFIED-COMPUTING-NOTIFS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-UNIFIED-COMPUTING-NOTIFS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:58:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
cucsFaultDescription, cucsFaultAffectedObjectId, cucsFaultCreationTime, cucsFaultType, cucsFaultId, cucsFaultCode, cucsFaultOccur, cucsFaultSeverity, cucsFaultAffectedObjectDn, cucsFaultProbableCause, cucsFaultLastModificationTime, cucsFaultIndex = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultDescription", "cucsFaultAffectedObjectId", "cucsFaultCreationTime", "cucsFaultType", "cucsFaultId", "cucsFaultCode", "cucsFaultOccur", "cucsFaultSeverity", "cucsFaultAffectedObjectDn", "cucsFaultProbableCause", "cucsFaultLastModificationTime", "cucsFaultIndex")
ciscoUnifiedComputingMIBObjects, ciscoUnifiedComputingMIB = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-MIB", "ciscoUnifiedComputingMIBObjects", "ciscoUnifiedComputingMIB")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, iso, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, MibIdentifier, Gauge32, Unsigned32, Counter32, TimeTicks, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "MibIdentifier", "Gauge32", "Unsigned32", "Counter32", "TimeTicks", "ModuleIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoUnifiedComputingMIBNotifs = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 719, 0))
ciscoUnifiedComputingMIBNotifs.setRevisions(('2010-01-29 00:00',))
if mibBuilder.loadTexts: ciscoUnifiedComputingMIBNotifs.setLastUpdated('201001290000Z')
if mibBuilder.loadTexts: ciscoUnifiedComputingMIBNotifs.setOrganization('Cisco')
cucsFaultActiveNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 719, 0, 1)).setObjects(("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultIndex"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultDescription"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultAffectedObjectId"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultAffectedObjectDn"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultCreationTime"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultLastModificationTime"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultCode"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultType"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultProbableCause"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultSeverity"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultOccur"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultId"))
if mibBuilder.loadTexts: cucsFaultActiveNotif.setStatus('current')
cucsFaultClearNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 719, 0, 2)).setObjects(("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultIndex"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultDescription"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultAffectedObjectId"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultAffectedObjectDn"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultCreationTime"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultLastModificationTime"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultCode"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultType"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultProbableCause"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultSeverity"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultOccur"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultId"))
if mibBuilder.loadTexts: cucsFaultClearNotif.setStatus('current')
mibBuilder.exportSymbols("CISCO-UNIFIED-COMPUTING-NOTIFS-MIB", cucsFaultClearNotif=cucsFaultClearNotif, cucsFaultActiveNotif=cucsFaultActiveNotif, ciscoUnifiedComputingMIBNotifs=ciscoUnifiedComputingMIBNotifs, PYSNMP_MODULE_ID=ciscoUnifiedComputingMIBNotifs)
