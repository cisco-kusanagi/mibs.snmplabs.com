#
# PySNMP MIB module CISCO-JOB-MONITORING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-JOB-MONITORING-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:46:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, Integer32, NotificationType, ObjectIdentity, iso, Unsigned32, ModuleIdentity, Counter32, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "Integer32", "NotificationType", "ObjectIdentity", "iso", "Unsigned32", "ModuleIdentity", "Counter32", "Bits", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoJobMonitoringCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 557))
ciscoJobMonitoringCapability.setRevisions(('2007-06-07 00:00',))
if mibBuilder.loadTexts: ciscoJobMonitoringCapability.setLastUpdated('200706070000Z')
if mibBuilder.loadTexts: ciscoJobMonitoringCapability.setOrganization('Cisco Systems, Inc.')
ciscoJobMonitoringCapabilityV12R04 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 557, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoJobMonitoringCapabilityV12R04 = ciscoJobMonitoringCapabilityV12R04.setProductRelease('Cisco IOS 12.4')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoJobMonitoringCapabilityV12R04 = ciscoJobMonitoringCapabilityV12R04.setStatus('current')
mibBuilder.exportSymbols("CISCO-JOB-MONITORING-CAPABILITY", PYSNMP_MODULE_ID=ciscoJobMonitoringCapability, ciscoJobMonitoringCapability=ciscoJobMonitoringCapability, ciscoJobMonitoringCapabilityV12R04=ciscoJobMonitoringCapabilityV12R04)
