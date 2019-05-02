#
# PySNMP MIB module SWAPCOM-SCC-TRAPS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SWAPCOM-SCC-TRAPS
# Produced by pysmi-0.3.4 at Wed May  1 15:12:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, Integer32, Gauge32, Counter32, ModuleIdentity, ObjectIdentity, Unsigned32, Bits, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Integer32", "Gauge32", "Counter32", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "Bits", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "TimeTicks", "Counter64")
TruthValue, TextualConvention, DateAndTime, StorageType, RowStatus, DisplayString, TestAndIncr, MacAddress, TimeInterval = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DateAndTime", "StorageType", "RowStatus", "DisplayString", "TestAndIncr", "MacAddress", "TimeInterval")
alarmProbeAlertSource, alarmProbeAlertType, alarmProbeSeverity = mibBuilder.importSymbols("SWAPCOM-SCC", "alarmProbeAlertSource", "alarmProbeAlertType", "alarmProbeSeverity")
swapcom = ModuleIdentity((1, 3, 6, 1, 4, 1, 11308))
swapcom.setRevisions(('1970-01-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: swapcom.setRevisionsDescriptions(('Revision Description',))
if mibBuilder.loadTexts: swapcom.setLastUpdated('2007381648Z')
if mibBuilder.loadTexts: swapcom.setOrganization('Organization name')
if mibBuilder.loadTexts: swapcom.setContactInfo('Contact information')
if mibBuilder.loadTexts: swapcom.setDescription('Description')
org = MibIdentifier((1, 3))
dod = MibIdentifier((1, 3, 6))
internet = MibIdentifier((1, 3, 6, 1))
private = MibIdentifier((1, 3, 6, 1, 4))
enterprises = MibIdentifier((1, 3, 6, 1, 4, 1))
sccTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 11308, 4))
sqlPoolUnavailable = NotificationType((1, 3, 6, 1, 4, 1, 11308, 4, 1)).setObjects(("SWAPCOM-SCC", "alarmProbeAlertType"), ("SWAPCOM-SCC", "alarmProbeAlertSource"), ("SWAPCOM-SCC", "alarmProbeSeverity"))
if mibBuilder.loadTexts: sqlPoolUnavailable.setStatus('current')
if mibBuilder.loadTexts: sqlPoolUnavailable.setDescription('')
sqlPoolHighCheckedOutConnections = NotificationType((1, 3, 6, 1, 4, 1, 11308, 4, 2)).setObjects(("SWAPCOM-SCC", "alarmProbeAlertType"), ("SWAPCOM-SCC", "alarmProbeAlertSource"), ("SWAPCOM-SCC", "alarmProbeSeverity"))
if mibBuilder.loadTexts: sqlPoolHighCheckedOutConnections.setStatus('current')
if mibBuilder.loadTexts: sqlPoolHighCheckedOutConnections.setDescription('')
slsUnavailable = NotificationType((1, 3, 6, 1, 4, 1, 11308, 4, 3)).setObjects(("SWAPCOM-SCC", "alarmProbeAlertType"), ("SWAPCOM-SCC", "alarmProbeAlertSource"), ("SWAPCOM-SCC", "alarmProbeSeverity"))
if mibBuilder.loadTexts: slsUnavailable.setStatus('current')
if mibBuilder.loadTexts: slsUnavailable.setDescription('')
remotePlatformUnavailable = NotificationType((1, 3, 6, 1, 4, 1, 11308, 4, 4)).setObjects(("SWAPCOM-SCC", "alarmProbeAlertType"), ("SWAPCOM-SCC", "alarmProbeAlertSource"), ("SWAPCOM-SCC", "alarmProbeSeverity"))
if mibBuilder.loadTexts: remotePlatformUnavailable.setStatus('current')
if mibBuilder.loadTexts: remotePlatformUnavailable.setDescription('')
schedulerTaskError = NotificationType((1, 3, 6, 1, 4, 1, 11308, 4, 5)).setObjects(("SWAPCOM-SCC", "alarmProbeAlertType"), ("SWAPCOM-SCC", "alarmProbeAlertSource"), ("SWAPCOM-SCC", "alarmProbeSeverity"))
if mibBuilder.loadTexts: schedulerTaskError.setStatus('current')
if mibBuilder.loadTexts: schedulerTaskError.setDescription('')
mibBuilder.exportSymbols("SWAPCOM-SCC-TRAPS", schedulerTaskError=schedulerTaskError, remotePlatformUnavailable=remotePlatformUnavailable, dod=dod, private=private, swapcom=swapcom, sqlPoolUnavailable=sqlPoolUnavailable, slsUnavailable=slsUnavailable, sqlPoolHighCheckedOutConnections=sqlPoolHighCheckedOutConnections, PYSNMP_MODULE_ID=swapcom, internet=internet, sccTraps=sccTraps, enterprises=enterprises, org=org)
