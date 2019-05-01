#
# PySNMP MIB module CISCO-OPTICAL-MONITOR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-OPTICAL-MONITOR-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:08:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
OpticalAlarmSeverityOrZero, = mibBuilder.importSymbols("CISCO-OPTICAL-MONITOR-MIB", "OpticalAlarmSeverityOrZero")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Unsigned32, Bits, ObjectIdentity, MibIdentifier, ModuleIdentity, TimeTicks, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, Gauge32, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "TimeTicks", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "Gauge32", "Integer32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoOpticalMonitorCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 528))
ciscoOpticalMonitorCapability.setRevisions(('2007-01-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoOpticalMonitorCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoOpticalMonitorCapability.setLastUpdated('200701080000Z')
if mibBuilder.loadTexts: ciscoOpticalMonitorCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoOpticalMonitorCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-dwdm@cisco.com, cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoOpticalMonitorCapability.setDescription('The capabilities description of CISCO-OPTICAL-MONITOR-MIB.')
ciscoOpticalMonCapCatOSV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 528, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOpticalMonCapCatOSV08R0601 = ciscoOpticalMonCapCatOSV08R0601.setProductRelease('Cisco CatOS 8.6(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOpticalMonCapCatOSV08R0601 = ciscoOpticalMonCapCatOSV08R0601.setStatus('current')
if mibBuilder.loadTexts: ciscoOpticalMonCapCatOSV08R0601.setDescription('CISCO-OPTICAL-MONITOR-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-OPTICAL-MONITOR-CAPABILITY", ciscoOpticalMonitorCapability=ciscoOpticalMonitorCapability, PYSNMP_MODULE_ID=ciscoOpticalMonitorCapability, ciscoOpticalMonCapCatOSV08R0601=ciscoOpticalMonCapCatOSV08R0601)
