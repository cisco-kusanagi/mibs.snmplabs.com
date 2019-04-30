#
# PySNMP MIB module SUPERMICRO-HEALTH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SUPERMICRO-HEALTH-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:04:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, iso, Gauge32, Counter32, Unsigned32, NotificationType, ModuleIdentity, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "Gauge32", "Counter32", "Unsigned32", "NotificationType", "ModuleIdentity", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "Integer32", "MibIdentifier")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
smHealth, = mibBuilder.importSymbols("SUPERMICRO-SMI", "smHealth")
smHealthMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 10876, 2, 1))
if mibBuilder.loadTexts: smHealthMIB.setLastUpdated('200110260000Z')
if mibBuilder.loadTexts: smHealthMIB.setOrganization('Super Micro Computer Inc.')
class SMHealthInfoTypes(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 64)

smHealthObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1))
smHealthMonitorTable = MibTable((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1), )
if mibBuilder.loadTexts: smHealthMonitorTable.setStatus('current')
smHealthMonitorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1), ).setIndexNames((0, "SUPERMICRO-HEALTH-MIB", "smHealthMonitorIndex"))
if mibBuilder.loadTexts: smHealthMonitorEntry.setStatus('current')
smHealthMonitorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: smHealthMonitorIndex.setStatus('current')
smHealthMonitorName = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smHealthMonitorName.setStatus('current')
smHealthMonitorType = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 3), SMHealthInfoTypes()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smHealthMonitorType.setStatus('current')
smHealthMonitorReading = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: smHealthMonitorReading.setStatus('current')
smHealthMonitorHighLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smHealthMonitorHighLimit.setStatus('current')
smHealthMonitorLowLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smHealthMonitorLowLimit.setStatus('current')
smHealthMonitorMaxReading = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: smHealthMonitorMaxReading.setStatus('current')
smHealthMonitorMinReading = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: smHealthMonitorMinReading.setStatus('current')
smHealthMonitorDivisor = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smHealthMonitorDivisor.setStatus('current')
smHealthMonitorMonitor = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 10), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smHealthMonitorMonitor.setStatus('current')
smHealthNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 10876, 2, 1, 2))
smHealthConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 10876, 2, 1, 3))
smHealthCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 10876, 2, 1, 3, 1))
smHealthGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 10876, 2, 1, 3, 2))
smHealthCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 10876, 2, 1, 3, 1, 1)).setObjects(("SUPERMICRO-HEALTH-MIB", "smHealthMonitorGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smHealthCompliance = smHealthCompliance.setStatus('current')
smHealthMonitorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10876, 2, 1, 3, 2, 1)).setObjects(("SUPERMICRO-HEALTH-MIB", "smHealthMonitorType"), ("SUPERMICRO-HEALTH-MIB", "smHealthMonitorName"), ("SUPERMICRO-HEALTH-MIB", "smHealthMonitorReading"), ("SUPERMICRO-HEALTH-MIB", "smHealthMonitorHighLimit"), ("SUPERMICRO-HEALTH-MIB", "smHealthMonitorLowLimit"), ("SUPERMICRO-HEALTH-MIB", "smHealthMonitorMaxReading"), ("SUPERMICRO-HEALTH-MIB", "smHealthMonitorMinReading"), ("SUPERMICRO-HEALTH-MIB", "smHealthMonitorMonitor"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smHealthMonitorGroup = smHealthMonitorGroup.setStatus('current')
mibBuilder.exportSymbols("SUPERMICRO-HEALTH-MIB", SMHealthInfoTypes=SMHealthInfoTypes, smHealthMonitorIndex=smHealthMonitorIndex, smHealthMonitorLowLimit=smHealthMonitorLowLimit, smHealthMonitorMonitor=smHealthMonitorMonitor, smHealthConformance=smHealthConformance, smHealthGroups=smHealthGroups, smHealthNotifications=smHealthNotifications, smHealthMonitorMinReading=smHealthMonitorMinReading, smHealthMonitorReading=smHealthMonitorReading, smHealthCompliance=smHealthCompliance, smHealthMonitorTable=smHealthMonitorTable, PYSNMP_MODULE_ID=smHealthMIB, smHealthMonitorMaxReading=smHealthMonitorMaxReading, smHealthObjects=smHealthObjects, smHealthMonitorName=smHealthMonitorName, smHealthMonitorEntry=smHealthMonitorEntry, smHealthMonitorGroup=smHealthMonitorGroup, smHealthCompliances=smHealthCompliances, smHealthMonitorHighLimit=smHealthMonitorHighLimit, smHealthMonitorType=smHealthMonitorType, smHealthMIB=smHealthMIB, smHealthMonitorDivisor=smHealthMonitorDivisor)
