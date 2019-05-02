#
# PySNMP MIB module CISCO-UNIFIED-COMPUTING-CONFORM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-UNIFIED-COMPUTING-CONFORM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:15:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
cucsFaultAffectedObjectId, cucsFaultType, cucsFaultSeverity, cucsFaultAffectedObjectDn, cucsFaultCode, cucsFaultLastModificationTime, cucsFaultDescription, cucsFaultCreationTime, cucsFaultOccur, cucsFaultProbableCause = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultAffectedObjectId", "cucsFaultType", "cucsFaultSeverity", "cucsFaultAffectedObjectDn", "cucsFaultCode", "cucsFaultLastModificationTime", "cucsFaultDescription", "cucsFaultCreationTime", "cucsFaultOccur", "cucsFaultProbableCause")
ciscoUnifiedComputingMIB, ciscoUnifiedComputingMIBObjects = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-MIB", "ciscoUnifiedComputingMIB", "ciscoUnifiedComputingMIBObjects")
cucsFaultClearNotif, cucsFaultActiveNotif = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-NOTIFS-MIB", "cucsFaultClearNotif", "cucsFaultActiveNotif")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, MibIdentifier, NotificationType, Counter32, Counter64, IpAddress, Bits, Gauge32, ObjectIdentity, TimeTicks, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "MibIdentifier", "NotificationType", "Counter32", "Counter64", "IpAddress", "Bits", "Gauge32", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoUnifiedComputingMIBConform = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 719, 2))
ciscoUnifiedComputingMIBConform.setRevisions(('2010-01-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoUnifiedComputingMIBConform.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoUnifiedComputingMIBConform.setLastUpdated('201001290000Z')
if mibBuilder.loadTexts: ciscoUnifiedComputingMIBConform.setOrganization('Cisco')
if mibBuilder.loadTexts: ciscoUnifiedComputingMIBConform.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: savbu-snmp-dev@cisco.com')
if mibBuilder.loadTexts: ciscoUnifiedComputingMIBConform.setDescription('Cisco UCS MIB conformance')
cucsFaultMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 719, 2, 1))
cucsFaultMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 719, 2, 1, 1))
cucsFaultMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 719, 2, 1, 2))
cucsFaultMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 719, 2, 1, 1, 1)).setObjects(("CISCO-UNIFIED-COMPUTING-CONFORM-MIB", "cucsFaultsNotifGroup"), ("CISCO-UNIFIED-COMPUTING-CONFORM-MIB", "cucsFaultsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cucsFaultMIBCompliance = cucsFaultMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cucsFaultMIBCompliance.setDescription('The compliance statement for entities that support the Cisco UCS Fault Managed Objects.')
cucsFaultsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 719, 2, 1, 2, 1)).setObjects(("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultDescription"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultAffectedObjectId"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultAffectedObjectDn"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultCreationTime"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultLastModificationTime"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultCode"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultType"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultProbableCause"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultSeverity"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultOccur"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cucsFaultsGroup = cucsFaultsGroup.setStatus('current')
if mibBuilder.loadTexts: cucsFaultsGroup.setDescription('A collection of objects providing UCS fault information.')
cucsFaultsNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 719, 2, 1, 2, 2)).setObjects(("CISCO-UNIFIED-COMPUTING-NOTIFS-MIB", "cucsFaultActiveNotif"), ("CISCO-UNIFIED-COMPUTING-NOTIFS-MIB", "cucsFaultClearNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cucsFaultsNotifGroup = cucsFaultsNotifGroup.setStatus('current')
if mibBuilder.loadTexts: cucsFaultsNotifGroup.setDescription('The set of UCS notifications defined by this MIB.')
mibBuilder.exportSymbols("CISCO-UNIFIED-COMPUTING-CONFORM-MIB", cucsFaultMIBConform=cucsFaultMIBConform, cucsFaultMIBCompliances=cucsFaultMIBCompliances, cucsFaultMIBGroups=cucsFaultMIBGroups, PYSNMP_MODULE_ID=ciscoUnifiedComputingMIBConform, cucsFaultsNotifGroup=cucsFaultsNotifGroup, ciscoUnifiedComputingMIBConform=ciscoUnifiedComputingMIBConform, cucsFaultMIBCompliance=cucsFaultMIBCompliance, cucsFaultsGroup=cucsFaultsGroup)
