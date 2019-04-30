#
# PySNMP MIB module CISCO-OPTICAL-MONITOR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-OPTICAL-MONITOR-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:51:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
OpticalAlarmSeverityOrZero, = mibBuilder.importSymbols("CISCO-OPTICAL-MONITOR-MIB", "OpticalAlarmSeverityOrZero")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter32, Bits, Gauge32, ObjectIdentity, IpAddress, Counter64, ModuleIdentity, Integer32, TimeTicks, NotificationType, iso, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter32", "Bits", "Gauge32", "ObjectIdentity", "IpAddress", "Counter64", "ModuleIdentity", "Integer32", "TimeTicks", "NotificationType", "iso", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoOpticalMonitorCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 528))
ciscoOpticalMonitorCapability.setRevisions(('2007-01-08 00:00',))
if mibBuilder.loadTexts: ciscoOpticalMonitorCapability.setLastUpdated('200701080000Z')
if mibBuilder.loadTexts: ciscoOpticalMonitorCapability.setOrganization('Cisco Systems, Inc.')
ciscoOpticalMonCapCatOSV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 528, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOpticalMonCapCatOSV08R0601 = ciscoOpticalMonCapCatOSV08R0601.setProductRelease('Cisco CatOS 8.6(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOpticalMonCapCatOSV08R0601 = ciscoOpticalMonCapCatOSV08R0601.setStatus('current')
mibBuilder.exportSymbols("CISCO-OPTICAL-MONITOR-CAPABILITY", ciscoOpticalMonitorCapability=ciscoOpticalMonitorCapability, PYSNMP_MODULE_ID=ciscoOpticalMonitorCapability, ciscoOpticalMonCapCatOSV08R0601=ciscoOpticalMonCapCatOSV08R0601)
