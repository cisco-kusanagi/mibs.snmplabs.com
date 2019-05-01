#
# PySNMP MIB module CISCO-JOB-MONITORING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-JOB-MONITORING-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:03:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, Bits, Gauge32, Unsigned32, Integer32, iso, Counter32, IpAddress, NotificationType, Counter64, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "Bits", "Gauge32", "Unsigned32", "Integer32", "iso", "Counter32", "IpAddress", "NotificationType", "Counter64", "ModuleIdentity", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoJobMonitoringCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 557))
ciscoJobMonitoringCapability.setRevisions(('2007-06-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoJobMonitoringCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoJobMonitoringCapability.setLastUpdated('200706070000Z')
if mibBuilder.loadTexts: ciscoJobMonitoringCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoJobMonitoringCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoJobMonitoringCapability.setDescription('Agent capabilities for Job-Monitoring-MIB')
ciscoJobMonitoringCapabilityV12R04 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 557, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoJobMonitoringCapabilityV12R04 = ciscoJobMonitoringCapabilityV12R04.setProductRelease('Cisco IOS 12.4')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoJobMonitoringCapabilityV12R04 = ciscoJobMonitoringCapabilityV12R04.setStatus('current')
if mibBuilder.loadTexts: ciscoJobMonitoringCapabilityV12R04.setDescription('JOB MONITORING MIB capabilities')
mibBuilder.exportSymbols("CISCO-JOB-MONITORING-CAPABILITY", ciscoJobMonitoringCapability=ciscoJobMonitoringCapability, ciscoJobMonitoringCapabilityV12R04=ciscoJobMonitoringCapabilityV12R04, PYSNMP_MODULE_ID=ciscoJobMonitoringCapability)
