#
# PySNMP MIB module ELTEX-MES-SYSLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-SYSLOG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:47:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
EltCPURateLimiterTrafficType, = mibBuilder.importSymbols("ELTEX-MES-SWITCH-RATE-LIMITER-MIB", "EltCPURateLimiterTrafficType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Counter32, Gauge32, MibIdentifier, ObjectIdentity, Unsigned32, ModuleIdentity, iso, NotificationType, Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "Gauge32", "MibIdentifier", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "iso", "NotificationType", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits")
RowStatus, TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TruthValue", "DisplayString")
eltMesSyslog = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 10))
if mibBuilder.loadTexts: eltMesSyslog.setLastUpdated('201605110000Z')
if mibBuilder.loadTexts: eltMesSyslog.setOrganization('Eltex Ltd.')
eltSyslogCPURateLimiterTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 10, 1), )
if mibBuilder.loadTexts: eltSyslogCPURateLimiterTable.setStatus('current')
eltSyslogCPURateLimiterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 10, 1, 1), ).setIndexNames((0, "ELTEX-MES-SYSLOG-MIB", "eltSyslogCPURateLimiterIndex"))
if mibBuilder.loadTexts: eltSyslogCPURateLimiterEntry.setStatus('current')
eltSyslogCPURateLimiterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 10, 1, 1, 1), EltCPURateLimiterTrafficType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltSyslogCPURateLimiterIndex.setStatus('current')
eltSyslogCPURateLimiterEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 10, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltSyslogCPURateLimiterEnabled.setStatus('current')
eltMesSyslogEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 10, 2))
eltSyslogEventsVrrpTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 10, 2, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltSyslogEventsVrrpTable.setStatus('current')
class EltSyslogEventsVRRPEventType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("eltSyslogEventsVRRPEventProtocolError", 1), ("eltSyslogEventsVRRPEventNewMaster", 2))

eltSyslogEventsVrrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 10, 2, 1, 1), ).setMaxAccess("readwrite").setIndexNames((0, "ELTEX-MES-SYSLOG-MIB", "eltSyslogEventsVRRPEventIndex"))
if mibBuilder.loadTexts: eltSyslogEventsVrrpEntry.setStatus('current')
eltSyslogEventsVRRPEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 10, 2, 1, 1, 1), EltSyslogEventsVRRPEventType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltSyslogEventsVRRPEventIndex.setStatus('current')
eltSyslogEventsVRRPEventEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 10, 2, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltSyslogEventsVRRPEventEnabled.setStatus('current')
eltSyslogUserCmdEnable = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 10, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltSyslogUserCmdEnable.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-SYSLOG-MIB", eltSyslogEventsVRRPEventIndex=eltSyslogEventsVRRPEventIndex, eltSyslogCPURateLimiterEnabled=eltSyslogCPURateLimiterEnabled, eltSyslogCPURateLimiterTable=eltSyslogCPURateLimiterTable, eltSyslogCPURateLimiterEntry=eltSyslogCPURateLimiterEntry, eltSyslogUserCmdEnable=eltSyslogUserCmdEnable, eltSyslogEventsVRRPEventEnabled=eltSyslogEventsVRRPEventEnabled, eltSyslogEventsVrrpTable=eltSyslogEventsVrrpTable, eltMesSyslogEvents=eltMesSyslogEvents, eltSyslogCPURateLimiterIndex=eltSyslogCPURateLimiterIndex, EltSyslogEventsVRRPEventType=EltSyslogEventsVRRPEventType, PYSNMP_MODULE_ID=eltMesSyslog, eltMesSyslog=eltMesSyslog, eltSyslogEventsVrrpEntry=eltSyslogEventsVrrpEntry)
